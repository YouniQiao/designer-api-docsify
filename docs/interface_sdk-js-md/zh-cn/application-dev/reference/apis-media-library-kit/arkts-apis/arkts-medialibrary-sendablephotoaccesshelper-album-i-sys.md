# Album

实体相册

**继承/实现关系：** Album extends [AbsAlbum](arkts-medialibrary-sendablephotoaccesshelper-absalbum-i.md)

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { sendablePhotoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## getFaceId

```TypeScript
getFaceId(): Promise<string>
```

获取人像相册或合影相册的封面人脸标识。使用Promise异步回调。

**起始版本：** 13

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |
