# PhotoCreateOptions（系统接口）

Defines the options for creating an image or video asset.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoCreateOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photocreateoptions-i-sys.md/arkts-medialibrary-photoaccesshelper-photocreateoptions-i-sys.md)

<!--Device-userFileManager-interface PhotoCreateOptions--><!--Device-userFileManager-interface PhotoCreateOptions-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { userFileManager } from 'kits/@kit.CoreFileKit';
```

## cameraShotKey

```TypeScript
cameraShotKey?: string
```

Key for the Ultra Snapshot feature.

This parameter is available only for the system camera, and the key value is defined by the system camera.

**类型：** string

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoCreateOptions.cameraShotKey](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photocreateoptions-i-sys.md/arkts-medialibrary-photoaccesshelper-photocreateoptions-i-sys.md#camerashotkey)

<!--Device-PhotoCreateOptions-cameraShotKey?: string--><!--Device-PhotoCreateOptions-cameraShotKey?: string-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## subType

```TypeScript
subType?: PhotoSubType
```

Subtype of the image or video.

**类型：** [PhotoSubType](arkts-corefile-userfilemanager-photosubtype-e-sys.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.PhotoCreateOptions.subType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photocreateoptions-i-sys.md/arkts-medialibrary-photoaccesshelper-photocreateoptions-i-sys.md#subtype)

<!--Device-PhotoCreateOptions-subType?: PhotoSubType--><!--Device-PhotoCreateOptions-subType?: PhotoSubType-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

