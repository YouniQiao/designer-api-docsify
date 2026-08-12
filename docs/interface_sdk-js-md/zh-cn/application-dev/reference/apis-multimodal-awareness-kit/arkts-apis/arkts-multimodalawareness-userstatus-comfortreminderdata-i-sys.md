# ComfortReminderData（系统接口）

舒适提醒数据。

**继承/实现关系：** ComfortReminderData extends [UserStatusData](arkts-multimodalawareness-userstatus-userstatusdata-i-sys.md#UserStatusData)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-userStatus-export interface ComfortReminderData extends UserStatusData--><!--Device-userStatus-export interface ComfortReminderData extends UserStatusData-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

## eventType

```TypeScript
eventType: int
```

事件类型。取值范围为0到1。0：注视事件，1：环境声音事件。

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

融合提醒数据。

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

摆动提醒数据。

**类型：** [ReminderLevel](arkts-multimodalawareness-userstatus-reminderlevel-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ComfortReminderData-swingReminderData: ReminderLevel--><!--Device-ComfortReminderData-swingReminderData: ReminderLevel-End-->

**系统能力：** SystemCapability.MultimodalAwareness.UserStatus

**系统接口：** 此接口为系统接口。

