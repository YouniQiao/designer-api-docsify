# createIncrementalSource

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createIncrementalSource

```TypeScript
function createIncrementalSource(buf: ArrayBuffer): ImageSource | undefined
```

Creates an ImageSource instance based on the buffer in incremental.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-image-function createIncrementalSource(buf: ArrayBuffer): ImageSource | undefined--><!--Device-image-function createIncrementalSource(buf: ArrayBuffer): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | The buffer of the image. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) | Returns the ImageSource instance if the operation is successful; returns undefined otherwise. |


## createIncrementalSource

```TypeScript
function createIncrementalSource(buf: ArrayBuffer, 
      options?: SourceOptions): ImageSource | undefined
```

Creates an ImageSource instance based on the buffer in incremental.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-image-function createIncrementalSource(buf: ArrayBuffer,       options?: SourceOptions): ImageSource | undefined--><!--Device-image-function createIncrementalSource(buf: ArrayBuffer,       options?: SourceOptions): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | The buffer of the image. |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | No | The config of source. |

**Return value:**

| Type | Description |
| --- | --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) | Returns the ImageSource instance if the operation is successful; returns undefined otherwise. |

