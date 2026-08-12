# createImageSource

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## createImageSource

```TypeScript
function createImageSource(uri: string): ImageSource
```

Creates an ImageSource instance based on a given URI.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call   
[release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-image-function createImageSource(uri: string): ImageSource--><!--Device-image-function createImageSource(uri: string): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Image path. Currently, only the application sandbox path is supported. &lt;br&gt;The following formats are supported: .jpg, .png, .gif, .bmp, .webp, .dng, .heic&lt;sup&gt;12+&lt;/sup&gt; (depending on the hardware), [.svg&lt;sup&gt;10+&lt;/sup&gt;](@ohos.multimedia.image:image.Functions#SVG Tags), and .ico&lt;sup&gt;11+&lt;/sup&gt;. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | ImageSource instance. If the operation fails, undefined is returned. |

## Examples

```TypeScript
async function CreateImageSource(context : Context) {
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  const path: string = context.filesDir + "/test.jpg";
  const imageSourceObj: image.ImageSource = image.createImageSource(path);
}
```


## createImageSource

```TypeScript
function createImageSource(uri: string): ImageSource | undefined
```

Creates an ImageSource instance based on the URI.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-image-function createImageSource(uri: string): ImageSource | undefined--><!--Device-image-function createImageSource(uri: string): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Image source URI. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | returns the ImageSource instance if the operation is successful; returns undefined otherwise. |


## createImageSource

```TypeScript
function createImageSource(uri: string, options: SourceOptions): ImageSource
```

Creates an ImageSource instance based on a given URI.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call   
[release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-image-function createImageSource(uri: string, options: SourceOptions): ImageSource--><!--Device-image-function createImageSource(uri: string, options: SourceOptions): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Image path. Currently, only the application sandbox path is supported. &lt;br&gt;The following formats are supported: .jpg, .png, .gif, .bmp, .webp, .dng, .heic&lt;sup&gt;12+&lt;/sup&gt; (depending on the hardware), [.svg&lt;sup&gt;10+&lt;/sup&gt;](@ohos.multimedia.image:image.Functions#SVG Tags), and .ico&lt;sup&gt;11+&lt;/sup&gt;. |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes | Image properties, including the image pixel density, pixel format, and image size. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | ImageSource instance. If the operation fails, undefined is returned. |

## Examples

```TypeScript
async function CreateImageSource(context : Context) {
  let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
  // 'test.png' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  const path: string = context.filesDir + "/test.png";
  let imageSourceObj: image.ImageSource = image.createImageSource(path, sourceOptions);
}
```


## createImageSource

```TypeScript
function createImageSource(uri: string, options: SourceOptions): ImageSource | undefined
```

Creates an ImageSource instance based on the URI.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-image-function createImageSource(uri: string, options: SourceOptions): ImageSource | undefined--><!--Device-image-function createImageSource(uri: string, options: SourceOptions): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Image source URI. |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes | The config of Image source. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | Returns the ImageSource instance if the operation is successful; returns undefined otherwise. |


## createImageSource

```TypeScript
function createImageSource(fd: int): ImageSource
```

Creates an ImageSource instance based on a given file descriptor.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call   
[release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-image-function createImageSource(fd: int): ImageSource--><!--Device-image-function createImageSource(fd: int): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | File descriptor. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | ImageSource instance. If the operation fails, undefined is returned. |

## Examples

```TypeScript
import { fileIo as fs } from '@kit.CoreFileKit';

async function CreateImageSource(context : Context) {
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  let filePath: string = context.filesDir + "/test.jpg";
  let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
  const imageSourceObj: image.ImageSource = image.createImageSource(file.fd);
}
```


## createImageSource

```TypeScript
function createImageSource(fd: int): ImageSource | undefined
```

Creates an ImageSource instance based on the file descriptor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-image-function createImageSource(fd: int): ImageSource | undefined--><!--Device-image-function createImageSource(fd: int): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | ID of a file descriptor |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | Returns the ImageSource instance if the operation is successful; returns undefined otherwise. |


## createImageSource

```TypeScript
function createImageSource(fd: int, options: SourceOptions): ImageSource
```

Creates an ImageSource instance based on a given file descriptor.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call   
[release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-image-function createImageSource(fd: int, options: SourceOptions): ImageSource--><!--Device-image-function createImageSource(fd: int, options: SourceOptions): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | File descriptor. |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes | Image properties, including the image pixel density, pixel format, and image size. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | ImageSource instance. If the operation fails, undefined is returned. |

## Examples

```TypeScript
import { fileIo as fs } from '@kit.CoreFileKit';

async function CreateImageSource(context : Context) {
  let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  const filePath: string = context.filesDir + "/test.jpg";
  let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
  const imageSourceObj: image.ImageSource = image.createImageSource(file.fd, sourceOptions);
}
```


## createImageSource

```TypeScript
function createImageSource(fd: int, options: SourceOptions): ImageSource | undefined
```

Creates an ImageSource instance based on the file descriptor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-image-function createImageSource(fd: int, options: SourceOptions): ImageSource | undefined--><!--Device-image-function createImageSource(fd: int, options: SourceOptions): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | ID of a file descriptor. |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes | The config of Image source. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | Returns the ImageSource instance if the operation is successful; returns undefined otherwise. |


## createImageSource

```TypeScript
function createImageSource(buf: ArrayBuffer): ImageSource
```

Creates an ImageSource instance based on buffers. The data passed by **buf** must be undecoded. Do not pass the pixel buffer data such as RBGA and YUV. If you want to create a PixelMap based on the pixel buffer data, call   
[image.createPixelMapSync](arkts-image-image-imagesource-i.md#createPixelMapSync-1).Images occupy a large amount of memory. When you finish using an ImageSource instance, call   
[release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-image-function createImageSource(buf: ArrayBuffer): ImageSource--><!--Device-image-function createImageSource(buf: ArrayBuffer): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | Array of image buffers. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | ImageSource instance. If the operation fails, undefined is returned. |

## Examples

```TypeScript
async function CreateImageSource() {
  const buf: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height * width *4.
  const imageSourceObj: image.ImageSource = image.createImageSource(buf);
}
```


## createImageSource

```TypeScript
function createImageSource(buf: ArrayBuffer): ImageSource | undefined
```

Creates an ImageSource instance based on the buffer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-image-function createImageSource(buf: ArrayBuffer): ImageSource | undefined--><!--Device-image-function createImageSource(buf: ArrayBuffer): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | The buffer of the image. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | Returns the ImageSource instance if the operation is successful; returns undefined otherwise. |


## createImageSource

```TypeScript
function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource
```

Creates an ImageSource instance based on buffers. The data passed by **buf** must be undecoded. Do not pass the pixel buffer data such as RBGA and YUV. If you want to create a PixelMap based on the pixel buffer data, call   
[image.createPixelMapSync](arkts-image-image-imagesource-i.md#createPixelMapSync-1).Images occupy a large amount of memory. When you finish using an ImageSource instance, call   
[release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-image-function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource--><!--Device-image-function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | Array of image buffers. |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes | Image properties, including the image pixel density, pixel format, and image size. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | ImageSource instance. If the operation fails, undefined is returned. |

## Examples

```TypeScript
async function CreateImageSource() {
  const data: ArrayBuffer = new ArrayBuffer(112);
  let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
  const imageSourceObj: image.ImageSource = image.createImageSource(data, sourceOptions);
}
```


## createImageSource

```TypeScript
function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource | undefined
```

Creates an ImageSource instance based on the buffer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-image-function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource | undefined--><!--Device-image-function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | The buffer of the image. |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes | The config of Image source. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | Returns the ImageSource instance if the operation is successful; returns undefined otherwise. |


## createImageSource

```TypeScript
function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions): ImageSource
```

Creates an ImageSource instance based on the raw file descriptor of an image resource file.Images occupy a large amount of memory. When you finish using an ImageSource instance, call   
[release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-image-function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions): ImageSource--><!--Device-image-function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rawfile | resourceManager.RawFileDescriptor | Yes | Raw file descriptor of the image resource file. |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | No | Image properties, including the image pixel density, pixel format, and image size. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | ImageSource instance. If the operation fails, undefined is returned. |

## Examples

```TypeScript
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
  
async function CreateImageSource(context : Context) {
  // Obtain a resource manager.
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  resourceMgr.getRawFd('test.jpg').then((rawFileDescriptor: resourceManager.RawFileDescriptor) => {
    const imageSourceObj: image.ImageSource = image.createImageSource(rawFileDescriptor);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get RawFileDescriptor.code is ${error.code}, message is ${error.message}`);
  })
}
```


## createImageSource

```TypeScript
function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions)
      : ImageSource | undefined
```

Creates an ImageSource instance based on the raw file descriptor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-image-function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions)      : ImageSource | undefined--><!--Device-image-function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions)      : ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rawfile | resourceManager.RawFileDescriptor | Yes | The raw file descriptor of the image. |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | No | The config of Image source. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | Returns the ImageSource instance if the operation is successful; returns undefined otherwise. |

