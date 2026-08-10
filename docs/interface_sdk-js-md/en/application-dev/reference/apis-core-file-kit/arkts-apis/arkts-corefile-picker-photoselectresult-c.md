# PhotoSelectResult

返回图库选择后的结果集。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectResult](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoselectresult-c.md/arkts-medialibrary-photoaccesshelper-photoselectresult-c.md)

<!--Device-picker-class PhotoSelectResult--><!--Device-picker-class PhotoSelectResult-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## Modules to Import

```TypeScript
import { picker } from 'kits/@kit.CoreFileKit';
```

## isOriginalPhoto

```TypeScript
isOriginalPhoto: boolean
```

返回图库选择后的媒体文件是否为原图。true为原图；false不是原图。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectResult#isOriginalPhoto](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoselectresult-c.md/arkts-medialibrary-photoaccesshelper-photoselectresult-c.md#isoriginalphoto)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoSelectResult-isOriginalPhoto: boolean--><!--Device-PhotoSelectResult-isOriginalPhoto: boolean-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## photoUris

```TypeScript
photoUris: Array<string>
```

返回图库选择后的媒体文件的URI数组。此URI数组只能通过临时授权的方式调用接口  
[photoAccessHelper.getAssets](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md/arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#getassets)去使用，具体使用方式参见用户文件URI介绍中的[媒体文件URI的使用方式](../../../file-management/user-file-uri-intro.md#媒体文件uri的使用方式)。

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectResult#photoUris](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoselectresult-c.md/arkts-medialibrary-photoaccesshelper-photoselectresult-c.md#photouris)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoSelectResult-photoUris: Array<string>--><!--Device-PhotoSelectResult-photoUris: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

