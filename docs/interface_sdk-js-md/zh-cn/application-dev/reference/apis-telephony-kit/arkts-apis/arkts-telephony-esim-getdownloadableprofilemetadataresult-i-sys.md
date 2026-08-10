# GetDownloadableProfileMetadataResult（系统接口）

Result the metadata for a downloadableProfile.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-eSIM-export interface GetDownloadableProfileMetadataResult--><!--Device-eSIM-export interface GetDownloadableProfileMetadataResult-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## downloadableProfile

```TypeScript
downloadableProfile: DownloadableProfile
```

Information about a profile which is downloadable to an eUICC using.

**类型：** [DownloadableProfile](arkts-telephony-esim-downloadableprofile-i.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-GetDownloadableProfileMetadataResult-downloadableProfile: DownloadableProfile--><!--Device-GetDownloadableProfileMetadataResult-downloadableProfile: DownloadableProfile-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## iccid

```TypeScript
iccid: string
```

The iccid of the profile.

**类型：** string

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-GetDownloadableProfileMetadataResult-iccid: string--><!--Device-GetDownloadableProfileMetadataResult-iccid: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## pprFlag

```TypeScript
pprFlag: boolean
```

The flag of profile policy rule.

**类型：** boolean

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-GetDownloadableProfileMetadataResult-pprFlag: boolean--><!--Device-GetDownloadableProfileMetadataResult-pprFlag: boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## pprType

```TypeScript
pprType: int
```

The type of profile policy rule.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-GetDownloadableProfileMetadataResult-pprType: int--><!--Device-GetDownloadableProfileMetadataResult-pprType: int-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## profileClass

```TypeScript
profileClass: ProfileClass
```

Profile class for the profile.

**类型：** [ProfileClass](arkts-telephony-esim-profileclass-e-sys.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-GetDownloadableProfileMetadataResult-profileClass: ProfileClass--><!--Device-GetDownloadableProfileMetadataResult-profileClass: ProfileClass-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## profileName

```TypeScript
profileName: string
```

The profile name.

**类型：** string

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-GetDownloadableProfileMetadataResult-profileName: string--><!--Device-GetDownloadableProfileMetadataResult-profileName: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## responseResult

```TypeScript
responseResult: ResultCode
```

Gets the result of the operation.

**类型：** [ResultCode](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-appaccount-resultcode-e.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-GetDownloadableProfileMetadataResult-responseResult: ResultCode--><!--Device-GetDownloadableProfileMetadataResult-responseResult: ResultCode-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## serviceProviderName

```TypeScript
serviceProviderName: string
```

The service provider name for the profile.

**类型：** string

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-GetDownloadableProfileMetadataResult-serviceProviderName: string--><!--Device-GetDownloadableProfileMetadataResult-serviceProviderName: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## solvableErrors

```TypeScript
solvableErrors: SolvableErrors
```

Gets the solvable errors.

**类型：** [SolvableErrors](arkts-telephony-esim-solvableerrors-e-sys.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-GetDownloadableProfileMetadataResult-solvableErrors: SolvableErrors--><!--Device-GetDownloadableProfileMetadataResult-solvableErrors: SolvableErrors-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

