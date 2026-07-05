# S3 Rest — Evaluation Report

## Step 6 — Kalibrierung (ECE)

- Cases: 487
- Accuracy: 96.5%
- ECE: 0.4349
- Brier: 0.2565
- Mean C_new: 0.5302

### Reliability Bins

| Bin | n | Conf | Acc | Gap |
|-----|---|------|-----|-----|
| [0.3,0.4) | 205 | 0.3 | 0.9268 | 0.6268 |
| [0.6,0.7) | 173 | 0.6 | 0.9884 | 0.3884 |
| [0.8,0.9) | 109 | 0.8522 | 1.0 | 0.1478 |

### Per Status

- **LI**: n=159 acc=100.0% ECE=0.5868 Brier=0.3655
- **PL**: n=173 acc=90.2% ECE=0.4613 Brier=0.3031
- **VC**: n=109 acc=100.0% ECE=0.1478 Brier=0.0218
- **IU**: n=46 acc=100.0% ECE=0.4913 Brier=0.2604

## Step 7 — Robustheit

- Baseline: 96.5%
- Adversarial: 96.5% (n=487)
- Noise: 96.5% (n=487)
- Short (<10w): 80.7% (n=57)
- Long (>50w): 0.0% (n=0)
- DE heuristic: 84.6% (n=78)
- EN heuristic: 98.8% (n=409)

## Step 8 — Reproduzierbarkeit

- Deterministic (2 runs): True (0 mismatches)
- Order independent: True (0 mismatches)

## Step 9 — Performance

- Mean: 1018.86 ms | Median: 811.16 ms | p95: 2207.74 ms
- Memory mean: 354.4 KB | max: 472.1 KB

### Skalierung

| Cases | Total s | ms/case |
|-------|---------|---------|
| 10 | 6.72 | 672.01 |
| 100 | 79.75 | 797.51 |
| 487 | 382.86 | 786.17 |
