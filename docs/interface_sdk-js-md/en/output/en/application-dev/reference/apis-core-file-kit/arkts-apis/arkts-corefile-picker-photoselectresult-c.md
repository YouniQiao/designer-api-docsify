# PhotoSelectResult

Defines information about the images or videos selected.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectResult](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoselectresult-c.md)

<!--Device-picker-class PhotoSelectResult--><!--Device-picker-class PhotoSelectResult-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## isOriginalPhoto

```TypeScript
isOriginalPhoto: boolean
```

Whether the selected image is the original one. The value **true** means the selected image is the original one; the value **false** means the opposite.

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectResult#isOriginalPhoto](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoselectresult-c.md#isoriginalphoto)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoSelectResult-isOriginalPhoto: boolean--><!--Device-PhotoSelectResult-isOriginalPhoto: boolean-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## photoUris

```TypeScript
photoUris: Array<string>
```

URIs of the media files selected. This URI array can be used only by [photoAccessHelper.getAssets]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ . For details, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectResult#photoUris](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoselectresult-c.md#photouris)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PhotoSelectResult-photoUris: Array<string>--><!--Device-PhotoSelectResult-photoUris: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

