# AsyKeySpecType

表示密钥参数类型的枚举。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-enum AsyKeySpecType--><!--Device-cryptoFramework-enum AsyKeySpecType-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## COMMON_PARAMS_SPEC

```TypeScript
COMMON_PARAMS_SPEC = 0
```

表示公私钥中包含的公共参数。使用此类型的参数可以调用  
[generateKeyPair](arkts-cryptoarchitecture-cryptoframework-asykeygeneratorbyspec-i.md#generatekeypair)随机生成密钥对。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyKeySpecType-COMMON_PARAMS_SPEC = 0--><!--Device-AsyKeySpecType-COMMON_PARAMS_SPEC = 0-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## PRIVATE_KEY_SPEC

```TypeScript
PRIVATE_KEY_SPEC = 1
```

表示私钥中包含的参数。使用此类型的参数可以调用  
[generatePriKey](arkts-cryptoarchitecture-cryptoframework-asykeygeneratorbyspec-i.md#generateprikey)生成指定的私钥。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyKeySpecType-PRIVATE_KEY_SPEC = 1--><!--Device-AsyKeySpecType-PRIVATE_KEY_SPEC = 1-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## PUBLIC_KEY_SPEC

```TypeScript
PUBLIC_KEY_SPEC = 2
```

表示公钥中包含的参数。使用此类型的参数可以调用  
[generatePubKey](arkts-cryptoarchitecture-cryptoframework-asykeygeneratorbyspec-i.md#generatepubkey)生成指定的公钥。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyKeySpecType-PUBLIC_KEY_SPEC = 2--><!--Device-AsyKeySpecType-PUBLIC_KEY_SPEC = 2-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

## KEY_PAIR_SPEC

```TypeScript
KEY_PAIR_SPEC = 3
```

表示公私钥中包含的全量参数。使用此类型的参数可以调用  
[generateKeyPair](arkts-cryptoarchitecture-cryptoframework-asykeygeneratorbyspec-i.md#generatekeypair)生成指定的密钥对。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AsyKeySpecType-KEY_PAIR_SPEC = 3--><!--Device-AsyKeySpecType-KEY_PAIR_SPEC = 3-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 10 to 11: SystemCapability.Security.CryptoFramework

