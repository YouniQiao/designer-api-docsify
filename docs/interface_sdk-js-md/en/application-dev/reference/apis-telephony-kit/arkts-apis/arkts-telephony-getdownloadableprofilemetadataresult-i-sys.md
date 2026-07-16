# GetDownloadableProfileMetadataResult (System API)

Result the metadata for a downloadableProfile.

**Since:** 18

<!--Device-eSIM-export interface GetDownloadableProfileMetadataResult--><!--Device-eSIM-export interface GetDownloadableProfileMetadataResult-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { eSIM } from '@kit.TelephonyKit';
```

## downloadableProfile

```TypeScript
downloadableProfile: DownloadableProfile
```

Information about a profile which is downloadable to an eUICC using.

**Type:** DownloadableProfile

**Since:** 18

<!--Device-GetDownloadableProfileMetadataResult-downloadableProfile: DownloadableProfile--><!--Device-GetDownloadableProfileMetadataResult-downloadableProfile: DownloadableProfile-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## iccid

```TypeScript
iccid: string
```

The iccid of the profile.

**Type:** string

**Since:** 18

<!--Device-GetDownloadableProfileMetadataResult-iccid: string--><!--Device-GetDownloadableProfileMetadataResult-iccid: string-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## pprFlag

```TypeScript
pprFlag: boolean
```

The flag of profile policy rule.

**Type:** boolean

**Since:** 18

<!--Device-GetDownloadableProfileMetadataResult-pprFlag: boolean--><!--Device-GetDownloadableProfileMetadataResult-pprFlag: boolean-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## pprType

```TypeScript
pprType: number
```

The type of profile policy rule.

**Type:** number

**Since:** 18

<!--Device-GetDownloadableProfileMetadataResult-pprType: int--><!--Device-GetDownloadableProfileMetadataResult-pprType: int-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## profileClass

```TypeScript
profileClass: ProfileClass
```

Profile class for the profile.

**Type:** ProfileClass

**Since:** 18

<!--Device-GetDownloadableProfileMetadataResult-profileClass: ProfileClass--><!--Device-GetDownloadableProfileMetadataResult-profileClass: ProfileClass-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## profileName

```TypeScript
profileName: string
```

The profile name.

**Type:** string

**Since:** 18

<!--Device-GetDownloadableProfileMetadataResult-profileName: string--><!--Device-GetDownloadableProfileMetadataResult-profileName: string-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## responseResult

```TypeScript
responseResult: ResultCode
```

Gets the result of the operation.

**Type:** ResultCode

**Since:** 18

<!--Device-GetDownloadableProfileMetadataResult-responseResult: ResultCode--><!--Device-GetDownloadableProfileMetadataResult-responseResult: ResultCode-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## serviceProviderName

```TypeScript
serviceProviderName: string
```

The service provider name for the profile.

**Type:** string

**Since:** 18

<!--Device-GetDownloadableProfileMetadataResult-serviceProviderName: string--><!--Device-GetDownloadableProfileMetadataResult-serviceProviderName: string-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## solvableErrors

```TypeScript
solvableErrors: SolvableErrors
```

Gets the solvable errors.

**Type:** SolvableErrors

**Since:** 18

<!--Device-GetDownloadableProfileMetadataResult-solvableErrors: SolvableErrors--><!--Device-GetDownloadableProfileMetadataResult-solvableErrors: SolvableErrors-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

