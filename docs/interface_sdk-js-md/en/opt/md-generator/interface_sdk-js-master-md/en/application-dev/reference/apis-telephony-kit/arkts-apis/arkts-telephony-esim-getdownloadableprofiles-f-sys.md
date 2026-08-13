# getDownloadableProfiles (System API)

## Modules to Import

```TypeScript
import { eSIM } from '@kit.TelephonyKit';
```

## getDownloadableProfiles

```TypeScript
function getDownloadableProfiles(slotId: number, portIndex: number,
                                   forceDisableProfile: boolean): Promise<GetDownloadableProfilesResult>
```

Gets downloadable profile List which are available for download on this device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function getDownloadableProfiles(slotId: int, portIndex: int,                                   forceDisableProfile: boolean): Promise<GetDownloadableProfilesResult>--><!--Device-eSIM-function getDownloadableProfiles(slotId: int, portIndex: int,                                   forceDisableProfile: boolean): Promise<GetDownloadableProfilesResult>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| portIndex | number | Yes |
| [forceDisableProfile](arkts-telephony-esim-downloadconfiguration-i-sys.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[GetDownloadableProfilesResult](arkts-telephony-esim-getdownloadableprofilesresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { eSIM } from '@kit.TelephonyKit';

eSIM.getDownloadableProfiles(1, 0, true).then((data: eSIM.GetDownloadableProfilesResult) => {
    console.info(`getDownloadableProfiles, GetDownloadableProfilesResult: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError<void>) => {
    console.error(`getDownloadableProfiles, GetDownloadableProfilesResult: err->${JSON.stringify(err)}`);
});
```
