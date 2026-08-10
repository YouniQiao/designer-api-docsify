# AlbumPickerController

The class for AlbumPickerController

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Observed

<!--Device-unnamed-export declare class AlbumPickerController--><!--Device-unnamed-export declare class AlbumPickerController-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { EmptyAreaClickCallback, AlbumPickerComponent, AlbumInfo, AlbumPickerOptions, AlbumPickerController } from 'kits/@kit.MediaLibraryKit';
```

## setFontSize

```TypeScript
public setFontSize(fontSize: int | string): void
```

Set font size to album picker component. Invalid value will result in the default font size being shown.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AlbumPickerController-public setFontSize(fontSize: int | string): void--><!--Device-AlbumPickerController-public setFontSize(fontSize: int | string): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontSize | int \| string | 是 | font size of album picker component |

