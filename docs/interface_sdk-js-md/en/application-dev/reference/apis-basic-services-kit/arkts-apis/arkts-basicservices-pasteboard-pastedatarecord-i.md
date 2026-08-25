# PasteDataRecord

Provides **PasteDataRecord** APIs. A **PasteDataRecord** is an abstract definition of the content in the pasteboard. The pasteboard content consists of one or more plain text, HTML, URI, or Want records. After creating a PasteDataRecord, it is not supported to modify the value of the default data type of the PasteDataRecord. The correct value for the default data type should be specified when creating the PasteDataRecord. If you need to refresh the attribute value of the PasteDataRecord, please use [addEntry](#addentry).

**Since:** 7

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## addEntry

```TypeScript
addEntry(type: string, value: ValueType): void
```

Adds PasteData of an extra type to **PasteDataRecord**. The type added using this method is not the default type of **Record**. You can only use the [getData](#getdata) API to read the corresponding data.

**Since:** 14

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## convertToText

```TypeScript
convertToText(callback: AsyncCallback<string>): void
```

Forcibly converts the content in a **PasteData** object to text. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [toPlainText](#toplaintext)()

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## convertToText

```TypeScript
convertToText(): Promise<string>
```

Forcibly converts the content in a **PasteData** object to text. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [toPlainText](#toplaintext)()

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getData

```TypeScript
getData(type: string): Promise<ValueType>
```

Obtains data of the specified type from **PasteDataRecord**.

**Since:** 14

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ValueType & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getValidTypes

```TypeScript
getValidTypes(types: Array<string>): Array<string>
```

Obtains the intersection of the input types and the types of the PasteData.

**Since:** 14

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## toPlainText

```TypeScript
toPlainText(): string
```

Forcibly converts HTML, plain, and URI content in a **PasteDataRecord** to the plain text.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## data

```TypeScript
data: Record<string, ArrayBuffer>
```

Content of custom data. Modifications to this attribute are ineffective.

**Type:** Record&lt;string, ArrayBuffer&gt;

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

## htmlText

```TypeScript
htmlText: string
```

HTML content, must conform to standard HTML format. Modifications to this attribute are ineffective. To refresh the attribute value, please use [addEntry](#addentry).

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

## mimeType

```TypeScript
mimeType: string
```

Default type of PasteDataRecord. Modifications to this attribute are ineffective.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

## pixelMap

```TypeScript
pixelMap: image.PixelMap
```

PixelMap content. Modifications to this attribute are ineffective. To refresh the attribute value, please use [addEntry](#addentry).

**Type:** image.PixelMap

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

## plainText

```TypeScript
plainText: string
```

Plain text. Modifications to this attribute are ineffective. To refresh the attribute value, please use [addEntry](#addentry).

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

## uri

```TypeScript
uri: string
```

URI content, must conform to standard URI format. Modifications to this attribute are ineffective. To refresh the attribute value, please use [addEntry](#addentry).

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

## want

```TypeScript
want: Want
```

Want content. Modifications to this attribute are ineffective. To refresh the attribute value, please use [addEntry](#addentry).

**Type:** [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard
