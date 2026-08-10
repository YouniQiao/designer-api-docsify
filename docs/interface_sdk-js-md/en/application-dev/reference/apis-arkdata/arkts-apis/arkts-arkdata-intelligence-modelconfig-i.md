# ModelConfig

管理嵌入模型的配置信息。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-intelligence-interface ModelConfig--><!--Device-intelligence-interface ModelConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

## Modules to Import

```TypeScript
import { intelligence } from 'kits/@kit.ArkData';
```

## cachePath

```TypeScript
cachePath?: string
```

如果使用NPU进行加速，则需要本地路径进行模型缓存。格式为/xxx/xxx/xxx，xxx为路径地址，例如"/data"。长度上限为512个字符。默认值为""。超出长度时抛出异常。

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-ModelConfig-cachePath?: string--><!--Device-ModelConfig-cachePath?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

## isNpuAvailable

```TypeScript
isNpuAvailable: boolean
```

指示是否使用NPU加速向量化过程，true表示使用，false表示不使用。如果设备不支持NPU，调用加载模型会失败，并抛出错误码31300000。

**Type:** boolean

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-ModelConfig-isNpuAvailable: boolean--><!--Device-ModelConfig-isNpuAvailable: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

## modelInfo

```TypeScript
modelInfo?: CloudModelInfo
```

云侧模型类型和版本信息，在使用文本向量模型时配置，通过[getSupportedCloudModel](arkts-arkdata-intelligence-getsupportedcloudmodel-f.md#getsupportedcloudmodel)接口获取支持的模型信息，默认值为空。

**Type:** [CloudModelInfo](arkts-arkdata-intelligence-cloudmodelinfo-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ModelConfig-modelInfo?: CloudModelInfo--><!--Device-ModelConfig-modelInfo?: CloudModelInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

## networkPolicy

```TypeScript
networkPolicy?: NetworkPolicy
```

下载云侧模型时使用的网络策略，默认值为WIFI_ONLY。此参数仅在使用文本嵌入模型时生效，在使用图像嵌入模型场景此参数不生效。

**Type:** [NetworkPolicy](arkts-arkdata-intelligence-networkpolicy-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ModelConfig-networkPolicy?: NetworkPolicy--><!--Device-ModelConfig-networkPolicy?: NetworkPolicy-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

## version

```TypeScript
version: ModelVersion
```

模型的版本。

**Type:** [ModelVersion](arkts-arkdata-intelligence-modelversion-e.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-ModelConfig-version: ModelVersion--><!--Device-ModelConfig-version: ModelVersion-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

