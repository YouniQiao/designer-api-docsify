# DataProxyConfig

数据代理操作配置的数据结构。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-dataShare-interface DataProxyConfig--><!--Device-dataShare-interface DataProxyConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## maxValueLength

```TypeScript
maxValueLength?: DataProxyMaxValueLength
```

设置共享配置的值允许的最大长度。如果未填写，默认为MAX_LENGTH_4K，即共享配置的值允许的最大长度为4096字节。

**Type:** [DataProxyMaxValueLength](arkts-arkdata-datashare-dataproxymaxvaluelength-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyConfig-maxValueLength?: DataProxyMaxValueLength--><!--Device-DataProxyConfig-maxValueLength?: DataProxyMaxValueLength-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## type

```TypeScript
type: DataProxyType
```

数据代理操作的类型。

**Type:** [DataProxyType](arkts-arkdata-datashare-dataproxytype-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyConfig-type: DataProxyType--><!--Device-DataProxyConfig-type: DataProxyType-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

