# createPixelMapFromSurface

## 导入模块

```TypeScript
```

## createPixelMapFromSurface

```TypeScript
function createPixelMapFromSurface(surfaceId: string, region: image.Region): Promise<PixelMap>
```

Creates a PixelMap object from surface id.

**起始版本：** 12

<!--Device-sendableImage-function createPixelMapFromSurface(surfaceId: string, region: image.Region): Promise<PixelMap>--><!--Device-sendableImage-function createPixelMapFromSurface(surfaceId: string, region: image.Region): Promise<PixelMap>-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |
| region | image.Region | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980178](../errorcode-image.md#62980178-pixelmap创建失败) |
| [62980105](../errorcode-image.md#62980105-图片获取数据错误) |

**示例**

```TypeScript
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

function createPixelMapFromSurface(surfaceId: string) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  sendableImage.createPixelMapFromSurface(surfaceId, region).then((pixelMap: sendableImage.PixelMap) => {
    console.info('Succeeded in creating the PixelMap from Surface.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to create the PixelMap from Surface. Code: ${err.code}, message: ${err.message}`);
  });
}
```
