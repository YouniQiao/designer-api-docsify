# getPaymentServices (System API)

## Modules to Import

```TypeScript
import { cardEmulation } from 'kits/@kit.ConnectivityKit';
```

## getPaymentServices

```TypeScript
function getPaymentServices(): AbilityInfo[]
```

Obtains all payment services. If an application declares the support for the HCE feature and **payment-aid**, the application is contained in the payment service list. For details, see [HCE and AID Declaration](../../../reference/apis-connectivity-kit/js-apis-cardEmulation.md#hce-and-aid-declaration).

**Since:** 11

**Required permissions:** ohos.permission.NFC_CARD_EMULATION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NFC.CardEmulation

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AbilityInfo](../../apis-ability-kit/arkts-apis/arkts-ability-abilityinfo-i.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
