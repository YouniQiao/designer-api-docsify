# createPixelMapUsingAllocatorSync

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## createPixelMapUsingAllocatorSync

```TypeScript
function createPixelMapUsingAllocatorSync(colors: ArrayBuffer, param: InitializationOptions,
    allocatorType?: AllocatorType): PixelMap
```

Create pixelmap by data buffer based on opts, the memory type used by the PixelMap can be specified by allocatorType. By default, the system selects the memory type based on the image type, image size, platform capability, etc. When processing the PixelMap returned by this interface, please always consider the impact of stride.

**Since:** 23

<!--Device-image-function createPixelMapUsingAllocatorSync(colors: ArrayBuffer, param: InitializationOptions,    allocatorType?: AllocatorType): PixelMap--><!--Device-image-function createPixelMapUsingAllocatorSync(colors: ArrayBuffer, param: InitializationOptions,    allocatorType?: AllocatorType): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colors | ArrayBuffer | Yes | The image color buffer. |
| param | [InitializationOptions](arkts-image-image-initializationoptions-i.md) | Yes | Initialization options for pixelmap. |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | No | Indicate which memory type will be used by the returned PixelMap. |

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | Returns the instance if the operation is successful;Otherwise, return undefined. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Memory alloc failed. |
| [7600302](../errorcode-image.md#7600302-memory-copy-failure) | Memory copy failed. |

**Examples**

```TypeScript
function CreatePixelMapSync() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height * width *4.
  let opts: image.InitializationOptions = { editable: true, srcPixelFormat: image.PixelMapFormat.RGBA_8888, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapUsingAllocatorSync(color, opts, image.AllocatorType.AUTO);
  return pixelMap;
}
```

```TypeScript
function CreatePixelMapSync() {
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapUsingAllocatorSync(opts, image.AllocatorType.AUTO);
  return pixelMap;
}
```

```TypeScript
async function CreatePixelMapUsingAllocator(context : Context) {
  // "test.jpg" is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  let filePath: string = context.filesDir + "/test.jpg";
  let imageSource = image.createImageSource(filePath);
  let decodingOptions: image.DecodingOptions = {
    editable: true,
    desiredSize: { width: 3072, height: 4096 },
    rotate: 10,
    desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
    desiredRegion: { size: { width: 3072, height: 4096 }, x: 0, y: 0 },
    // If both desiredSize and desiredRegion are passed to the decoding API, you must also include cropAndScaleStrategy to determine whether to crop or scale first. CROP_FIRST is recommended.
    cropAndScaleStrategy: image.CropAndScaleStrategy.CROP_FIRST,
    index: 0
  };
  let pixelmap = imageSource.createPixelMapUsingAllocatorSync(decodingOptions, image.AllocatorType.AUTO);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
  } else {
    console.error('Failed to create pixelMap.');
  }
}
```


## createPixelMapUsingAllocatorSync

```TypeScript
function createPixelMapUsingAllocatorSync(param: InitializationOptions, allocatorType?: AllocatorType): PixelMap
```

Create an empty pixelmap by data buffer based on opts, the memory type used by the PixelMap can be specified by allocatorType. By default, the system selects the memory type based on the image type, image size, platform capability, etc. When processing the PixelMap returned by this interface, please always consider the impact of stride.

**Since:** 23

<!--Device-image-function createPixelMapUsingAllocatorSync(param: InitializationOptions, allocatorType?: AllocatorType): PixelMap--><!--Device-image-function createPixelMapUsingAllocatorSync(param: InitializationOptions, allocatorType?: AllocatorType): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [InitializationOptions](arkts-image-image-initializationoptions-i.md) | Yes | Initialization options for pixelmap. |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | No | Indicate which memory type will be used by the returned PixelMap. |

**Return value:**

| Type | Description |
| --- | --- |
| PixelMap | Returns the instance if the operation is successful;Otherwise, return undefined. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Memory alloc failed. |

**Examples**

See [createPixelMapUsingAllocatorSync](#createpixelmapusingallocatorsync)

