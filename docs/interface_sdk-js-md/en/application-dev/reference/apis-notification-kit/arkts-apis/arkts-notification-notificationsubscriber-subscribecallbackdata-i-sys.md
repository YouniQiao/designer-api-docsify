# SubscribeCallbackData (System API)

返回携带系统属性值的通知信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface SubscribeCallbackData--><!--Device-unnamed-export interface SubscribeCallbackData-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## notificationClassification

```TypeScript
readonly notificationClassification?: NotificationClassification
```

通知分类信息。仅在[NotificationSubscribeInfo](arkts-notification-notificationsubscribeinfo-notificationsubscribeinfo-i-sys.md)中的enableClassification为true时存在。

**Type:** [NotificationClassification](arkts-notification-notificationsubscriber-notificationclassification-i-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubscribeCallbackData-readonly notificationClassification?: NotificationClassification--><!--Device-SubscribeCallbackData-readonly notificationClassification?: NotificationClassification-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## reason

```TypeScript
readonly reason?: int
```

删除原因（1:点击通知后删除通知，2:用户删除通知） 。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-SubscribeCallbackData-readonly reason?: int--><!--Device-SubscribeCallbackData-readonly reason?: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## request

```TypeScript
readonly request: NotificationRequest
```

通知内容。

**Type:** [NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i-sys.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-SubscribeCallbackData-readonly request: NotificationRequest--><!--Device-SubscribeCallbackData-readonly request: NotificationRequest-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## sortingMap

```TypeScript
readonly sortingMap?: NotificationSortingMap
```

通知排序信息。

**Type:** [NotificationSortingMap](arkts-notification-notificationsortingmap-notificationsortingmap-i-sys.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-SubscribeCallbackData-readonly sortingMap?: NotificationSortingMap--><!--Device-SubscribeCallbackData-readonly sortingMap?: NotificationSortingMap-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## sound

```TypeScript
readonly sound?: string
```

通知声音。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-SubscribeCallbackData-readonly sound?: string--><!--Device-SubscribeCallbackData-readonly sound?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## vibrationValues

```TypeScript
readonly vibrationValues?: Array<long>
```

通知振动。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;long&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-SubscribeCallbackData-readonly vibrationValues?: Array<long>--><!--Device-SubscribeCallbackData-readonly vibrationValues?: Array<long>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## voiceContent

```TypeScript
voiceContent?: VoiceContent
```

通知语音播报内容。

**Type:** [VoiceContent](arkts-notification-notificationsubscriber-voicecontent-i-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubscribeCallbackData-voiceContent?: VoiceContent--><!--Device-SubscribeCallbackData-voiceContent?: VoiceContent-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

