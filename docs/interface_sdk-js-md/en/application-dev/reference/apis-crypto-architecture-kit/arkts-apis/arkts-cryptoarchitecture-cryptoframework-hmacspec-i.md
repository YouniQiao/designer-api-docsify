# HmacSpec

Represents the child class of [MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md#macspec). It is used as an input parameter for HMAC computation. > **NOTE：**> > **mdName** specifies the HMAC message digest algorithm. It is mandatory.

**Inheritance/Implementation:** HmacSpec extends [MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md#macspec)

**Since:** 23

<!--Device-cryptoFramework-interface HmacSpec--><!--Device-cryptoFramework-interface HmacSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## mdName

```TypeScript
mdName: string
```

Message digest algorithm.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-HmacSpec-mdName: string--><!--Device-HmacSpec-mdName: string-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

