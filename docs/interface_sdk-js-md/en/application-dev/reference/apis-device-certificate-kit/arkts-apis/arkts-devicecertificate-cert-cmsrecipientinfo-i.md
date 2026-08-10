# CmsRecipientInfo

CMS封装数据的接收者信息。

> **说明：**
> 
> 至少需要设置一个接收者。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-cert-interface CmsRecipientInfo--><!--Device-cert-interface CmsRecipientInfo-End-->

**System capability:** SystemCapability.Security.Cert

## Modules to Import

```TypeScript
import { cert } from 'kits/@kit.DeviceCertificateKit';
```

## keyAgreeInfo

```TypeScript
keyAgreeInfo?: CmsKeyAgreeRecipientInfo
```

keyAgree接收者信息。

**Type:** [CmsKeyAgreeRecipientInfo](arkts-devicecertificate-cert-cmskeyagreerecipientinfo-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsRecipientInfo-keyAgreeInfo?: CmsKeyAgreeRecipientInfo--><!--Device-CmsRecipientInfo-keyAgreeInfo?: CmsKeyAgreeRecipientInfo-End-->

**System capability:** SystemCapability.Security.Cert

## keyTransInfo

```TypeScript
keyTransInfo?: CmsKeyTransRecipientInfo
```

keyTrans接收者信息。

**Type:** [CmsKeyTransRecipientInfo](arkts-devicecertificate-cert-cmskeytransrecipientinfo-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsRecipientInfo-keyTransInfo?: CmsKeyTransRecipientInfo--><!--Device-CmsRecipientInfo-keyTransInfo?: CmsKeyTransRecipientInfo-End-->

**System capability:** SystemCapability.Security.Cert

