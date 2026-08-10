# EnabledSilentReminderCallbackData (System API)

应用通知静默提醒开关状态的回调函数类型。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-unnamed-export interface EnabledSilentReminderCallbackData--><!--Device-unnamed-export interface EnabledSilentReminderCallbackData-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## bundle

```TypeScript
readonly bundle: string
```

应用的包名。

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EnabledSilentReminderCallbackData-readonly bundle: string--><!--Device-EnabledSilentReminderCallbackData-readonly bundle: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## enableStatus

```TypeScript
readonly enableStatus: notificationManager.SwitchState
```

应用通知的静默提醒开关状态。  
- USER_MODIFIED_OFF：用户设置的关闭状态。  
- USER_MODIFIED_ON：用户设置的开启状态。  
- SYSTEM_DEFAULT_OFF：用户设置前的初始关闭状态。  
- SYSTEM_DEFAULT_ON：用户设置前的初始开启状态。

**Type:** notificationManager.SwitchState

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EnabledSilentReminderCallbackData-readonly enableStatus: notificationManager.SwitchState--><!--Device-EnabledSilentReminderCallbackData-readonly enableStatus: notificationManager.SwitchState-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## uid

```TypeScript
readonly uid: int
```

应用的uid。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EnabledSilentReminderCallbackData-readonly uid: int--><!--Device-EnabledSilentReminderCallbackData-readonly uid: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

