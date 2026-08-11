# UpdateOperation

Represents the batch update operation information.

**Since:** 12

<!--Device-dataShare-interface UpdateOperation--><!--Device-dataShare-interface UpdateOperation-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## predicates

```TypeScript
predicates: dataSharePredicates.DataSharePredicates
```

Conditions for updating data.

**Type:** dataSharePredicates.DataSharePredicates

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-UpdateOperation-predicates: dataSharePredicates.DataSharePredicates--><!--Device-UpdateOperation-predicates: dataSharePredicates.DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## values

```TypeScript
values: ValuesBucket
```

Data to be updated.

**Type:** [ValuesBucket](arkts-arkdata-valuesbucket-t.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-UpdateOperation-values: ValuesBucket--><!--Device-UpdateOperation-values: ValuesBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer
