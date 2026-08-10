# CmsSignerConfig

表示Cms签名者的配置选项。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cert-interface CmsSignerConfig--><!--Device-cert-interface CmsSignerConfig-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## addAttr

```TypeScript
addAttr?: boolean
```

是否添加签名属性。默认为true。true为需要，false为不需要。

**Type:** boolean

**Default:** true

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CmsSignerConfig-addAttr?: boolean--><!--Device-CmsSignerConfig-addAttr?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## addCert

```TypeScript
addCert?: boolean
```

是否添加证书。默认为true。true为需要，false为不需要。

**Type:** boolean

**Default:** true

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CmsSignerConfig-addCert?: boolean--><!--Device-CmsSignerConfig-addCert?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## addSmimeCapAttr

```TypeScript
addSmimeCapAttr?: boolean
```

是否将SMIME能力添加到Cms对象。默认为true。true为需要，false为不需要。

**Type:** boolean

**Default:** true

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CmsSignerConfig-addSmimeCapAttr?: boolean--><!--Device-CmsSignerConfig-addSmimeCapAttr?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## mdName

```TypeScript
mdName: string
```

消息摘要算法的名称，例如 "SHA384", 当前支持"SHA1"、"SHA256"、"SHA384"、"SHA512"。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CmsSignerConfig-mdName: string--><!--Device-CmsSignerConfig-mdName: string-End-->

**System capability:** SystemCapability.Security.Cert

## rsaSignaturePadding

```TypeScript
rsaSignaturePadding?: CmsRsaSignaturePadding
```

RSA签名填充方式。默认值为：PKCS1_PADDING。&lt;br&gt;当设置为 PKCS1_PSS_PADDING 时，mdName 必须为 "SHA256"、"SHA384" 或 "SHA512"。

> **说明：**
> 
> 仅当签名者私钥类型为RSA时有效。

**Type:** [CmsRsaSignaturePadding](arkts-devicecertificate-cert-cmsrsasignaturepadding-e.md)

**Default:** CmsRsaSignaturePadding.PKCS1_PADDING

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsSignerConfig-rsaSignaturePadding?: CmsRsaSignaturePadding--><!--Device-CmsSignerConfig-rsaSignaturePadding?: CmsRsaSignaturePadding-End-->

**System capability:** SystemCapability.Security.Cert

