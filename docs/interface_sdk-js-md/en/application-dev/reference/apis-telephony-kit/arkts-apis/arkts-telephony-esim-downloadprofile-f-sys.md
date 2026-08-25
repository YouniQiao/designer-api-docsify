# downloadProfile (System API)

## Modules to Import

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## downloadProfile

```TypeScript
function downloadProfile(slotId: number, portIndex: number, profile: DownloadableProfile,
                           configuration: DownloadConfiguration): Promise<DownloadProfileResult>
```

Downloads a profile. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.SET_TELEPHONY_ESIM_STATE

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| portIndex | number | Yes |
| profile | [DownloadableProfile](arkts-telephony-esim-downloadableprofile-i.md) | Yes |
| configuration | [DownloadConfiguration](arkts-telephony-esim-downloadconfiguration-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DownloadProfileResult](arkts-telephony-esim-downloadprofileresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) |
