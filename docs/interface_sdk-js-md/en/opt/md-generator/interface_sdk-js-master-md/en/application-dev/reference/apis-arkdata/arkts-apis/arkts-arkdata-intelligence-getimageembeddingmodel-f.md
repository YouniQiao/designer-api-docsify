# getImageEmbeddingModel

## Modules to Import

```TypeScript
import { intelligence } from 'kits/@kit.ArkData';
```

## getImageEmbeddingModel

```TypeScript
function getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding>
```

Obtains an image embedding model.

**Since:** 15

<!--Device-intelligence-function getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding>--><!--Device-intelligence-function getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [ModelConfig](arkts-arkdata-intelligence-modelconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ImageEmbedding&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [31300000](../errorcode-intelligence.md#31300000-internal-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let imageConfig: intelligence.ModelConfig = {
  version: intelligence.ModelVersion.BASIC_MODEL,
  isNpuAvailable: false,
  cachePath: "/data"
}
let imageEmbedding: intelligence.ImageEmbedding;

intelligence.getImageEmbeddingModel(imageConfig)
  .then((data: intelligence.ImageEmbedding) => {
    console.info("Succeeded in getting ImageModel");
    imageEmbedding = data;
  })
  .catch((err: BusinessError) => {
    console.error("Failed to get ImageModel and code is " + err.code);
  })
```
