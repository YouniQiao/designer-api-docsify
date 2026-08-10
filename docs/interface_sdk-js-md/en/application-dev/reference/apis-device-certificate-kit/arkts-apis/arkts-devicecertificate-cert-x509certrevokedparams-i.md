# X509CertRevokedParams

表示证书吊销检查参数。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-cert-interface X509CertRevokedParams--><!--Device-cert-interface X509CertRevokedParams-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## allowDownloadCrl

```TypeScript
allowDownloadCrl?: boolean
```

是否允许下载CRL，默认值为false。true：尝试使用证书的CDP扩展下载CRL；false：不尝试下载CRL。

> **说明：**
> 
> 如果crls中存在匹配的CRL，则跳过下载。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-X509CertRevokedParams-allowDownloadCrl?: boolean--><!--Device-X509CertRevokedParams-allowDownloadCrl?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## allowOcspCheckOnline

```TypeScript
allowOcspCheckOnline?: boolean
```

是否允许在线OCSP检查，默认值为false。  
- true：执行在线OCSP检查，即尝试从证书AIA扩展获取OCSP URL并发送请求获取响应；  
- false：不执行在线OCSP检查。

> **说明：**
> 
> 如果在ocspResponses中找到匹配的OCSP响应，则跳过在线OCSP检查。

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-X509CertRevokedParams-allowOcspCheckOnline?: boolean--><!--Device-X509CertRevokedParams-allowOcspCheckOnline?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## crls

```TypeScript
crls?: Array<X509CRL>
```

CRL列表。最大个数：100。

**Type:** Array&lt;X509CRL&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-X509CertRevokedParams-crls?: Array<X509CRL>--><!--Device-X509CertRevokedParams-crls?: Array<X509CRL>-End-->

**System capability:** SystemCapability.Security.Cert

## ocspDigest

```TypeScript
ocspDigest?: OcspDigest
```

OCSP请求使用的摘要算法，默认值为SHA256。

**Type:** [OcspDigest](arkts-devicecertificate-cert-ocspdigest-e.md)

**Default:** SHA256

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-X509CertRevokedParams-ocspDigest?: OcspDigest--><!--Device-X509CertRevokedParams-ocspDigest?: OcspDigest-End-->

**System capability:** SystemCapability.Security.Cert

## ocspResponses

```TypeScript
ocspResponses?: Array<Uint8Array>
```

OCSP响应数据。预置的OCSP响应数据。最大个数：100。

**Type:** Array&lt;Uint8Array&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-X509CertRevokedParams-ocspResponses?: Array<Uint8Array>--><!--Device-X509CertRevokedParams-ocspResponses?: Array<Uint8Array>-End-->

**System capability:** SystemCapability.Security.Cert

## revocationFlags

```TypeScript
revocationFlags: Array<CertRevocationFlag>
```

吊销检查标志。数组长度范围：[1, 4]。数组必须包含CERT_REVOCATION_CRL_CHECK或CERT_REVOCATION_OCSP_CHECK。

**Type:** Array&lt;CertRevocationFlag&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-X509CertRevokedParams-revocationFlags: Array<CertRevocationFlag>--><!--Device-X509CertRevokedParams-revocationFlags: Array<CertRevocationFlag>-End-->

**System capability:** SystemCapability.Security.Cert

