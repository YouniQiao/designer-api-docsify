# PhotoSelectOptions

Defines additional options for selecting media assets from Gallery. It inherits from **BaseSelectOptions**. It is used to start the picker of the corresponding user ID space.

**Inheritance/Implementation:** PhotoSelectOptions extends [BaseSelectOptions](arkts-medialibrary-photoaccesshelper-baseselectoptions-c.md)

**Since:** 26.0.0

<!--Device-photoAccessHelper-class PhotoSelectOptions--><!--Device-photoAccessHelper-class PhotoSelectOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## themeColor

```TypeScript
themeColor?: CustomColors
```

Theme color

**Type:** [CustomColors](../../apis-na/arkts-apis/arkts-na-customcolors-t.md)

**Since:** 26.0.0

<!--Device-PhotoSelectOptions-themeColor?: CustomColors--><!--Device-PhotoSelectOptions-themeColor?: CustomColors-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## userId

```TypeScript
userId?: int
```

ID of the user space to access. The default value is **-1**. To use it as a parameter of [PhotoViewPicker.select](arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md#select) , request the permission **ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS**.

**Type:** int

**Since:** 26.0.0

<!--Device-PhotoSelectOptions-userId?: int--><!--Device-PhotoSelectOptions-userId?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

