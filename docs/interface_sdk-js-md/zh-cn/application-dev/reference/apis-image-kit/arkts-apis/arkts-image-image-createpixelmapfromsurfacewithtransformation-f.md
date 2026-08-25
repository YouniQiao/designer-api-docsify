# createPixelMapFromSurfaceWithTransformation

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPixelMapFromSurfaceWithTransformation

```TypeScript
function createPixelMapFromSurfaceWithTransformation(surfaceId: string, transformEnabled: boolean): Promise<PixelMap>
```

Creates a PixelMap object based on the ID of a Surface with transformation.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |
| transformEnabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600206](../errorcode-image.md#7600206-无效参数) |
| [7600305](../errorcode-image.md#7600305-创建pixelmap失败) |
