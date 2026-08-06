# DHPriKeySpec

Defines a child class of [AsyKeySpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ used to specify the parameters of the private key in the DH algorithm.

\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_To generate a key based on key parameters, pass it to  
[createAsyKeyGeneratorBySpec()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to create a key generator.

**Inheritance/Implementation:** DHPriKeySpec extends [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface DHPriKeySpec extends AsyKeySpec--><!--Device-cryptoFramework-interface DHPriKeySpec extends AsyKeySpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

## params

```TypeScript
params: DHCommonParamsSpec
```

Common parameters of the public and private keys in the DH algorithm.

**Type:** DHCommonParamsSpec

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DHPriKeySpec-params: DHCommonParamsSpec--><!--Device-DHPriKeySpec-params: DHCommonParamsSpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

## sk

```TypeScript
sk: bigint
```

Private key **sk** in the DH algorithm.

**Type:** bigint

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DHPriKeySpec-sk: bigint--><!--Device-DHPriKeySpec-sk: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 11: SystemCapability.Security.CryptoFramework

