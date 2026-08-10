# NotificationParameters

描述[NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md)中wantAgent的部分信息。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-unnamed-export interface NotificationParameters--><!--Device-unnamed-export interface NotificationParameters-End-->

**System capability:** SystemCapability.Notification.Notification

## wantAction

```TypeScript
wantAction?:string
```

应用在创建wantAgent时，传入的want的action字段，具体含义请参考[action](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md/arkts-ability-app-ability-want-want-c.md)。

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationParameters-wantAction?:string--><!--Device-NotificationParameters-wantAction?:string-End-->

**System capability:** SystemCapability.Notification.Notification

## wantParameters

```TypeScript
wantParameters?:Record<string, Object>
```

应用在创建wantAgent时，传入的want的parameters字段，具体含义请参考[parameters](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md/arkts-ability-app-ability-want-want-c.md)。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationParameters-wantParameters?:Record<string, Object>--><!--Device-NotificationParameters-wantParameters?:Record<string, Object>-End-->

**System capability:** SystemCapability.Notification.Notification

## wantUri

```TypeScript
wantUri?:string
```

应用在创建wantAgent时，传入的want的uri字段，具体含义请参考[uri](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md/arkts-ability-app-ability-want-want-c.md)。

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationParameters-wantUri?:string--><!--Device-NotificationParameters-wantUri?:string-End-->

**System capability:** SystemCapability.Notification.Notification

