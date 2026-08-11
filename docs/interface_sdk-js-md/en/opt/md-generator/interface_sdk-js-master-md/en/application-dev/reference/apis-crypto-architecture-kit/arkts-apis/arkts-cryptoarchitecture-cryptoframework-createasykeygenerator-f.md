# createAsyKeyGenerator

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## createAsyKeyGenerator

```TypeScript
function createAsyKeyGenerator(algName: string): AsyKeyGenerator
```

Creates an **AsyKeyGenerator** instance based on the specified algorithm.

&lt;br&gt;For details about the supported specifications, see  
[Asymmetric Key Generation and Conversion Specifications](../../../security/CryptoArchitectureKit/crypto-key-generation-conversion.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cryptoFramework-function createAsyKeyGenerator(algName: string): AsyKeyGenerator--><!--Device-cryptoFramework-function createAsyKeyGenerator(algName: string): AsyKeyGenerator-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| algName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AsyKeyGenerator](arkts-cryptoarchitecture-cryptoframework-asykeygenerator-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
```
