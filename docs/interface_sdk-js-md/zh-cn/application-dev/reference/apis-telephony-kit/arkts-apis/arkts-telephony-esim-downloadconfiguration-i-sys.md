# DownloadConfiguration（系统接口）

Specifies the download configuration.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-eSIM-export interface DownloadConfiguration--><!--Device-eSIM-export interface DownloadConfiguration-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## forceDisableProfile

```TypeScript
forceDisableProfile: boolean
```

Specifies whether to forcibly disable the profile. If true, the active profile is disabled in order to perform the operation. Otherwise, {@link RESULT_MUST_DISABLE_PROFILE} is returned in resultCode to ask for the user's agreement to the operation.

**类型：** boolean

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-DownloadConfiguration-forceDisableProfile: boolean--><!--Device-DownloadConfiguration-forceDisableProfile: boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## isPprAllowed

```TypeScript
isPprAllowed: boolean
```

Specifies whether the user allows the service provider to enforce this Profile Policy Rule (PPR)after being informed of its restrictions.

**类型：** boolean

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-DownloadConfiguration-isPprAllowed: boolean--><!--Device-DownloadConfiguration-isPprAllowed: boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## switchAfterDownload

```TypeScript
switchAfterDownload: boolean
```

Specifies whether to enable the profile after successful download.

**类型：** boolean

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-DownloadConfiguration-switchAfterDownload: boolean--><!--Device-DownloadConfiguration-switchAfterDownload: boolean-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

