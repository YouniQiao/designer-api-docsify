# GroupInfo (System API)

组通知信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export interface GroupInfo--><!--Device-unnamed-export interface GroupInfo-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## groupTitle

```TypeScript
groupTitle?: string
```

通知成组后展示的组标题。当该通知是通知组中最新的一条通知时，该字段生效。默认为空。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GroupInfo-groupTitle?: string--><!--Device-GroupInfo-groupTitle?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## isGroupIcon

```TypeScript
isGroupIcon?: boolean
```

是否使用该通知[NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md)中的smallIcon字段作为通知成组后展示的组图标。当该通知是通知组中最新的一条通知，且开发者传入smallIcon时，是否使用smallIcon作为组图标。默认值为false。

- true：使用smallIcon作为组通知的图标。  
- false：不使用smallIcon作为组通知的图标。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GroupInfo-isGroupIcon?: boolean--><!--Device-GroupInfo-isGroupIcon?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

