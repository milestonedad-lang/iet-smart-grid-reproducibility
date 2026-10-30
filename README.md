# Mobile storage service accounting results

Public results cross-check package for **Service State Accounting and Independent Verification in Mobile Energy Storage Scheduling**.

Authors: Mingming Dong, Ge Chen, Wei Chen, Puhe Deng.
Version: 1.0.0. Released: 2026-10-30.

## Contents

- configuration_means.csv: eight policy/budget configurations, including both custom greedy baselines.
- pilot_pair_metrics.csv: all six paired counterfactual comparisons, including negative outcomes.
- evidence_summary.json: aggregate evidence counts and interpretation boundaries.
- check_results.py: standard-library checks and recomputation of three matched configuration differences from saved means.
- SHA256SUMS.txt: file identities for this release.

## Run

Use Python 3.11 or later, from the repository root:

```
python check_results.py
```

No third-party dependencies or network are needed. The script prints its results and does not modify input files. These are checks of saved aggregate metrics. They do not independently validate aggregation from raw trajectories, physical feasibility, scheduling decisions, or model optimality. This repository is a results cross-check package, not a complete public implementation or independent reproduction of the study.

## Evidence and interpretation

The formal set comprises 192 trajectories over 12 fixed conditions, with 6,912 epochs. Repeats are not independent disaster samples. Pilot evidence comprises 12 suffixes at two exploratory episodes, producing six paired comparisons; it must not be pooled with the formal trajectories. All six pilot service comparisons tie; three have higher connection-site energy not supplied. Negative results are retained. The study does not establish general algorithmic superiority, AC feeder restoration capability or field effectiveness.

Power/energy measures distinguish connection-site ENS from other demand domains; the exposed ENS column is connection-site energy not supplied in MWh. Runtime is observed computation in seconds, not a hard real-time guarantee. Policy labels LATE_ONLY and BOTH identify certificate representations; GREEDY_SERVICE and GREEDY_ENERGY are custom comparison rules. budget_s is a nominal decision budget; blank values apply to the greedy rules. Pilot deltas are RECERT_COMMIT minus BASELINE; positive miss/ENS deltas are worse.

## Availability and reuse

Only the aggregate results and generic cross-check script listed here are publicly disclosed. Core scheduling algorithms, recertification implementations, detailed parameters, constraint matrices, solution vectors, epoch-level trajectories, initialization states and raw checkpoints are excluded from this public repository. Third-party benchmark datasets are not bundled. Full implementation details and raw records are not publicly available under the current disclosure scope; any further access is subject to the applicable permissions and restrictions.

No open-source or open-data reuse license has been granted by this release. Public access does not grant a blanket MIT, BSD or Creative Commons license, nor rights to third-party materials. No DOI has been assigned. The repository has a new history containing only this approved reduced payload; the full review and reproducibility archives remain private.
