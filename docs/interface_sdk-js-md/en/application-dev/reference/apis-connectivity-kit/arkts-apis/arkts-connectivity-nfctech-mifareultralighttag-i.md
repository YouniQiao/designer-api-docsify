# MifareUltralightTag

Provides APIs to access MIFARE Ultralight properties and perform I/O operations on a tag. This class inherits from **TagSession**.  
**TagSession** is the base class of all NFC tag technologies. It provides common interfaces for establishing connections and transferring data. For more details, see [TagSession](arkts-connectivity-tagsession-tagsession-i.md).For details about how to obtain a **MifareUltralightTag** object, see [NFC Tag Read/Write Development](../../../connectivity/nfc/nfc-tag-access-guide.md).The following describes the unique APIs of **MifareUltralightTag**.

**Inheritance/Implementation:** MifareUltralightTag extends TagSession

**Since:** 9

**System capability:** SystemCapability.Communication.NFC.Tag

## getType

```TypeScript
getType(): tag.MifareUltralightType
```

Obtains the type of this MIFARE Ultralight tag.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| tag.MifareUltralightType |

## readMultiplePages

```TypeScript
readMultiplePages(pageIndex: number): Promise<number[]>
```

Reads four pages of data (16 bytes in total) from the tag. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pageIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |

## readMultiplePages

```TypeScript
readMultiplePages(pageIndex: number, callback: AsyncCallback<number[]>): void
```

Reads four pages of data (16 bytes in total) from the tag. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pageIndex | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |

## writeSinglePage

```TypeScript
writeSinglePage(pageIndex: number, data: number[]): Promise<void>
```

Writes one page (4 bytes) of data to this tag. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pageIndex | number | Yes |
| data | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |

## writeSinglePage

```TypeScript
writeSinglePage(pageIndex: number, data: number[], callback: AsyncCallback<void>): void
```

Writes one page (4 bytes) of data to this tag. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pageIndex | number | Yes |
| data | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
