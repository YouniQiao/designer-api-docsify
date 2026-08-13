# TagInfo

Provides tag information. &lt;p&gt;This class provides the technology a tag supports, for example, NFC-A. Applications can create different tags based on the supported technology.

**Since:** 23

**Deprecated since:** -1

<!--Device-tag-export interface TagInfo--><!--Device-tag-export interface TagInfo-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## supportedProfiles

```TypeScript
supportedProfiles: number[]
```

The supported technology list of this tag.

**Type:** number[]

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [technology](#technology)

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-TagInfo-supportedProfiles: number[]--><!--Device-TagInfo-supportedProfiles: number[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## technology

```TypeScript
technology: number[]
```

The supported technology list of this tag.

**Type:** number[]

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TagInfo-technology: int[]--><!--Device-TagInfo-technology: int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## uid

```TypeScript
uid: number[]
```

The uid of this tag, it.

**Type:** number[]

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TagInfo-uid: int[]--><!--Device-TagInfo-uid: int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag
