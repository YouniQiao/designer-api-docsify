# ImageSource

ImageSource类，用于获取图片相关信息。在调用ImageSource的方法前，需要先通过 [sendableImage.createImageSource](arkts-image-sendableimage-createimagesource-f.md)构建一个ImageSource实例。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](arkts-image-sendableimage-pixelmap-i.md#release)方法及时释放内存。释放时应确保该实例的所有异步方法均执行 完成，且后续不再使用该实例。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

## 导入模块

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## createPixelMap

```TypeScript
createPixelMap(options?: image.DecodingOptions): Promise<PixelMap>
```

通过图片解码参数创建PixelMap对象。使用Promise异步回调。由于图片占用内存较大，所以当PixelMap对象使用完成后，应主动调用[release](arkts-image-sendableimage-pixelmap-i.md#release)方法及时释放内存。释放时应确保该对象的所有异步方法均执行完成， 且后续不再使用该对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | image.DecodingOptions | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PixelMap & gt; |

## release

```TypeScript
release(): Promise<void>
```

释放ImageSource实例。使用Promise异步回调。由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
