# CmsRecipientInfo

Represents recipient information for the CMS message. > **NOTE** > > At least one recipient needs to be set.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-cert-interface CmsRecipientInfo--><!--Device-cert-interface CmsRecipientInfo-End-->

**System capability:** SystemCapability.Security.Cert

## keyAgreeInfo

```TypeScript
keyAgreeInfo?: CmsKeyAgreeRecipientInfo
```

KeyAgree recipient information.

**Type:** CmsKeyAgreeRecipientInfo

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsRecipientInfo-keyAgreeInfo?: CmsKeyAgreeRecipientInfo--><!--Device-CmsRecipientInfo-keyAgreeInfo?: CmsKeyAgreeRecipientInfo-End-->

**System capability:** SystemCapability.Security.Cert

## keyTransInfo

```TypeScript
keyTransInfo?: CmsKeyTransRecipientInfo
```

KeyTrans recipient information.

**Type:** CmsKeyTransRecipientInfo

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CmsRecipientInfo-keyTransInfo?: CmsKeyTransRecipientInfo--><!--Device-CmsRecipientInfo-keyTransInfo?: CmsKeyTransRecipientInfo-End-->

**System capability:** SystemCapability.Security.Cert

