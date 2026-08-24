# ImageSource

Provides APIs to obtain image information. Before calling any API in ImageSource, you must use [sendableImage.createImageSource](arkts-image-sendableimage-createimagesource-f.md) to create an ImageSource instance.Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-sendableimage-pixelmap-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 12

<!--Device-sendableImage-interface ImageSource--><!--Device-sendableImage-interface ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## Modules to Import

```TypeScript
import { sendableImage } from '@kit.ImageKit';
```

## createPixelMap

```TypeScript
createPixelMap(options?: image.DecodingOptions): Promise<PixelMap>
```

Creates a PixelMap object based on decoding options. This API uses a promise to return the result.Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](arkts-image-sendableimage-pixelmap-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ImageSource-createPixelMap(options?: image.DecodingOptions): Promise<PixelMap>--><!--Device-ImageSource-createPixelMap(options?: image.DecodingOptions): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | image.DecodingOptions | No | Decoding options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | Promise used to return the PixelMap object. |

**Examples**

```TypeScript
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo() {
    const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height * width *4.
    let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
    sendableImage.createPixelMap(color, opts).then((pixelMap: sendableImage.PixelMap) => {
        console.info('Succeeded in creating pixelmap.');
    }).catch((error: BusinessError) => {
        console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
    })
}
```

```TypeScript
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(context : Context) {
  const path: string = context.cacheDir + "/test.jpg";
  const sendableImageSourceObj: sendableImage.ImageSource = sendableImage.createImageSource(path);
  sendableImageSourceObj.createPixelMap().then((pixelMap: sendableImage.PixelMap) => {
    console.info('Succeeded in creating pixelMap object through image decoding parameters.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to create pixelMap object through image decoding parameters. code ${error.code}, message is ${error.message}`);
  })
}
```

## release

```TypeScript
release(): Promise<void>
```

Releases this ImageSource instance. This API uses a promise to return the result.Images occupy a large amount of memory. When you finish using an ImageSource instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 12

<!--Device-ImageSource-release(): Promise<void>--><!--Device-ImageSource-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sendableImage } from '@kit.ImageKit';

async function Demo(pixelMap: sendableImage.PixelMap) {
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
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function Demo(context : Context) {
  const path: string = context.cacheDir + "/test.jpg";
  const sendableImageSourceObj: sendableImage.ImageSource = sendableImage.createImageSource(path);
  sendableImageSourceObj.release().then(() => {
    console.info('Succeeded in releasing the image source instance.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to release the image source instance. code ${error.code}, message is ${error.message}`);
  })
}
```

```TypeScript
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

async function Demo() {
  let size: image.Size = {
    height: 8192,
    width: 8
  }
  let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
  let img = await receiver.readNextImage();
  img.release().then(() => {
    console.info('release succeeded.');
  }).catch((error: BusinessError) => {
    console.error(`release failed. code ${error.code}, message is ${error.message}`);
  })
}
```

```TypeScript
import { sendableImage } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

async function Demo() {
  let size: image.Size = {
    height: 8192,
    width: 8
  }
  let receiver: sendableImage.ImageReceiver = sendableImage.createImageReceiver(size, image.ImageFormat.JPEG, 8);
  receiver.release().then(() => {
    console.info('release succeeded.');
  }).catch((error: BusinessError) => {
    console.error(`release failed. code ${error.code}, message is ${error.message}`);
  })
}
```

