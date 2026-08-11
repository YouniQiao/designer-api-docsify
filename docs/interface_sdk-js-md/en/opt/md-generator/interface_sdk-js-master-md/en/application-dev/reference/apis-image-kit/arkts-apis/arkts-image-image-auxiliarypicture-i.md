# AuxiliaryPicture

The **AuxiliaryPicture** class is used to read or write auxiliary picture data of an image and obtain auxiliary picture information of an image. The supported types of auxiliary pictures can be found in   
[AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md).

Before calling any API in AuxiliaryPicture, you must create an AuxiliaryPicture instance using   
[image.createAuxiliaryPicture](arkts-image-image-createauxiliarypicture-f.md#createauxiliarypicture) or   
[getAuxiliaryPicture](arkts-image-image-picture-i.md#getauxiliarypicture) in Picture.

Images occupy a large amount of memory. When you finish using an AuxiliaryPicture instance, call   
[release](arkts-image-image-auxiliarypicture-i.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 13

<!--Device-image-interface AuxiliaryPicture--><!--Device-image-interface AuxiliaryPicture-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
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

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AuxiliaryPictureInfo](arkts-image-image-auxiliarypictureinfo-i.md) |

## getMetadata

```TypeScript
getMetadata(metadataType: MetadataType): Promise<Metadata>
```

Obtains the metadata of this auxiliary picture. This API uses a promise to return the result.

**Since:** 13

<!--Device-AuxiliaryPicture-getMetadata(metadataType: MetadataType): Promise<Metadata>--><!--Device-AuxiliaryPicture-getMetadata(metadataType: MetadataType): Promise<Metadata>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Metadata&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) |

## getType

```TypeScript
getType(): AuxiliaryPictureType
```

Obtains the type of this auxiliary picture.

**Since:** 13

<!--Device-AuxiliaryPicture-getType(): AuxiliaryPictureType--><!--Device-AuxiliaryPicture-getType(): AuxiliaryPictureType-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AuxiliaryPictureType](arkts-image-image-auxiliarypicturetype-e.md) |

## readPixelsToBuffer

```TypeScript
readPixelsToBuffer(): Promise<ArrayBuffer>
```

Reads pixels of this auxiliary picture and writes the data to an ArrayBuffer. This API uses a promise to return the result.

**Since:** 13

<!--Device-AuxiliaryPicture-readPixelsToBuffer(): Promise<ArrayBuffer>--><!--Device-AuxiliaryPicture-readPixelsToBuffer(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ArrayBuffer&gt; |

## release

```TypeScript
release():void
```

Releases this AuxiliaryPicture object. No value is returned.

Images occupy a large amount of memory. When you finish using an AuxiliaryPicture instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Since:** 13

<!--Device-AuxiliaryPicture-release():void--><!--Device-AuxiliaryPicture-release():void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## setAuxiliaryPictureInfo

```TypeScript
setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void
```

Sets the auxiliary picture information.

**Since:** 13

<!--Device-AuxiliaryPicture-setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void--><!--Device-AuxiliaryPicture-setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [AuxiliaryPictureInfo](arkts-image-image-auxiliarypictureinfo-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setMetadata

```TypeScript
setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>
```

Sets the metadata for this auxiliary picture. This API uses a promise to return the result.

**Since:** 13

<!--Device-AuxiliaryPicture-setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>--><!--Device-AuxiliaryPicture-setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| metadataType | [MetadataType](arkts-image-image-metadatatype-e.md) | Yes |
| metadata | [Metadata](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-metadata-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) |

## writePixelsFromBuffer

```TypeScript
writePixelsFromBuffer(data: ArrayBuffer): Promise<void>
```

Reads pixels from an ArrayBuffer and writes the data to this AuxiliaryPicture object. This API uses a promise to return the result.

**Since:** 13

<!--Device-AuxiliaryPicture-writePixelsFromBuffer(data: ArrayBuffer): Promise<void>--><!--Device-AuxiliaryPicture-writePixelsFromBuffer(data: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
