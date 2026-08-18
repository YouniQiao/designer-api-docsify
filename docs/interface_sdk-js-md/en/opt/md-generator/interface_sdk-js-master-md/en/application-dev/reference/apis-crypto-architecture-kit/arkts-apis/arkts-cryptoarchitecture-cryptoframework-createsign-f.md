# createSign

## Modules to Import

```TypeScript
```

## createSign

```TypeScript
function createSign(algName: string): Sign
```

Creates a **Sign** instance. <br>For details about the supported specifications, see [Signing and Signature Verification Overview and Algorithm Specifications](../../../security/CryptoArchitectureKit/crypto-sign-sig-verify-overview.md).

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cryptoFramework-function createSign(algName: string): Sign--><!--Device-cryptoFramework-function createSign(algName: string): Sign-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Signature
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| algName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Sign](arkts-cryptoarchitecture-cryptoframework-sign-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let signer1 = cryptoFramework.createSign('RSA1024|PKCS1|SHA256');

let signer2 = cryptoFramework.createSign('RSA1024|PSS|SHA256|MGF1_SHA256');

let signer3 = cryptoFramework.createSign('ECC224|SHA256');

let signer4 = cryptoFramework.createSign('DSA2048|SHA256');

let signer5 = cryptoFramework.createSign('RSA1024|PKCS1|SHA256|OnlySign');
```
