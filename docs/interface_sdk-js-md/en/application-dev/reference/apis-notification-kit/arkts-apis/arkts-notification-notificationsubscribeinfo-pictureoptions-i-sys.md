# PictureOptions (System API)

Describes the image options of the live notification.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export interface PictureOptions--><!--Device-unnamed-export interface PictureOptions-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## preparseLiveViewPicList

```TypeScript
preparseLiveViewPicList?: string[]
```

Subscribes to the image information in **extraInfo** of [NotificationLiveViewContent](arkts-notification-notificationcontent-notificationliveviewcontent-i-sys.md#NotificationLiveViewContent-(System-API)) in a common live notification. The input parameter is the **Key** of the image file name that needs to be parsed into the pixelMap format in **extraInfo**.&lt;br&gt;When the application publishes a common live notification, the parsed image information is called back to the subscriber through [onConsume](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md#onConsume) and stored in **pictureInfo** of **NotificationLiveViewContent**.

**Type:** string[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PictureOptions-preparseLiveViewPicList?: string[]--><!--Device-PictureOptions-preparseLiveViewPicList?: string[]-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

