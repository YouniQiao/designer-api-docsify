# ImageEmbedding

Describes the image embedding functions of the multi-modal embedding model.

**Since:** 23

**Deprecated since:** -1

<!--Device-intelligence-interface ImageEmbedding--><!--Device-intelligence-interface ImageEmbedding-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

## Modules to Import

```TypeScript
import { intelligence } from '@kit.ArkData';
```

## getEmbedding

```TypeScript
getEmbedding(image: Image): Promise<Array<number>>
```

Obtains the embedding vector of the given image. The model can handle images below 20 MB in size in a single inference.

**Since:** 23

**Deprecated since:** -1

<!--Device-ImageEmbedding-getEmbedding(image: Image): Promise<Array<double>>--><!--Device-ImageEmbedding-getEmbedding(image: Image): Promise<Array<double>>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| image | [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [31300000](../errorcode-intelligence.md#31300000-internal-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

imageEmbedding.loadModel();
let image = 'file://<packageName>/data/storage/el2/base/haps/entry/files/xxx.jpg';
imageEmbedding.getEmbedding(image)
  .then((data: Array<number>) => {
    console.info("Succeeded in getting Embedding");
  })
  .catch((err: BusinessError) => {
    console.error("Failed to get Embedding and code is " + err.code);
  })
```

## loadModel

```TypeScript
loadModel(): Promise<void>
```

Loads this image embedding model. If the loading fails, an error code is returned.

**Since:** 23

**Deprecated since:** -1

<!--Device-ImageEmbedding-loadModel(): Promise<void>--><!--Device-ImageEmbedding-loadModel(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [31300000](../errorcode-intelligence.md#31300000-internal-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

imageEmbedding.loadModel()
  .then(() => {
    console.info("Succeeded in loading Model");
  })
  .catch((err: BusinessError) => {
    console.error("Failed to load Model and code is " + err.code);
  })
```

## releaseModel

```TypeScript
releaseModel(): Promise<void>
```

Releases this image embedding model. If the releasing fails, an error code is returned.

**Since:** 23

**Deprecated since:** -1

<!--Device-ImageEmbedding-releaseModel(): Promise<void>--><!--Device-ImageEmbedding-releaseModel(): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [31300000](../errorcode-intelligence.md#31300000-internal-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

imageEmbedding.releaseModel()
  .then(() => {
    console.info("Succeeded in releasing Model");
  })
  .catch((err: BusinessError) => {
    console.error("Failed to release Model and code is " + err.code);
  })
```
