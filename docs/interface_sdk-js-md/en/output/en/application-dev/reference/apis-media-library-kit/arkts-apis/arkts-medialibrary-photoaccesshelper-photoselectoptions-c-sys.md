# PhotoSelectOptions

Defines additional options for selecting media assets from Gallery. It inherits from **BaseSelectOptions**. It is used to start the picker of the corresponding user ID space.

**Inheritance/Implementation:** PhotoSelectOptions extends [BaseSelectOptions](arkts-medialibrary-photoaccesshelper-baseselectoptions-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 26.0.0.

<!--Device-photoAccessHelper-class PhotoSelectOptions extends BaseSelectOptions--><!--Device-photoAccessHelper-class PhotoSelectOptions extends BaseSelectOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## themeColor

```TypeScript
themeColor?: CustomColors
```

Theme color

**Type:** CustomColors

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.0.0.

<!--Device-PhotoSelectOptions-themeColor?: CustomColors--><!--Device-PhotoSelectOptions-themeColor?: CustomColors-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## userId

```TypeScript
userId?: int
```

ID of the user space to access. The default value is **-1**. To use it as a parameter of [PhotoViewPicker.select]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ , request the permission **ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS**.

**Type:** int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 26.0.0.

<!--Device-PhotoSelectOptions-userId?: int--><!--Device-PhotoSelectOptions-userId?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

