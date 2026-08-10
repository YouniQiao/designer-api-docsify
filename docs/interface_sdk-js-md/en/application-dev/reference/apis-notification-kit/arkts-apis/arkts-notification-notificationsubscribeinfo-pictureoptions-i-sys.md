# PictureOptions (System API)

实况通知图片配置项。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export interface PictureOptions--><!--Device-unnamed-export interface PictureOptions-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## preparseLiveViewPicList

```TypeScript
preparseLiveViewPicList?: string[]
```

订阅普通实况类型通知中  
[NotificationLiveViewContent](arkts-notification-notificationcontent-notificationliveviewcontent-i-sys.md)的extraInfo中的图片信息。入参为extraInfo中需要解析为pixelMap格式的图片文件名的Key。&lt;br&gt;当应用发布普通实况类型通知时，通过  
[onConsume](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md#onconsume)将解析后的图片信息回调给订阅者，解析后的图片信息存放于NotificationLiveViewContent的pictureInfo内。

**Type:** string[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PictureOptions-preparseLiveViewPicList?: string[]--><!--Device-PictureOptions-preparseLiveViewPicList?: string[]-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

