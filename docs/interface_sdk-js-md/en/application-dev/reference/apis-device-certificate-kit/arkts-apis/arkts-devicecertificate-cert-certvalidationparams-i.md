# CertValidationParams

证书验证的参数。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-cert-interface CertValidationParams--><!--Device-cert-interface CertValidationParams-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## allowDownloadIntermediateCa

```TypeScript
allowDownloadIntermediateCa?: boolean
```

是否允许从网络下载中间CA证书。默认值为false。  
- true：当构建证书链缺失中间证书时，尝试使用证书AIA扩展中颁发者地址下载颁发者证书，解决证书链不完整的问题；  
- false：不允许从网络下载中间的CA证书。  
&lt;br&gt;下载地址从证书的AIA扩展中获取，仅支持HTTP。若要使用网络进行下载，需要申请ohos.permission.INTERNET权限。关于权限配置的详细信息，请参见声明权限[Declaring Permissions](../../../security/AccessToken/declare-permissions.md)。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-allowDownloadIntermediateCa?: boolean--><!--Device-CertValidationParams-allowDownloadIntermediateCa?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## date

```TypeScript
date?: string
```

校验日期。格式为YYMMDDHHMMSSZ或YYYYMMDDHHMMSSZ，默认使用当前系统时间。&lt;br&gt;支持自定义验证时间，适用于离线验证历史签名等场景。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-date?: string--><!--Device-CertValidationParams-date?: string-End-->

**System capability:** SystemCapability.Security.Cert

## emailAddresses

```TypeScript
emailAddresses?: Array<string>
```

邮箱地址。验证证书是否包含指定的邮箱地址。最大个数：1，邮箱地址最大长度：128。

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-emailAddresses?: Array<string>--><!--Device-CertValidationParams-emailAddresses?: Array<string>-End-->

**System capability:** SystemCapability.Security.Cert

## hostnames

```TypeScript
hostnames?: Array<string>
```

主机名列表。验证证书的主体备用名（SAN）或通用名（CN）是否包含指定的主机名。最大个数：100，每个主机名最大长度：128。&lt;br&gt;只要匹配其中一个主机名即校验成功。

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-hostnames?: Array<string>--><!--Device-CertValidationParams-hostnames?: Array<string>-End-->

**System capability:** SystemCapability.Security.Cert

## ignoreErrs

```TypeScript
ignoreErrs?: Array<CertResult>
```

允许忽略特定的验证错误。最大个数：8。&lt;br&gt;可忽略的错误包括：ERR_CERT_NOT_YET_VALID、ERR_CERT_HAS_EXPIRED、ERR_UNKNOWN_CRITICAL_EXTENSION、ERR_CRL_NOT_FOUND、ERR_CRL_NOT_YET_VALID、ERR_CRL_HAS_EXPIRED、ERR_OCSP_RESPONSE_NOT_FOUND、ERR_NETWORK_TIMEOUT。

**Type:** Array&lt;CertResult&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-ignoreErrs?: Array<CertResult>--><!--Device-CertValidationParams-ignoreErrs?: Array<CertResult>-End-->

**System capability:** SystemCapability.Security.Cert

## keyUsage

```TypeScript
keyUsage?: Array<KeyUsageType>
```

密钥用途列表。验证证书的密钥用途扩展是否包含指定的用途。最大个数：9。&lt;br&gt;证书必须包含所有指定的密钥用途才校验成功。

**Type:** Array&lt;KeyUsageType&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-keyUsage?: Array<KeyUsageType>--><!--Device-CertValidationParams-keyUsage?: Array<KeyUsageType>-End-->

**System capability:** SystemCapability.Security.Cert

## partialChain

```TypeScript
partialChain?: boolean
```

是否允许部分链验证。默认值为false。  
- true：允许使用信任证书中的任意证书作为信任锚，而非必须追溯到根证书；  
- false：构建证书链时必须追溯到根证书。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-partialChain?: boolean--><!--Device-CertValidationParams-partialChain?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## revokedParams

```TypeScript
revokedParams?: X509CertRevokedParams
```

证书吊销检查参数。用于检查证书是否被吊销。包含CRL列表、OCSP响应数据、是否允许在线检查等配置。

**Type:** [X509CertRevokedParams](arkts-devicecertificate-cert-x509certrevokedparams-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-revokedParams?: X509CertRevokedParams--><!--Device-CertValidationParams-revokedParams?: X509CertRevokedParams-End-->

**System capability:** SystemCapability.Security.Cert

## trustSystemCa

```TypeScript
trustSystemCa?: boolean
```

是否信任系统CA。默认值为false。  
- true：使用系统预置的CA证书库作为信任锚；  
- false：不使用系统预置的CA证书库作为信任锚。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-trustSystemCa?: boolean--><!--Device-CertValidationParams-trustSystemCa?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## trustedCerts

```TypeScript
trustedCerts?: Array<X509Cert>
```

信任证书列表。指定信任的根证书或中间CA证书，作为验证的信任锚点。最大个数：100。&lt;br&gt;验证时，证书链须追溯至信任证书，必须设置此参数或将trustSystemCa设为true。

**Type:** Array&lt;X509Cert&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-trustedCerts?: Array<X509Cert>--><!--Device-CertValidationParams-trustedCerts?: Array<X509Cert>-End-->

**System capability:** SystemCapability.Security.Cert

## untrustedCerts

```TypeScript
untrustedCerts?: Array<X509Cert>
```

非信任证书列表。仅用于构建证书链的中间证书，不作为信任锚点。最大个数：100。

**Type:** Array&lt;X509Cert&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-untrustedCerts?: Array<X509Cert>--><!--Device-CertValidationParams-untrustedCerts?: Array<X509Cert>-End-->

**System capability:** SystemCapability.Security.Cert

## userId

```TypeScript
userId?: Uint8Array
```

用户ID。用于验证国密SM2证书时设置签名验证所需的用户标识符。最大长度：128。&lt;br&gt;国密证书场景最常用的值为  
[0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38]（对应ASCII字符串为"1234567812345678"，16字节）。设置userId后不支持证书吊销检查。

**Type:** Uint8Array

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-userId?: Uint8Array--><!--Device-CertValidationParams-userId?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

## validateDate

```TypeScript
validateDate?: boolean
```

是否校验日期。true：校验证书和CRL有效期；false：不校验证书和CRL有效期。

**Type:** boolean

**Default:** true

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CertValidationParams-validateDate?: boolean--><!--Device-CertValidationParams-validateDate?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

