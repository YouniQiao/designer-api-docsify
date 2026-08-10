# ComfortReminderData（系统接口）

Defines comfort reminder data.

**继承/实现关系：** ComfortReminderData extends [UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-userStatus-export interface ComfortReminderData extends UserStatusData--><!--Device-userStatus-export interface ComfortReminderData extends UserStatusData-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { userStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## eventType

```TypeScript
eventType: int
```

Event type.The value ranges from 0 to 1. 0: Gaze event, 1: Ambient sound event..

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComfortReminderData-eventType: int--><!--Device-ComfortReminderData-eventType: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## fusionReminderData

```TypeScript
fusionReminderData: ReminderLevel
```

Fusion reminder data.

**类型：** [ReminderLevel](arkts-multimodalawareness-userstatus-reminderlevel-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComfortReminderData-fusionReminderData: ReminderLevel--><!--Device-ComfortReminderData-fusionReminderData: ReminderLevel-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## swingReminderData

```TypeScript
swingReminderData: ReminderLevel
```

Swing reminder data.

**类型：** [ReminderLevel](arkts-multimodalawareness-userstatus-reminderlevel-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComfortReminderData-swingReminderData: ReminderLevel--><!--Device-ComfortReminderData-swingReminderData: ReminderLevel-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

