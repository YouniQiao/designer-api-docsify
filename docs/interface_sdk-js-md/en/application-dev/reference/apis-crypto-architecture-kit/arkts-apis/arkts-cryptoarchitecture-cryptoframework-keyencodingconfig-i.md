# KeyEncodingConfig

RSA私钥编码参数，使用获取私钥字符串时，可以添加此参数，生成指定算法、密码的编码后的私钥字符串。

> **说明：**
> 
> - password是必选参数，表示编码用到的密码。
> 
> - cipherName是必选参数，指定编码用到的算法。当前仅支持AES-128-CBC、AES-192-CBC、AES-256-CBC、DES-EDE3-CBC。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cryptoFramework-interface KeyEncodingConfig--><!--Device-cryptoFramework-interface KeyEncodingConfig-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

## Modules to Import

```TypeScript
import { cryptoFramework } from 'kits/@kit.CryptoArchitectureKit';
```

## cipherName

```TypeScript
cipherName: string
```

用于编码私钥的对称密码算法。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-KeyEncodingConfig-cipherName: string--><!--Device-KeyEncodingConfig-cipherName: string-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

## password

```TypeScript
password: string
```

密码。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-KeyEncodingConfig-password: string--><!--Device-KeyEncodingConfig-password: string-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

