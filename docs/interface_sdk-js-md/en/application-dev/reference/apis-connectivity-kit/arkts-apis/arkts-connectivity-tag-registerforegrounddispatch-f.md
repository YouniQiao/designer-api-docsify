# registerForegroundDispatch

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## registerForegroundDispatch

```TypeScript
function registerForegroundDispatch(elementName: ElementName, discTech: int[], callback: AsyncCallback<TagInfo>): void
```

Register tag foreground dispatch. Dispatches to this application only if a tag discovered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_TAG

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-tag-function registerForegroundDispatch(elementName: ElementName, discTech: int[], callback: AsyncCallback<TagInfo>): void--><!--Device-tag-function registerForegroundDispatch(elementName: ElementName, discTech: int[], callback: AsyncCallback<TagInfo>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes | The element name of application, must include the bundleName and abilityName. |
| discTech | ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[] | Yes | The technologies list to set for discovering. From {@link NFC_A} to {@link MIFARE_ULTRALIGHT}. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;TagInfo&gt; | Yes | The callback to dispatched the TagInfo object for application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [3100202](../errorcode-nfc.md#3100202-application-status-error) | The element state is invalid. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

