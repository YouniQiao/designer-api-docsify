# onReaderMode

## Modules to Import

```TypeScript
import { tag } from 'tag';
```

## onReaderMode

```TypeScript
function onReaderMode(elementName: ElementName, discTech: int[], callback: AsyncCallback<TagInfo>): void
```

Set reader mode enabled when the specific application is foreground. Dispatches to this application only if a tag discovered.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-tag-function onReaderMode(elementName: ElementName, discTech: int[], callback: AsyncCallback<TagInfo>): void--><!--Device-tag-function onReaderMode(elementName: ElementName, discTech: int[], callback: AsyncCallback<TagInfo>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes | The element name of application, must include the bundleName and abilityName. |
| discTech | int[] | Yes | The technologies list to set for discovering. From [NFC_A](arkts-connectivity-tag-con.md#NFC_A) to [MIFARE_ULTRALIGHT](arkts-connectivity-tag-con.md#MIFARE_ULTRALIGHT). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[TagInfo](arkts-connectivity-tag-taginfo-i.md)&gt; | Yes | The callback to dispatched the TagInfo object for application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100202](../errorcode-nfc.md#3100202-application-status-error) | The element state is invalid. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

