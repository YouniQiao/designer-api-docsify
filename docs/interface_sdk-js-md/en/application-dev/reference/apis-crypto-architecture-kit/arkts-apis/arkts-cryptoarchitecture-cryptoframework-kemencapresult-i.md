# KemEncapResult

KEM封装结果。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-cryptoFramework-interface KemEncapResult--><!--Device-cryptoFramework-interface KemEncapResult-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## sharedSecret

```TypeScript
sharedSecret: Uint8Array
```

KEM的共享密钥。

**Type:** Uint8Array

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-KemEncapResult-sharedSecret: Uint8Array--><!--Device-KemEncapResult-sharedSecret: Uint8Array-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

## wrappedKey

```TypeScript
wrappedKey: Uint8Array
```

KEM封装的密钥，即KEM的密文。

**Type:** Uint8Array

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-KemEncapResult-wrappedKey: Uint8Array--><!--Device-KemEncapResult-wrappedKey: Uint8Array-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Cipher

