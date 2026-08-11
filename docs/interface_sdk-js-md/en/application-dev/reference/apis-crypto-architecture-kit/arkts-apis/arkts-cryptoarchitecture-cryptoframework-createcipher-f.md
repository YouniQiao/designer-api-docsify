# createCipher

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## createCipher

```TypeScript
function createCipher(transformation: string): Cipher
```

Creates a **Cipher** instance.

&lt;br&gt;For details about the supported specifications, see[Encryption and Decryption Algorithm Specifications](../../../security/CryptoArchitectureKit/crypto-encryption-decryption.md).

> **NOTE：**
> 
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

<!--Device-cryptoFramework-function createCipher(transformation: string): Cipher--><!--Device-cryptoFramework-function createCipher(transformation: string): Cipher-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Cipher
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transformation | string | Yes | Combination of the algorithm name (including the key length), encryption mode, and padding algorithm of the **Cipher** instance to create.&lt;br&gt;For details about the supported specifications, see [Symmetric Key Encryption and Decryption Algorithm Specifications](../../../security/CryptoArchitectureKit/crypto-encryption-decryption.md) and [Asymmetric Key Encryption and Decryption Algorithm Specifications](../../../security/CryptoArchitectureKit/crypto-encryption-decryption.md) . |

**Return value:**

| Type | Description |
| --- | --- |
| [Cipher](arkts-cryptoarchitecture-system-cipher-cipher-c.md) | Returns the **Cipher** instance corresponding to the specified algorithm. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameters. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | This operation is not supported. |
| [17620001](../errorcode-crypto-framework.md#17620001-memory-operation-failed) | Memory operation failed. |

## Examples

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

