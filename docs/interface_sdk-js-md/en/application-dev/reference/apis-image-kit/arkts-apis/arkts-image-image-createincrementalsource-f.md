# createIncrementalSource

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## createIncrementalSource

```TypeScript
function createIncrementalSource(buf: ArrayBuffer): ImageSource | undefined
```

Creates an ImageSource instance based on the buffer in incremental.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-image-function createIncrementalSource(buf: ArrayBuffer): ImageSource | undefined--><!--Device-image-function createIncrementalSource(buf: ArrayBuffer): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buf | ArrayBuffer | Yes | The buffer of the image. |

**Return value:**

| Type | Description |
| --- | --- |
| ImageSource | Returns the ImageSource instance if the operation is successful; returns undefined otherwise. |


## createIncrementalSource

```TypeScript
function createIncrementalSource(buf: ArrayBuffer, 
      options?: SourceOptions): ImageSource | undefined
```

Creates an ImageSource instance based on the buffer in incremental.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

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
| ImageSource | Returns the ImageSource instance if the operation is successful; returns undefined otherwise. |

