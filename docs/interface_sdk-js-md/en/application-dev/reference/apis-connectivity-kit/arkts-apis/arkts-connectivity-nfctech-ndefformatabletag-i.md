# NdefFormatableTag

Provides methods for accessing NdefFormatable tag.

**Inheritance/Implementation:** NdefFormatableTag extends TagSession

**Since:** 23

<!--Device-unnamed-export interface NdefFormatableTag--><!--Device-unnamed-export interface NdefFormatableTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## format

```TypeScript
format(message: NdefMessage): Promise<void>
```

Formats a tag as NDEF tag, writes NDEF message into the NDEF Tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefFormatableTag-format(message: NdefMessage): Promise<void>--><!--Device-NdefFormatableTag-format(message: NdefMessage): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes | NDEF message to write while format. It can be null, then only format the tag. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The void |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The tag I/O operation failed. |

## format

```TypeScript
format(message: NdefMessage, callback: AsyncCallback<void>): void
```

Formats a tag as NDEF tag, writes NDEF message into the NDEF Tag.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefFormatableTag-format(message: NdefMessage, callback: AsyncCallback<void>): void--><!--Device-NdefFormatableTag-format(message: NdefMessage, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes | NDEF message to write while format. It can be null, then only format the tag. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | The callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The Tag I/O operation failed. |

## formatReadOnly

```TypeScript
formatReadOnly(message: NdefMessage): Promise<void>
```

Formats a tag as NDEF tag, writes NDEF message into the NDEF Tag, then sets the tag readonly.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefFormatableTag-formatReadOnly(message: NdefMessage): Promise<void>--><!--Device-NdefFormatableTag-formatReadOnly(message: NdefMessage): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes | NDEF message to write while format. It can be null, then only format the tag. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The void |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The tag I/O operation failed. |

## formatReadOnly

```TypeScript
formatReadOnly(message: NdefMessage, callback: AsyncCallback<void>): void
```

Formats a tag as NDEF tag, writes NDEF message into the NDEF Tag, then sets the tag readonly.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NdefFormatableTag-formatReadOnly(message: NdefMessage, callback: AsyncCallback<void>): void--><!--Device-NdefFormatableTag-formatReadOnly(message: NdefMessage, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes | NDEF message to write while format. It can be null, then only format the tag. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | The callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [3100204](../errorcode-nfc.md#3100204-nfc-chip-io-exception) | The Tag I/O operation failed. |

