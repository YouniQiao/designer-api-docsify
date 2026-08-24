# CmacSpec

Represents the child class of [MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md). It is used as an input parameter for CMAC computation.

> **NOTE：**&gt;
> **cipherName** specifies the symmetric cipher algorithm used by CMAC. It is mandatory.

**Inheritance/Implementation:** CmacSpec extends [MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md)

**Since:** 23

<!--Device-cryptoFramework-interface CmacSpec--><!--Device-cryptoFramework-interface CmacSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## cipherName

```TypeScript
cipherName: string
```

Symmetric cipher algorithm used by CMAC.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CmacSpec-cipherName: string--><!--Device-CmacSpec-cipherName: string-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

