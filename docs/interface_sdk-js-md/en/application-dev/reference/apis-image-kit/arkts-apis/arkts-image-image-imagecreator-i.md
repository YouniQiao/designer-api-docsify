# ImageCreator

The ImageCreator class provides APIs for applications to request an image data area and compile image data.Before calling any APIs in ImageCreator, you must use [image.createImageCreator](arkts-image-image-createimagecreator-f.md) to create an ImageCreator instance. ImageCreator does not support multiple threads.Images occupy a large amount of memory. When you finish using an ImageCreator instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## dequeueImage

```TypeScript
dequeueImage(callback: AsyncCallback<Image>): void
```

Obtains an image buffer from the idle queue and writes image data into it. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Image&gt; | Yes |

## dequeueImage

```TypeScript
dequeueImage(): Promise<Image>
```

Obtains an image buffer from the idle queue and writes image data into it. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Image & gt; |

## off('imageRelease')

```TypeScript
off(type: 'imageRelease', callback?: AsyncCallback<void>): void
```

Unregisters the callback function that is triggered when the buffer is released. This API uses an asynchronous callback to return the result.

**Since:** 13

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imageRelease' | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

## on('imageRelease')

```TypeScript
on(type: 'imageRelease', callback: AsyncCallback<void>): void
```

Listens for image release events. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imageRelease' | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## queueImage

```TypeScript
queueImage(image: Image, callback: AsyncCallback<void>): void
```

Places the drawn image in the queue. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [image](arkts-multimedia-image.md) | [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## queueImage

```TypeScript
queueImage(image: Image): Promise<void>
```

Places the drawn image in the queue. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [image](arkts-multimedia-image.md) | [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this ImageCreator instance. This API uses an asynchronous callback to return the result.Images occupy a large amount of memory. When you finish using an ImageCreator instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## release

```TypeScript
release(): Promise<void>
```

Releases this ImageCreator instance. This API uses a promise to return the result.Images occupy a large amount of memory. When you finish using an ImageCreator instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## capacity

```TypeScript
readonly capacity: number
```

Maximum number of images that can be accessed at the same time. This parameter is used only as an expected value. The actual capacity is determined by the device hardware.

**Type:** number

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

## format

```TypeScript
readonly format: ImageFormat
```

Image format.

**Type:** [ImageFormat](arkts-image-image-imageformat-e.md)

**Since:** 9

**System capability:** SystemCapability.Multimedia.Image.ImageCreator
