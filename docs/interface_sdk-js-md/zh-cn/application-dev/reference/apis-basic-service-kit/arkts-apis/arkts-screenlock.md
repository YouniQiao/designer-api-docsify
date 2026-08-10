# @ohos.screenLock

systemScreenLock

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace screenLock--><!--Device-unnamed-declare namespace screenLock-End-->

**系统能力：** SystemCapability.MiscServices.ScreenLock

## 导入模块

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [isScreenLocked](arkts-basicservices-screenlock-isscreenlocked-f.md#isscreenlocked) | Checks whether the screen is currently locked. |
| [isScreenLocked](arkts-basicservices-screenlock-isscreenlocked-f.md#isscreenlocked-1) | Checks whether the screen is currently locked. |
| [isSecureMode](arkts-basicservices-screenlock-issecuremode-f.md#issecuremode) | Checks whether the screen lock of the current device is secure. |
| [isSecureMode](arkts-basicservices-screenlock-issecuremode-f.md#issecuremode-1) | Checks whether the screen lock of the current device is secure. |
| [unlockScreen](arkts-basicservices-screenlock-unlockscreen-f.md#unlockscreen) | Unlock the screen. |
| [unlockScreen](arkts-basicservices-screenlock-unlockscreen-f.md#unlockscreen-1) | Unlock the screen. |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [getScreenLockAuthState](arkts-basicservices-screenlock-getscreenlockauthstate-f-sys.md#getscreenlockauthstate) | Obtain the screen lock authentication state for os account local userId. |
| [getStrongAuth](arkts-basicservices-screenlock-getstrongauth-f-sys.md#getstrongauth) | Obtain strong authentication reason flags for os account local userId. |
| [getUnlockPolicy](arkts-basicservices-screenlock-getunlockpolicy-f-sys.md#getunlockpolicy) | Obtains the authentication policy used to unlock the screen. |
| [isDeviceLocked](arkts-basicservices-screenlock-isdevicelocked-f-sys.md#isdevicelocked) | Check whether the device is currently locked and the screenlock requires an identity to authenticate and unlock. |
| [isLocked](arkts-basicservices-screenlock-islocked-f-sys.md#islocked) | Checks whether the screen is currently locked. |
| [isScreenLockDisabled](arkts-basicservices-screenlock-isscreenlockdisabled-f-sys.md#isscreenlockdisabled) | Check whether screen lock is disabled for os account local userId. |
| [lock](arkts-basicservices-screenlock-lock-f-sys.md#lock) | Lock the screen. |
| [lock](arkts-basicservices-screenlock-lock-f-sys.md#lock-1) | Lock the screen. |
| [onSystemEvent](arkts-basicservices-screenlock-onsystemevent-f-sys.md#onsystemevent) | Register system event related to screen lock service. |
| [requestStrongAuth](arkts-basicservices-screenlock-requeststrongauth-f-sys.md#requeststrongauth) | Request strong authentication for os account local userId. |
| [sendScreenLockEvent](arkts-basicservices-screenlock-sendscreenlockevent-f-sys.md#sendscreenlockevent) | The screen lock app sends the event to the screen lock service. |
| [sendScreenLockEvent](arkts-basicservices-screenlock-sendscreenlockevent-f-sys.md#sendscreenlockevent-1) | The screen lock app sends the event to the screen lock service. |
| [setScreenLockAuthState](arkts-basicservices-screenlock-setscreenlockauthstate-f-sys.md#setscreenlockauthstate) | Set the screen lock authentication state for os account local userId. |
| [setScreenLockDisabled](arkts-basicservices-screenlock-setscreenlockdisabled-f-sys.md#setscreenlockdisabled) | Disable screen lock showing for os account local userId. This only becomes effective when there is no password. |
| [unlock](arkts-basicservices-screenlock-unlock-f-sys.md#unlock) | Unlock the screen. |
| [unlock](arkts-basicservices-screenlock-unlock-f-sys.md#unlock-1) | Unlock the screen. |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [SystemEvent](arkts-basicservices-screenlock-systemevent-i-sys.md) | Indicates the system event type and parameter related to the screenlock management service. |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [AuthState](arkts-basicservices-screenlock-authstate-e-sys.md) | Indicates the screen lock authentication state. |
| [StrongAuthReasonFlags](arkts-basicservices-screenlock-strongauthreasonflags-e-sys.md) | Indicates the strong authentication reason flags used to request. |
| [UnlockPolicy](arkts-basicservices-screenlock-unlockpolicy-e-sys.md) | Indicates the screen lock authentication policy used to unlock the screen. |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 | 说明 |
| --- | --- |
| [EventType](arkts-basicservices-screenlock-eventtype-t-sys.md) | Indicates the system event type related to the screen lock management service. Added unlockPolicyChanged. |
<!--DelEnd-->

