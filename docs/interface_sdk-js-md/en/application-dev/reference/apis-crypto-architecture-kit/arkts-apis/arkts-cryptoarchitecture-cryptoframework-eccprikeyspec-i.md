# ECCPriKeySpec

Defines a child class of [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md) used to specify the parameters of the private key in the ECC algorithm.

<br>To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](arkts-cryptoarchitecture-cryptoframework-createasykeygeneratorbyspec-f.md) to create a key generator.

**Inheritance/Implementation:** ECCPriKeySpec extends [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md)

**Since:** 23

<!--Device-cryptoFramework-interface ECCPriKeySpec--><!--Device-cryptoFramework-interface ECCPriKeySpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

## params

```TypeScript
params: ECCCommonParamsSpec
```

Common parameters of the public and private keys in the ECC algorithm.

**Type:** [ECCCommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ECCPriKeySpec-params: ECCCommonParamsSpec--><!--Device-ECCPriKeySpec-params: ECCCommonParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## sk

```TypeScript
sk: bigint
```

Private key **sk** in the ECC algorithm.

**Type:** bigint

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ECCPriKeySpec-sk: bigint--><!--Device-ECCPriKeySpec-sk: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

