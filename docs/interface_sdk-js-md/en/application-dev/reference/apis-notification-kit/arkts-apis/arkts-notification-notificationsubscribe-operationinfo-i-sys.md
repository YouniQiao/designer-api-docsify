# OperationInfo (System API)

Defines cross-device collaborative operation information.

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

Operation button displayed in the notification. The value must be the same as that of **title** in   
[NotificationActionButton](arkts-notification-notificationactionbutton-notificationactionbutton-i.md).

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

Index of the non-live view button or live view auxiliary area that the user taps.

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

Operation type.

- **0**: The user taps the non-live view.  
- **1**: The user taps the non-live view button.  
- **32**: The user taps the live view.  
- **33**: The user taps the live view auxiliary area.

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

User input, used to apply quick reply across devices. The value must be the same as that of **inputKey** in   
[NotificationUserInput](arkts-notification-notificationuserinput-notificationuserinput-i.md).

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-OperationInfo-userInput?: string--><!--Device-OperationInfo-userInput?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

