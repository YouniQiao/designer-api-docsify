# onReaderModeWithInterval

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
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

Set reader mode enabled when the specific application is on foreground and set card presence interval.Tag infomation will be dispatched to the application only if a NFC tag is discovered.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-tag-function onReaderModeWithInterval(    elementName: ElementName,    discTech: int[],    callback: Callback<TagInfo>,    interval: int  ): void--><!--Device-tag-function onReaderModeWithInterval(    elementName: ElementName,    discTech: int[],    callback: Callback<TagInfo>,    interval: int  ): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes | The element name of application, must include the bundleName and abilityName. |
| discTech | int[] | Yes | The technologies list to set for discovering. From {@link NFC_A} to {@link MIFARE_ULTRALIGHT}. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TagInfo&gt; | Yes | The callback to dispatched the TagInfo object for application. |
| interval | int | Yes | The interval for reader presence check. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [3100202](../errorcode-nfc.md#3100202-application-status-error) | The element state is invalid. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

