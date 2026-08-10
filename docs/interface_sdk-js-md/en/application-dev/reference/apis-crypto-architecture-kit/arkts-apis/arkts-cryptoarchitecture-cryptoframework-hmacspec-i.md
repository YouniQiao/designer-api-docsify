# HmacSpec

消息认证码参数[MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md)的子类，作为HMAC计算的输入。

> **说明：**
> 
> mdName是必选参数，表示HMAC摘要算法。

**Inheritance/Implementation:** HmacSpec extends [MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface HmacSpec extends MacSpec--><!--Device-cryptoFramework-interface HmacSpec extends MacSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## mdName

```TypeScript
mdName: string
```

摘要算法名。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-HmacSpec-mdName: string--><!--Device-HmacSpec-mdName: string-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

