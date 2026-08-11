# X963KdfSpec

Defines the child class of [KdfSpec](arkts-cryptoarchitecture-cryptoframework-kdfspec-i.md). It is a parameter for X963KDF key derivation function (KDF).

> **NOTE：**
> 
> **key** is the original key material entered by the user.

**Inheritance/Implementation:** X963KdfSpec extends [KdfSpec](arkts-cryptoarchitecture-cryptoframework-kdfspec-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface X963KdfSpec extends KdfSpec--><!--Device-cryptoFramework-interface X963KdfSpec extends KdfSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## info

```TypeScript
info: Uint8Array
```

Shared information.

**Type:** Uint8Array

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-X963KdfSpec-info: Uint8Array--><!--Device-X963KdfSpec-info: Uint8Array-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

## key

```TypeScript
key: string | Uint8Array
```

Key material.

**Type:** string \| Uint8Array

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-X963KdfSpec-key: string | Uint8Array--><!--Device-X963KdfSpec-key: string | Uint8Array-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

## keySize

```TypeScript
keySize: int
```

Length of the derived key, in bytes.The value must be a positive integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-X963KdfSpec-keySize: int--><!--Device-X963KdfSpec-keySize: int-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Kdf

