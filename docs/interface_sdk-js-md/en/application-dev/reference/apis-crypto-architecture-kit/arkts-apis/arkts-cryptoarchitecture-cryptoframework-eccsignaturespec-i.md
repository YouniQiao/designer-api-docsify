# EccSignatureSpec

Represents the ECC/SM2 signature data that contains (r, s). > **NOTE：**> > **r** and **s** are each 256 bits long.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-cryptoFramework-interface EccSignatureSpec--><!--Device-cryptoFramework-interface EccSignatureSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

## Modules to Import

```TypeScript
import { cryptoFramework } from 'cryptoFramework';
```

## r

```TypeScript
r: bigint
```

Randomized value derived from the elliptic curve calculation using the ephemeral private key during signature generation.

**Type:** bigint

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-EccSignatureSpec-r: bigint--><!--Device-EccSignatureSpec-r: bigint-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

## s

```TypeScript
s: bigint
```

Signature component, computed using the signer's private key, r, and the hashed message.

**Type:** bigint

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-EccSignatureSpec-s: bigint--><!--Device-EccSignatureSpec-s: bigint-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

