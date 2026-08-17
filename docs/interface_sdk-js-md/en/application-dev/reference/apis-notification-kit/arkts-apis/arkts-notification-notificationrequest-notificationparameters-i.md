# NotificationParameters

Describes part of the **wantAgent** information in NotificationRequest.

**Since:** 24

<!--Device-unnamed-export interface NotificationParameters--><!--Device-unnamed-export interface NotificationParameters-End-->

**System capability:** SystemCapability.Notification.Notification

## wantAction

```TypeScript
wantAction?:string
```

**action** field passed in **want** when **wantAgent** is created. For details, see [action](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md#want).

**Type:** string

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationParameters-wantAction?:string--><!--Device-NotificationParameters-wantAction?:string-End-->

**System capability:** SystemCapability.Notification.Notification

## wantParameters

```TypeScript
wantParameters?:Record<string, RecordData>
```

**parameters** field passed in **want** when **wantAgent** is created. For details, see [parameters](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md#want).

**Type:** Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationParameters-wantParameters?:Record<string, RecordData>--><!--Device-NotificationParameters-wantParameters?:Record<string, RecordData>-End-->

**System capability:** SystemCapability.Notification.Notification

## wantUri

```TypeScript
wantUri?:string
```

**uri** field passed in **want** when **wantAgent** is created. For details, see [uri](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md#want).

**Type:** string

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationParameters-wantUri?:string--><!--Device-NotificationParameters-wantUri?:string-End-->

**System capability:** SystemCapability.Notification.Notification

