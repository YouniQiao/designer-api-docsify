# ImageSource

Provides APIs to obtain image information. Before calling any API in ImageSource, you must use [sendableImage.createImageSource](arkts-image-sendableimage-createimagesource-f.md) to create an ImageSource instance.Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](arkts-image-sendableimage-pixelmap-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageSource

## Modules to Import

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## createPixelMap

```TypeScript
createPixelMap(options?: image.DecodingOptions): Promise<PixelMap>
```

Creates a PixelMap object based on decoding options. This API uses a promise to return the result.Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](arkts-image-sendableimage-pixelmap-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | image.DecodingOptions | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PixelMap & gt; |

## release

```TypeScript
release(): Promise<void>
```

Releases this ImageSource instance. This API uses a promise to return the result.Images occupy a large amount of memory. When you finish using an ImageSource instance, call this API to free the memory promptly.Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
