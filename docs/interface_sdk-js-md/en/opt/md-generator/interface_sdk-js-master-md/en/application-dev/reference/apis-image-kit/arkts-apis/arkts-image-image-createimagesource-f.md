# createImageSource

## Modules to Import

```TypeScript
```

## createImageSource

```TypeScript
function createImageSource(uri: string): ImageSource
```

Creates an ImageSource instance based on a given URI. Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-image-function createImageSource(uri: string): ImageSource--><!--Device-image-function createImageSource(uri: string): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |

**Examples**

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

<!--Device-image-function createImageSource(uri: string): ImageSource | undefined--><!--Device-image-function createImageSource(uri: string): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(uri: string, options: SourceOptions): ImageSource
```

Creates an ImageSource instance based on a given URI. Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-image-function createImageSource(uri: string, options: SourceOptions): ImageSource--><!--Device-image-function createImageSource(uri: string, options: SourceOptions): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |

**Examples**

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

<!--Device-image-function createImageSource(uri: string, options: SourceOptions): ImageSource | undefined--><!--Device-image-function createImageSource(uri: string, options: SourceOptions): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(fd: number): ImageSource
```

Creates an ImageSource instance based on a given file descriptor. Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-image-function createImageSource(fd: int): ImageSource--><!--Device-image-function createImageSource(fd: int): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |

**Examples**

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

async function CreateImageSource(context : Context) {
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  let filePath: string = context.filesDir + "/test.jpg";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
  const imageSourceObj: image.ImageSource = image.createImageSource(file.fd);
}
```


## createImageSource

```TypeScript
function createImageSource(fd: number): ImageSource | undefined
```

Creates an ImageSource instance based on the file descriptor.

**Since:** 23

<!--Device-image-function createImageSource(fd: int): ImageSource | undefined--><!--Device-image-function createImageSource(fd: int): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(fd: number, options: SourceOptions): ImageSource
```

Creates an ImageSource instance based on a given file descriptor. Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-image-function createImageSource(fd: int, options: SourceOptions): ImageSource--><!--Device-image-function createImageSource(fd: int, options: SourceOptions): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |

**Examples**

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

async function CreateImageSource(context : Context) {
  let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  const filePath: string = context.filesDir + "/test.jpg";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
  const imageSourceObj: image.ImageSource = image.createImageSource(file.fd, sourceOptions);
}
```


## createImageSource

```TypeScript
function createImageSource(fd: number, options: SourceOptions): ImageSource | undefined
```

Creates an ImageSource instance based on the file descriptor.

**Since:** 23

<!--Device-image-function createImageSource(fd: int, options: SourceOptions): ImageSource | undefined--><!--Device-image-function createImageSource(fd: int, options: SourceOptions): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(buf: ArrayBuffer): ImageSource
```

Creates an ImageSource instance based on buffers. The data passed by **buf** must be undecoded. Do not pass the pixel buffer data such as RBGA and YUV. If you want to create a PixelMap based on the pixel buffer data, call [image.createPixelMapSync](arkts-image-image-imagesource-i.md#createpixelmapsync) . Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-image-function createImageSource(buf: ArrayBuffer): ImageSource--><!--Device-image-function createImageSource(buf: ArrayBuffer): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |

**Examples**

```TypeScript
async function CreateImageSource() {
  const buf: ArrayBuffer = new ArrayBuffer(96); // 96 indicates the size of the pixel buffer to create. The value is calculated as follows: width × height × 4.
  const imageSourceObj: image.ImageSource = image.createImageSource(buf);
}
```


## createImageSource

```TypeScript
function createImageSource(buf: ArrayBuffer): ImageSource | undefined
```

Creates an ImageSource instance based on the buffer.

**Since:** 23

<!--Device-image-function createImageSource(buf: ArrayBuffer): ImageSource | undefined--><!--Device-image-function createImageSource(buf: ArrayBuffer): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource
```

Creates an ImageSource instance based on buffers. The data passed by **buf** must be undecoded. Do not pass the pixel buffer data such as RBGA and YUV. If you want to create a PixelMap based on the pixel buffer data, call [image.createPixelMapSync](arkts-image-image-imagesource-i.md#createpixelmapsync) . Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-image-function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource--><!--Device-image-function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |

**Examples**

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

<!--Device-image-function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource | undefined--><!--Device-image-function createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createImageSource

```TypeScript
function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions): ImageSource
```

Creates an ImageSource instance based on the raw file descriptor of an image resource file. Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-image-imagesource-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-image-function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions): ImageSource--><!--Device-image-function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions): ImageSource-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rawfile | resourceManager.RawFileDescriptor | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |

**Examples**

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

<!--Device-image-function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions)      : ImageSource | undefined--><!--Device-image-function createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions)      : ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rawfile | resourceManager.RawFileDescriptor | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |
