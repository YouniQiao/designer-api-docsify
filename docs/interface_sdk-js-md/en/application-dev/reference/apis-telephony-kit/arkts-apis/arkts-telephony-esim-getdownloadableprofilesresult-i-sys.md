# GetDownloadableProfilesResult (System API)

Obtains the list of default downloadable profiles.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

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

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## responseResult

```TypeScript
responseResult: ResultCode
```

Promise used to return the operation result.

**Type:** ResultCode

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.
