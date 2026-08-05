# ED25519PubKeySpec

Defines a child class of [AsyKeySpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ used to specify the parameters of the public key in the Ed25519 algorithm. \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to create a key generator.

**Inheritance/Implementation:** ED25519PubKeySpec extends [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface ED25519PubKeySpec extends AsyKeySpec--><!--Device-cryptoFramework-interface ED25519PubKeySpec extends AsyKeySpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

## pk

```TypeScript
pk: bigint
```

Public key **pk** in the Ed25519 algorithm.

**Type:** bigint

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ED25519PubKeySpec-pk: bigint--><!--Device-ED25519PubKeySpec-pk: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

