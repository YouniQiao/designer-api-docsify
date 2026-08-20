# onReaderModeWithInterval

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## onReaderModeWithInterval

```TypeScript
function onReaderModeWithInterval(
    elementName: ElementName,
    discTech: int[],
    callback: Callback<TagInfo>,
    interval: int
  ): void
```

Set reader mode enabled when the specific application is on foreground and set card presence interval. Tag infomation will be dispatched to the application only if a NFC tag is discovered.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-tag-function onReaderModeWithInterval(    elementName: ElementName,    discTech: int[],    callback: Callback<TagInfo>,    interval: int  ): void--><!--Device-tag-function onReaderModeWithInterval(    elementName: ElementName,    discTech: int[],    callback: Callback<TagInfo>,    interval: int  ): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes | The element name of application, must include the bundleName and abilityName. |
| discTech | int[] | Yes | The technologies list to set for discovering. From [NFC_A](arkts-connectivity-tag-con.md#nfc_a) to [MIFARE_ULTRALIGHT](arkts-connectivity-tag-con.md#mifare_ultralight). |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[TagInfo](arkts-connectivity-tag-taginfo-i.md)&gt; | Yes | The callback to dispatched the TagInfo object for application. |
| interval | int | Yes | The interval for reader presence check. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [3100202](../errorcode-nfc.md#3100202-application-status-error) | The element state is invalid. |

