# createPictureByHdrAndSdrPixelMap（系统接口）

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPictureByHdrAndSdrPixelMap

```TypeScript
function createPictureByHdrAndSdrPixelMap(hdrPixelMap: PixelMap, sdrPixelMap: PixelMap): Promise<Picture>
```

根据HDR PixelMap和SDR PixelMap创建Picture对象。系统将使用HDR和SDR PixelMap生成一个增益图（gainmap），返回的Picture对象将包含SDR PixelMap和生成的gainmap PixelMap，像素格式为RGBA8888。使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hdrPixelMap | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |
| sdrPixelMap | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |


## createPictureByHdrAndSdrPixelMap

```TypeScript
function createPictureByHdrAndSdrPixelMap(hdrPixelMap: PixelMap, sdrPixelMap: PixelMap, 
      params: GainmapParams): Promise<Picture>
```

根据HDR PixelMap和SDR PixelMap创建Picture对象。系统将使用HDR和SDR PixelMap生成一个Gainmap（增益图），返回的Picture对象将包含SDR PixelMap和生成的Gainmap PixelMap，像素格式为RGBA8888。Gainmap PixelMap的尺寸可以通过设置params进行选择。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hdrPixelMap | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |
| sdrPixelMap | [PixelMap](arkts-image-image-pixelmap-i.md) | 是 |
| params | [GainmapParams](arkts-image-image-gainmapparams-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Picture](arkts-image-image-picture-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7600201](../errorcode-image.md#7600201-不支持的操作) |
