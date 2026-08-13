# offReaderMode

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## offReaderMode

```TypeScript
function offReaderMode(elementName: ElementName, callback?: AsyncCallback<TagInfo>): void
```

Disable foreground reader mode settings explicitly.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-tag-function offReaderMode(elementName: ElementName, callback?: AsyncCallback<TagInfo>): void--><!--Device-tag-function offReaderMode(elementName: ElementName, callback?: AsyncCallback<TagInfo>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[TagInfo](arkts-connectivity-tag-taginfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100203](../errorcode-nfc.md#3100203-incorrect-api-call-sequence) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
