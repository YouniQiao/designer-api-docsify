# KeyEncodingConfig

Represents the RSA private key encoding parameters. You can use it to generate an encoded private key string with the specified algorithm and password. > **NOTE：**> > - **password** specifies the password used for encoding the private key. It is mandatory. > > - **cipherName** specifies the algorithm used for encoding. It is mandatory. Currently, only **AES-128-CBC**, > **AES-192-CBC**, **AES-256-CBC**, and **DES-EDE3-CBC** are supported.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-cryptoFramework-interface KeyEncodingConfig--><!--Device-cryptoFramework-interface KeyEncodingConfig-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

## Modules to Import

```TypeScript
import { cryptoFramework } from 'cryptoFramework';
```

## cipherName

```TypeScript
cipherName: string
```

Symmetric cipher algorithm used for encoding the private key.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyEncodingConfig-cipherName: string--><!--Device-KeyEncodingConfig-cipherName: string-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

## password

```TypeScript
password: string
```

Password used for encoding the private key.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-KeyEncodingConfig-password: string--><!--Device-KeyEncodingConfig-password: string-End-->

**System capability:** SystemCapability.Security.CryptoFramework.Key.AsymKey

