# getAttestStatus（系统接口）

## 导入模块

```TypeScript
import { deviceAttest } from 'kits/@kit.BasicServicesKit';
```

## getAttestStatus

```TypeScript
function getAttestStatus(callback: AsyncCallback<AttestResultInfo>): void
```

Obtains the AttestResultInfo object.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-deviceAttest-function getAttestStatus(callback: AsyncCallback<AttestResultInfo>): void--><!--Device-deviceAttest-function getAttestStatus(callback: AsyncCallback<AttestResultInfo>): void-End-->

**系统能力：** SystemCapability.XTS.DeviceAttest

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;AttestResultInfo&gt; | 是 | Indicates the callback containing the AttestResultInfo object. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 20000001 | System service exception, please try again or reboot your device. |
| 401 | Input parameters wrong, the number of parameters is incorrect,or the type of parameters is incorrect. |
| 202 | This api is system api, Please use the system application to call this api. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    deviceAttest.getAttestStatus((error: BusinessError, value: deviceAttest.AttestResultInfo) => {
    if (typeof error != 'undefined') {
        console.error("error code:" + error.code + " message:" + error.message);
    } else {
        console.info("auth:" + value.authResult + " software:" + value.softwareResult + " ticket:" + value.ticket);
        console.info("versionIdResult:" + value.softwareResultDetail[0],
        " patchLevelResult:" + value.softwareResultDetail[1],
        " rootHashResult:" + value.softwareResultDetail[2],
        " PCIDResult:" + value.softwareResultDetail[3],
        " reserved:" + value.softwareResultDetail[4]);
    }
    })
} catch (error) {
    let code: number = (error as BusinessError).code;
    let message: string = (error as BusinessError).message;
    console.error("error code:" + code + " message:" + message);
}
```


## getAttestStatus

```TypeScript
function getAttestStatus(): Promise<AttestResultInfo>
```

Obtains the AttestResultInfo object.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-deviceAttest-function getAttestStatus(): Promise<AttestResultInfo>--><!--Device-deviceAttest-function getAttestStatus(): Promise<AttestResultInfo>-End-->

**系统能力：** SystemCapability.XTS.DeviceAttest

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;AttestResultInfo&gt; | Returns that the AttestResultInfo object is returned in Promise mode. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 20000001 | System service exception, please try again or reboot your device. |
| 401 | Input parameters wrong, the number of parameters is incorrect,or the type of parameters is incorrect. |
| 202 | This api is system api, Please use the system application to call this api. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    deviceAttest.getAttestStatus().then((value: deviceAttest.AttestResultInfo) => {
    console.info("auth:" + value.authResult + " software:" + value.softwareResult + " ticket:" + value.ticket);
    console.info("versionIdResult:" + value.softwareResultDetail[0],
        " patchLevelResult:" + value.softwareResultDetail[1],
        " rootHashResult:" + value.softwareResultDetail[2],
        " PCIDResult:" + value.softwareResultDetail[3],
        " reserved:" + value.softwareResultDetail[4]);
    }).catch((error: BusinessError) => {
        console.error("error code:" + error.code + " message:" + error.message);
    });
} catch (error) {
    let code: number = (error as BusinessError).code;
    let message: string = (error as BusinessError).message;
    console.error("error code:" + code + " message:" + message);
}
```

