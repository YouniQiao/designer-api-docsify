# addProfile

## Modules to Import

```TypeScript
import { eSIM } from '@kit.TelephonyKit';
```

## addProfile

```TypeScript
function addProfile(profile: DownloadableProfile): Promise<boolean>
```

Starts a page through an ability, on which users can touch the button to download a profile.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_TELEPHONY_ESIM_STATE_OPEN

<!--Device-eSIM-function addProfile(profile: DownloadableProfile): Promise<boolean>--><!--Device-eSIM-function addProfile(profile: DownloadableProfile): Promise<boolean>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profile | [DownloadableProfile](arkts-telephony-esim-downloadableprofile-i.md) | Yes | Bound profile package data returned by the SM-DP+ server. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Returns { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
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

eSIM.addProfile(profile).then(() => {
    console.info(`addProfile invoking succeeded.`);
}).catch((err: BusinessError<void>) => {
    console.error(`addProfile, promise: err->${JSON.stringify(err)}`);
});
```

