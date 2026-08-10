# CmsGeneratorOptions

表示生成CMS消息的配置选项。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-cert-interface CmsGeneratorOptions--><!--Device-cert-interface CmsGeneratorOptions-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## contentDataFormat

```TypeScript
contentDataFormat?: CmsContentDataFormat
```

内容数据的格式。默认为CmsContentDataFormat.BINARY。

**Type:** [CmsContentDataFormat](arkts-devicecertificate-cert-cmscontentdataformat-e.md)

**Default:** CmsContentDataFormat.BINARY

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CmsGeneratorOptions-contentDataFormat?: CmsContentDataFormat--><!--Device-CmsGeneratorOptions-contentDataFormat?: CmsContentDataFormat-End-->

**System capability:** SystemCapability.Security.Cert

## isDetached

```TypeScript
isDetached?: boolean
```

Cms最终数据是否不包含原始数据。默认为false。true为不包含，false为包含。

**Type:** boolean

**Default:** false

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CmsGeneratorOptions-isDetached?: boolean--><!--Device-CmsGeneratorOptions-isDetached?: boolean-End-->

**System capability:** SystemCapability.Security.Cert

## outFormat

```TypeScript
outFormat?: CmsFormat
```

Cms最终数据的输出格式。默认为DER。

**Type:** [CmsFormat](arkts-devicecertificate-cert-cmsformat-e.md)

**Default:** CmsFormat.DER

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CmsGeneratorOptions-outFormat?: CmsFormat--><!--Device-CmsGeneratorOptions-outFormat?: CmsFormat-End-->

**System capability:** SystemCapability.Security.Cert

