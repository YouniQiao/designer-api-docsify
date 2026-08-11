# Cipher

提供加解密接口。

**起始版本：** 3

**废弃版本：** 9

**替代接口：** ohos.security.cryptoFramework.Cipher

<!--Device-unnamed-export default class Cipher--><!--Device-unnamed-export default class Cipher-End-->

**系统能力：** SystemCapability.Security.Cipher

## aes

```TypeScript
static aes(options: CipherAesOptions): void
```

使用AES对数据进行加密或解密。

**起始版本：** 3

**废弃版本：** 9

**替代接口：** ohos.security.cryptoFramework.Cipher

<!--Device-Cipher-static aes(options: CipherAesOptions): void--><!--Device-Cipher-static aes(options: CipherAesOptions): void-End-->

**系统能力：** SystemCapability.Security.Cipher

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [CipherAesOptions](arkts-cryptoarchitecture-system-cipher-cipheraesoptions-i.md) | 是 |

## rsa

```TypeScript
static rsa(options: CipherRsaOptions): void
```

使用RSA对数据进行加密或解密。

**起始版本：** 3

**废弃版本：** 9

**替代接口：** ohos.security.cryptoFramework.Cipher

<!--Device-Cipher-static rsa(options: CipherRsaOptions): void--><!--Device-Cipher-static rsa(options: CipherRsaOptions): void-End-->

**系统能力：** SystemCapability.Security.Cipher

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [CipherRsaOptions](arkts-cryptoarchitecture-system-cipher-cipherrsaoptions-i.md) | 是 |
