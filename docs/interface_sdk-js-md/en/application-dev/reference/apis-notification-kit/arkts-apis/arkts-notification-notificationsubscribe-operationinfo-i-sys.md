# OperationInfo (System API)

跨设备协同操作信息。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-notificationSubscribe-export interface OperationInfo--><!--Device-notificationSubscribe-export interface OperationInfo-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { notificationSubscribe } from 'kits/@kit.NotificationKit';
```

## actionName

```TypeScript
actionName?: string
```

描述通知中显示的操作按钮（与通知  
[NotificationActionButton](arkts-notification-notificationactionbutton-notificationactionbutton-i.md)中title字段保持一致）。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-OperationInfo-actionName?: string--><!--Device-OperationInfo-actionName?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## buttonIndex

```TypeScript
buttonIndex?: int
```

用户点击的非实况通知按钮序号或实况通知辅助区序号。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-OperationInfo-buttonIndex?: int--><!--Device-OperationInfo-buttonIndex?: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## operationType

```TypeScript
operationType?: int
```

用户点击操作类型。

- 0：用户点击非实况通知本体。  
- 1：用户点击非实况通知按钮。  
- 32：用户点击实况通知本体。  
- 33：用户点击实况通知辅助区

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-OperationInfo-operationType?: int--><!--Device-OperationInfo-operationType?: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## userInput

```TypeScript
userInput?: string
```

用户输入（用于通知跨设备快捷回复场景传递用户输入，与通知  
[NotificationUserInput](arkts-notification-notificationuserinput-notificationuserinput-i.md)中inputKey字段保持一致）。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-OperationInfo-userInput?: string--><!--Device-OperationInfo-userInput?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

