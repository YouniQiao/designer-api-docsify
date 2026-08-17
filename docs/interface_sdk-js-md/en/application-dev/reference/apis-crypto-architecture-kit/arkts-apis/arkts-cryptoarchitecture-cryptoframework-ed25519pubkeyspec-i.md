# ED25519PubKeySpec

Defines a child class of [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md#asykeyspec) used to specify the parameters of the public key in the Ed25519 algorithm. <br>To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](arkts-cryptoarchitecture-cryptoframework-createasykeygeneratorbyspec-f.md#createasykeygeneratorbyspec) to create a key generator.

**Inheritance/Implementation:** ED25519PubKeySpec extends [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md#asykeyspec)

**Since:** 23

<!--Device-cryptoFramework-interface ED25519PubKeySpec--><!--Device-cryptoFramework-interface ED25519PubKeySpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'cryptoFramework';
```

## pk

```TypeScript
pk: bigint
```

Public key **pk** in the Ed25519 algorithm.

**Type:** bigint

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ED25519PubKeySpec-pk: bigint--><!--Device-ED25519PubKeySpec-pk: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

