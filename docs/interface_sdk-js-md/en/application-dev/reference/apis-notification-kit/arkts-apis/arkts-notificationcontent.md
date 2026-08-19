# notificationContent

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [NotificationBasicContent](arkts-notification-notificationcontent-notificationbasiccontent-i.md) | Describes the basic text notification, which is used to display the title and body content. It serves as the basic content structure for other notification types. Other notification types (such as long text, multi-line text, picture, and live view) inherit this API and extend their own specific fields on this basis. |
| [NotificationButton](arkts-notification-notificationcontent-notificationbutton-i.md) | Describes the notification button, which is used to display an interactive button in the live view. &gt; **NOTE：**&gt; &gt; The actual display effect depends on the device capabilities and the notification center UI style. |
| [NotificationCapsule](arkts-notification-notificationcontent-notificationcapsule-i.md) | Describes the notification capsule, which is used to display the capsule form in the live view. &gt; **NOTE：**&gt; &gt; The actual display effect depends on the device capabilities and the notification center UI style. |
| [NotificationContent](arkts-notification-notificationcontent-notificationcontent-i.md) | Describes the notification contents. |
| [NotificationLongTextContent](arkts-notification-notificationcontent-notificationlongtextcontent-i.md) | Describes the long text notification. This API is inherited from NotificationBasicContent. &gt; **NOTE：**&gt; &gt; - When this notification type forms a group notification with other notifications, its display effect defaults &gt; to the collapsed state, and the displayed title and body are the **title** and **text** inherited from &gt; NotificationBasicContent. When this notification type is displayed alone and does not form a group notification &gt; with other notifications, its display effect defaults to the expanded state, where the displayed title is the &gt; expanded title **expandedTitle**, and the displayed body content is the long text **longText**. &gt; &gt; - When a user taps a group notification to view the notification details, the display effect of this &gt; notification changes to the expanded state. &gt; &gt; - The actual display effect depends on the device capabilities and the notification center UI style. |
| [NotificationMultiLineContent](arkts-notification-notificationcontent-notificationmultilinecontent-i.md) | Describes the multi-line text notification. This API is inherited from NotificationBasicContent. &gt; **NOTE：**&gt; &gt; - When this notification type forms a group notification with other notifications, its display effect defaults &gt; to the collapsed state, and the displayed title and body are the **title** and **text** inherited from &gt; NotificationBasicContent. When this notification type is displayed alone and does not form a group notification &gt; with other notifications, its display effect defaults to the expanded state, where the displayed title is the &gt; expanded title **longTitle**, and the multi-line text content **lines** is displayed as the body. &gt; &gt; - When a user taps a group notification to view the notification details, the display effect of this &gt; notification changes to the expanded state. &gt; &gt; - The actual display effect depends on the device capabilities and the notification center UI style. |
| [NotificationPictureContent](arkts-notification-notificationcontent-notificationpicturecontent-i.md) | Describes the picture-attached notification. This API is inherited from NotificationBasicContent. &gt; **NOTE：**&gt; &gt; - When this notification type forms a group notification with other notifications, its display effect defaults &gt; to the collapsed state, and the displayed title and body are the **title** and **text** inherited from &gt; NotificationBasicContent. When this notification type is displayed alone and does not form a group notification &gt; with other notifications, its display effect defaults to the expanded state, where the displayed title is the &gt; expanded title **expandedTitle**, and the displayed body is the **text** inherited from &gt; NotificationBasicContent and the picture content **picture** of this type. &gt; &gt; - When a user taps a group notification to view the notification details, the display effect of this &gt; notification changes to the expanded state. &gt; &gt; - The actual display effect depends on the device capabilities and the notification center UI style. |
| [NotificationProgress](arkts-notification-notificationcontent-notificationprogress-i.md) | Describes the notification progress, which is used to display progress bar information in the live view. &gt; **NOTE：**&gt; &gt; The actual display effect depends on the device capabilities and the notification center UI style. |
| [NotificationSystemLiveViewContent](arkts-notification-notificationcontent-notificationsystemliveviewcontent-i.md) | Describes the system live view notification content, which is used to display real-time status information in the live view. Third-party applications are not supported to directly create this notification type. After the system proxy creates a system live view notification, a third-party application can publish a notification with the same ID to update the specified content. This API is inherited from NotificationBasicContent. &gt; **NOTE：**&gt; &gt; The actual display effect depends on the device capabilities and the notification center UI style. |
| [NotificationTime](arkts-notification-notificationcontent-notificationtime-i.md) | Describes the notification timing information. &gt; **NOTE：**&gt; &gt; The actual display effect depends on the device capabilities and the notification center UI style. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [NotificationBasicContent](arkts-notification-notificationcontent-notificationbasiccontent-i-sys.md) | Describes the basic text notification, which is used to display the title and body content. It serves as the basic content structure for other notification types. Other notification types (such as long text, multi-line text, picture, and live view) inherit this API and extend their own specific fields on this basis. |
| [NotificationCapsule](arkts-notification-notificationcontent-notificationcapsule-i-sys.md) | Describes the notification capsule, which is used to display the capsule form in the live view. &gt; **NOTE：**&gt; &gt; The actual display effect depends on the device capabilities and the notification center UI style. |
| [NotificationContent](arkts-notification-notificationcontent-notificationcontent-i-sys.md) | Describes the notification contents. |
| [NotificationIconButton](arkts-notification-notificationcontent-notificationiconbutton-i-sys.md) | Describes the system notification button. |
| [NotificationLiveViewContent](arkts-notification-notificationcontent-notificationliveviewcontent-i-sys.md) | Describes the normal live notification content. This API inherits from NotificationBasicContent. |
| [NotificationMultiLineContent](arkts-notification-notificationcontent-notificationmultilinecontent-i-sys.md) | Describes the multi-line text notification. This API is inherited from NotificationBasicContent. &gt; **NOTE：**&gt; &gt; - When this notification type forms a group notification with other notifications, its display effect defaults &gt; to the collapsed state, and the displayed title and body are the **title** and **text** inherited from &gt; NotificationBasicContent. When this notification type is displayed alone and does not form a group notification &gt; with other notifications, its display effect defaults to the expanded state, where the displayed title is the &gt; expanded title **longTitle**, and the multi-line text content **lines** is displayed as the body. &gt; &gt; - When a user taps a group notification to view the notification details, the display effect of this &gt; notification changes to the expanded state. &gt; &gt; - The actual display effect depends on the device capabilities and the notification center UI style. |
| [NotificationSystemLiveViewContent](arkts-notification-notificationcontent-notificationsystemliveviewcontent-i-sys.md) | Describes the system live view notification content, which is used to display real-time status information in the live view. Third-party applications are not supported to directly create this notification type. After the system proxy creates a system live view notification, a third-party application can publish a notification with the same ID to update the specified content. This API is inherited from NotificationBasicContent. &gt; **NOTE：**&gt; &gt; The actual display effect depends on the device capabilities and the notification center UI style. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [LiveViewStatus](arkts-notification-notificationcontent-liveviewstatus-e-sys.md) | Enumerates the statuses of the common live view. |
| [LiveViewTypes](arkts-notification-notificationcontent-liveviewtypes-e-sys.md) | Enumerates live view types. |
<!--DelEnd-->

<!--Del-->
### Types(System API)

| Name | Description |
| --- | --- |
| [IconType](arkts-notification-icontype-t-sys.md) | Describes the icon types. |
<!--DelEnd-->

