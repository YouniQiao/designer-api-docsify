# on

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## on('readerMode')

```TypeScript
function on(type: 'readerMode', elementName: ElementName, discTech: number[], callback: AsyncCallback<TagInfo>): void
```

Subscribes to the NFC tag read event to implement dispatch of the tag to a foreground application preferentially. The device enters the reader mode and disables card emulation. You can set the supported NFC tag technologies in **discTech**. The [TagInfo](arkts-connectivity-tag-taginfo-i.md) read is returned through a callback. This API must be used with tag.off in pairs. If the NFC reader mode is enabled by **tag.on**, tag.off must be called when the application page exits the foreground or is destroyed. This API uses an asynchronous callback to return the result. This API and tag.on are mutually exclusive.

**Since:** 11

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'readerMode' | Yes |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes |
| discTech | number[] | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[TagInfo](arkts-connectivity-tag-taginfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100202](../errorcode-nfc.md#3100202-application-status-error) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |


## on('readerModeWithInterval')

```TypeScript
function on(
    type: 'readerModeWithInterval',
    elementName: ElementName,
    discTech: number[],
    callback: Callback<TagInfo>,
    interval: number
  ): void
```

Subscribes to the NFC tag read event so that the tag can be preferentially dispatched to a foreground application. You can also set the interval for detecting whether a card is present. This API uses an asynchronous callback to return the result.  
- The device enters the reader mode and disables card emulation.  
- You can set the supported NFC tag technologies in **discTech** and set the interval for detecting whether a card  
is present. The callback returns [TagInfo](arkts-connectivity-tag-taginfo-i.md) read.  
- This API must be used with  
tag.off in pairs. If the NFC reader mode is enabled by **tag.on**, tag.off must be called when the application page exits the foreground or is destroyed.  
- This API and  
tag.on are mutually exclusive.

**Since:** 23

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'readerModeWithInterval' | Yes |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes |
| discTech | number[] | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TagInfo](arkts-connectivity-tag-taginfo-i.md)&gt; | Yes |
| interval | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
| [3100202](../errorcode-nfc.md#3100202-application-status-error) |
