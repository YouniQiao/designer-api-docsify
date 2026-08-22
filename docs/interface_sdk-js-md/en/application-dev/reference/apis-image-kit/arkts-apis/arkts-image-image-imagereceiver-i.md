# ImageReceiver

The **ImageReceiver** class provides APIs to obtain the surface ID of a component, read the latest image, read the next image, and release the ImageReceiver instance. The ImageReceiver acts as the receiver and consumer of images. Its parameter properties do not actually affect the received images. The configuration of image properties should be done on the sending side (the producer), such as when creating a camera preview stream with [createPreviewOutput](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md#createpreviewoutput) . Before calling any APIs in ImageReceiver, you must use [image.createImageReceiver](arkts-image-image-createimagereceiver-f.md) to create an ImageReceiver instance. Since API version 23, you are advised to use [image.createImageReceiver](arkts-image-image-createimagereceiver-f.md) to create an **ImageReceiver** instance based on the passed [ImageReceiverOptions](arkts-image-image-imagereceiveroptions-i.md). Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-image-interface ImageReceiver--><!--Device-image-interface ImageReceiver-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## getReceivingSurfaceId

```TypeScript
getReceivingSurfaceId(callback: AsyncCallback<string>): void
```

Obtains a surface ID for the camera or other components. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-ImageReceiver-getReceivingSurfaceId(callback: AsyncCallback<string>): void--><!--Device-ImageReceiver-getReceivingSurfaceId(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the surface ID obtained. Otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetReceivingSurfaceId(receiver : image.ImageReceiver) {
  receiver.getReceivingSurfaceId((err: BusinessError, id: string) => {
    if (err) {
      console.error(`Failed to get the ReceivingSurfaceId.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in getting the ReceivingSurfaceId.');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function GetReceivingSurfaceId(receiver : image.ImageReceiver) {
  receiver.getReceivingSurfaceId().then((id: string) => { 
    console.info('Succeeded in getting the ReceivingSurfaceId.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to get the ReceivingSurfaceId.code ${error.code},message is ${error.message}`);
  })
}
```

## getReceivingSurfaceId

```TypeScript
getReceivingSurfaceId(): Promise<string>
```

Obtains a surface ID for the camera or other components. This API uses a promise to return the result.

**Since:** 23

<!--Device-ImageReceiver-getReceivingSurfaceId(): Promise<string>--><!--Device-ImageReceiver-getReceivingSurfaceId(): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the surface ID. |

**Examples**

See [getReceivingSurfaceId](#getreceivingsurfaceid)

## off('imageArrival')

```TypeScript
off(type: 'imageArrival', callback?: AsyncCallback<void>): void
```

Unregisters the callback function that is triggered when the buffer is released. This API uses an asynchronous callback to return the result.

**Since:** 13

<!--Device-ImageReceiver-off(type: 'imageArrival', callback?: AsyncCallback<void>): void--><!--Device-ImageReceiver-off(type: 'imageArrival', callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imageArrival' | Yes | Type of event, which is **'imageArrival'**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No | Callback to unregister. |

## offImageArrival

```TypeScript
offImageArrival(callback?: AsyncCallback<void>): void
```

Remove callback subscriptions when releasing buffer.

**Since:** 23

<!--Device-ImageReceiver-offImageArrival(callback?: AsyncCallback<void>): void--><!--Device-ImageReceiver-offImageArrival(callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No | Callback to be removed. |

## on('imageArrival')

```TypeScript
on(type: 'imageArrival', callback: AsyncCallback<void>): void
```

Listens for image arrival events. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-ImageReceiver-on(type: 'imageArrival', callback: AsyncCallback<void>): void--><!--Device-ImageReceiver-on(type: 'imageArrival', callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'imageArrival' | Yes | Type of event to listen for. The value is fixed at **'imageArrival'**, which is triggered when an image is received. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## onImageArrival

```TypeScript
onImageArrival(callback: AsyncCallback<void>): void
```

Subscribe callback when receiving an image.

**Since:** 23

<!--Device-ImageReceiver-onImageArrival(callback: AsyncCallback<void>): void--><!--Device-ImageReceiver-onImageArrival(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return image. |

## readLatestImage

```TypeScript
readLatestImage(callback: AsyncCallback<Image>): void
```

Reads the latest image from the ImageReceiver instance. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> This API can be called to receive data only after the
> [on](#onimagearrival) callback is triggered.
> When the [Image](arkts-image-image-image-i.md) object returned by this API is no longer needed, call
> [release](arkts-image-image-image-i.md#release) to release the
> object. New data can be received only after the release.

**Since:** 23

<!--Device-ImageReceiver-readLatestImage(callback: AsyncCallback<Image>): void--><!--Device-ImageReceiver-readLatestImage(callback: AsyncCallback<Image>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Image&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the latest image obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadLatestImage(receiver : image.ImageReceiver) {
  receiver.readLatestImage((err: BusinessError, img: image.Image) => {
    if (err) {
      console.error(`Failed to read the latest Image.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in reading the latest Image.');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadLatestImage(receiver : image.ImageReceiver) {
  receiver.readLatestImage().then((img: image.Image) => {
    console.info('Succeeded in reading the latest Image.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to read the latest Image.code ${error.code},message is ${error.message}`);
  });
}
```

## readLatestImage

```TypeScript
readLatestImage(): Promise<Image>
```

Reads the latest image from the ImageReceiver instance. This API uses a promise to return the result.

> **NOTE：**
> 
> This API can be called to receive data only after the
> [on](#onimagearrival) callback is triggered.
> When the [Image](arkts-image-image-image-i.md) object returned by this API is no longer needed, call
> [release](arkts-image-image-image-i.md#release) to release the
> object. New data can be received only after the release.

**Since:** 23

<!--Device-ImageReceiver-readLatestImage(): Promise<Image>--><!--Device-ImageReceiver-readLatestImage(): Promise<Image>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Image&gt; | Promise used to return the latest image. |

**Examples**

See [readLatestImage](#readlatestimage)

## readNextImage

```TypeScript
readNextImage(callback: AsyncCallback<Image>): void
```

Reads the next image from the ImageReceiver instance. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> This API can be called to receive data only after the
> [on](#onimagearrival) callback is triggered.
> When the [Image](arkts-image-image-image-i.md) object returned by this API is no longer needed, call
> [release](arkts-image-image-image-i.md#release) to release the
> object. New data can be received only after the release.

**Since:** 23

<!--Device-ImageReceiver-readNextImage(callback: AsyncCallback<Image>): void--><!--Device-ImageReceiver-readNextImage(callback: AsyncCallback<Image>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Image&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the next image obtained. Otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadNextImage(receiver : image.ImageReceiver) {
  receiver.readNextImage((err: BusinessError, img: image.Image) => {
    if (err) {
      console.error(`Failed to read the next Image.code ${err.code},message is ${err.message}`);
    } else {
      console.info('Succeeded in reading the next Image.');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function ReadNextImage(receiver : image.ImageReceiver) {
  receiver.readNextImage().then((img: image.Image) => {
    console.info('Succeeded in reading the next Image.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to read the next Image.code ${error.code},message is ${error.message}`);
  });
}
```

## readNextImage

```TypeScript
readNextImage(): Promise<Image>
```

Reads the next image from the ImageReceiver instance. This API uses a promise to return the result.

> **NOTE：**
> 
> This API can be called to receive data only after the
> [on](#onimagearrival) callback is triggered.
> When the [Image](arkts-image-image-image-i.md) object returned by this API is no longer needed, call
> [release](arkts-image-image-image-i.md#release) to release the
> object. New data can be received only after the release.

**Since:** 23

<!--Device-ImageReceiver-readNextImage(): Promise<Image>--><!--Device-ImageReceiver-readNextImage(): Promise<Image>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Image&gt; | Promise used to return the next image. |

**Examples**

See [readNextImage](#readnextimage)

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases this ImageReceiver instance. This API uses an asynchronous callback to return the result.

Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-ImageReceiver-release(callback: AsyncCallback<void>): void--><!--Device-ImageReceiver-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

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

Releases this ImageReceiver instance. This API uses a promise to return the result.

Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-ImageReceiver-release(): Promise<void>--><!--Device-ImageReceiver-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

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

<!--Device-ImageReceiver-readonly capacity: int--><!--Device-ImageReceiver-readonly capacity: int-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

## format

```TypeScript
readonly format: ImageFormat
```

Image format. The value is an enum value of [ImageFormat](arkts-image-image-imageformat-e.md). ( Currently, only **ImageFormat:JPEG** is supported. The format actually returned depends on the producer, for example, camera.)

**Type:** [ImageFormat](arkts-image-image-imageformat-e.md)

**Since:** 23

<!--Device-ImageReceiver-readonly format: ImageFormat--><!--Device-ImageReceiver-readonly format: ImageFormat-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

## size

```TypeScript
readonly size: Size
```

Image size. This parameter does not affect the size of the received image. The actual returned size is determined by the producer, for example, the camera.

**Type:** Size

**Since:** 23

<!--Device-ImageReceiver-readonly size: Size--><!--Device-ImageReceiver-readonly size: Size-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageReceiver

