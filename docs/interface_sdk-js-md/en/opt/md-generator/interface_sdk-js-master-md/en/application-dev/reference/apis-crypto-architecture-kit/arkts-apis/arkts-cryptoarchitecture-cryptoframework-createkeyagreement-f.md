# createKeyAgreement

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## createKeyAgreement

```TypeScript
function createKeyAgreement(algName: string): KeyAgreement
```

Creates a **KeyAgreement** instance.

&lt;br&gt;For details about the supported specifications, see[Key Agreement Overview and Algorithm Specifications](../../../security/CryptoArchitectureKit/crypto-key-agreement-overview.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cryptoFramework-function createKeyAgreement(algName: string): KeyAgreement--><!--Device-cryptoFramework-function createKeyAgreement(algName: string): KeyAgreement-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.KeyAgreement
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| algName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [KeyAgreement](arkts-cryptoarchitecture-cryptoframework-keyagreement-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');
```
