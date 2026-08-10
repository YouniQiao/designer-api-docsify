# downloadProfile（系统接口）

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## downloadProfile

```TypeScript
function downloadProfile(slotId: int, portIndex: int, profile: DownloadableProfile,
                           configuration: DownloadConfiguration): Promise<DownloadProfileResult>
```

Attempt to download the given downloadable Profile.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function downloadProfile(slotId: int, portIndex: int, profile: DownloadableProfile,                           configuration: DownloadConfiguration): Promise<DownloadProfileResult>--><!--Device-eSIM-function downloadProfile(slotId: int, portIndex: int, profile: DownloadableProfile,                           configuration: DownloadConfiguration): Promise<DownloadProfileResult>-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number. |
| portIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Index of the port for the slot. |
| profile | [DownloadableProfile](arkts-telephony-esim-downloadableprofile-i.md) | 是 | The Bound Profile Package data returned by SM-DP+ server. |
| configuration | [DownloadConfiguration](arkts-telephony-esim-downloadconfiguration-i-sys.md) | 是 | Configuration information during downloading. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;DownloadProfileResult&gt; | Return the given downloadableProfile. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 3120002 | System internal error. |
| 3120001 | Service connection failed. |

## 示例

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

let configuration: eSIM.DownloadConfiguration = {
  switchAfterDownload: true,
  forceDisableProfile: true,
  isPprAllowed: true,
};

eSIM.downloadProfile(1, 0, profile, configuration).then((data: eSIM.DownloadProfileResult) => {
    console.info(`downloadProfile, DownloadProfileResult: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError<void>) => {
    console.error(`downloadProfile, DownloadProfileResult: err->${JSON.stringify(err)}`);
});
```

