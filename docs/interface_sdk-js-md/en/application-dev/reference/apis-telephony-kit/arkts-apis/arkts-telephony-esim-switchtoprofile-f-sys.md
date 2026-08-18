# switchToProfile (System API)

## Modules to Import

```TypeScript
import { eSIM } from '@kit.TelephonyKit';
```

## switchToProfile

```TypeScript
function switchToProfile(slotId: int, portIndex: int, iccid: string,
                           forceDisableProfile: boolean): Promise<ResultCode>
```

Switch to (enable) the given profile on the eUICC.

**Since:** 23

**Required permissions:** ohos.permission.SET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function switchToProfile(slotId: int, portIndex: int, iccid: string,                           forceDisableProfile: boolean): Promise<ResultCode>--><!--Device-eSIM-function switchToProfile(slotId: int, portIndex: int, iccid: string,                           forceDisableProfile: boolean): Promise<ResultCode>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number. |
| portIndex | int | Yes | Index of the port for the slot. |
| iccid | string | Yes | The iccid of the profile to switch to. |
| forceDisableProfile | boolean | Yes | If true, the active profile must be disabled in order to perform the operation. Otherwise, the resultCode should return [RESULT_MUST_DISABLE_PROFILE](arkts-telephony-esim-resultcode-e-sys.md#result_must_disable_profile) to allow the user to agree to this operation first. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ResultCode&gt; | Returns the response to switch profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) | System internal error. |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) | Service connection failed. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { eSIM } from '@kit.TelephonyKit';

eSIM.switchToProfile(1, 0, 'testId', true).then(() => {
    console.info(`switchToProfile invoking succeeded.`);
}).catch((err: BusinessError<void>) => {
    console.error(`switchToProfile, ErrorState: err->${JSON.stringify(err)}`);
});
```

