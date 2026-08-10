# EccSignatureSpec

包含（r、s）的ECC/SM2签名数据的对象。

> **说明：**
> 
> r和s的长度各为256位。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface EccSignatureSpec--><!--Device-cryptoFramework-interface EccSignatureSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## r

```TypeScript
r: bigint
```

r分量。

**Type:** bigint

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-EccSignatureSpec-r: bigint--><!--Device-EccSignatureSpec-r: bigint-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

## s

```TypeScript
s: bigint
```

s分量。

**Type:** bigint

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-EccSignatureSpec-s: bigint--><!--Device-EccSignatureSpec-s: bigint-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Signature

