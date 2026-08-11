# getPaymentServices (System API)

## Modules to Import

```TypeScript
import { cardEmulation } from 'kits/@kit.ConnectivityKit';
```

## getPaymentServices

```TypeScript
function getPaymentServices(): AbilityInfo[]
```

Gets all payment services.

**Since:** 11

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-cardEmulation-function getPaymentServices(): AbilityInfo[]--><!--Device-cardEmulation-function getPaymentServices(): AbilityInfo[]-End-->

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AbilityInfo](../../apis-ability-kit/arkts-apis/arkts-ability-abilityinfo-i.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
