# MimeTypeFilter

Describes the configuration for file type filtering.

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-class MimeTypeFilter--><!--Device-photoAccessHelper-class MimeTypeFilter-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## mimeTypeArray

```TypeScript
mimeTypeArray: Array<string>
```

Types of media files that PhotoPicker allows users to filter by. The maximum array length is 10, thus supporting up to 10 specified types.

The filter type is defined by the MIME type, for example, image/jpeg and video/mp4.

**类型：** Array&lt;string&gt;

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MimeTypeFilter-mimeTypeArray: Array<string>--><!--Device-MimeTypeFilter-mimeTypeArray: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

