# onReaderModeWithInterval

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## onReaderModeWithInterval

```TypeScript
function onReaderModeWithInterval(
    elementName: ElementName,
    discTech: number[],
    callback: Callback<TagInfo>,
    interval: number
  ): void
```

Set reader mode enabled when the specific application is on foreground and set card presence interval. Tag infomation will be dispatched to the application only if a NFC tag is discovered.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-tag-function onReaderModeWithInterval(    elementName: ElementName,    discTech: int[],    callback: Callback<TagInfo>,    interval: int  ): void--><!--Device-tag-function onReaderModeWithInterval(    elementName: ElementName,    discTech: int[],    callback: Callback<TagInfo>,    interval: int  ): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes |
| discTech | number[] | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TagInfo](arkts-connectivity-tag-taginfo-i.md)&gt; | Yes |
| interval | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100202](../errorcode-nfc.md#3100202-application-status-error) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
