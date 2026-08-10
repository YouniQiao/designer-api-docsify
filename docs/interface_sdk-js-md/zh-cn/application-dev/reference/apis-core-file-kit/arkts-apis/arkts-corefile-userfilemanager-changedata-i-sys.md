# ChangeData（系统接口）

Defines the return value of the listener callback.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.ChangeData](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-changedata-i.md/arkts-medialibrary-photoaccesshelper-changedata-i.md)

<!--Device-userFileManager-interface ChangeData--><!--Device-userFileManager-interface ChangeData-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { userFileManager } from 'kits/@kit.CoreFileKit';
```

## subUris

```TypeScript
subUris: Array<string>
```

URIs of the changed files in the album. The value may be undefined. Check whether the value is undefined before using it.

**类型：** Array&lt;string&gt;

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**废弃版本：** 26.0.0

<!--Device-ChangeData-subUris: Array<string>--><!--Device-ChangeData-subUris: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## type

```TypeScript
type: NotifyType
```

Notification type.

**类型：** [NotifyType](arkts-corefile-cloudsync-notifytype-e.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.ChangeData.type](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-changedata-i.md/arkts-medialibrary-photoaccesshelper-changedata-i.md#type)

<!--Device-ChangeData-type: NotifyType--><!--Device-ChangeData-type: NotifyType-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

## uris

```TypeScript
uris: Array<string>
```

Array of all file asset or album URIs with the same [NotifyType](arkts-corefile-userfilemanager-notifytype-e-sys.md).

**类型：** Array&lt;string&gt;

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.ChangeData.uris](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-changedata-i.md/arkts-medialibrary-photoaccesshelper-changedata-i.md#uris)

<!--Device-ChangeData-uris: Array<string>--><!--Device-ChangeData-uris: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

