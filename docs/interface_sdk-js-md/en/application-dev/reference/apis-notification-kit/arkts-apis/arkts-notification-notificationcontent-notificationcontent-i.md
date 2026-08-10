# NotificationContent

通知内容。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationContent--><!--Device-unnamed-export interface NotificationContent-End-->

**System capability:** SystemCapability.Notification.Notification

## contentType

```TypeScript
contentType?: notification.ContentType
```

通知内容类型。

**Type:** notification.ContentType

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

**Substitutes:** [NotificationContent#notificationContentType](arkts-notification-notificationcontent-notificationcontent-i.md#notificationcontenttype)

<!--Device-NotificationContent-contentType?: notification.ContentType--><!--Device-NotificationContent-contentType?: notification.ContentType-End-->

**System capability:** SystemCapability.Notification.Notification

## longText

```TypeScript
longText?: NotificationLongTextContent
```

长文本类型通知内容。当notificationContentType为NOTIFICATION_CONTENT_LONG_TEXT时使用，通知展开后可展示完整长文本内容。

**Type:** [NotificationLongTextContent](arkts-notification-notificationmanager-notificationlongtextcontent-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationContent-longText?: NotificationLongTextContent--><!--Device-NotificationContent-longText?: NotificationLongTextContent-End-->

**System capability:** SystemCapability.Notification.Notification

## multiLine

```TypeScript
multiLine?: NotificationMultiLineContent
```

多行类型通知内容。当notificationContentType为NOTIFICATION_CONTENT_MULTILINE时使用，通知展开后以多行列表样式展示。

**Type:** [NotificationMultiLineContent](arkts-notification-notificationcontent-notificationmultilinecontent-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationContent-multiLine?: NotificationMultiLineContent--><!--Device-NotificationContent-multiLine?: NotificationMultiLineContent-End-->

**System capability:** SystemCapability.Notification.Notification

## normal

```TypeScript
normal?: NotificationBasicContent
```

基本类型通知内容。当notificationContentType为NOTIFICATION_CONTENT_BASIC_TEXT时使用，通知以普通文本样式展示标题和正文。

**Type:** [NotificationBasicContent](arkts-notification-notificationmanager-notificationbasiccontent-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationContent-normal?: NotificationBasicContent--><!--Device-NotificationContent-normal?: NotificationBasicContent-End-->

**System capability:** SystemCapability.Notification.Notification

## notificationContentType

```TypeScript
notificationContentType?: notificationManager.ContentType
```

通知内容类型，用于指定通知的内容布局类型，决定了通知在通知中心中的展示样式。需与对应类型的通知内容对象配合使用，例如设置为NOTIFICATION_CONTENT_BASIC_TEXT时需同时填充normal字段。

**Type:** notificationManager.ContentType

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationContent-notificationContentType?: notificationManager.ContentType--><!--Device-NotificationContent-notificationContentType?: notificationManager.ContentType-End-->

**System capability:** SystemCapability.Notification.Notification

## picture

```TypeScript
picture?: NotificationPictureContent
```

图片类型通知内容。当notificationContentType为NOTIFICATION_CONTENT_PICTURE时使用。通知展开后可展示图片。

**Type:** [NotificationPictureContent](arkts-notification-notificationcontent-notificationpicturecontent-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationContent-picture?: NotificationPictureContent--><!--Device-NotificationContent-picture?: NotificationPictureContent-End-->

**System capability:** SystemCapability.Notification.Notification

## systemLiveView

```TypeScript
systemLiveView?: NotificationSystemLiveViewContent
```

系统实况窗类型通知内容。不支持三方应用直接创建该类型通知，可以由系统代理创建系统实况窗类型通知后，三方应用发布同ID的通知来更新指定内容。

**Type:** [NotificationSystemLiveViewContent](arkts-notification-notificationcontent-notificationsystemliveviewcontent-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationContent-systemLiveView?: NotificationSystemLiveViewContent--><!--Device-NotificationContent-systemLiveView?: NotificationSystemLiveViewContent-End-->

**System capability:** SystemCapability.Notification.Notification

