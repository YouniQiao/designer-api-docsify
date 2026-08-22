# ImageCreator

The ImageCreator class provides APIs for applications to request an image data area and compile image data.

Before calling any APIs in ImageCreator, you must use [image.createImageCreator](arkts-image-image-createimagecreator-f.md) to create an ImageCreator instance. ImageCreator does not support multiple threads.

Images occupy a large amount of memory. When you finish using an ImageCreator instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-image-interface ImageCreator--><!--Device-image-interface ImageCreator-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## dequeueImage

```TypeScript
dequeueImage(callback: AsyncCallback<Image>): void
```

Obtains an image buffer from the idle queue and writes image data into it. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-ImageCreator-dequeueImage(callback: AsyncCallback<Image>): void--><!--Device-ImageCreator-dequeueImage(callback: AsyncCallback<Image>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Image&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the latest image obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function DequeueImage(creator : image.ImageCreator) {
  creator.dequeueImage((err: BusinessError, img: image.Image) => {
    if (err) {
      console.error(`Failed to dequeue the Image.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in dequeuing the Image.');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function DequeueImage(creator : image.ImageCreator) {
  creator.dequeueImage().then((img: image.Image) => {
    console.info('Succeeded in dequeuing the Image.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to dequeue the Image.code ${error.code},message is ${error.message}`);
  })
}
```

## dequeueImage

```TypeScript
dequeueImage(): Promise<Image>
```

Obtains an image buffer from the idle queue and writes image data into it. This API uses a promise to return the result.

**Since:** 23

<!--Device-ImageCreator-dequeueImage(): Promise<Image>--><!--Device-ImageCreator-dequeueImage(): Promise<Image>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Image&gt; | Promise used to return the latest image. |

**Examples**

See [dequeueImage](#dequeueimage)

## off('imageRelease')

```TypeScript
off(type: 'imageRelease', callback?: AsyncCallback<void>): void
```

Unregisters the callback function that is triggered when the buffer is released. This API uses an asynchronous callback to return the result.

**Since:** 13

<!--Device-ImageCreator-off(type: 'imageRelease', callback?: AsyncCallback<void>): void--><!--Device-ImageCreator-off(type: 'imageRelease', callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imageRelease' | Yes | Type of event, which is **'imageRelease'**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No | Callback used to return the result. If the operation is successful, **err** is null; otherwise, **err** is an error object. |

## offImageRelease

```TypeScript
offImageRelease(callback?: AsyncCallback<void>): void
```

Remove callback subscriptions when releasing buffer

**Since:** 23

<!--Device-ImageCreator-offImageRelease(callback?: AsyncCallback<void>): void--><!--Device-ImageCreator-offImageRelease(callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No | Callback to be removed. |

## on('imageRelease')

```TypeScript
on(type: 'imageRelease', callback: AsyncCallback<void>): void
```

Listens for image release events. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-ImageCreator-on(type: 'imageRelease', callback: AsyncCallback<void>): void--><!--Device-ImageCreator-on(type: 'imageRelease', callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imageRelease' | Yes | Type of event, which is **'imageRelease'**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## onImageRelease

```TypeScript
onImageRelease(callback: AsyncCallback<void>): void
```

Subscribe callback when releasing buffer

**Since:** 23

<!--Device-ImageCreator-onImageRelease(callback: AsyncCallback<void>): void--><!--Device-ImageCreator-onImageRelease(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the operation result. |

## queueImage

```TypeScript
queueImage(image: Image, callback: AsyncCallback<void>): void
```

Places the drawn image in the queue. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-ImageCreator-queueImage(image: Image, callback: AsyncCallback<void>): void--><!--Device-ImageCreator-queueImage(image: Image, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| image | Image | Yes | Drawn image. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function QueueImage(creator : image.ImageCreator) {
  creator.dequeueImage().then((img: image.Image) => {
    // Draw the image.
    img.getComponent(4).then((component : image.Component) => {
      let bufferArr: Uint8Array = new Uint8Array(component.byteBuffer);
      for (let i = 0; i < bufferArr.length; i += 4) {
        bufferArr[i] = 0; // B
        bufferArr[i + 1] = 0; // G
        bufferArr[i + 2] = 255; // R
        bufferArr[i + 3] = 255; // A
      }
    })
    creator.queueImage(img, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to queue the Image.code ${err.code},message is ${err.message}`);
      } else {
        console.info('Succeeded in queuing the Image.');
      }
    })
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function QueueImage(creator : image.ImageCreator) {
  creator.dequeueImage().then((img: image.Image) => {
    // Draw the image.
    img.getComponent(4).then((component: image.Component) => {
      let bufferArr: Uint8Array = new Uint8Array(component.byteBuffer);
      for (let i = 0; i < bufferArr.length; i += 4) {
        bufferArr[i] = 0; // B
        bufferArr[i + 1] = 0; // G
        bufferArr[i + 2] = 255; // R
        bufferArr[i + 3] = 255; // A
      }
    })
    creator.queueImage(img).then(() => {
      console.info('Succeeded in queuing the Image.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to queue the Image.code ${error.code},message is ${error.message}`);
    })
  })
}
```

## queueImage

```TypeScript
queueImage(image: Image): Promise<void>
```

Places the drawn image in the queue. This API uses a promise to return the result.

**Since:** 23

<!--Device-ImageCreator-queueImage(image: Image): Promise<void>--><!--Device-ImageCreator-queueImage(image: Image): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| image | Image | Yes | Drawn image. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [queueImage](#queueimage)

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this ImageCreator instance. This API uses an asynchronous callback to return the result.

Images occupy a large amount of memory. When you finish using an ImageCreator instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-ImageCreator-release(callback: AsyncCallback<void>): void--><!--Device-ImageCreator-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
async function Release(auxPictureObj: image.AuxiliaryPicture) {
  let funcName = "Release";
  if (auxPictureObj != null) {
    auxPictureObj.release();
    if (auxPictureObj.getType() == null) {
      console.info(funcName, 'Success !');
    } else {
      console.error(funcName, 'Failed !');
    }
  } else {
    console.error('PictureObj is null');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the image instance.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the image instance.');
    }
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(img : image.Image) {
  img.release().then(() => {
    console.info('Succeeded in releasing the image instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image instance.code ${error.code},message is ${error.message}`);
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(creator : image.ImageCreator) {
  creator.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the creator.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing creator.');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(creator : image.ImageCreator) {
  creator.release().then(() => {
    console.info('Succeeded in releasing creator.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the creator.code ${error.code},message is ${error.message}`);
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.release((err: BusinessError)=>{
    if (err) {
      console.error(`Failed to release image packaging.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing image packaging.');
    }
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
  imagePackerObj.release().then(() => {
    console.info('Succeeded in releasing image packaging.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release image packaging.code ${error.code},message is ${error.message}`);
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver : image.ImageReceiver) {
  receiver.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the receiver.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the receiver.');
    }
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(receiver : image.ImageReceiver) {
  receiver.release().then(() => {
    console.info('Succeeded in releasing the receiver.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the receiver.code ${error.code},message is ${error.message}`);
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(imageSourceObj : image.ImageSource) {
  imageSourceObj.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release the image source instance.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in releasing the image source instance.');
    }
  })
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(imageSourceObj : image.ImageSource) {
  imageSourceObj.release().then(() => {
    console.info('Succeeded in releasing the image source instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image source instance.code ${error.code},message is ${error.message}`);
  })
}
```

```TypeScript
async function Release(pictureObj : image.Picture) {
  let funcName = "Release";
  if (pictureObj != null) {
    pictureObj.release();
    if (pictureObj.getMainPixelmap() == null) {
      console.info(funcName, 'Success !');
    } else {
      console.error(funcName, 'Failed !');
    }
  } else {
    console.error('PictureObj is null');
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    await pixelMap.release().then(() => {
      console.info('Succeeded in releasing pixelmap object.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to release pixelmap object. code is ${error.code}, message is ${error.message}`);
    })
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function Release(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.release((err: BusinessError) => {
      if (err) {
        console.error(`Failed to release pixelmap object. code is ${err.code}, message is ${err.message}`);
        return;
      } else {
        console.info('Succeeded in releasing pixelmap object.');
      }
    })
  }
}
```

## release

```TypeScript
release(): Promise<void>
```

Releases this ImageCreator instance. This API uses a promise to return the result.

Images occupy a large amount of memory. When you finish using an ImageCreator instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-ImageCreator-release(): Promise<void>--><!--Device-ImageCreator-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [release](#release)

## capacity

```TypeScript
readonly capacity: int
```

Maximum number of images that can be accessed at the same time. This parameter is used only as an expected value. The actual capacity is determined by the device hardware.

**Type:** int

**Since:** 23

<!--Device-ImageCreator-readonly capacity: int--><!--Device-ImageCreator-readonly capacity: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

## format

```TypeScript
readonly format: ImageFormat
```

Image format.

**Type:** [ImageFormat](arkts-image-image-imageformat-e.md)

**Since:** 23

<!--Device-ImageCreator-readonly format: ImageFormat--><!--Device-ImageCreator-readonly format: ImageFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageCreator

