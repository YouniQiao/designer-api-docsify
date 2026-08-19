# NotificationLongTextContent

Describes the long text notification. This API is inherited from NotificationBasicContent. &gt; **NOTE：**&gt; &gt; - When this notification type forms a group notification with other notifications, its display effect defaults &gt; to the collapsed state, and the displayed title and body are the **title** and **text** inherited from &gt; NotificationBasicContent. When this notification type is displayed alone and does not form a group notification &gt; with other notifications, its display effect defaults to the expanded state, where the displayed title is the &gt; expanded title **expandedTitle**, and the displayed body content is the long text **longText**. &gt; &gt; - When a user taps a group notification to view the notification details, the display effect of this &gt; notification changes to the expanded state. &gt; &gt; - The actual display effect depends on the device capabilities and the notification center UI style.

**Inheritance/Implementation:** NotificationLongTextContent extends [NotificationBasicContent](arkts-notification-notificationcontent-notificationbasiccontent-i.md)

**Since:** 23

<!--Device-unnamed-export interface NotificationLongTextContent--><!--Device-unnamed-export interface NotificationLongTextContent-End-->

**System capability:** SystemCapability.Notification.Notification

## briefText

```TypeScript
briefText: string
```

Notification summary content, which is a summary of the notification content and is not displayed in the notification center. It cannot be an empty string. The size does not exceed 1024 bytes, and the excess part will be truncated.

**Type:** string

**Since:** 23

<!--Device-NotificationLongTextContent-briefText: string--><!--Device-NotificationLongTextContent-briefText: string-End-->

**System capability:** SystemCapability.Notification.Notification

## expandedTitle

```TypeScript
expandedTitle: string
```

Title when the notification is expanded. It cannot be an empty string. The size does not exceed 1024 bytes, and the excess part will be truncated.

**Type:** string

**Since:** 23

<!--Device-NotificationLongTextContent-expandedTitle: string--><!--Device-NotificationLongTextContent-expandedTitle: string-End-->

**System capability:** SystemCapability.Notification.Notification

## longText

```TypeScript
longText: string
```

Full long text content displayed after the notification is expanded. It cannot be an empty string. The size does not exceed 3072 bytes, and the excess part will be truncated.

**Type:** string

**Since:** 23

<!--Device-NotificationLongTextContent-longText: string--><!--Device-NotificationLongTextContent-longText: string-End-->

**System capability:** SystemCapability.Notification.Notification

