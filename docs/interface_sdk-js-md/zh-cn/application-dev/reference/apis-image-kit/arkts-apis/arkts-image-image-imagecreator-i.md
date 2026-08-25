# ImageCreator

ImageCreator类，作为图片的生产者，用于将图片写入到Surface中。在调用以下方法前需要先通过[image.createImageCreator](arkts-image-image-createimagecreator-f.md)创建ImageCreator实例，ImageCreator不支持多线程。由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用[release](#release)方法 及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

> **说明：**&gt;
> - 本Interface首批接口从API version 9开始支持。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

## 导入模块

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## dequeueImage

```TypeScript
dequeueImage(callback: AsyncCallback<Image>): void
```

从空闲队列中获取buffer图片，用于绘制UI内容。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Image&gt; | 是 |

## dequeueImage

```TypeScript
dequeueImage(): Promise<Image>
```

从空闲队列中获取buffer图片，用于绘制UI内容。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**返回值：**

| 类型 |
| --- |
| Promise & lt;Image & gt; |

## off('imageRelease')

```TypeScript
off(type: 'imageRelease', callback?: AsyncCallback<void>): void
```

释放buffer时，移除注册的回调函数。使用callback异步回调。

**起始版本：** 13

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imageRelease' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

## on('imageRelease')

```TypeScript
on(type: 'imageRelease', callback: AsyncCallback<void>): void
```

监听imageRelease事件。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imageRelease' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## queueImage

```TypeScript
queueImage(image: Image, callback: AsyncCallback<void>): void
```

将绘制好的图片放入队列。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [image](arkts-multimedia-image.md) | [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## queueImage

```TypeScript
queueImage(image: Image): Promise<void>
```

将绘制好的图片放入队列。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [image](arkts-multimedia-image.md) | [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放当前图像。使用callback异步回调。由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## release

```TypeScript
release(): Promise<void>
```

释放当前图像。使用Promise异步回调。由于图片占用内存较大，所以当ImageCreator实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保该实例的所有异步方法均执行完成，且后续不再使用该实例。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

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

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

## format

```TypeScript
readonly format: ImageFormat
```

图像格式。

**类型：** [ImageFormat](arkts-image-image-imageformat-e.md)

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator
