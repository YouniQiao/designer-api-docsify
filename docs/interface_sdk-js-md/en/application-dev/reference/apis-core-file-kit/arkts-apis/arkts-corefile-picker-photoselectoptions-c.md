# PhotoSelectOptions

图库选择选项。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoselectoptions-c.md/arkts-medialibrary-photoaccesshelper-photoselectoptions-c.md)

<!--Device-picker-class PhotoSelectOptions--><!--Device-picker-class PhotoSelectOptions-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## Modules to Import

```TypeScript
import { picker } from 'kits/@kit.CoreFileKit';
```

## MIMEType

```TypeScript
MIMEType?: PhotoViewMIMETypes
```

可选择的媒体文件类型。若无此参数，则默认为图片和视频类型。

**Type:** [PhotoViewMIMETypes](arkts-corefile-picker-photoviewmimetypes-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** @ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectOptions#MIMEType

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoSelectOptions-MIMEType?: PhotoViewMIMETypes--><!--Device-PhotoSelectOptions-MIMEType?: PhotoViewMIMETypes-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## maxSelectNumber

```TypeScript
maxSelectNumber?: number
```

选择媒体文件数量的最大值，默认值为50，最大值为500。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** @ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectOptions#maxSelectNumber

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoSelectOptions-maxSelectNumber?: number--><!--Device-PhotoSelectOptions-maxSelectNumber?: number-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

