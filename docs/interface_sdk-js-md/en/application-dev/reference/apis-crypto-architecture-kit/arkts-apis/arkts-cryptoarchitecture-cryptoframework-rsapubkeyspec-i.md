# RSAPubKeySpec

Defines a child class of [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md) used to specify the parameters of the public key in the RSA algorithm.

&lt;br&gt;To generate a key based on key parameters, pass it to  
[createAsyKeyGeneratorBySpec()](arkts-cryptoarchitecture-cryptoframework-createasykeygeneratorbyspec-f.md#createasykeygeneratorbyspec) to create a key generator.

**Inheritance/Implementation:** RSAPubKeySpec extends [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface RSAPubKeySpec extends AsyKeySpec--><!--Device-cryptoFramework-interface RSAPubKeySpec extends AsyKeySpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## params

```TypeScript
params: RSACommonParamsSpec
```

Common parameters of the public and private keys in the RSA algorithm.

**Type:** [RSACommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-rsacommonparamsspec-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RSAPubKeySpec-params: RSACommonParamsSpec--><!--Device-RSAPubKeySpec-params: RSACommonParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## pk

```TypeScript
pk: bigint
```

Public key **pk** in the RSA algorithm.

**Type:** bigint

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RSAPubKeySpec-pk: bigint--><!--Device-RSAPubKeySpec-pk: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

