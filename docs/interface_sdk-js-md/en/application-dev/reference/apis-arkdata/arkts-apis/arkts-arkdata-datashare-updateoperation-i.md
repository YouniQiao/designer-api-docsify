# UpdateOperation

批量更新操作的参数结构。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

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

筛选条件。

**Type:** dataSharePredicates.DataSharePredicates

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UpdateOperation-predicates: dataSharePredicates.DataSharePredicates--><!--Device-UpdateOperation-predicates: dataSharePredicates.DataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## values

```TypeScript
values: ValuesBucket
```

要更新的数据。

**Type:** [ValuesBucket](arkts-arkdata-valuesbucket-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UpdateOperation-values: ValuesBucket--><!--Device-UpdateOperation-values: ValuesBucket-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

