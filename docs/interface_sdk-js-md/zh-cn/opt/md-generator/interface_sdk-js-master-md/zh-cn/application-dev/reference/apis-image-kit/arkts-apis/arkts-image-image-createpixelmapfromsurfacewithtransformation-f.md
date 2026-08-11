# createPixelMapFromSurfaceWithTransformation

## createPixelMapFromSurfaceWithTransformation

```TypeScript
function createPixelMapFromSurfaceWithTransformation(surfaceId: string, transformEnabled: boolean): Promise<PixelMap>
```

Creates a PixelMap object based on the ID of a Surface with transformation.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-image-function createPixelMapFromSurfaceWithTransformation(surfaceId: string, transformEnabled: boolean): Promise<PixelMap>--><!--Device-image-function createPixelMapFromSurfaceWithTransformation(surfaceId: string, transformEnabled: boolean): Promise<PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |
| transformEnabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;PixelMap&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600305](../errorcode-image.md#7600305-创建pixelmap失败) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
| [7600104](../errorcode-image.md#7600104-获取图像数据失败) |
| [7600206](../errorcode-image.md#7600206-无效参数) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createPixelMapFromSurfaceWithTransformation(surfaceId: string, transformEnabled: boolean) {
  image.createPixelMapFromSurfaceWithTransformation(surfaceId, transformEnabled).then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in creating the PixelMap from Surface.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to create the PixelMap from Surface. Code: ${err.code}, message: ${err.message}`);
  });
}
```
