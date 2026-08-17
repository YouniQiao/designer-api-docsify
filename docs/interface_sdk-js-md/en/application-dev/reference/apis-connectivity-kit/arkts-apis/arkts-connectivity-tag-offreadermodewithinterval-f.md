# offReaderModeWithInterval

## Modules to Import

```TypeScript
import { tag } from 'tag';
```

## offReaderModeWithInterval

```TypeScript
function offReaderModeWithInterval(elementName: ElementName, callback?: Callback<TagInfo>): void
```

Disable foreground reader mode settings explicitly.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-tag-function offReaderModeWithInterval(elementName: ElementName, callback?: Callback<TagInfo>): void--><!--Device-tag-function offReaderModeWithInterval(elementName: ElementName, callback?: Callback<TagInfo>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes | The element name of application, must include the bundleName and abilityName. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TagInfo](arkts-connectivity-tag-taginfo-i.md)&gt; | No | The callback to dispatched the TagInfo object for application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100203](../errorcode-nfc.md#3100203-incorrect-api-call-sequence) | The off() API can be called only when the on() has been called. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

