# hasHceCapability

## Modules to Import

```TypeScript
import { cardEmulation } from 'cardEmulation';
```

## hasHceCapability

```TypeScript
function hasHceCapability(): boolean
```

Checks whether Host Card Emulation(HCE) capability is supported.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-cardEmulation-function hasHceCapability(): boolean--><!--Device-cardEmulation-function hasHceCapability(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if HCE is supported, otherwise false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
// Applicable to devices other than lite wearables
import { cardEmulation } from '@kit.ConnectivityKit';

let hasHceCap: boolean = cardEmulation.hasHceCapability();
if (!hasHceCap) {
    console.error('this device hasHceCapability false, ignore it.');
}
```

```TypeScript
// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

let hasHceCap = cardEmulation.hasHceCapability();
if (!hasHceCap) {
    console.error('this device hasHceCapability false, ignore it.');
}
```

