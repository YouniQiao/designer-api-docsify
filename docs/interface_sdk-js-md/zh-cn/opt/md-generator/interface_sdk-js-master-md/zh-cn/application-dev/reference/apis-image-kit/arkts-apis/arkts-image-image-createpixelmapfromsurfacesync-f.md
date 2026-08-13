# createPixelMapFromSurfaceSync

## createPixelMapFromSurfaceSync

```TypeScript
function createPixelMapFromSurfaceSync(surfaceId: string, region: Region): PixelMap
```

Creates a PixelMap object from surface id.

**起始版本：** 23

**废弃版本：** -1

<!--Device-image-function createPixelMapFromSurfaceSync(surfaceId: string, region: Region): PixelMap--><!--Device-image-function createPixelMapFromSurfaceSync(surfaceId: string, region: Region): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |
| region | [Region](arkts-image-image-region-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980178](../errorcode-image.md#62980178-pixelmap创建失败) |
| [62980105](../errorcode-image.md#62980105-图片获取数据错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createPixelMapFromSurfaceSync(surfaceId: string) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  try {
    let pixelMap: image.PixelMap = image.createPixelMapFromSurfaceSync(surfaceId, region);
    console.info('Succeeded in creating the PixelMap from Surface.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to create the PixelMap from Surface. Code: ${err.code}, message: ${err.message}`);
  }
}
```


## createPixelMapFromSurfaceSync

```TypeScript
function createPixelMapFromSurfaceSync(surfaceId: string): PixelMap
```

Creates a PixelMap object from surface id.

**起始版本：** 23

**废弃版本：** -1

<!--Device-image-function createPixelMapFromSurfaceSync(surfaceId: string): PixelMap--><!--Device-image-function createPixelMapFromSurfaceSync(surfaceId: string): PixelMap-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| surfaceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| [PixelMap](../../apis-na/arkts-apis/arkts-na-pixelmap-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980178](../errorcode-image.md#62980178-pixelmap创建失败) |
| [62980105](../errorcode-image.md#62980105-图片获取数据错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createPixelMapFromSurfaceSync(surfaceId: string) {
  try {
    let pixelMap: image.PixelMap = image.createPixelMapFromSurfaceSync(surfaceId);
    console.info('Succeeded in creating the PixelMap from Surface.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to create the PixelMap from Surface. Code: ${err.code}, message: ${err.message}`);
  }
}
```
