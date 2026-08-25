# createPixelMapFromPixelsSync

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPixelMapFromPixelsSync

```TypeScript
function createPixelMapFromPixelsSync(pixels: ArrayBuffer, param: InitializationOptions): PixelMap
```

Creates a PixelMap from existing pixel data. The pixel data will be copied and converted to the specified pixel format to initialize the PixelMap.The following pixel formats are not supported for PixelMap creation: RGBA_1010102, YCBCR_P010, YCRCB_P010, ASTC_4x4.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pixels](arkts-image-image-positionarea-i.md) | ArrayBuffer | 是 |
| param | [InitializationOptions](arkts-image-image-initializationoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600207](../errorcode-image.md#7600207-不支持的数据格式) |
| [7600301](../errorcode-image.md#7600301-申请内存失败) |
| [7600305](../errorcode-image.md#7600305-创建pixelmap失败) |
