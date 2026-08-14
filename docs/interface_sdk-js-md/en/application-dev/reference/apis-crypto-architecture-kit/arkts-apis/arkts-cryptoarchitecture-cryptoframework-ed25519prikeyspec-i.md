# ED25519PriKeySpec

Defines a child class of [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md#AsyKeySpec) used to specify the parameters of the private key in the Ed25519 algorithm. <br>To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()](arkts-cryptoarchitecture-cryptoframework-createasykeygeneratorbyspec-f.md#createAsyKeyGeneratorBySpec) to create a key generator.

**Inheritance/Implementation:** ED25519PriKeySpec extends [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md#AsyKeySpec)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-cryptoFramework-interface ED25519PriKeySpec--><!--Device-cryptoFramework-interface ED25519PriKeySpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'cryptoFramework';
```

## sk

```TypeScript
sk: bigint
```

Private key **sk** in the Ed25519 algorithm.

**Type:** bigint

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ED25519PriKeySpec-sk: bigint--><!--Device-ED25519PriKeySpec-sk: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

