# hasHceCapability

## Modules to Import

```TypeScript
import { cardEmulation } from 'kits/@kit.ConnectivityKit';
```

## hasHceCapability

```TypeScript
function hasHceCapability(): boolean
```

Checks whether Host Card Emulation(HCE) capability is supported.

**Since:** 12

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-cardEmulation-function hasHceCapability(): boolean--><!--Device-cardEmulation-function hasHceCapability(): boolean-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |

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
