# GetDownloadableProfilesResult (System API)

Obtains the list of default downloadable profiles.

**Since:** 23

<!--Device-eSIM-export interface GetDownloadableProfilesResult--><!--Device-eSIM-export interface GetDownloadableProfilesResult-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { eSIM } from '@kit.TelephonyKit';
```

## downloadableProfiles

```TypeScript
downloadableProfiles: Array<DownloadableProfile>
```

Downloadable file array.

**Type:** Array&lt;[DownloadableProfile](arkts-telephony-esim-downloadableprofile-i.md)&gt;

**Since:** 23

<!--Device-GetDownloadableProfilesResult-downloadableProfiles: Array<DownloadableProfile>--><!--Device-GetDownloadableProfilesResult-downloadableProfiles: Array<DownloadableProfile>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## responseResult

```TypeScript
responseResult: ResultCode
```

Promise used to return the operation result.

**Type:** ResultCode

**Since:** 23

<!--Device-GetDownloadableProfilesResult-responseResult: ResultCode--><!--Device-GetDownloadableProfilesResult-responseResult: ResultCode-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

