# createIncrementalSource

## Modules to Import

```TypeScript
```

## createIncrementalSource

```TypeScript
function createIncrementalSource(buf: ArrayBuffer): ImageSource | undefined
```

Creates an ImageSource instance based on the buffer in incremental.

**Since:** 23

<!--Device-image-function createIncrementalSource(buf: ArrayBuffer): ImageSource | undefined--><!--Device-image-function createIncrementalSource(buf: ArrayBuffer): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createIncrementalSource

```TypeScript
function createIncrementalSource(buf: ArrayBuffer, 
      options?: SourceOptions): ImageSource | undefined
```

Creates an ImageSource instance based on the buffer in incremental.

**Since:** 23

<!--Device-image-function createIncrementalSource(buf: ArrayBuffer,       options?: SourceOptions): ImageSource | undefined--><!--Device-image-function createIncrementalSource(buf: ArrayBuffer,       options?: SourceOptions): ImageSource | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |
