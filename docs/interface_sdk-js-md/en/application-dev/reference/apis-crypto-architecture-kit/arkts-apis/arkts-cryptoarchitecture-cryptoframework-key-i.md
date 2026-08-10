# Key

密钥（父类），在运行密码算法（如加解密）时需要提前生成其子类对象，并传入[Cipher](arkts-cryptoarchitecture-cryptoframework-cipher-i.md)实例的  
[init()](arkts-cryptoarchitecture-cryptoframework-cipher-i.md#init)方法。

&lt;br&gt;密钥通过子类密钥生成器来生成，详见子类描述。具体子类有：  
[SymKey](arkts-cryptoarchitecture-cryptoframework-symkey-i.md)、[PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md)、  
[PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface Key--><!--Device-cryptoFramework-interface Key-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## getEncoded

```TypeScript
getEncoded(): DataBlob
```

同步方法，获取密钥数据的字节流。密钥可以是对称密钥、公钥或私钥。公钥格式需符合ASN.1语法、X.509规范和DER编码；私钥格式需符合ASN.1语法、PKCS#8规范和DER编码。

> **说明：**
> 
> RSA算法使用密钥参数生成私钥时，私钥对象支持getEncoded。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Key-getEncoded(): DataBlob--><!--Device-Key-getEncoded(): DataBlob-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key
- API version 9 to 11: SystemCapability.Security.CryptoFramework

**Return value:**

| Type | Description |
| --- | --- |
| [DataBlob](arkts-cryptoarchitecture-cryptoframework-datablob-i.md) | 获取的密钥数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | 该操作不支持。 |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateAesKey() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  let symKey = await symKeyGenerator.generateSymKey();
  let encodedKey = symKey.getEncoded();
  console.info('key hex: ' + encodedKey.data);
}
```

## getKeySize

ArkTS-Dyn:
```TypeScript
getKeySize(): number
```

ArkTS-Sta:
```TypeScript
getKeySize(): int
```

获取密钥大小，单位为bits。密钥可以是对称密钥、公钥或私钥。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Key-getKeySize(): int--><!--Device-Key-getKeySize(): int-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 密钥大小，单位为bits。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17630001 | 密码操作错误。 |
| 17620001 | 内存操作失败。 |
| 17620002 | 获取Native对象失败或参数转换失败。 |

## Examples

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateAesKey() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  let symKey = await symKeyGenerator.generateSymKey();
  let symKeyLen = symKey.getKeySize();
  console.info('keysize is: ' + symKeyLen);
}
```

## algName

```TypeScript
readonly algName: string
```

密钥对应的算法名（如果是对称密钥，则含密钥长度，否则不含密钥长度）。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Key-readonly algName: string--><!--Device-Key-readonly algName: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## format

```TypeScript
readonly format: string
```

密钥的格式。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Key-readonly format: string--><!--Device-Key-readonly format: string-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key
- API version 9 to 11: SystemCapability.Security.CryptoFramework

