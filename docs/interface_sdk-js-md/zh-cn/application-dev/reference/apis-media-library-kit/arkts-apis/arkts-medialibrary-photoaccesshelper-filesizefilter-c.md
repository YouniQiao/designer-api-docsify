# FileSizeFilter

Describes the configuration for file size filtering.

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

<!--Device-photoAccessHelper-class FileSizeFilter--><!--Device-photoAccessHelper-class FileSizeFilter-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## extraFileSize

```TypeScript
extraFileSize?: long
```

Maximum file size in **FilterOperator.BETWEEN** mode. The default value is **-1**.

The unit is bytes.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-FileSizeFilter-extraFileSize?: long--><!--Device-FileSizeFilter-extraFileSize?: long-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## fileSize

```TypeScript
fileSize: long
```

File size used for filtering.

The unit is bytes.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-FileSizeFilter-fileSize: long--><!--Device-FileSizeFilter-fileSize: long-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## filterOperator

```TypeScript
filterOperator: FilterOperator
```

Filter operator.

For example, files can be filtered based on being greater than or less than a certain file size.

**类型：** [FilterOperator](arkts-medialibrary-photoaccesshelper-filteroperator-e.md)

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-FileSizeFilter-filterOperator: FilterOperator--><!--Device-FileSizeFilter-filterOperator: FilterOperator-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

