#!/usr/bin/env python3
import argparse
import math
import logging
from collections import Counter

# -----------------------------
# Helper functions
# -----------------------------

def read_fastq_sequences(filename):
    """Yield sequences from a FASTQ file (4 lines per record)."""
    with open(filename, 'r') as f:
        while True:
            header = f.readline()
            if not header:
                break
            seq = f.readline().strip()
            f.readline()  # plus line
            f.readline()  # quality line
            yield seq

def shannon_entropy(kmer):
    """Compute Shannon entropy (bits) for a kmer."""
    counts = Counter(kmer)
    total = len(kmer)
    return -sum((c/total) * math.log2(c/total) for c in counts.values())

def count_kmers(fastq_file, k):
    """Count kmers of length k from FASTQ reads."""
    logger = logging.getLogger("InchwormAssembler")
    kmer_counts = Counter()
    n_reads = 0
    for seq in read_fastq_sequences(fastq_file):
        n_reads += 1
        seq = seq.upper()
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            if 'N' not in kmer:
                kmer_counts[kmer] += 1
        if n_reads % 100000 == 0:
            logger.info(f"Processed {n_reads:,} reads...")
    logger.info(f"Total reads processed: {n_reads:,}")
    logger.info(f"Unique kmers counted: {len(kmer_counts):,}")
    return kmer_counts

# -----------------------------
# Core Inchworm-like assembler
# -----------------------------

def inchworm_assemble(kmer_counts, k, min_entropy=0.0, log_interval=1000):
    logger = logging.getLogger("InchwormAssembler")

    # Precompute entropy once for each kmer
    entropy_map = {kmer: shannon_entropy(kmer) for kmer in kmer_counts}
    
    # Filter kmers by entropy
    valid_kmers = {kmer: count for kmer, count in kmer_counts.items()
                   if entropy_map[kmer] >= min_entropy}

    logger.info(f"Filtered kmers (entropy ≥ {min_entropy:.2f}): {len(valid_kmers):,}")

    # Build prefix and suffix lookup dicts: prefix -> set(kmers), suffix -> set(kmers)
    prefix_dict = {}
    suffix_dict = {}

    for kmer in valid_kmers:
        prefix = kmer[:k-1]
        suffix = kmer[1:]
        prefix_dict.setdefault(prefix, set()).add(kmer)
        suffix_dict.setdefault(suffix, set()).add(kmer)

    assembled_contigs = []
    contig_counter = 0

    while valid_kmers:
        # Seed = most abundant remaining kmer
        seed = max(valid_kmers, key=valid_kmers.get)
        contig = seed
        contig_counter += 1

        if contig_counter % log_interval == 0:
            logger.info(f"Contigs built so far: {contig_counter:,} | Remaining kmers: {len(valid_kmers):,}")

        # Remove seed from valid kmers and prefix/suffix dicts
        def remove_kmer(kmer):
            valid_kmers.pop(kmer, None)
            prefix = kmer[:k-1]
            suffix = kmer[1:]
            prefix_dict[prefix].discard(kmer)
            if not prefix_dict[prefix]:
                del prefix_dict[prefix]
            suffix_dict[suffix].discard(kmer)
            if not suffix_dict[suffix]:
                del suffix_dict[suffix]

        remove_kmer(seed)

        # Forward extension
        extended = True
        while extended:
            suffix = contig[-(k-1):]
            candidates = prefix_dict.get(suffix, set())
            if not candidates:
                extended = False
                break
            # Pick candidate with highest count
            next_kmer = max(candidates, key=lambda x: valid_kmers[x])
            contig += next_kmer[-1]
            remove_kmer(next_kmer)

        # Backward extension
        extended = True
        while extended:
            prefix = contig[:k-1]
            candidates = suffix_dict.get(prefix, set())
            if not candidates:
                extended = False
                break
            prev_kmer = max(candidates, key=lambda x: valid_kmers[x])
            contig = prev_kmer[0] + contig
            remove_kmer(prev_kmer)

        assembled_contigs.append(contig)

    logger.info(f"Assembly complete. Built {len(assembled_contigs):,} contigs.")

    # Top 5 contigs by length (logged)
    if assembled_contigs:
        top5 = sorted(assembled_contigs, key=len, reverse=True)[:5]
        logger.info("Top 5 contigs by length:")
        for i, contig in enumerate(top5, start=1):
            logger.info(f"  {i}. length={len(contig):,} | sequence={contig[:60]}...")
    else:
        logger.info("No contigs were assembled.")

    return assembled_contigs


# -----------------------------
# Main program
# -----------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Simplified Inchworm-like assembler from FASTQ reads."
    )
    parser.add_argument("fastq_file", help="Input FASTQ file")
    parser.add_argument("k", type=int, help="K-mer size")
    parser.add_argument(
        "--min_entropy",
        type=float,
        default=0.0,
        help="Minimum entropy required for seed kmers (default: 0.0)"
    )
    parser.add_argument(
        "--log_interval",
        type=int,
        default=1000,
        help="Log progress every N contigs (default: 1000)"
    )

    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s: %(message)s",
        datefmt="%H:%M:%S"
    )

    logger = logging.getLogger("Main")
    logger.info(f"Starting Inchworm assembly on {args.fastq_file} with k={args.k}")

    kmer_counts = count_kmers(args.fastq_file, args.k)
    contigs = inchworm_assemble(kmer_counts, args.k, args.min_entropy, args.log_interval)

    
    # Print final summary
    logger.info(f"\nTotal contigs assembled: {len(contigs)}")

    # Print only top 20 longest contigs in FASTA format
    print("\nAssembled contigs (top 20 longest):")
    top20 = sorted(contigs, key=len, reverse=True)[:20]
    for i, contig in enumerate(top20, start=1):
        print(f">contig_{i} length={len(contig)}")
        print(contig)

if __name__ == "__main__":
    main()
