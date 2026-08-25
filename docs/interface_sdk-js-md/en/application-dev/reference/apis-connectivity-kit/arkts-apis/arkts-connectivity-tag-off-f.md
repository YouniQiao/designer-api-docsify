# off

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## off('readerMode')

```TypeScript
function off(type: 'readerMode', elementName: ElementName, callback?: AsyncCallback<TagInfo>): void
```

Unsubscribes from the NFC tag card read event. The device exits the reader mode and resumes card emulation. If the NFC reader mode is enabled by tag.on, this API must be used when the application page exits the foreground or is destroyed.

**Since:** 11

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'readerMode' | Yes |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[TagInfo](arkts-connectivity-tag-taginfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100203](../errorcode-nfc.md#3100203-incorrect-api-call-sequence) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |


## off('readerModeWithInterval')

```TypeScript
function off(type: 'readerModeWithInterval', elementName: ElementName, callback?: Callback<TagInfo>): void
```

Unsubscribes from the NFC tag card read event. The device exits the reader mode and resumes card emulation. If the NFC reader mode is enabled by tag.on, this API must be used when the application page exits the foreground or is destroyed. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'readerModeWithInterval' | Yes |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TagInfo](arkts-connectivity-tag-taginfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [3100203](../errorcode-nfc.md#3100203-incorrect-api-call-sequence) |
