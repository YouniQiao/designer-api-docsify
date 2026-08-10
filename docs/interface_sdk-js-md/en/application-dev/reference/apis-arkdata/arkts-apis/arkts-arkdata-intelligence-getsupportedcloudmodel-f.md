# getSupportedCloudModel

## Modules to Import

```TypeScript
import { intelligence } from 'kits/@kit.ArkData';
```

## getSupportedCloudModel

```TypeScript
function getSupportedCloudModel(): Promise<Array<CloudModelInfo>>
```

获取支持的云侧模型信息。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-intelligence-function getSupportedCloudModel(): Promise<Array<CloudModelInfo>>--><!--Device-intelligence-function getSupportedCloudModel(): Promise<Array<CloudModelInfo>>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;CloudModelInfo&gt;&gt; | Promise对象，返回支持的云侧模型信息。 |

