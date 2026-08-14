# ECCPubKeySpec

Defines a child class of [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md#AsyKeySpec) used to specify the parameters of the public key in the ECC algorithm. <br>To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](arkts-cryptoarchitecture-cryptoframework-createasykeygeneratorbyspec-f.md#createAsyKeyGeneratorBySpec) to create a key generator.

**Inheritance/Implementation:** ECCPubKeySpec extends [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md#AsyKeySpec)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-cryptoFramework-interface ECCPubKeySpec--><!--Device-cryptoFramework-interface ECCPubKeySpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'cryptoFramework';
```

## params

```TypeScript
params: ECCCommonParamsSpec
```

Common parameters of the public and private keys in the ECC algorithm.

**Type:** [ECCCommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ECCPubKeySpec-params: ECCCommonParamsSpec--><!--Device-ECCPubKeySpec-params: ECCCommonParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## pk

```TypeScript
pk: Point
```

Public key **pk** in the ECC algorithm.

**Type:** Point

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ECCPubKeySpec-pk: Point--><!--Device-ECCPubKeySpec-pk: Point-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

