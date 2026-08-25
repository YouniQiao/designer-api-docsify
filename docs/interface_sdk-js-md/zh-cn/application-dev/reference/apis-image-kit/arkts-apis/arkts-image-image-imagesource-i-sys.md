# ImageSource

ImageSource类，用于获取图片相关信息。在调用ImageSource的方法前，需要先通过[image.createImageSource](arkts-image-image-createimagesource-f.md)构建一个ImageSource实例。ImageSource的所有方法均不支持并发调用。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-image-image-imagesource-i.md#release)方法及时 释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 6

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createWideGamutSdrPixelMap

```TypeScript
createWideGamutSdrPixelMap(): Promise<PixelMap>
```

创建SDR的PixelMap对象。当图片为带有3通道GainMap的HDR图片时，会将其基础图扩展为BT.2020色域的SDR图。使用Promise异步回调。

> **说明：**&gt;
> - 对SDR图片源，按图片自带的色彩空间解码，输出SDR图。&gt;
> - 对带有单通道GainMap的HDR图片源，解码其基础图（SDR图），忽略GainMap。&gt;
> - 对带有3通道GainMap的HDR图片源，解码其基础图（SDR图），并将输出SDR图的色域扩展为
> [ColorSpace](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-colorspacemanager-colorspace-e.md).DISPLAY_BT2020_SRGB。

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700103](../errorcode-image.md#7700103-图片太大) |
| [7700301](../errorcode-image.md#7700301-解码失败) |

## isJpegProgressive

```TypeScript
isJpegProgressive(): Promise<boolean>
```

判断Jpeg图片是否是渐进式图片。使用Promise异步回调。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7700101](../errorcode-image.md#7700101-图片源存在问题) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |

## modifyImageAllProperties

```TypeScript
modifyImageAllProperties(records: Record<string, string|null>): Promise<void>
```

批量修改图片属性。使用Promise异步回调。Exif属性中除"JPEGInterchangeFormat"/"JPEGInterchangeFormatLength"/"GIFLoopCount"字段外，其他均支持修改。

> **说明：**&gt;
> - 调用该接口修改属性会改变属性字节长度，建议通过传入文件描述符来创建[image.createImageSource](arkts-image-image-createimagesource-f.md)实例或通过传入的uri创建
> [image.createImageSource](arkts-image-image-createimagesource-f.md)实例。&gt;
> - 支持修改JPEG、PNG、HEIF和WEBP文件类型的图片属性，图片需要包含Exif信息。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| records | Record & lt;string, string \ | null & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7700102](../errorcode-image.md#7700102-不支持的mime类型) |
| [7700202](../errorcode-image.md#7700202-不支持的元数据) |
| [7700304](../errorcode-image.md#7700304-图片信息写入文件失败) |
