# PBKDF2Spec

Defines the child class of [KdfSpec](arkts-cryptoarchitecture-cryptoframework-kdfspec-i.md#KdfSpec). It is used as a parameter for PBKDF2 key derivation.

> **NOTE：**
> 
> **password** is the original password. If **password** of the string type is used, pass in the actual data for
> key derivation, rather than a HexString or Base64-encoded value. In addition, the string must be encoded in
> UTF-8, as other encodings may alter the derivation outcome.

**Inheritance/Implementation:** PBKDF2Spec extends [KdfSpec](arkts-cryptoarchitecture-cryptoframework-kdfspec-i.md#KdfSpec)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface PBKDF2Spec extends KdfSpec--><!--Device-cryptoFramework-interface PBKDF2Spec extends KdfSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Kdf
- API version 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## iterations

```TypeScript
iterations: int
```

Number of iterations. The value must be a positive integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PBKDF2Spec-iterations: int--><!--Device-PBKDF2Spec-iterations: int-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Kdf
- API version 11: SystemCapability.Security.CryptoFramework

## keySize

```TypeScript
keySize: int
```

Length of the derived key, in bytes.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PBKDF2Spec-keySize: int--><!--Device-PBKDF2Spec-keySize: int-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Kdf
- API version 11: SystemCapability.Security.CryptoFramework

## password

```TypeScript
password: string | Uint8Array
```

Original password entered by the user.

**Type:** string \| Uint8Array

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PBKDF2Spec-password: string | Uint8Array--><!--Device-PBKDF2Spec-password: string | Uint8Array-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Kdf
- API version 11: SystemCapability.Security.CryptoFramework

## salt

```TypeScript
salt: Uint8Array
```

Salt value.

**Type:** Uint8Array

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PBKDF2Spec-salt: Uint8Array--><!--Device-PBKDF2Spec-salt: Uint8Array-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Kdf
- API version 11: SystemCapability.Security.CryptoFramework

