# PixelMap

Sendable PixelMap instance.

**继承/实现关系：** PixelMap extends [ISendable](arkts-image-sendableimage-isendable-t.md)

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

## 导入模块

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## applyColorSpace

```TypeScript
applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>
```

Apply color space of pixelmap, the pixels will be changed by input color space. This method uses a promise to return the result.This method is used to change color space of PixelMap. Pixel data will be changed by calling this method. If you want to set the colorspace property of PixelMap only, use method {@Link #setColorSpace(colorSpaceManager.ColorSpaceManager)}.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetColorSpace | colorSpaceManager.ColorSpaceManager | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [62980104](../errorcode-image.md#62980104-图片初始化错误) |
| [62980108](../errorcode-image.md#62980108-图片颜色转换错误) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |

## createAlphaPixelmap

```TypeScript
createAlphaPixelmap(): Promise<PixelMap>
```

Obtains new pixelmap with alpha information. This method uses a promise to return the information.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

## createAlphaPixelmapSync

```TypeScript
createAlphaPixelmapSync(): PixelMap
```

Obtains new pixelmap with alpha information.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## crop

```TypeScript
crop(region: image.Region): Promise<void>
```

Crop the image. This method uses a promise to return the result.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | image.Region | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## cropSync

```TypeScript
cropSync(region: image.Region): void
```

Crop the image.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| region | image.Region | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## flip

```TypeScript
flip(horizontal: boolean, vertical: boolean): Promise<void>
```

Image flipping. This method uses a promise to return the result.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| horizontal | boolean | 是 |
| vertical | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## flipSync

```TypeScript
flipSync(horizontal: boolean, vertical: boolean): void
```

Image flipping.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| horizontal | boolean | 是 |
| vertical | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## getBytesNumberPerRow

```TypeScript
getBytesNumberPerRow(): number
```

Obtains the number of bytes in each line of the image pixelmap.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| number |

## getColorSpace

```TypeScript
getColorSpace(): colorSpaceManager.ColorSpaceManager
```

Get color space of pixelmap.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| colorSpaceManager.ColorSpaceManager |

**错误码：**

| 错误码ID |
| --- |
| [62980101](../errorcode-image.md#62980101-图片输入数据错误) |
| [62980103](../errorcode-image.md#62980103-图片类型不支持) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |

## getDensity

```TypeScript
getDensity(): number
```

Obtains the density of the image pixelmap.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| number |

## getImageInfo

```TypeScript
getImageInfo(): Promise<image.ImageInfo>
```

Obtains pixelmap information about this image. This method uses a promise to return the information.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ImageInfo](arkts-image-image-imageinfo-i.md)&gt; |

## getImageInfoSync

```TypeScript
getImageInfoSync(): image.ImageInfo
```

Get image information from image source.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 |
| --- |
| [ImageInfo](arkts-image-image-imageinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [501](../errorcode-image.md#501-无法调用接口) |

## getPixelBytesNumber

```TypeScript
getPixelBytesNumber(): number
```

Obtains the total number of bytes of the image pixelmap.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| number |

## marshalling

```TypeScript
marshalling(sequence: rpc.MessageSequence): void
```

Marshalling PixelMap and write into MessageSequence.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sequence | rpc.MessageSequence | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980097](../errorcode-image.md#62980097-pixelmap序列化传输失败) |

## opacity

```TypeScript
opacity(rate: number): Promise<void>
```

Set the transparent rate of pixelmap. This method uses a promise to return the result.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rate | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## opacitySync

```TypeScript
opacitySync(rate: number): void
```

Set the transparent rate of pixelmap.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rate | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## readPixels

```TypeScript
readPixels(area: image.PositionArea): Promise<void>
```

Reads image pixelmap data in an area. This method uses a promise to return the data read.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | image.PositionArea | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## readPixelsSync

```TypeScript
readPixelsSync(area: image.PositionArea): void
```

Reads image pixelmap data in an area.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | image.PositionArea | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(dst: ArrayBuffer): Promise<void>
```

Reads image pixelmap data and writes the data to an ArrayBuffer. This method uses a promise to return the result.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## readPixelsToBufferSync

```TypeScript
readPixelsToBufferSync(dst: ArrayBuffer): void
```

Reads image pixelmap data and writes the data to an ArrayBuffer.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## release

```TypeScript
release(): Promise<void>
```

Releases this PixelMap object. This method uses a promise to return the result.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## rotate

```TypeScript
rotate(angle: number): Promise<void>
```

Image rotation. This method uses a promise to return the result.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## rotateSync

```TypeScript
rotateSync(angle: number): void
```

Image rotation.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## scale

```TypeScript
scale(x: number, y: number): Promise<void>
```

Image zoom in width and height. This method uses a promise to return the result.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## scaleSync

```TypeScript
scaleSync(x: number, y: number): void
```

Image zoom in width and height.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## setColorSpace

```TypeScript
setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void
```

Set color space of pixelmap.This method is only used to set the colorspace property of PixelMap, while all pixel data remains the same after calling this method. If you want to change colorspace for all pixels, use method {@Link #applyColorSpace(colorSpaceManager.ColorSpaceManager)}.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorSpace | colorSpaceManager.ColorSpaceManager | 是 |

**错误码：**

| 错误码ID |
| --- |
| [62980111](../errorcode-image.md#62980111-图片源数据不完整) |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |

## translate

```TypeScript
translate(x: number, y: number): Promise<void>
```

Image position transformation. This method uses a promise to return the result.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## translateSync

```TypeScript
translateSync(x: number, y: number): void
```

Image position transformation.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## unmarshalling

```TypeScript
unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>
```

Creates a PixelMap object based on MessageSequence parameter.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sequence | rpc.MessageSequence | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [62980115](../errorcode-image.md#62980115-图片无效参数) |
| [62980097](../errorcode-image.md#62980097-pixelmap序列化传输失败) |
| [62980096](../errorcode-image.md#62980096-操作失败) |

## writeBufferToPixels

```TypeScript
writeBufferToPixels(src: ArrayBuffer): Promise<void>
```

Reads image data in an ArrayBuffer and writes the data to a PixelMap object. This method uses a promise to return the result.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## writeBufferToPixelsSync

```TypeScript
writeBufferToPixelsSync(src: ArrayBuffer): void
```

Reads image data in an ArrayBuffer and writes the data to a PixelMap object.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## writePixels

```TypeScript
writePixels(area: image.PositionArea): Promise<void>
```

Writes image pixelmap data to the specified area. This method uses a promise to return the operation result.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | image.PositionArea | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## writePixelsSync

```TypeScript
writePixelsSync(area: image.PositionArea): void
```

Writes image pixelmap data to the specified area.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| area | image.PositionArea | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [501](../errorcode-image.md#501-无法调用接口) |

## isEditable

```TypeScript
readonly isEditable: boolean
```

Whether the image pixelmap can be edited.

**类型：** boolean

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

## isStrideAlignment

```TypeScript
readonly isStrideAlignment: boolean
```

Is it stride Alignment

**类型：** boolean

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core
