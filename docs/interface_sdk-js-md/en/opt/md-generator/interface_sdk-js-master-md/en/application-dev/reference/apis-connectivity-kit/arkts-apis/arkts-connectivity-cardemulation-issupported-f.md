# isSupported

## Modules to Import

```TypeScript
import { cardEmulation } from 'kits/@kit.ConnectivityKit';
```

## isSupported

```TypeScript
function isSupported(feature: number): boolean
```

Checks whether a specified type of card emulation is supported.&lt;p&gt;This method is used to check Whether the host or secure element supports card emulation.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** ohos.nfc.cardEmulation/cardEmulation#hasHceCapability

**Model restriction:** This API can be used only in the stage model.

<!--Device-cardEmulation-function isSupported(feature: number): boolean--><!--Device-cardEmulation-function isSupported(feature: number): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| feature | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
// Applicable to devices other than lite wearables
import { cardEmulation } from '@kit.ConnectivityKit';

let isHceSupported: boolean = cardEmulation.isSupported(cardEmulation.FeatureType.HCE);
if (!isHceSupported) {
    console.info('this device is not supported for HCE, ignore it.');
}
```

```TypeScript
// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

let isHceSupported = cardEmulation.isSupported(cardEmulation.FeatureType.HCE);
if (!isHceSupported) {
    console.error('this device is not supported for HCE, ignore it.');
}
```
