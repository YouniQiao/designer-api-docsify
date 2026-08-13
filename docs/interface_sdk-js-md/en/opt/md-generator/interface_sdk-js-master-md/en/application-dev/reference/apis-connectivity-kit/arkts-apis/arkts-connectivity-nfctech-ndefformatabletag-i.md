# NdefFormatableTag

Provides methods for accessing NdefFormatable tag.

**Inheritance/Implementation:** NdefFormatableTag extends TagSession

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-export interface NdefFormatableTag--><!--Device-unnamed-export interface NdefFormatableTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## format

```TypeScript
format(message: NdefMessage): Promise<void>
```

Formats a tag as NDEF tag, writes NDEF message into the NDEF Tag.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefFormatableTag-format(message: NdefMessage): Promise<void>--><!--Device-NdefFormatableTag-format(message: NdefMessage): Promise<void>-End-->

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## format

```TypeScript
format(message: NdefMessage, callback: AsyncCallback<void>): void
```

Formats a tag as NDEF tag, writes NDEF message into the NDEF Tag.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefFormatableTag-format(message: NdefMessage, callback: AsyncCallback<void>): void--><!--Device-NdefFormatableTag-format(message: NdefMessage, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## formatReadOnly

```TypeScript
formatReadOnly(message: NdefMessage): Promise<void>
```

Formats a tag as NDEF tag, writes NDEF message into the NDEF Tag, then sets the tag readonly.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefFormatableTag-formatReadOnly(message: NdefMessage): Promise<void>--><!--Device-NdefFormatableTag-formatReadOnly(message: NdefMessage): Promise<void>-End-->

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## formatReadOnly

```TypeScript
formatReadOnly(message: NdefMessage, callback: AsyncCallback<void>): void
```

Formats a tag as NDEF tag, writes NDEF message into the NDEF Tag, then sets the tag readonly.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefFormatableTag-formatReadOnly(message: NdefMessage, callback: AsyncCallback<void>): void--><!--Device-NdefFormatableTag-formatReadOnly(message: NdefMessage, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
