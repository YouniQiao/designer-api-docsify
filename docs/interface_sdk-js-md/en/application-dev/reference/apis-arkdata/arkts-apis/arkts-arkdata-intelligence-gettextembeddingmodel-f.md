# getTextEmbeddingModel

## Modules to Import

```TypeScript
import { intelligence } from 'kits/@kit.ArkData';
```

## getTextEmbeddingModel

```TypeScript
function getTextEmbeddingModel(config: ModelConfig): Promise<TextEmbedding>
```

Obtains a text embedding model.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-intelligence-function getTextEmbeddingModel(config: ModelConfig): Promise<TextEmbedding>--><!--Device-intelligence-function getTextEmbeddingModel(config: ModelConfig): Promise<TextEmbedding>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [ModelConfig](arkts-arkdata-intelligence-modelconfig-i.md) | Yes | The configuration of the embedding model. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;TextEmbedding&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [31300000](../errorcode-intelligence.md#31300000-internal-error) | Inner error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let textConfig: intelligence.ModelConfig = {
  version: intelligence.ModelVersion.BASIC_MODEL,
  isNpuAvailable: false,
  cachePath: "/data"
}
let textEmbedding: intelligence.TextEmbedding;

intelligence.getTextEmbeddingModel(textConfig)
  .then((data: intelligence.TextEmbedding) => {
    console.info("Succeeded in getting TextModel");
    textEmbedding = data;
  })
  .catch((err: BusinessError) => {
    console.error("Failed to get TextModel and code is " + err.code);
  })
```

