# KeyPair

非对称密钥对包含公钥和私钥。

&lt;br&gt;可以通过非对称密钥生成器[AsyKeyGenerator](arkts-cryptoarchitecture-cryptoframework-asykeygenerator-i.md)、  
[AsyKeyGeneratorBySpec](arkts-cryptoarchitecture-cryptoframework-asykeygeneratorbyspec-i.md)来生成。

> **说明：**
> 
> KeyPair对象中的pubKey对象和priKey对象是KeyPair对象的成员。当KeyPair对象超出作用域时，其内部的pubKey对象和priKey对象将被析构。
> 
> 业务方使用时应持有KeyPair对象的引用，而非内部pubKey或priKey对象的引用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface KeyPair--><!--Device-cryptoFramework-interface KeyPair-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## priKey

```TypeScript
readonly priKey: PriKey
```

私钥。

**Type:** [PriKey](arkts-cryptoarchitecture-cryptoframework-prikey-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyPair-readonly priKey: PriKey--><!--Device-KeyPair-readonly priKey: PriKey-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

## pubKey

```TypeScript
readonly pubKey: PubKey
```

公钥。

**Type:** [PubKey](arkts-cryptoarchitecture-cryptoframework-pubkey-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyPair-readonly pubKey: PubKey--><!--Device-KeyPair-readonly pubKey: PubKey-End-->

**System capability:** 
- API version 12 and later: SystemCapability.Security.CryptoFramework.Key.AsymKey
- API version 9 to 11: SystemCapability.Security.CryptoFramework

