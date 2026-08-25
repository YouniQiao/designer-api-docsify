# isTokenizerSupported

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## isTokenizerSupported

```TypeScript
function isTokenizerSupported(tokenizer: Tokenizer): boolean
```

Checks whether the specified tokenizer is supported. This API returns the result synchronously.This API returns **true** if the specified tokenizer is supported; returns **false** otherwise.

**Since:** 18

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [tokenizer](arkts-arkdata-relationalstore-storeconfig-i.md) | [Tokenizer](arkts-arkdata-relationalstore-tokenizer-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
