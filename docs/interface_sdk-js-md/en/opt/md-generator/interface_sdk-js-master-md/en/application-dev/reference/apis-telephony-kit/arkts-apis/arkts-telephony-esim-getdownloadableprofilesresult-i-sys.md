# GetDownloadableProfilesResult (System API)

Result of downloadable Profile list.

**Since:** 18

<!--Device-eSIM-export interface GetDownloadableProfilesResult--><!--Device-eSIM-export interface GetDownloadableProfilesResult-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## downloadableProfiles

```TypeScript
downloadableProfiles: Array<DownloadableProfile>
```

Gets the downloadable Profiles with filled-in metadata.

**Type:** Array&lt;DownloadableProfile&gt;

**Since:** 18

<!--Device-GetDownloadableProfilesResult-downloadableProfiles: Array<DownloadableProfile>--><!--Device-GetDownloadableProfilesResult-downloadableProfiles: Array<DownloadableProfile>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## responseResult

```TypeScript
responseResult: ResultCode
```

Gets the result of the operation.

**Type:** [ResultCode](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-appaccount-resultcode-e.md)

**Since:** 18

<!--Device-GetDownloadableProfilesResult-responseResult: ResultCode--><!--Device-GetDownloadableProfilesResult-responseResult: ResultCode-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.
