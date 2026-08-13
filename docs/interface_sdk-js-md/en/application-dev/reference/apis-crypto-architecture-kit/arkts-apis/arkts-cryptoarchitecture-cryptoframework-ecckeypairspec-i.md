# ECCKeyPairSpec

Defines a child class of [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md#AsyKeySpec) used to specify full parameters of the public and private keys in the ECC algorithm. &lt;br&gt;To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](arkts-cryptoarchitecture-cryptoframework-createasykeygeneratorbyspec-f.md#createAsyKeyGeneratorBySpec) to create a key generator.

**Inheritance/Implementation:** ECCKeyPairSpec extends [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md#AsyKeySpec)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-cryptoFramework-interface ECCKeyPairSpec--><!--Device-cryptoFramework-interface ECCKeyPairSpec-End-->

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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ECCKeyPairSpec-params: ECCCommonParamsSpec--><!--Device-ECCKeyPairSpec-params: ECCCommonParamsSpec-End-->

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

<!--Device-ECCKeyPairSpec-pk: Point--><!--Device-ECCKeyPairSpec-pk: Point-End-->

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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ECCKeyPairSpec-sk: bigint--><!--Device-ECCKeyPairSpec-sk: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

