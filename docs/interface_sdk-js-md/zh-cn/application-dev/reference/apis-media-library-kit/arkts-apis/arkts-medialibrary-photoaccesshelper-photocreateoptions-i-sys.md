# PhotoCreateOptions（系统接口）

Options for creating an image or video asset.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface PhotoCreateOptions--><!--Device-photoAccessHelper-interface PhotoCreateOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## cameraShotKey

```TypeScript
cameraShotKey?: string
```

Key for the Ultra Snapshot feature, which allows the camera to take photos or record videos with the screen off. (This parameter is available only for the system camera, and the key value is defined by the system camera.)

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-PhotoCreateOptions-cameraShotKey?: string--><!--Device-PhotoCreateOptions-cameraShotKey?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## subtype

```TypeScript
subtype?: PhotoSubtype
```

Subtype of the image or video.

**类型：** [PhotoSubtype](arkts-medialibrary-sendablephotoaccesshelper-photosubtype-e-sys.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-PhotoCreateOptions-subtype?: PhotoSubtype--><!--Device-PhotoCreateOptions-subtype?: PhotoSubtype-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## userId

```TypeScript
userId?: int
```

User ID.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

<!--Device-PhotoCreateOptions-userId?: int--><!--Device-PhotoCreateOptions-userId?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

