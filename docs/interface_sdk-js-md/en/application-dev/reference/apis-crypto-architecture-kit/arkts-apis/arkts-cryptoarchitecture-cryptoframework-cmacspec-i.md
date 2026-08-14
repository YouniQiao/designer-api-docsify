# CmacSpec

Represents the child class of [MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md#MacSpec). It is used as an input parameter for CMAC computation. > **NOTE：**> > **cipherName** specifies the symmetric cipher algorithm used by CMAC. It is mandatory.

**Inheritance/Implementation:** CmacSpec extends [MacSpec](arkts-cryptoarchitecture-cryptoframework-macspec-i.md#MacSpec)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-cryptoFramework-interface CmacSpec--><!--Device-cryptoFramework-interface CmacSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

## Modules to Import

```TypeScript
import { cryptoFramework } from 'cryptoFramework';
```

## cipherName

```TypeScript
cipherName: string
```

Symmetric cipher algorithm used by CMAC.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CmacSpec-cipherName: string--><!--Device-CmacSpec-cipherName: string-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

