# getSupportedCloudModel

## Modules to Import

```TypeScript
import { intelligence } from 'intelligence';
```

## getSupportedCloudModel

```TypeScript
function getSupportedCloudModel(): Promise<Array<CloudModelInfo>>
```

Obtains the supported cloud embedding models.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-intelligence-function getSupportedCloudModel(): Promise<Array<CloudModelInfo>>--><!--Device-intelligence-function getSupportedCloudModel(): Promise<Array<CloudModelInfo>>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[CloudModelInfo](arkts-arkdata-intelligence-cloudmodelinfo-i.md)&gt;&gt; | The promise returned by the function. |

