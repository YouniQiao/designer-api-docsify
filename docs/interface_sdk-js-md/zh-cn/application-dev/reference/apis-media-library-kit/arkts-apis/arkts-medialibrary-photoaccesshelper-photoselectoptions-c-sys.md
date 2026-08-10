# PhotoSelectOptions

Defines additional options for selecting media assets from Gallery. It inherits from **BaseSelectOptions**. It is used to start the picker of the corresponding user ID space.

**继承/实现关系：** PhotoSelectOptions extends [BaseSelectOptions](arkts-medialibrary-photoaccesshelper-baseselectoptions-c.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-class PhotoSelectOptions extends BaseSelectOptions--><!--Device-photoAccessHelper-class PhotoSelectOptions extends BaseSelectOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## themeColor

```TypeScript
themeColor?: CustomColors
```

Theme color

**类型：** [CustomColors](../../apis-arkui/arkts-apis/arkts-arkui-customcolors-t.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为26.0.0。

<!--Device-PhotoSelectOptions-themeColor?: CustomColors--><!--Device-PhotoSelectOptions-themeColor?: CustomColors-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## userId

```TypeScript
userId?: int
```

ID of the user space to access. The default value is **-1**.

To use it as a parameter of   
[PhotoViewPicker.select](arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md#select), request the permission **ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS**.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为26.0.0。

<!--Device-PhotoSelectOptions-userId?: int--><!--Device-PhotoSelectOptions-userId?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

