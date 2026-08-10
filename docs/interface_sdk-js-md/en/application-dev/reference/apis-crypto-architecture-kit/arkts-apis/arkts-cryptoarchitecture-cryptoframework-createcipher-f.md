# createCipher

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## createCipher

```TypeScript
function createCipher(transformation: string): Cipher
```

创建加解密实例。

&lt;br&gt;支持的规格详见[加解密算法规格](../../../security/CryptoArchitectureKit/crypto-encryption-decryption.md)。

> **说明：**
> 
> 1. 在对称加解密中，PKCS #5和PKCS #7的实现方式相同，即补位长度和块大小保持一致。3DES补位为8字节，AES补位为16字节。**NoPadding**
> 表示不进行补位。
> 需要了解不同分组模式的区别，使用正确的参数规格。例如，ECB和CBC模式需要补位，否则需保证明文长度为块大小的整数倍。其他模式建议不补位，
> 此时密文长度和明文长度一致。
> 2. 使用RSA或SM2进行非对称加解密时，需要创建两个**Cipher**对象分别进行加密和解密。对称加解密不需要如此，算法规格相同时，可以使用同
> 一个**Cipher**对象进行加解密。

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
| transformation | string | Yes | 待生成Cipher的算法名称（含密钥长度）、加密模式以及填充方法的组合。&lt;br&gt;支持的规格详见 [对称密钥加解密算法规格](../../../security/CryptoArchitectureKit/crypto-encryption-decryption.md)和 [非对称密钥加解密算法规格](../../../security/CryptoArchitectureKit/crypto-encryption-decryption.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Cipher](arkts-cryptoarchitecture-system-cipher-cipher-c.md) | 返回对应算法的Cipher实例。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | 非法入参。可能的原因： &lt;br&gt;1. 必填参数未指定； &lt;br&gt;2. 参数类型不正确； &lt;br&gt;3. 参数验证失败。 |
| 801 | 该操作不支持。 |
| 17620001 | 内存操作失败。 |

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

