# NdefFormatableTag

Provides APIs for formatting NDEF formattable tags. This class inherits from **TagSession**.  
**TagSession** is the base class of all NFC tag technologies. It provides common interfaces for establishing connections and transferring data. For more details, see [TagSession](arkts-connectivity-tagsession-tagsession-i.md).For details about how to obtain an **NdefFormatableTag** object, see [NFC Tag Read/Write Development](../../../connectivity/nfc/nfc-tag-access-guide.md).The following describes the unique APIs of **NdefFormatableTag**.

**Inheritance/Implementation:** NdefFormatableTag extends TagSession

**Since:** 9

**System capability:** SystemCapability.Communication.NFC.Tag

## format

```TypeScript
format(message: NdefMessage): Promise<void>
```

Formats this tag as an NDEF tag, and writes an NDEF message to it. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes |

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

## format

```TypeScript
format(message: NdefMessage, callback: AsyncCallback<void>): void
```

Formats this tag as an NDEF tag, and writes an NDEF message to it. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |

## formatReadOnly

```TypeScript
formatReadOnly(message: NdefMessage): Promise<void>
```

Formats this tag as an NDEF tag, writes an NDEF message to it, and then sets the tag to read-only. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes |

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

## formatReadOnly

```TypeScript
formatReadOnly(message: NdefMessage, callback: AsyncCallback<void>): void
```

Formats this tag as an NDEF tag, writes an NDEF message to the NDEF tag, and then sets the tag to read-only. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
