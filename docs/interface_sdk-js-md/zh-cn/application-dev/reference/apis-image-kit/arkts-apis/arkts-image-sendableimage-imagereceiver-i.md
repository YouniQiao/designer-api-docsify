# ImageReceiver

图像接收类，用于获取组件Surface ID，接收最新的图片和读取下一张图片，以及释放ImageReceiver实例。在调用以下方法前需要先创建ImageReceiver实例。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

## 导入模块

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## getReceivingSurfaceId

```TypeScript
getReceivingSurfaceId(): Promise<string>
```

用于获取一个Surface ID供Camera或其他组件使用。使用promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## on('imageArrival')

```TypeScript
on(type: 'imageArrival', callback: AsyncCallback<void>): void
```

接收图片时注册。使用callback异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imageArrival' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## readLatestImage

```TypeScript
readLatestImage(): Promise<Image>
```

从ImageReceiver读取最新的图片。使用promise异步回调。

> **注意**：&gt;
> 此接口需要在[on](#onimagearrival)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](arkts-image-sendableimage-image-i.md)对象使
> 用完毕后需要调用[release](arkts-image-sendableimage-pixelmap-i.md#release)方法释放，释放后才可以继续接收新的数据。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

| 类型 |
| --- |
| Promise & lt;Image & gt; |

## readNextImage

```TypeScript
readNextImage(): Promise<Image>
```

从ImageReceiver读取下一张图片。使用promise异步回调。

> **注意**：&gt;
> 此接口需要在[on](#onimagearrival)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](arkts-image-sendableimage-image-i.md)对象使
> 用完毕后需要调用[release](arkts-image-sendableimage-pixelmap-i.md#release)方法释放，释放后才可以继续接收新的数据。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

| 类型 |
| --- |
| Promise & lt;Image & gt; |

## release

```TypeScript
release(): Promise<void>
```

释放ImageReceiver实例。使用promise异步回调。由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## capacity

```TypeScript
readonly capacity: number
```

同时访问的图像数。该参数仅作为期望值，实际capacity由设备硬件决定。

**类型：** number

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

## format

```TypeScript
readonly format: image.ImageFormat
```

图像格式。

**类型：** image.ImageFormat

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

## size

```TypeScript
readonly size: image.Size
```

图片大小。

**类型：** image.Size

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver
