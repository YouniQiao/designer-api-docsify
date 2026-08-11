# isDefaultService

## Modules to Import

```TypeScript
import { cardEmulation } from 'kits/@kit.ConnectivityKit';
```

## isDefaultService

```TypeScript
function isDefaultService(elementName: ElementName, type: CardType): boolean
```

Checks whether a service is default for given type.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cardEmulation-function isDefaultService(elementName: ElementName, type: CardType): boolean--><!--Device-cardEmulation-function isDefaultService(elementName: ElementName, type: CardType): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | [ElementName](../../apis-ability-kit/arkts-apis/arkts-ability-elementname-i.md) | Yes | The element name of the service ability |
| type | [CardType](arkts-connectivity-cardemulation-cardtype-e.md) | Yes | The type to query, payment or other. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the service is default, otherwise false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
// Applicable to devices other than lite wearables
import { cardEmulation } from '@kit.ConnectivityKit';
import { bundleManager, Want } from '@kit.AbilityKit';

// Initialize elementName, bundleName, and abilityName and set their values correctly based on the actual application information.
let elementName: bundleManager.ElementName = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  abilityName: "EntryAbility"
};

let isDefaultService: boolean = cardEmulation.isDefaultService(elementName, cardEmulation.CardType.PAYMENT);
```

```TypeScript
// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

let appName = "com.example.testquestionlite";
let isDefaultService = cardEmulation.isDefaultService(appName, cardEmulation.CardType.PAYMENT);
```

