# TagInfo

Provides tag information. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_This class provides the technology a tag supports, for example, NFC-A. Applications can create different tags based on the supported technology.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-tag-export interface TagInfo--><!--Device-tag-export interface TagInfo-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## supportedProfiles

```TypeScript
supportedProfiles: number[]
```

The supported technology list of this tag.

**Type:** number[]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.nfc.tag/tag.TagInfo#technology

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagInfo-supportedProfiles: number[]--><!--Device-TagInfo-supportedProfiles: number[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## technology

```TypeScript
technology: int[]
```

The supported technology list of this tag.

**Type:** int[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TagInfo-technology: int[]--><!--Device-TagInfo-technology: int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## uid

```TypeScript
uid: int[]
```

The uid of this tag, it.

**Type:** int[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TagInfo-uid: int[]--><!--Device-TagInfo-uid: int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

