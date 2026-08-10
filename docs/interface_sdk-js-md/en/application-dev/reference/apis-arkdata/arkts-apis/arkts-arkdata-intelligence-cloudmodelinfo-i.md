# CloudModelInfo

云侧模型的配置信息，在使用云侧文本向量模型时配置，可通过[getSupportedCloudModel](arkts-arkdata-intelligence-getsupportedcloudmodel-f.md#getsupportedcloudmodel)接口获取当前设备支持的云侧模型信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-intelligence-interface CloudModelInfo--><!--Device-intelligence-interface CloudModelInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

## Modules to Import

```TypeScript
import { intelligence } from 'kits/@kit.ArkData';
```

## modelType

```TypeScript
modelType: string
```

模型类型名称，如"arkdata_text_embedding"表示云侧文本向量模型。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CloudModelInfo-modelType: string--><!--Device-CloudModelInfo-modelType: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

## modelVersionCode

```TypeScript
modelVersionCode?: string
```

模型版本，默认值为空。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CloudModelInfo-modelVersionCode?: string--><!--Device-CloudModelInfo-modelVersionCode?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

