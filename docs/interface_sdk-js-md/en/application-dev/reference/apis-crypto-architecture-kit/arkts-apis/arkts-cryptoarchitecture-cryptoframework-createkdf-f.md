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

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cryptoFramework-function createKdf(algName: string): Kdf--><!--Device-cryptoFramework-function createKdf(algName: string): Kdf-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Kdf
- API version 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| algName | string | Yes | Key derivation algorithm (including the hash function for the HMAC). Currently, PBKDF2, HKDF, SCRYPT, and X963KDF are supported. For example, **PBKDF2\|SHA256**, **HKDF\|SHA256**, **SCRYPT**, and **X963KDF\|SHA256**.&lt;br&gt;For details about the supported specifications, see [Key Derivation Function Specifications](../../../security/CryptoArchitectureKit/crypto-key-derivation-overview.md). |

**Return value:**

| Type | Description |
| --- | --- |
| [Kdf](arkts-cryptoarchitecture-cryptoframework-kdf-i.md) | Returns the **Kdf** instance corresponding to the specified algorithm. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | This operation is not supported. |
| [17620001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-crypto-architecture-kit/errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |

## Examples

PBKDF2

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
```

