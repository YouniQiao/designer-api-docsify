# ECFieldFp

指定椭圆曲线的素数域。是[ECField](arkts-cryptoarchitecture-cryptoframework-ecfield-i.md)的子类。

**Inheritance/Implementation:** ECFieldFp extends [ECField](arkts-cryptoarchitecture-cryptoframework-ecfield-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface ECFieldFp extends ECField--><!--Device-cryptoFramework-interface ECFieldFp extends ECField-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## p

```TypeScript
p: bigint
```

指定素数p的值。

**Type:** bigint

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ECFieldFp-p: bigint--><!--Device-ECFieldFp-p: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

