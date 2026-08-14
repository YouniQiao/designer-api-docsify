# getDownloadableProfileMetadata (System API)

## Modules to Import

```TypeScript
import { eSIM } from 'eSIM';
```

## getDownloadableProfileMetadata

```TypeScript
function getDownloadableProfileMetadata(slotId: int, portIndex: int,
                                          profile: DownloadableProfile, forceDisableProfile: boolean): Promise<GetDownloadableProfileMetadataResult>
```

Fills in and gets the metadata for a downloadable profile.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function getDownloadableProfileMetadata(slotId: int, portIndex: int,                                          profile: DownloadableProfile, forceDisableProfile: boolean): Promise<GetDownloadableProfileMetadataResult>--><!--Device-eSIM-function getDownloadableProfileMetadata(slotId: int, portIndex: int,                                          profile: DownloadableProfile, forceDisableProfile: boolean): Promise<GetDownloadableProfileMetadataResult>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number. |
| portIndex | int | Yes | Index of the port for the slot. |
| profile | [DownloadableProfile](arkts-telephony-esim-downloadableprofile-i.md) | Yes | The Bound Profile Package data returned by SM-DP+ server. |
| forceDisableProfile | boolean | Yes | If true, the active profile must be disabled in order to perform the operation. Otherwise, the resultCode should return [RESULT_MUST_DISABLE_PROFILE](arkts-telephony-esim-resultcode-e-sys.md#RESULT_MUST_DISABLE_PROFILE) to allow the user to agree to this operation first. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[GetDownloadableProfileMetadataResult](arkts-telephony-esim-getdownloadableprofilemetadataresult-i-sys.md)&gt; | Return the metadata for profile. |

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

eSIM.getDownloadableProfileMetadata(1, 0, profile, true).then((data: eSIM.GetDownloadableProfileMetadataResult) => {
    console.info(`getDownloadableProfileMetadata, GetDownloadableProfileMetadataResult: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError<void>) => {
    console.error(`getDownloadableProfileMetadata, GetDownloadableProfileMetadataResult: err->${JSON.stringify(err)}`);
});
```

