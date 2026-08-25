# Album

实体相册

**继承/实现关系：** Album extends [AbsAlbum](arkts-medialibrary-sendablephotoaccesshelper-absalbum-i.md)

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { sendablePhotoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## commitModify

```TypeScript
commitModify(): Promise<void>
```

更新相册属性修改到数据库中。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## convertToPhotoAlbum

```TypeScript
convertToPhotoAlbum(): photoAccessHelper.Album
```

将Sendable类型Album转换为非Sendable类型Album。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| photoAccessHelper.Album |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## imageCount

```TypeScript
readonly imageCount?: number
```

相册中图片数量。

**类型：** number

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## videoCount

```TypeScript
readonly videoCount?: number
```

相册中视频数量。

**类型：** number

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core
