# downloadProfile (System API)

## Modules to Import

```TypeScript
import { eSIM } from 'eSIM';
```

## downloadProfile

```TypeScript
function downloadProfile(slotId: int, portIndex: int, profile: DownloadableProfile,
                           configuration: DownloadConfiguration): Promise<DownloadProfileResult>
```

Attempt to download the given downloadable Profile.

**Since:** 23

**Required permissions:** ohos.permission.SET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function downloadProfile(slotId: int, portIndex: int, profile: DownloadableProfile,                           configuration: DownloadConfiguration): Promise<DownloadProfileResult>--><!--Device-eSIM-function downloadProfile(slotId: int, portIndex: int, profile: DownloadableProfile,                           configuration: DownloadConfiguration): Promise<DownloadProfileResult>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number. |
| portIndex | int | Yes | Index of the port for the slot. |
| profile | [DownloadableProfile](arkts-telephony-esim-downloadableprofile-i.md) | Yes | The Bound Profile Package data returned by SM-DP+ server. |
| configuration | [DownloadConfiguration](arkts-telephony-esim-downloadconfiguration-i-sys.md) | Yes | Configuration information during downloading. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DownloadProfileResult](arkts-telephony-esim-downloadprofileresult-i-sys.md)&gt; | Return the given downloadableProfile. |

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

let profile: eSIM.DownloadableProfile = {
  activationCode:'1',
  confirmationCode:'1',
  carrierName:'test',
  accessRules:[{
    certificateHashHexStr:'test',
    packageName:'com.example.testcoreservice',
    accessType:0
  }]
};

let configuration: eSIM.DownloadConfiguration = {
  switchAfterDownload: true,
  forceDisableProfile: true,
  isPprAllowed: true,
};

eSIM.downloadProfile(1, 0, profile, configuration).then((data: eSIM.DownloadProfileResult) => {
    console.info(`downloadProfile, DownloadProfileResult: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError<void>) => {
    console.error(`downloadProfile, DownloadProfileResult: err->${JSON.stringify(err)}`);
});
```

