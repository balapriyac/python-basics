#!/usr/bin/env python3
"""
text_word_frequency_analyzer.py

Read a plain text file and report word/sentence counts, average sentence
length, the most frequently used words (excluding common stop words),
and an estimated reading time.

Usage:
    python 03_text_word_frequency_analyzer.py essay.txt --top 15 --wpm 200
"""

import argparse
import re
from collections import Counter

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "if", "of", "to", "in", "on", "for",
    "is", "are", "was", "were", "be", "been", "being", "it", "its", "this",
    "that", "these", "those", "with", "as", "at", "by", "from", "so", "than",
    "then", "there", "their", "they", "them", "he", "she", "his", "her",
    "you", "your", "we", "our", "i", "my", "me", "not", "no", "do", "does",
    "did", "has", "have", "had", "will", "would", "can", "could", "should",
    "about", "into", "up", "out", "over", "under", "again", "further", "just",
}


def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def split_sentences(text):
    # Simple sentence splitter: break on . ! ? followed by whitespace
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return [s for s in sentences if s.strip()]


def extract_words(text):
    return re.findall(r"[a-zA-Z']+", text.lower())


def analyze(text, top_n=10, words_per_minute=200):
    words = extract_words(text)
    sentences = split_sentences(text)

    word_count = len(words)
    sentence_count = len(sentences) or 1
    avg_sentence_length = word_count / sentence_count

    meaningful_words = [w for w in words if w not in STOP_WORDS and len(w) > 1]
    top_words = Counter(meaningful_words).most_common(top_n)

    reading_time_minutes = word_count / words_per_minute

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "avg_sentence_length": avg_sentence_length,
        "top_words": top_words,
        "reading_time_minutes": reading_time_minutes,
    }


def format_reading_time(minutes):
    if minutes < 1:
        return f"{int(minutes * 60)} sec"
    whole_minutes = int(minutes)
    seconds = int(round((minutes - whole_minutes) * 60))
    return f"{whole_minutes} min {seconds} sec" if seconds else f"{whole_minutes} min"


def main():
    parser = argparse.ArgumentParser(
        description="Analyze word frequency and estimated reading time for a text file."
    )
    parser.add_argument("text_file", help="Path to a plain text (.txt) file")
    parser.add_argument("--top", type=int, default=10, help="Number of top words to show (default: 10)")
    parser.add_argument("--wpm", type=int, default=200,
                         help="Assumed reading speed in words per minute (default: 200)")
    args = parser.parse_args()

    text = load_text(args.text_file)
    stats = analyze(text, top_n=args.top, words_per_minute=args.wpm)

    print(f"Analysis of {args.text_file}")
    print("-" * 40)
    print(f"Word count:            {stats['word_count']}")
    print(f"Sentence count:        {stats['sentence_count']}")
    print(f"Avg. words/sentence:   {stats['avg_sentence_length']:.1f}")
    print(f"Estimated reading time: {format_reading_time(stats['reading_time_minutes'])}")
    print()
    print(f"Top {args.top} most frequent words (stop words excluded):")
    for word, count in stats["top_words"]:
        print(f"  {word:<15} {count}")


if __name__ == "__main__":
    main()
  
