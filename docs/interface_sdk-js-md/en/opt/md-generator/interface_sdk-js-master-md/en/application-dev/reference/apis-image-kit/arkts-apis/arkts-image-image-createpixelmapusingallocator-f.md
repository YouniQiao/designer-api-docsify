# createPixelMapUsingAllocator

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPixelMapUsingAllocator

```TypeScript
function createPixelMapUsingAllocator(colors: ArrayBuffer, param: InitializationOptions,
    allocatorType?: AllocatorType): Promise<PixelMap>
```

Create pixelmap by data buffer based on opts, the memory type used by the PixelMap can be specified by allocatorType. By default, the system selects the memory type based on the image type, image size,platform capability, etc. When processing the PixelMap returned by this interface, please always consider the impact of stride.

**Since:** 20

<!--Device-image-function createPixelMapUsingAllocator(colors: ArrayBuffer, param: InitializationOptions,    allocatorType?: AllocatorType): Promise<PixelMap>--><!--Device-image-function createPixelMapUsingAllocator(colors: ArrayBuffer, param: InitializationOptions,    allocatorType?: AllocatorType): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colors | ArrayBuffer | Yes |
| param | [InitializationOptions](arkts-image-image-initializationoptions-i.md) | Yes |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;PixelMap&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) |
| [7600302](../errorcode-image.md#7600302-memory-copy-failure) |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createPixelMapUsingAllocator() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 indicates the size of the pixel buffer to create. The value is calculated as follows: width × height × 4.
  let opts: image.InitializationOptions = {
    size: { height: 4, width: 6 },
    srcPixelFormat: image.PixelMapFormat.RGBA_8888, // Pixel format of the source pixel data in the buffer.
    pixelFormat: image.PixelMapFormat.BGRA_8888, // Pixel format of the new PixelMap.
    editable: true
  };
  image.createPixelMapUsingAllocator(color, opts, image.AllocatorType.DMA).then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in creating the PixelMap.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to create the PixelMap. Code: ${err.code}, message: ${err.message}`);
  });
}
```
