# createCipher

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## createCipher

```TypeScript
function createCipher(transformation: string): Cipher
```

Creates a **Cipher** instance.<br>For details about the supported specifications, seeEncryption and Decryption Algorithm Specifications.

> **NOTE：**&gt;
> 1. In symmetric encryption and decryption, PKCS #5 and PKCS #7 share the same implementation, with padding
> length and block size remaining consistent. In 3DES, padding is applied in 8-byte blocks; in AES, padding
> is applied in 16-byte blocks. **NoPadding** means no padding is applied.
> You need to understand the differences between different block cipher modes and use the correct parameter
> specifications. For example, padding is required for ECB and CBC. Otherwise, ensure that the plaintext
> length is an integer multiple of the block size. No padding is recommended for other modes. In this case,
> the ciphertext length is the same as the plaintext length.
> 2. When RSA or SM2 is used for asymmetric encryption and decryption, two **Cipher** objects must be created
> to perform encryption and decryption separately. This is not required for symmetric encryption and
> decryption. If the algorithm specifications are the same, the same **Cipher** object can be used for
> encryption and decryption.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transformation | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Cipher](arkts-cryptoarchitecture-system-cipher-cipher-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) |

**Examples**

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let cipherAlgName = '3DES192|ECB|PKCS7';
try {
  let cipher = cryptoFramework.createCipher(cipherAlgName);
  console.info('cipher algName: ' + cipher.algName);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```
