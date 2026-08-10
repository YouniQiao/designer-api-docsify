# NotificationSwitchChangedCallbackData (System API)

通知开关状态变化的回调函数类型。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export interface NotificationSwitchChangedCallbackData--><!--Device-unnamed-export interface NotificationSwitchChangedCallbackData-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## enableStatus

```TypeScript
readonly enableStatus: notificationManager.SwitchState
```

通知开关状态。

**Type:** notificationManager.SwitchState

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSwitchChangedCallbackData-readonly enableStatus: notificationManager.SwitchState--><!--Device-NotificationSwitchChangedCallbackData-readonly enableStatus: notificationManager.SwitchState-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## switchName

```TypeScript
readonly switchName: string
```

通知开关名称。取值为：DEAL（交易类通知聚合开关）、LOGISTICS（物流类通知聚合开关）。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSwitchChangedCallbackData-readonly switchName: string--><!--Device-NotificationSwitchChangedCallbackData-readonly switchName: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## userId

```TypeScript
readonly userId: int
```

用户ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSwitchChangedCallbackData-readonly userId: int--><!--Device-NotificationSwitchChangedCallbackData-readonly userId: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

