# getDownloadableProfileMetadata (System API)

## Modules to Import

```TypeScript
import { eSIM } from '@kit.TelephonyKit';
```

## getDownloadableProfileMetadata

```TypeScript
function getDownloadableProfileMetadata(slotId: number, portIndex: number,
                                          profile: DownloadableProfile, forceDisableProfile: boolean): Promise<GetDownloadableProfileMetadataResult>
```

Fills in and gets the metadata for a downloadable profile.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function getDownloadableProfileMetadata(slotId: int, portIndex: int,                                          profile: DownloadableProfile, forceDisableProfile: boolean): Promise<GetDownloadableProfileMetadataResult>--><!--Device-eSIM-function getDownloadableProfileMetadata(slotId: int, portIndex: int,                                          profile: DownloadableProfile, forceDisableProfile: boolean): Promise<GetDownloadableProfileMetadataResult>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| portIndex | number | Yes |
| profile | [DownloadableProfile](arkts-telephony-esim-downloadableprofile-i.md) | Yes |
| [forceDisableProfile](arkts-telephony-esim-downloadconfiguration-i-sys.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[GetDownloadableProfileMetadataResult](arkts-telephony-esim-getdownloadableprofilemetadataresult-i-sys.md)&gt; |

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
