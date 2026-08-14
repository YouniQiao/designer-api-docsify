# getOsuStatus (System API)

## Modules to Import

```TypeScript
import { eSIM } from 'eSIM';
```

## getOsuStatus

```TypeScript
function getOsuStatus(slotId: int): Promise<OsuStatus>
```

Returns the current status of eUICC OS upgrade.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function getOsuStatus(slotId: int): Promise<OsuStatus>--><!--Device-eSIM-function getOsuStatus(slotId: int): Promise<OsuStatus>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[OsuStatus](arkts-telephony-esim-osustatus-e-sys.md)&gt; | Return the status of eUICC OS upgrade. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) | System internal error. |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) | Service connection failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { eSIM } from '@kit.TelephonyKit';

eSIM.getOsuStatus(1).then(() => {
    console.info(`getOsuStatus invoking succeeded.`);
}).catch((err: BusinessError<void>) => {
    console.error(`getOsuStatus, promise: err->${JSON.stringify(err)}`);
});
```

