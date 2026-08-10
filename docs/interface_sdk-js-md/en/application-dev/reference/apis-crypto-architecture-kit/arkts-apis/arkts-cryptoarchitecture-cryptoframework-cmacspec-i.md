# CmacSpec

消息认证码参数[MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md)的子类，作为CMAC计算的输入。

> **说明：**
> 
> cipherName是必选参数，表示CMAC使用的对称密码算法。

**Inheritance/Implementation:** CmacSpec extends [MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface CmacSpec extends MacSpec--><!--Device-cryptoFramework-interface CmacSpec extends MacSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## cipherName

```TypeScript
cipherName: string
```

CMAC使用的对称密码算法名。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CmacSpec-cipherName: string--><!--Device-CmacSpec-cipherName: string-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

