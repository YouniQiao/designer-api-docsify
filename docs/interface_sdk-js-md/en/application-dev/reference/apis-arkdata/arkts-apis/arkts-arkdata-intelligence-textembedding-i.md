# TextEmbedding

Describes the text embedding functions of the multi-modal embedding model. Chinese and English are supported.@interface TextEmbedding

**Since:** 15

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

## Modules to Import

```TypeScript
import { intelligence } from 'kits/@kit.ArkData';
```

## getEmbedding

```TypeScript
getEmbedding(text: string): Promise<Array<number>>
```

Obtains the embedding vector of the given text. The model can process up to 512 characters of text per inference, supporting both Chinese and English.

**Since:** 15

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

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

## getEmbedding

```TypeScript
getEmbedding(batchTexts: Array<string>): Promise<Array<Array<number>>>
```

Obtains the embedding vector of a given batch of text. The model can process up to 512 characters of text per inference, supporting both Chinese and English.

**Since:** 15

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| batchTexts | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;Array & lt;number & gt; & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [31300000](../errorcode-intelligence.md#31300000-internal-error) |

## loadModel

```TypeScript
loadModel(): Promise<void>
```

Loads this text embedding model. If the loading fails, an error code is returned.

**Since:** 15

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

## releaseModel

```TypeScript
releaseModel(): Promise<void>
```

Releases this text embedding model. If the releasing fails, an error code is returned.

**Since:** 15

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
