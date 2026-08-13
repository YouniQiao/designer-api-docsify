# Picture

An image that contains special information can be decoded into a picture object, which generally contains the main picture, auxiliary picture, and metadata. The main picture contains most information about the image and is mainly used to render the image. The auxiliary picture is used to store data related to but different from the main picture, revealing more comprehensive details. The metadata is generally used to store information about the image file. The picture object class is used to read or write picture objects. Before calling any API in Picture, you must use [image.createPicture](arkts-image-image-createpicture-f.md#createPicture) to create a Picture object. Images occupy a large amount of memory. When you finish using a Picture instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

**Deprecated since:** -1

<!--Device-image-interface Picture--><!--Device-image-interface Picture-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## getAuxiliaryPicture

```TypeScript
getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null
```

Obtains an auxiliary picture by type.

**Since:** 23

**Deprecated since:** -1

<!--Device-Picture-getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null--><!--Device-Picture-getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getGainmapPixelmap

```TypeScript
getGainmapPixelmap(): PixelMap | null
```

Obtains the PixelMap object of the gain map.

**Since:** 23

**Deprecated since:** -1

<!--Device-Picture-getGainmapPixelmap(): PixelMap | null--><!--Device-Picture-getGainmapPixelmap(): PixelMap | null-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

## getHdrComposedPixelmap

```TypeScript
getHdrComposedPixelmap(): Promise<PixelMap>
```

Generates a High Dynamic Range (HDR) image and obtains its PixelMap object. This API uses a promise to return the result.

**Since:** 13

**Deprecated since:** -1

<!--Device-Picture-getHdrComposedPixelmap(): Promise<PixelMap>--><!--Device-Picture-getHdrComposedPixelmap(): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600901](../errorcode-image.md#7600901-unknown-error) |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) |

## getHdrComposedPixelmap

```TypeScript
getHdrComposedPixelmap(): Promise<PixelMap | undefined>
```

Obtains the hdr pixel map. This method uses a promise to return the PixelMap object.

**Since:** 23

**Deprecated since:** -1

<!--Device-Picture-getHdrComposedPixelmap(): Promise<PixelMap | undefined>--><!--Device-Picture-getHdrComposedPixelmap(): Promise<PixelMap | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PixelMap \ | undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600901](../errorcode-image.md#7600901-unknown-error) |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) |

## getHdrComposedPixelmapWithOptions

```TypeScript
getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>
```

Composites an HDR image and returns PixelMap of the image. Composition options (such as PixelMapFormat) can be passed. This API uses a promise to return the result. The Picture object that calls this API must contain the main picture, gain map, and metadata.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Picture-getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>--><!--Device-Picture-getHdrComposedPixelmapWithOptions(options?: HdrComposeOptions): Promise<PixelMap | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [HdrComposeOptions](arkts-image-image-hdrcomposeoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PixelMap \ | undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) |

## getMainPixelmap

```TypeScript
getMainPixelmap(): PixelMap
```

Obtains the PixelMap object of the main picture. This API returns the result synchronously.

**Since:** 13

**Deprecated since:** -1

<!--Device-Picture-getMainPixelmap(): PixelMap--><!--Device-Picture-getMainPixelmap(): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

## getMainPixelmap

```TypeScript
getMainPixelmap(): PixelMap | undefined
```

Obtains the pixel map of the main image.

**Since:** 23

**Deprecated since:** -1

<!--Device-Picture-getMainPixelmap(): PixelMap | undefined--><!--Device-Picture-getMainPixelmap(): PixelMap | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

## getMetadata

```TypeScript
getMetadata(metadataType: MetadataType): Promise<Metadata>
```

Obtains the metadata of this Picture object. This API uses a promise to return the result.

**Since:** 13

**Deprecated since:** -1

<!--Device-Picture-getMetadata(metadataType: MetadataType): Promise<Metadata>--><!--Device-Picture-getMetadata(metadataType: MetadataType): Promise<Metadata>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Metadata & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) |

## getMetadata

```TypeScript
getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>
```

Obtains the metadata of main picture.

**Since:** 23

**Deprecated since:** -1

<!--Device-Picture-getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>--><!--Device-Picture-getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Metadata \ | undefined & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) |

## hdrComposeToMainPixelmap

```TypeScript
hdrComposeToMainPixelmap(): Promise<void>
```

Invokes the VPE algorithm to compose the main pixelmap and gainmap. The composed result will replace the main pixelmap of the current picture object. The Picture object that calls this API must contain the main pixelmap, gain map.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Picture-hdrComposeToMainPixelmap(): Promise<void>--><!--Device-Picture-hdrComposeToMainPixelmap(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) |

## marshalling

```TypeScript
marshalling(sequence: rpc.MessageSequence): void
```

Marshals this Picture object and writes it to a MessageSequence object.

**Since:** 23

**Deprecated since:** -1

<!--Device-Picture-marshalling(sequence: rpc.MessageSequence): void--><!--Device-Picture-marshalling(sequence: rpc.MessageSequence): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sequence | rpc.MessageSequence | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [62980097](../errorcode-image.md#62980097-pixelmap-serialization-failed) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## release

```TypeScript
release(): void
```

Releases this Picture object. Images occupy a large amount of memory. When you finish using a Picture instance, call this API to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

**Deprecated since:** -1

<!--Device-Picture-release(): void--><!--Device-Picture-release(): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## setAuxiliaryPicture

```TypeScript
setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void
```

Sets an auxiliary picture.

**Since:** 23

**Deprecated since:** -1

<!--Device-Picture-setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void--><!--Device-Picture-setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) | Yes |
| auxiliaryPicture | [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setMainPixelmap

```TypeScript
setMainPixelmap(pixelmap: PixelMap): void
```

Sets the PixelMap object of the picture.

**Since:** 26.1.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Picture-setMainPixelmap(pixelmap: PixelMap): void--><!--Device-Picture-setMainPixelmap(pixelmap: PixelMap): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmap | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7700204](../errorcode-image.md#7700204-invalid-parameter) |

## setMetadata

```TypeScript
setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>
```

Sets the metadata for this Picture object. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-Picture-setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>--><!--Device-Picture-setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes |
| metadata | [Metadata](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-metadata-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) |
