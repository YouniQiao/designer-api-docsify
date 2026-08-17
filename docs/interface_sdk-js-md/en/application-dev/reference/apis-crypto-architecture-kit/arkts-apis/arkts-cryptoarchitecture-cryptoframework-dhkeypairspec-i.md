# DHKeyPairSpec

Defines a child class of [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md#asykeyspec) used to specify full parameters of the public and private keys in the DH algorithm. <br>To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](arkts-cryptoarchitecture-cryptoframework-createasykeygeneratorbyspec-f.md#createasykeygeneratorbyspec) to create a key generator.

**Inheritance/Implementation:** DHKeyPairSpec extends [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md#asykeyspec)

**Since:** 23

<!--Device-cryptoFramework-interface DHKeyPairSpec--><!--Device-cryptoFramework-interface DHKeyPairSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'cryptoFramework';
```

## params

```TypeScript
params: DHCommonParamsSpec
```

Common parameters of the public and private keys in the DH algorithm.

**Type:** [DHCommonParamsSpec](arkts-cryptoarchitecture-cryptoframework-dhcommonparamsspec-i.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DHKeyPairSpec-params: DHCommonParamsSpec--><!--Device-DHKeyPairSpec-params: DHCommonParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

## pk

```TypeScript
pk: bigint
```

Public key **pk** in the DH algorithm.

**Type:** bigint

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DHKeyPairSpec-pk: bigint--><!--Device-DHKeyPairSpec-pk: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

## sk

```TypeScript
sk: bigint
```

Private key **sk** in the DH algorithm.

**Type:** bigint

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DHKeyPairSpec-sk: bigint--><!--Device-DHKeyPairSpec-sk: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

