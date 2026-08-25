# PasteData

Implements a **PasteData** object. PasteData contains one or more data records ([PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md)) and property description objects ([PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md)). Before calling any API in **PasteData**, you must use ** [createData()](arkts-basicservices-pasteboard-createdata-f.md)** or ** [getData()](arkts-basicservices-pasteboard-systempasteboard-i.md#getdata)** to create a **PasteData** object.

**Since:** 6

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## addHtmlRecord

```TypeScript
addHtmlRecord(htmlText: string): void
```

Adds an HTML record to the PasteData, and adds **MIMETYPE_TEXT_HTML** to **mimeTypes** in [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md). The parameters cannot be empty. Otherwise, the operation fails.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addRecord](#addrecord)(mimeType: string, value: ValueType)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [htmlText](arkts-basicservices-pasteboard-pastedatarecord-i.md) | string | Yes |

## addRecord

```TypeScript
addRecord(record: PasteDataRecord): void
```

Adds a data record to the PasteData, and adds its type to **mimeTypes** in [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md). The parameters cannot be empty. Otherwise, the operation fails.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| record | [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Yes |

## addRecord

```TypeScript
addRecord(mimeType: string, value: ValueType): void
```

Adds a data record to the PasteData, and adds its type to **mimeTypes** in [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md). The parameters cannot be empty. Otherwise, the operation fails.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mimeType | string | Yes |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12900002](../errorcode-pasteboard.md#12900002-maximum-number-of-records-reached) |

## addTextRecord

```TypeScript
addTextRecord(text: string): void
```

Adds a plain text record to the PasteData, and adds **MIMETYPE_TEXT_PLAIN** to **mimeTypes** in [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md). The parameters cannot be empty. Otherwise, the operation fails.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addRecord](#addrecord)(mimeType: string, value: ValueType)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

## addUriRecord

```TypeScript
addUriRecord(uri: string): void
```

Adds a URI record to the PasteData, and adds **MIMETYPE_TEXT_URI** to **mimeTypes** in [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md). The parameters cannot be empty. Otherwise, the operation fails.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addRecord](#addrecord)(mimeType: string, value: ValueType)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

## addWantRecord

```TypeScript
addWantRecord(want: Want): void
```

Adds a Want record to the PasteData, and adds **MIMETYPE_TEXT_WANT** to **mimeTypes** in [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md). The parameters cannot be empty. Otherwise, the operation fails.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addRecord](#addrecord)(mimeType: string, value: ValueType)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

## getMimeTypes

```TypeScript
getMimeTypes(): Array<string>
```

Obtains types of [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) of the PasteData.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

## getPrimaryHtml

```TypeScript
getPrimaryHtml(): string
```

Obtains the HTML content of the primary record.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getPrimaryMimeType

```TypeScript
getPrimaryMimeType(): string
```

Obtains the data type of the primary record in the pasteboard.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getPrimaryPixelMap

```TypeScript
getPrimaryPixelMap(): image.PixelMap
```

Obtains the PixelMap of the primary record.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

## getPrimaryText

```TypeScript
getPrimaryText(): string
```

Obtains the plain text of the primary record.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getPrimaryUri

```TypeScript
getPrimaryUri(): string
```

Obtains the URI of the primary record.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getPrimaryWant

```TypeScript
getPrimaryWant(): Want
```

Obtains the **Want** object of the primary record.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) |

## getProperty

```TypeScript
getProperty(): PasteDataProperty
```

Obtains the property of the PasteData.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) |

## getRecord

```TypeScript
getRecord(index: number): PasteDataRecord
```

Obtains the record with a specific index in PasteData.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12900001](../errorcode-pasteboard.md#12900001-index-out-of-range) |

## getRecordAt

```TypeScript
getRecordAt(index: number): PasteDataRecord
```

Obtains the record with a specific index in PasteData.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getRecord](#getrecord)(index: int)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getRecordCount

```TypeScript
getRecordCount(): number
```

Obtains the number of records in a PasteData object.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getTag

```TypeScript
getTag(): string
```

Obtains the custom tag from the PasteData. If no custom tag is set, an empty string is returned.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## hasMimeType

```TypeScript
hasMimeType(mimeType: string): boolean
```

Checks whether the PasteData contains data of the specified type.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [hasType](#hastype)(mimeType: string)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mimeType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## hasType

```TypeScript
hasType(mimeType: string): boolean
```

Checks whether the PasteData contains data of the specified MIME type.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mimeType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## pasteComplete

```TypeScript
pasteComplete(): void
```

Invoked to notify pasteboard service the utilization of PasteData has completed and occupied resources can be released for further usage

**Since:** 12

**System capability:** SystemCapability.MiscServices.Pasteboard

## pasteStart

```TypeScript
pasteStart(): void
```

Notifies the pasteboard service to retain the cross-device channel before reading data from the pasteboard.

**Since:** 12

**System capability:** SystemCapability.MiscServices.Pasteboard

## removeRecord

```TypeScript
removeRecord(index: number): void
```

Removes the record with a specific index in PasteData.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12900001](../errorcode-pasteboard.md#12900001-index-out-of-range) |

## removeRecordAt

```TypeScript
removeRecordAt(index: number): boolean
```

Removes the record with a specific index in PasteData.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeRecord](#removerecord)(index: int)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## replaceRecord

```TypeScript
replaceRecord(index: number, record: PasteDataRecord): void
```

Replaces the record with a specific index in PasteData.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| record | [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12900001](../errorcode-pasteboard.md#12900001-index-out-of-range) |

## replaceRecordAt

```TypeScript
replaceRecordAt(index: number, record: PasteDataRecord): boolean
```

Replaces the record with a specific index in PasteData.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [replaceRecord](#replacerecord)(index: int, record: PasteDataRecord)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| record | [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setProperty

```TypeScript
setProperty(property: PasteDataProperty): void
```

Sets a [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| property | [PasteDataProperty](arkts-basicservices-pasteboard-pastedataproperty-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
