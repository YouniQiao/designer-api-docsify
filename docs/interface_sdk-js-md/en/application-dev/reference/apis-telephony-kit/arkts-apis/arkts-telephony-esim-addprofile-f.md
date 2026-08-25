# addProfile

## Modules to Import

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## addProfile

```TypeScript
function addProfile(profile: DownloadableProfile): Promise<boolean>
```

Launches the download page for the user to add a single profile. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.SET_TELEPHONY_ESIM_STATE_OPEN

**System capability:** SystemCapability.Telephony.CoreService.Esim

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| profile | [DownloadableProfile](arkts-telephony-esim-downloadableprofile-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) |
