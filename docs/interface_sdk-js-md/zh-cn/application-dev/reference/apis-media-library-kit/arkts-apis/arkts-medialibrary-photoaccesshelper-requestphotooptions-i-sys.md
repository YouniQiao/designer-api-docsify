# RequestPhotoOptions（系统接口）

Defines the options for obtaining the thumbnail of an image or video.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface RequestPhotoOptions--><!--Device-photoAccessHelper-interface RequestPhotoOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## requestPhotoType

```TypeScript
requestPhotoType?: RequestPhotoType
```

Operation to perform.

**类型：** [RequestPhotoType](arkts-medialibrary-photoaccesshelper-requestphototype-e-sys.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-RequestPhotoOptions-requestPhotoType?: RequestPhotoType--><!--Device-RequestPhotoOptions-requestPhotoType?: RequestPhotoType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## size

```TypeScript
size?: image.Size
```

Size of the thumbnail to obtain.

**类型：** image.Size

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-RequestPhotoOptions-size?: image.Size--><!--Device-RequestPhotoOptions-size?: image.Size-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

