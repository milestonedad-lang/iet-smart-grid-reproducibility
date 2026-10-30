from pathlib import Path
import json,csv,math
R=Path(__file__).resolve().parent
with (R/'configuration_means.csv').open(encoding='utf-8') as f:rows=list(csv.DictReader(f))
assert len(rows)==8 and sum(int(x['runs']) for x in rows)==192
result=[]
for budget in ['6','18','60']:
 a=next(x for x in rows if x['policy']=='LATE_ONLY' and x['budget_s']==budget);b=next(x for x in rows if x['policy']=='BOTH' and x['budget_s']==budget)
 result.append({'budget_s':int(budget),'BOTH_minus_LATE_ONLY_mean_misses':float(b['mean_final_service_misses'])-float(a['mean_final_service_misses']),'BOTH_minus_LATE_ONLY_mean_ENS_MWh':float(b['mean_connection_site_ENS_MWh'])-float(a['mean_connection_site_ENS_MWh'])})
with (R/'pilot_pair_metrics.csv').open(encoding='utf-8') as f:pairs=list(csv.DictReader(f))
assert len(pairs)==6
for p in pairs:
 assert math.isclose(float(p['miss_delta']),float(p['recert_misses'])-float(p['baseline_misses']),abs_tol=1e-12)
 assert math.isclose(float(p['ENS_S_delta_MWh']),float(p['recert_ENS_S_MWh'])-float(p['baseline_ENS_S_MWh']),abs_tol=1e-12)
assert all(float(x['miss_delta'])==0 for x in pairs)
assert sum(float(x['ENS_S_delta_MWh'])>1e-7 for x in pairs)==3
print(json.dumps({'status':'passed','scope':'saved aggregate metric cross-check only','configuration_differences':result,'pilot_pairs':6,'service_ties':6,'energy_worse_pairs':3,'optimizer_calls':0},indent=2))
