# DSACommonParamsSpec

Defines a child class of [AsyKeySpec]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ used to specify the common parameters of the public and private keys in the DSA algorithm. It can be used to randomly generate a public or private key. \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_To generate a key based on key parameters, pass it to [createAsyKeyGeneratorBySpec()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to create a key generator.

**Inheritance/Implementation:** DSACommonParamsSpec extends [AsyKeySpec](arkts-cryptoarchitecture-cryptoframework-asykeyspec-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface DSACommonParamsSpec extends AsyKeySpec--><!--Device-cryptoFramework-interface DSACommonParamsSpec extends AsyKeySpec-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## g

```TypeScript
g: bigint
```

Parameter **g** in the DSA algorithm.

**Type:** bigint

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DSACommonParamsSpec-g: bigint--><!--Device-DSACommonParamsSpec-g: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## p

```TypeScript
p: bigint
```

Prime modulus **p** in the DSA algorithm.

**Type:** bigint

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DSACommonParamsSpec-p: bigint--><!--Device-DSACommonParamsSpec-p: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## q

```TypeScript
q: bigint
```

Parameter **q**, prime factor of (p - 1) in the DSA algorithm.

**Type:** bigint

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DSACommonParamsSpec-q: bigint--><!--Device-DSACommonParamsSpec-q: bigint-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

