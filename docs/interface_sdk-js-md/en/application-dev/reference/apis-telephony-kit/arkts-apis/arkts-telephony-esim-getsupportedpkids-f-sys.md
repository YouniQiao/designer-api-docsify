# getSupportedPkids (System API)

## Modules to Import

```TypeScript
import { eSIM } from 'eSIM';
```

## getSupportedPkids

```TypeScript
function getSupportedPkids(slotId: int) : Promise<string>
```

Get supported pkids

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function getSupportedPkids(slotId: int) : Promise<string>--><!--Device-eSIM-function getSupportedPkids(slotId: int) : Promise<string>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Returns the supported pkids. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) | System internal error. |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) | Service connection failed. |

## Examples

```TypeScript
import { eSIM } from '@kit.TelephonyKit';

try {
    let supportedPkids: string = await eSIM.getSupportedPkids(1);
    console.info(`supported pkids is:` + supportedPkids);
} catch (err) {
    console.error(`getSupportedPkids, promise: err->${JSON.stringify(err)}`)
}
```

