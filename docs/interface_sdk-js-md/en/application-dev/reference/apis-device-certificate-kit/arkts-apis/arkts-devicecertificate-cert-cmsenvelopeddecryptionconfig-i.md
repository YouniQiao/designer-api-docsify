# CmsEnvelopedDecryptionConfig

CMS解封装的配置。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-cert-interface CmsEnvelopedDecryptionConfig--><!--Device-cert-interface CmsEnvelopedDecryptionConfig-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## cert

```TypeScript
cert?: X509Cert
```

公钥证书。默认为空。

**Type:** [X509Cert](../../apis-network-kit/arkts-apis/arkts-network-http-x509cert-t.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsEnvelopedDecryptionConfig-cert?: X509Cert--><!--Device-CmsEnvelopedDecryptionConfig-cert?: X509Cert-End-->

**System capability:** SystemCapability.Security.Cert

## contentDataFormat

```TypeScript
contentDataFormat?: CmsContentDataFormat
```

内容数据的格式。

**Type:** [CmsContentDataFormat](arkts-devicecertificate-cert-cmscontentdataformat-e.md)

**Default:** CmsContentDataFormat.BINARY

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsEnvelopedDecryptionConfig-contentDataFormat?: CmsContentDataFormat--><!--Device-CmsEnvelopedDecryptionConfig-contentDataFormat?: CmsContentDataFormat-End-->

**System capability:** SystemCapability.Security.Cert

## encryptedContentData

```TypeScript
encryptedContentData?: Uint8Array
```

加密的内容数据，如果CMS不包含指定数据。

**Type:** Uint8Array

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsEnvelopedDecryptionConfig-encryptedContentData?: Uint8Array--><!--Device-CmsEnvelopedDecryptionConfig-encryptedContentData?: Uint8Array-End-->

**System capability:** SystemCapability.Security.Cert

## keyInfo

```TypeScript
keyInfo?: PrivateKeyInfo
```

私钥参数。默认为空。

**Type:** [PrivateKeyInfo](arkts-devicecertificate-cert-privatekeyinfo-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsEnvelopedDecryptionConfig-keyInfo?: PrivateKeyInfo--><!--Device-CmsEnvelopedDecryptionConfig-keyInfo?: PrivateKeyInfo-End-->

**System capability:** SystemCapability.Security.Cert

