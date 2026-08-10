# isTokenizerSupported

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## isTokenizerSupported

```TypeScript
function isTokenizerSupported(tokenizer: Tokenizer): boolean
```

判断当前平台是否支持传入的分词器，此为同步接口。

如果当前平台支持传入的分词器时，此接口返回值为true；反之，返回值为false。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-relationalStore-function isTokenizerSupported(tokenizer: Tokenizer): boolean--><!--Device-relationalStore-function isTokenizerSupported(tokenizer: Tokenizer): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenizer | [Tokenizer](arkts-arkdata-relationalstore-tokenizer-e.md) | Yes | 需要被判断是否支持的分词器。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示当前平台支持当前传入的分词器，false表示当前平台不支持当前传入的分词器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
let customType = relationalStore.Tokenizer.CUSTOM_TOKENIZER;
let customTypeSupported = relationalStore.isTokenizerSupported(customType);
console.info("custom tokenizer supported on current platform: " + customTypeSupported);
```

