# createSign

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## createSign

```TypeScript
function createSign(algName: string): Sign
```

Creates a **Sign** instance.

&lt;br&gt;For details about the supported specifications, see  
 [Signing and Signature Verification Overview and Algorithm Specifications](../../../security/CryptoArchitectureKit/crypto-sign-sig-verify-overview.md).

**Since:** 9

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [17620001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let signer1 = cryptoFramework.createSign('RSA1024|PKCS1|SHA256');

let signer2 = cryptoFramework.createSign('RSA1024|PSS|SHA256|MGF1_SHA256');

let signer3 = cryptoFramework.createSign('ECC224|SHA256');

let signer4 = cryptoFramework.createSign('DSA2048|SHA256');

let signer5 = cryptoFramework.createSign('RSA1024|PKCS1|SHA256|OnlySign');
```
