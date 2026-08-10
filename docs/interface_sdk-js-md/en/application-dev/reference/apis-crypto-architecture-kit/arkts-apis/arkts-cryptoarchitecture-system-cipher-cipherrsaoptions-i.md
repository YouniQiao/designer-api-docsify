# CipherRsaOptions

调用cipher rsa方法时，传入的参数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 11

**Substitutes:** ohos.security.cryptoFramework.Cipher

<!--Device-unnamed-export interface CipherRsaOptions--><!--Device-unnamed-export interface CipherRsaOptions-End-->

**System capability:** SystemCapability.Security.Cipher

## Modules to Import

```TypeScript
import { CipherAesOptions, CipherResponse, CipherRsaOptions } from 'kits/@kit.CryptoArchitectureKit';
```

## complete

```TypeScript
complete: () => void
```

接口调用结束的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 11

**Substitutes:** ohos.security.cryptoFramework.Cipher

<!--Device-CipherRsaOptions-complete: () => void--><!--Device-CipherRsaOptions-complete: () => void-End-->

**System capability:** SystemCapability.Security.Cipher

## fail

```TypeScript
fail: (data: string, code: number) => void
```

接口调用失败的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 11

**Substitutes:** ohos.security.cryptoFramework.Cipher

<!--Device-CipherRsaOptions-fail: (data: string, code: number) => void--><!--Device-CipherRsaOptions-fail: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Security.Cipher

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success: (data: CipherResponse) => void
```

接口调用成功的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 11

**Substitutes:** ohos.security.cryptoFramework.Cipher

<!--Device-CipherRsaOptions-success: (data: CipherResponse) => void--><!--Device-CipherRsaOptions-success: (data: CipherResponse) => void-End-->

**System capability:** SystemCapability.Security.Cipher

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [CipherResponse](arkts-cryptoarchitecture-system-cipher-cipherresponse-i.md) | Yes |  |

## action

```TypeScript
action: string
```

加解密操作类型，可选项有：

1. encrypt 加密；2. decrypt 解密。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 11

**Substitutes:** ohos.security.cryptoFramework.Cipher

<!--Device-CipherRsaOptions-action: string--><!--Device-CipherRsaOptions-action: string-End-->

**System capability:** SystemCapability.Security.Cipher

## key

```TypeScript
key: string
```

加解密使用的RSA密钥。加密时key为公钥，解密时key为私钥。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 11

**Substitutes:** ohos.security.cryptoFramework.Cipher

<!--Device-CipherRsaOptions-key: string--><!--Device-CipherRsaOptions-key: string-End-->

**System capability:** SystemCapability.Security.Cipher

## text

```TypeScript
text: string
```

待加密或解密的文本内容。待加密的文本内容应该是一段普通文本，长度不能超过keySize / 8 - 66，其中keySize是密钥的长度（例如密钥长度为1024时，text不能超过62个字节）。待解密的文本内容应该是经过base64编码的一段二进制值。base64编码使用默认风格。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 11

**Substitutes:** ohos.security.cryptoFramework.Cipher

<!--Device-CipherRsaOptions-text: string--><!--Device-CipherRsaOptions-text: string-End-->

**System capability:** SystemCapability.Security.Cipher

## transformation

```TypeScript
transformation?: string
```

RSA算法的填充项，默认为RSA/None/OAEPWithSHA256AndMGF1Padding。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 11

**Substitutes:** ohos.security.cryptoFramework.Cipher

<!--Device-CipherRsaOptions-transformation?: string--><!--Device-CipherRsaOptions-transformation?: string-End-->

**System capability:** SystemCapability.Security.Cipher

