# Cipher

Defines the cipher functions.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** ohos.security.cryptoFramework.Cipher

<!--Device-unnamed-export default class Cipher--><!--Device-unnamed-export default class Cipher-End-->

**System capability:** SystemCapability.Security.Cipher

## Modules to Import

```TypeScript
import { CipherAesOptions, CipherResponse, CipherRsaOptions } from 'kits/@kit.CryptoArchitectureKit';
```

## aes

```TypeScript
static aes(options: CipherAesOptions): void
```

Encrypts or decrypts data using AES.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** ohos.security.cryptoFramework.Cipher

<!--Device-Cipher-static aes(options: CipherAesOptions): void--><!--Device-Cipher-static aes(options: CipherAesOptions): void-End-->

**System capability:** SystemCapability.Security.Cipher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [CipherAesOptions](arkts-cryptoarchitecture-system-cipher-cipheraesoptions-i.md) | Yes |

## rsa

```TypeScript
static rsa(options: CipherRsaOptions): void
```

Encrypts or decrypts data using RSA.

**Since:** 3

**Deprecated since:** 9

**Substitutes:** ohos.security.cryptoFramework.Cipher

<!--Device-Cipher-static rsa(options: CipherRsaOptions): void--><!--Device-Cipher-static rsa(options: CipherRsaOptions): void-End-->

**System capability:** SystemCapability.Security.Cipher

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [CipherRsaOptions](arkts-cryptoarchitecture-system-cipher-cipherrsaoptions-i.md) | Yes |
