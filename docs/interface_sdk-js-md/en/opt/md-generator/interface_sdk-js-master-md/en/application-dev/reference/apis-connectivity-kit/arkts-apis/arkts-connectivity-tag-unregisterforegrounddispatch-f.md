# unregisterForegroundDispatch

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## unregisterForegroundDispatch

```TypeScript
function unregisterForegroundDispatch(elementName: ElementName): void
```

Unregister tag foreground dispatch.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-tag-function unregisterForegroundDispatch(elementName: ElementName): void--><!--Device-tag-function unregisterForegroundDispatch(elementName: ElementName): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
