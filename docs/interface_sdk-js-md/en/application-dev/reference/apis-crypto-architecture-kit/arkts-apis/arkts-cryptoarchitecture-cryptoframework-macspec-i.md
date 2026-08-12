# MacSpec

Represents the message authentication code (MAC) parameters. You need to construct a child class object and use it as a parameter when computing an HMAC or a CMAC.

> **NOTE：**
> 
> **algName** specifies the MAC algorithm to use. It is mandatory.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface MacSpec--><!--Device-cryptoFramework-interface MacSpec-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## algName

```TypeScript
algName: string
```

Algorithm to use.

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MacSpec-algName: string--><!--Device-MacSpec-algName: string-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Mac

