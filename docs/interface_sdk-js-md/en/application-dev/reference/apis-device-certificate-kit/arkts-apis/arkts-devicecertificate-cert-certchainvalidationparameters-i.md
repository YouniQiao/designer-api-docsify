# CertChainValidationParameters

表示证书链校验的参数。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cert-interface CertChainValidationParameters--><!--Device-cert-interface CertChainValidationParameters-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## allowDownloadIntermediateCa

```TypeScript
allowDownloadIntermediateCa?: boolean
```

表示是否允许尝试从网络下载缺失的中间CA证书。 true表示允许；false表示不允许。默认值为false。&lt;br&gt;下载地址将从证书AIA扩展中获取，仅支持http，如需使用网络下载，需申请ohos.permission.INTERNET权限。配置方式请参见  
[声明权限](../../../security/AccessToken/declare-permissions.md)。

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CertChainValidationParameters-allowDownloadIntermediateCa?: boolean--><!--Device-CertChainValidationParameters-allowDownloadIntermediateCa?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## certCRLs

```TypeScript
certCRLs?: Array<CertCRLCollection>
```

用于检查证书是否被吊销的CRL集合。

**Type:** Array&lt;CertCRLCollection&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainValidationParameters-certCRLs?: Array<CertCRLCollection>--><!--Device-CertChainValidationParameters-certCRLs?: Array<CertCRLCollection>-End-->

**System capability:** SystemCapability.Security.Cert

## date

```TypeScript
date?: string
```

用于检查证书有效性的日期。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainValidationParameters-date?: string--><!--Device-CertChainValidationParameters-date?: string-End-->

**System capability:** SystemCapability.Security.Cert

## keyUsage

```TypeScript
keyUsage?: Array<KeyUsageType>
```

表示需要校验证书中的密钥用途。

**Type:** Array&lt;KeyUsageType&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainValidationParameters-keyUsage?: Array<KeyUsageType>--><!--Device-CertChainValidationParameters-keyUsage?: Array<KeyUsageType>-End-->

**System capability:** SystemCapability.Security.Cert

## policy

```TypeScript
policy?: ValidationPolicyType
```

表示需要校验证书的策略类型。

**Type:** [ValidationPolicyType](arkts-devicecertificate-cert-validationpolicytype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainValidationParameters-policy?: ValidationPolicyType--><!--Device-CertChainValidationParameters-policy?: ValidationPolicyType-End-->

**System capability:** SystemCapability.Security.Cert

## revocationCheckParam

```TypeScript
revocationCheckParam?: RevocationCheckParameter
```

表示需要校验证书吊销状态的参数对象。

**Type:** [RevocationCheckParameter](arkts-devicecertificate-cert-revocationcheckparameter-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainValidationParameters-revocationCheckParam?: RevocationCheckParameter--><!--Device-CertChainValidationParameters-revocationCheckParam?: RevocationCheckParameter-End-->

**System capability:** SystemCapability.Security.Cert

## sslHostname

```TypeScript
sslHostname?: string
```

表示需要校验证书中主机名，与policy配合使用。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainValidationParameters-sslHostname?: string--><!--Device-CertChainValidationParameters-sslHostname?: string-End-->

**System capability:** SystemCapability.Security.Cert

## trustAnchors

```TypeScript
trustAnchors: Array<X509TrustAnchor>
```

表示信任锚列表。

**Type:** Array&lt;X509TrustAnchor&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CertChainValidationParameters-trustAnchors: Array<X509TrustAnchor>--><!--Device-CertChainValidationParameters-trustAnchors: Array<X509TrustAnchor>-End-->

**System capability:** SystemCapability.Security.Cert

## trustSystemCa

```TypeScript
trustSystemCa?: boolean
```

表示是否使用系统预置CA证书校验证书链。true表示使用；false表示不使用。

**Type:** boolean

**Default:** false

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CertChainValidationParameters-trustSystemCa?: boolean--><!--Device-CertChainValidationParameters-trustSystemCa?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

