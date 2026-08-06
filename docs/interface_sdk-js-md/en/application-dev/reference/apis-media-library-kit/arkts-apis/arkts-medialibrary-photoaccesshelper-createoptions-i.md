# CreateOptions

Options for creating an image or video asset.

The title must meet the following requirements:

- It must not contain a file name extension.  
- The total length of the file name must be between 1 and 255 characters.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-photoAccessHelper-interface CreateOptions--><!--Device-photoAccessHelper-interface CreateOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## subtype

```TypeScript
subtype?: PhotoSubtype
```

Subtype of the image or video file.

**Type:** PhotoSubtype

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CreateOptions-subtype?: PhotoSubtype--><!--Device-CreateOptions-subtype?: PhotoSubtype-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## title

```TypeScript
title?: string
```

Title of the image or video.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CreateOptions-title?: string--><!--Device-CreateOptions-title?: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

