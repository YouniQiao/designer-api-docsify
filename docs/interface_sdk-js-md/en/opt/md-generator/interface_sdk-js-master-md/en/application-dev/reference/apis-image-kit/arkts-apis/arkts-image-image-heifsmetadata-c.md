# HeifsMetadata

HeifsMetadata implements Metadata

HEIF image sequence metadata.

**Inheritance/Implementation:** HeifsMetadata implements [Metadata](arkts-image-image-metadata-i.md)

**Since:** 23

<!--Device-image-class HeifsMetadata implements Metadata--><!--Device-image-class HeifsMetadata implements Metadata-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## clone

```TypeScript
clone(): Promise<HeifsMetadata>
```

Clones the HEIFS metadata. This API returns the result asynchronously through a promise.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeifsMetadata-clone(): Promise<HeifsMetadata>--><!--Device-HeifsMetadata-clone(): Promise<HeifsMetadata>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[HeifsMetadata](arkts-image-image-heifsmetadata-c.md)&gt; |

## createInstance

```TypeScript
static createInstance(): HeifsMetadata
```

Creates an empty [HeifsMetadata](arkts-image-image-heifsmetadata-c.md) instance.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeifsMetadata-static createInstance(): HeifsMetadata--><!--Device-HeifsMetadata-static createInstance(): HeifsMetadata-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HeifsMetadata](arkts-image-image-heifsmetadata-c.md) |

## getAllProperties

```TypeScript
getAllProperties(): Promise<Record<string, string | null>>
```

Obtains all properties and their values from the image metadata. This API returns the result asynchronously through a promise.

For details about the properties, see   
[HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeifsMetadata-getAllProperties(): Promise<Record<string, string | null>>--><!--Device-HeifsMetadata-getAllProperties(): Promise<Record<string, string | null>>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Record&lt;string, string \| null&gt;&gt; |

## getBlob

```TypeScript
getBlob(): Promise<ArrayBuffer>
```

Obtains the metadata in binary format. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeifsMetadata-getBlob(): Promise<ArrayBuffer>--><!--Device-HeifsMetadata-getBlob(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ArrayBuffer&gt; |

## getProperties

```TypeScript
getProperties(key: Array<string>): Promise<Record<string, string | null>>
```

Obtains the property values of image metadata. This API returns the result asynchronously through a promise.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeifsMetadata-getProperties(key: Array<string>): Promise<Record<string, string | null>>--><!--Device-HeifsMetadata-getProperties(key: Array<string>): Promise<Record<string, string | null>>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Record&lt;string, string \| null&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) |

## setBlob

```TypeScript
setBlob(blob: ArrayBuffer): Promise<void>
```

Replaces the current metadata with binary data. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeifsMetadata-setBlob(blob: ArrayBuffer): Promise<void>--><!--Device-HeifsMetadata-setBlob(blob: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blob | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |

## setProperties

```TypeScript
setProperties(records: Record<string, string | null>): Promise<void>
```

Sets the values of specified properties in image metadata in batches. This API returns the result asynchronously through a promise.

For details about the properties, see   
[HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeifsMetadata-setProperties(records: Record<string, string | null>): Promise<void>--><!--Device-HeifsMetadata-setProperties(records: Record<string, string | null>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| records | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string \| null&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) |

## heifsCanvasHeight

```TypeScript
readonly heifsCanvasHeight?: number
```

Canvas height.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeifsMetadata-readonly heifsCanvasHeight?: int--><!--Device-HeifsMetadata-readonly heifsCanvasHeight?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## heifsCanvasWidth

```TypeScript
readonly heifsCanvasWidth?: number
```

Canvas width.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeifsMetadata-readonly heifsCanvasWidth?: int--><!--Device-HeifsMetadata-readonly heifsCanvasWidth?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## heifsDelayTime

```TypeScript
readonly heifsDelayTime?: number
```

Playback duration of each frame in an HEIF image sequence, in ms.

**Type:** number

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeifsMetadata-readonly heifsDelayTime?: int--><!--Device-HeifsMetadata-readonly heifsDelayTime?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## heifsUnclampedDelayTime

```TypeScript
readonly heifsUnclampedDelayTime?: number
```

Unclamped delay of each frame in ms.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HeifsMetadata-readonly heifsUnclampedDelayTime?: int--><!--Device-HeifsMetadata-readonly heifsUnclampedDelayTime?: int-End-->

**System capability:** SystemCapability.Multimedia.Image.Core
