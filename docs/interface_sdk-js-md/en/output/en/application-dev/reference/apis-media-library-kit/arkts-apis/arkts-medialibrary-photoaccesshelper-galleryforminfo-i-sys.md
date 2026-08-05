# GalleryFormInfo (System API)

Defines the Gallery widget information.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-photoAccessHelper-interface GalleryFormInfo--><!--Device-photoAccessHelper-interface GalleryFormInfo-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## assetUris

```TypeScript
assetUris?: Array<string>
```

URIs of the images or albums bound to the widget. This parameter cannot be empty when creating or updating a widget. If you attempt to create or update a widget with more than 500 URIs in **assetUris**, only the first 500 URIs are registered for listening. Any URIs beyond the first 500 are not registered. When deleting a widget, this parameter can be omitted.

**Type:** Array&lt;string&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-GalleryFormInfo-assetUris?: Array<string>--><!--Device-GalleryFormInfo-assetUris?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## formId

```TypeScript
formId: string
```

Widget ID, which is provided when a widget is created in Gallery.

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-GalleryFormInfo-formId: string--><!--Device-GalleryFormInfo-formId: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

