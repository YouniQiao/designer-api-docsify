# ChangeEvent（系统接口）

```TypeScript
type ChangeEvent =
    'deviceChange'
    | 'albumChange'
    | 'imageChange'
    | 'audioChange'
    | 'videoChange'
    | 'remoteFileChange'
```

Enumerates the type of changes to observe.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 26.0.0

**替代接口：** [@ohos.file.photoAccessHelper:photoAccessHelper.ChangeData](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-changedata-i.md/arkts-medialibrary-photoaccesshelper-changedata-i.md)

<!--Device-userFileManager-type ChangeEvent =    'deviceChange'    | 'albumChange'    | 'imageChange'    | 'audioChange'    | 'videoChange'    | 'remoteFileChange'--><!--Device-userFileManager-type ChangeEvent =    'deviceChange'    | 'albumChange'    | 'imageChange'    | 'audioChange'    | 'videoChange'    | 'remoteFileChange'-End-->

**系统能力：** SystemCapability.FileManagement.UserFileManager.Core

**系统接口：** 此接口为系统接口。

| 类型 | 说明 |
| --- | --- |
| 'deviceChange' | Device. The value is fixed at **'deviceChange'**. |
| 'albumChange' | Album. The value is fixed at **'albumChange'**. |
| 'imageChange' | Image. The value is fixed at **'imageChange'**. |
| 'audioChange' | Audio. The value is fixed at **'audioChange'**. |
| 'videoChange' | Video. The value is fixed at **'videoChange'**. |
| 'remoteFileChange' | Remote file. The value is fixed at **'remoteFileChange'**. |

