# GetDownloadableProfilesResult（系统接口）

Result of downloadable Profile list.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-eSIM-export interface GetDownloadableProfilesResult--><!--Device-eSIM-export interface GetDownloadableProfilesResult-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## downloadableProfiles

```TypeScript
downloadableProfiles: Array<DownloadableProfile>
```

Gets the downloadable Profiles with filled-in metadata.

**类型：** Array&lt;DownloadableProfile&gt;

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-GetDownloadableProfilesResult-downloadableProfiles: Array<DownloadableProfile>--><!--Device-GetDownloadableProfilesResult-downloadableProfiles: Array<DownloadableProfile>-End-->

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

<!--Device-GetDownloadableProfilesResult-responseResult: ResultCode--><!--Device-GetDownloadableProfilesResult-responseResult: ResultCode-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

