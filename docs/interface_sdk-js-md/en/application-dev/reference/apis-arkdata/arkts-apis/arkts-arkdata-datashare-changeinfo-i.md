# ChangeInfo

数据变更时通知用户具体变更的内容，包括数据变更类型、变化的uri、变更的数据内容。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-dataShare-interface ChangeInfo--><!--Device-dataShare-interface ChangeInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## type

```TypeScript
type: ChangeType
```

通知变更的类型。

**Type:** [ChangeType](arkts-arkdata-relationalstore-changetype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChangeInfo-type: ChangeType--><!--Device-ChangeInfo-type: ChangeType-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## uri

```TypeScript
uri: string
```

指定uri。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChangeInfo-uri: string--><!--Device-ChangeInfo-uri: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## values

```TypeScript
values: Array<ValuesBucket>
```

更新的数据。

**Type:** Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChangeInfo-values: Array<ValuesBucket>--><!--Device-ChangeInfo-values: Array<ValuesBucket>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

