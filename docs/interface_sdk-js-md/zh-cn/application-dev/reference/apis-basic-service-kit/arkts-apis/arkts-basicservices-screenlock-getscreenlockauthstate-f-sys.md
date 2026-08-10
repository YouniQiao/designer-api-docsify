# getScreenLockAuthState（系统接口）

## 导入模块

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## getScreenLockAuthState

```TypeScript
function getScreenLockAuthState(userId: int): AuthState
```

Obtain the screen lock authentication state for os account local userId.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ACCESS_SCREEN_LOCK

<!--Device-screenLock-function getScreenLockAuthState(userId: int): AuthState--><!--Device-screenLock-function getScreenLockAuthState(userId: int): AuthState-End-->

**系统能力：** SystemCapability.MiscServices.ScreenLock

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Os account local userId. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuthState](arkts-basicservices-screenlock-authstate-e-sys.md) | the screen lock authentication state. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 201 | permission denied. |
| 202 | permission verification failed, application which is not a system application uses system API. |
| 13200002 | the screenlock management service is abnormal. |

