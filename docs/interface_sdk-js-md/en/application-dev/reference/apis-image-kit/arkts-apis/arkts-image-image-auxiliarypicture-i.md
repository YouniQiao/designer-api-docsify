# AuxiliaryPicture

The **AuxiliaryPicture** class is used to read or write auxiliary picture data of an image and obtain auxiliary picture information of an image. The supported types of auxiliary pictures can be found in [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md). Before calling any API in AuxiliaryPicture, you must create an AuxiliaryPicture instance using [image.createAuxiliaryPicture](arkts-image-image-createauxiliarypicture-f.md) or [getAuxiliaryPicture](arkts-image-image-picture-i.md#getauxiliarypicture) in Picture. Images occupy a large amount of memory. When you finish using an AuxiliaryPicture instance, call [release](#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-image-interface AuxiliaryPicture--><!--Device-image-interface AuxiliaryPicture-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## getAuxiliaryPictureInfo

```TypeScript
getAuxiliaryPictureInfo(): AuxiliaryPictureInfo
```

Obtains the auxiliary picture information.

**Since:** 13

<!--Device-AuxiliaryPicture-getAuxiliaryPictureInfo(): AuxiliaryPictureInfo--><!--Device-AuxiliaryPicture-getAuxiliaryPictureInfo(): AuxiliaryPictureInfo-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AuxiliaryPictureInfo](arkts-image-image-auxiliarypictureinfo-i.md) | Auxiliary picture information. |

## getAuxiliaryPictureInfo

```TypeScript
getAuxiliaryPictureInfo(): AuxiliaryPictureInfo | undefined
```

Obtains the information about this auxiliary picture.

**Since:** 23

<!--Device-AuxiliaryPicture-getAuxiliaryPictureInfo(): AuxiliaryPictureInfo | undefined--><!--Device-AuxiliaryPicture-getAuxiliaryPictureInfo(): AuxiliaryPictureInfo | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AuxiliaryPictureInfo](arkts-image-image-auxiliarypictureinfo-i.md) | Returns the auxiliary picture information. If the operation fails, an error message is returned. |

## getMetadata

```TypeScript
getMetadata(metadataType: MetadataType): Promise<Metadata>
```

Obtains the metadata of this auxiliary picture. This API uses a promise to return the result.

**Since:** 13

<!--Device-AuxiliaryPicture-getMetadata(metadataType: MetadataType): Promise<Metadata>--><!--Device-AuxiliaryPicture-getMetadata(metadataType: MetadataType): Promise<Metadata>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes | Metadata type, which is used to obtain metadata of the corresponding type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Metadata&gt; | Promise that returns the metadata. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

## getMetadata

```TypeScript
getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>
```

Obtains the metadata of auxiliary picture.

**Since:** 23

<!--Device-AuxiliaryPicture-getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>--><!--Device-AuxiliaryPicture-getMetadata(metadataType: MetadataType): Promise<Metadata | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes | The type of metadata. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Metadata \| undefined&gt; | Return the metadata of auxiliary picture. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

## getType

```TypeScript
getType(): AuxiliaryPictureType
```

Obtains the type of this auxiliary picture.

**Since:** 13

<!--Device-AuxiliaryPicture-getType(): AuxiliaryPictureType--><!--Device-AuxiliaryPicture-getType(): AuxiliaryPictureType-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) | Type of the auxiliary picture. |

## getType

```TypeScript
getType(): AuxiliaryPictureType | undefined
```

Obtains the type of auxiliary picture.

**Since:** 23

<!--Device-AuxiliaryPicture-getType(): AuxiliaryPictureType | undefined--><!--Device-AuxiliaryPicture-getType(): AuxiliaryPictureType | undefined-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) | Returns the type of auxiliary picture. |

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(): Promise<ArrayBuffer>
```

Reads pixels of this auxiliary picture and writes the data to an ArrayBuffer. This API uses a promise to return the result.

**Since:** 13

<!--Device-AuxiliaryPicture-readPixelsToBuffer(): Promise<ArrayBuffer>--><!--Device-AuxiliaryPicture-readPixelsToBuffer(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise used to return the pixels of the auxiliary picture. |

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(): Promise<ArrayBuffer | undefined>
```

Reads image pixel map data and writes the data to an ArrayBuffer. This method uses a promise to return the result.

**Since:** 23

<!--Device-AuxiliaryPicture-readPixelsToBuffer(): Promise<ArrayBuffer | undefined>--><!--Device-AuxiliaryPicture-readPixelsToBuffer(): Promise<ArrayBuffer | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer \| undefined&gt; | A Promise instance used to return the pixel map data. |

## release

```TypeScript
release():void
```

Releases this AuxiliaryPicture object. No value is returned. Images occupy a large amount of memory. When you finish using an AuxiliaryPicture instance, call this API to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 23

<!--Device-AuxiliaryPicture-release():void--><!--Device-AuxiliaryPicture-release():void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## setAuxiliaryPictureInfo

```TypeScript
setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void
```

Sets the auxiliary picture information.

**Since:** 23

<!--Device-AuxiliaryPicture-setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void--><!--Device-AuxiliaryPicture-setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [AuxiliaryPictureInfo](arkts-image-image-auxiliarypictureinfo-i.md) | Yes | Auxiliary picture information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

## setMetadata

```TypeScript
setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>
```

Sets the metadata for this auxiliary picture. This API uses a promise to return the result.

**Since:** 23

<!--Device-AuxiliaryPicture-setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>--><!--Device-AuxiliaryPicture-setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes | Metadata type, which is used to set the corresponding metadata. |
| metadata | Metadata | Yes | Metadata object. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

## writePixelsFromBuffer

```TypeScript
writePixelsFromBuffer(data: ArrayBuffer): Promise<void>
```

Reads pixels from an ArrayBuffer and writes the data to this AuxiliaryPicture object. This API uses a promise to return the result.

**Since:** 23

<!--Device-AuxiliaryPicture-writePixelsFromBuffer(data: ArrayBuffer): Promise<void>--><!--Device-AuxiliaryPicture-writePixelsFromBuffer(data: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | ArrayBuffer | Yes | Pixels of the auxiliary picture. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

