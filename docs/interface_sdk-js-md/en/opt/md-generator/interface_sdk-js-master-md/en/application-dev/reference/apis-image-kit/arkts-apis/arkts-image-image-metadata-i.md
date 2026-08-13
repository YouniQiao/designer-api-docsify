# Metadata

The **Metadata** class provides APIs for storing image metadata. For details about the supported metadata types, see [MetadataType](arkts-image-image-metadatatype-e.md#MetadataType).

**Since:** 23

**Deprecated since:** -1

<!--Device-image-interface Metadata--><!--Device-image-interface Metadata-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## clone

```TypeScript
clone(): Promise<Metadata>
```

Clones the metadata. This API uses a promise to return the result.

**Since:** 13

**Deprecated since:** -1

<!--Device-Metadata-clone(): Promise<Metadata>--><!--Device-Metadata-clone(): Promise<Metadata>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Metadata & gt; |

## clone

```TypeScript
clone(): Promise<Metadata | undefined>
```

Obtains a clone of metadata. This method uses a promise to return the metadata.

**Since:** 23

**Deprecated since:** -1

<!--Device-Metadata-clone(): Promise<Metadata | undefined>--><!--Device-Metadata-clone(): Promise<Metadata | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Metadata \ | undefined & gt; |

## getAllProperties

```TypeScript
getAllProperties(): Promise<Record<string, string | null>>
```

Obtains all properties and values from the image's metadata. This API uses a promise to return the result. For details about how to query the property values, see [PropertyKey](arkts-image-image-propertykey-e.md#PropertyKey), [FragmentMapPropertyKey](arkts-image-image-fragmentmappropertykey-e.md#FragmentMapPropertyKey), [GifPropertyKey](arkts-image-image-gifpropertykey-e.md#GifPropertyKey), and [HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md#HeifsPropertyKey).

**Since:** 13

**Deprecated since:** -1

<!--Device-Metadata-getAllProperties(): Promise<Record<string, string | null>>--><!--Device-Metadata-getAllProperties(): Promise<Record<string, string | null>>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, string \| null & gt; & gt; |

## getAllProperties

```TypeScript
getAllProperties(): Promise<Record<string, string|null> | undefined>
```

Obtains the value of all properties in an image. This method uses a promise to return the property values in array of records.

**Since:** 23

**Deprecated since:** -1

<!--Device-Metadata-getAllProperties(): Promise<Record<string, string|null> | undefined>--><!--Device-Metadata-getAllProperties(): Promise<Record<string, string|null> | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, string \| null & gt; \ | undefined & gt; |

## getBlob

```TypeScript
getBlob(): Promise<ArrayBuffer>
```

Obtains the metadata in binary format. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Metadata-getBlob(): Promise<ArrayBuffer>--><!--Device-Metadata-getBlob(): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

## getProperties

```TypeScript
getProperties(key: Array<string>): Promise<Record<string, string | null>>
```

Obtains the values of properties from the image's metadata. This API uses a promise to return the result. For details about how to query the property values, see [PropertyKey](arkts-image-image-propertykey-e.md#PropertyKey), [FragmentMapPropertyKey](arkts-image-image-fragmentmappropertykey-e.md#FragmentMapPropertyKey), [GifPropertyKey](arkts-image-image-gifpropertykey-e.md#GifPropertyKey), and [HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md#HeifsPropertyKey).

**Since:** 23

**Deprecated since:** -1

<!--Device-Metadata-getProperties(key: Array<string>): Promise<Record<string, string | null>>--><!--Device-Metadata-getProperties(key: Array<string>): Promise<Record<string, string | null>>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, string \| null & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) |

## setBlob

```TypeScript
setBlob(blob: ArrayBuffer): Promise<void>
```

Replaces the current metadata with binary data. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Metadata-setBlob(blob: ArrayBuffer): Promise<void>--><!--Device-Metadata-setBlob(blob: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| blob | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |

## setProperties

```TypeScript
setProperties(records: Record<string, string | null>): Promise<void>
```

Sets the values of properties for the image's metadata. This API uses a promise to return the result. For details about how to query the property values, see [PropertyKey](arkts-image-image-propertykey-e.md#PropertyKey), [FragmentMapPropertyKey](arkts-image-image-fragmentmappropertykey-e.md#FragmentMapPropertyKey), [GifPropertyKey](arkts-image-image-gifpropertykey-e.md#GifPropertyKey), and [HeifsPropertyKey](arkts-image-image-heifspropertykey-e.md#HeifsPropertyKey).

**Since:** 23

**Deprecated since:** -1

<!--Device-Metadata-setProperties(records: Record<string, string | null>): Promise<void>--><!--Device-Metadata-setProperties(records: Record<string, string | null>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| records | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, string \| null & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [7600202](../errorcode-image.md#7600202-unsupported-metadata-readwrite-operation) |
