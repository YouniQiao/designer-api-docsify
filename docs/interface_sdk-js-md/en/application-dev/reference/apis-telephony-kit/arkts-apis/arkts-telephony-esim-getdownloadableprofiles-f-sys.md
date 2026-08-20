# getDownloadableProfiles (System API)

## Modules to Import

```TypeScript
import { eSIM } from '@kit.TelephonyKit';
```

## getDownloadableProfiles

```TypeScript
function getDownloadableProfiles(slotId: int, portIndex: int,
                                   forceDisableProfile: boolean): Promise<GetDownloadableProfilesResult>
```

Gets downloadable profile List which are available for download on this device.

**Since:** 23

**Required permissions:** ohos.permission.GET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function getDownloadableProfiles(slotId: int, portIndex: int,                                   forceDisableProfile: boolean): Promise<GetDownloadableProfilesResult>--><!--Device-eSIM-function getDownloadableProfiles(slotId: int, portIndex: int,                                   forceDisableProfile: boolean): Promise<GetDownloadableProfilesResult>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number. |
| portIndex | int | Yes | Index of the port for the slot. |
| forceDisableProfile | boolean | Yes | If true, the active profile must be disabled in order to perform the operation. Otherwise, the resultCode should return [RESULT_MUST_DISABLE_PROFILE](arkts-telephony-esim-resultcode-e-sys.md#result_must_disable_profile) to allow the user to agree to this operation first. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[GetDownloadableProfilesResult](arkts-telephony-esim-getdownloadableprofilesresult-i-sys.md)&gt; | Return metadata for downloadableProfile which are available for download on this device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) | Service connection failed. |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) | System internal error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { eSIM } from '@kit.TelephonyKit';

eSIM.getDownloadableProfiles(1, 0, true).then((data: eSIM.GetDownloadableProfilesResult) => {
    console.info(`getDownloadableProfiles, GetDownloadableProfilesResult: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError<void>) => {
    console.error(`getDownloadableProfiles, GetDownloadableProfilesResult: err->${JSON.stringify(err)}`);
});
```

