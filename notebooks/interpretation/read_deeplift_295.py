from glob import glob
import sys
import numpy as np

tasks = [("HepG2", "minP"), ("K562", "minP"), ("HepG2", "SV40P"), ("K562", "SV40P")]

def get_deep(directory):
    deeplift = {task: {} for task in tasks} # experiment -> chrom -> start_position
    for f in glob(directory+'*'):
        print f
        with open(f) as deep_data:
            for line in deep_data:
                parts = line.split(',')
                chrom, start = parts[:2]
                if len(parts) != 582: continue
                data = map(float, parts[2:])
                start = int(start)
                for i, task in enumerate(tasks):
                    if chrom not in deeplift[task]: deeplift[task][chrom] = {}
                    for shift in range(120):
                        pos = start + shift
                        if pos not in deeplift[task][chrom]: deeplift[task][chrom][pos] = []
                        deeplift[task][chrom][pos] += [data[shift + i*145]]
    return deeplift
