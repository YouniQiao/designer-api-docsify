# createKdf

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## createKdf

```TypeScript
function createKdf(algName: string): Kdf
```

Creates a key derivation function instance.

&lt;br&gt;For details about the supported specifications, see  
 [Key Derivation Function Specifications](../../../security/CryptoArchitectureKit/crypto-key-derivation-overview.md).

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cryptoFramework-function createKdf(algName: string): Kdf--><!--Device-cryptoFramework-function createKdf(algName: string): Kdf-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Kdf
- API version 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| algName | string | Yes | Key derivation algorithm (including the hash function for the HMAC). Currently, PBKDF2, HKDF, SCRYPT, and X963KDF are supported. For example, **PBKDF2\|SHA256**, **HKDF\|SHA256**, **SCRYPT**, and **X963KDF\|

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Kdf](arkts-cryptoarchitecture-cryptoframework-kdf-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [17620001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) |

## Examples

PBKDF2

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
```
