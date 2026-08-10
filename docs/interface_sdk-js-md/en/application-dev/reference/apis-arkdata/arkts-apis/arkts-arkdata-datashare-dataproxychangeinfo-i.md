# DataProxyChangeInfo

通知订阅者共享配置变更的数据结构。包括数据变更类型、变化的URI、变更的数据内容。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-dataShare-interface DataProxyChangeInfo--><!--Device-dataShare-interface DataProxyChangeInfo-End-->

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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyChangeInfo-type: ChangeType--><!--Device-DataProxyChangeInfo-type: ChangeType-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## uri

```TypeScript
uri: string
```

通知变更指定URI。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyChangeInfo-uri: string--><!--Device-DataProxyChangeInfo-uri: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## value

```TypeScript
value: ValueType
```

更新的数据。

**Type:** [ValueType](arkts-arkdata-valuetype-t.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyChangeInfo-value: ValueType--><!--Device-DataProxyChangeInfo-value: ValueType-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## values

```TypeScript
values?: ValueType[]
```

多值类型的变更数据。如果变更的数据类型不是多值类型，则**values**值为undefined。

**Type:** [ValueType](arkts-arkdata-valuetype-t.md)[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyChangeInfo-values?: ValueType[]--><!--Device-DataProxyChangeInfo-values?: ValueType[]-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

