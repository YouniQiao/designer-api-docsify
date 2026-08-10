# CmsVerificationConfig

CMS验签的配置。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-cert-interface CmsVerificationConfig--><!--Device-cert-interface CmsVerificationConfig-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## contentData

```TypeScript
contentData?: Uint8Array
```

内容数据，如果是detached模式，则需要指定明文数据。attached模式可以不传。

**Type:** Uint8Array

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsVerificationConfig-contentData?: Uint8Array--><!--Device-CmsVerificationConfig-contentData?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

## contentDataFormat

```TypeScript
contentDataFormat?: CmsContentDataFormat
```

内容数据的格式。默认为CmsContentDataFormat.BINARY。

**Type:** [CmsContentDataFormat](arkts-devicecertificate-cert-cmscontentdataformat-e.md)

**Default:** CmsContentDataFormat.BINARY

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsVerificationConfig-contentDataFormat?: CmsContentDataFormat--><!--Device-CmsVerificationConfig-contentDataFormat?: CmsContentDataFormat-End-->

**System capability:** SystemCapability.Security.Cert

## signerCerts

```TypeScript
signerCerts?: Array<X509Cert>
```

签名者证书。

**Type:** Array&lt;X509Cert&gt;

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsVerificationConfig-signerCerts?: Array<X509Cert>--><!--Device-CmsVerificationConfig-signerCerts?: Array<X509Cert>-End-->

**System capability:** SystemCapability.Security.Cert

## trustCerts

```TypeScript
trustCerts: Array<X509Cert>
```

信任证书。

> **说明：**
> 
> 需要配置所有签名者的信任证书。

**Type:** Array&lt;X509Cert&gt;

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsVerificationConfig-trustCerts: Array<X509Cert>--><!--Device-CmsVerificationConfig-trustCerts: Array<X509Cert>-End-->

**System capability:** SystemCapability.Security.Cert

