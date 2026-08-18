# NotificationSubscribeInfo (System API)

The **NotificationSubscribeInfo** module provides APIs for defining the information about the publisher for notification subscription.

**Since:** 23

<!--Device-unnamed-export interface NotificationSubscribeInfo--><!--Device-unnamed-export interface NotificationSubscribeInfo-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## bundleNames

```TypeScript
bundleNames?: Array<string>
```

Bundle names of the applications whose notifications to subscribe to. If this parameter is not specified, the subscription defaults to notifications from all applications.

**Type:** Array&lt;string&gt;

**Since:** 23

<!--Device-NotificationSubscribeInfo-bundleNames?: Array<string>--><!--Device-NotificationSubscribeInfo-bundleNames?: Array<string>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## deviceType

```TypeScript
deviceType?: string
```

Device type. If this parameter is not specified, the subscription defaults to notifications from the current device. The value is obtained based on [device information](../../apis-na/arkts-apis/arkts-deviceinfo.md#ohosdeviceinfo).

**Type:** string

**Since:** 23

<!--Device-NotificationSubscribeInfo-deviceType?: string--><!--Device-NotificationSubscribeInfo-deviceType?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## enableClassification

```TypeScript
enableClassification?: boolean
```

Whether to enable notification classification. - **true**: yes. - **false**: no. The default value is **false**.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscribeInfo-enableClassification?: boolean--><!--Device-NotificationSubscribeInfo-enableClassification?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## filterLimit

```TypeScript
filterLimit?: long
```

Notification filtering range. The default value is **0**. The options are as follows: - **0**: All notifications are included in the subscription. - **1**: Filter out notifications whose slot type is [SOCIAL_COMMUNICATION](arkts-notification-notificationmanager-slottype-e.md#slottype) and [userInput](arkts-notification-notificationactionbutton-notificationactionbutton-i.md#notificationactionbutton) is empty. - **2**: Filter out notifications whose slot type is [SOCIAL_COMMUNICATION](arkts-notification-notificationmanager-slottype-e.md#slottype) and [userInput](arkts-notification-notificationactionbutton-notificationactionbutton-i.md#notificationactionbutton) is not empty.

**Type:** long

**Since:** 23

<!--Device-NotificationSubscribeInfo-filterLimit?: long--><!--Device-NotificationSubscribeInfo-filterLimit?: long-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## needSilentReplayOnSubscribe

```TypeScript
needSilentReplayOnSubscribe?: boolean
```

Whether to enable silent replay upon subscription. - **true**: yes. - **false**: no. The default value is **false**. After this feature is enabled, historical notifications are silently re-pushed upon the first subscription, without ringing or vibration reminders.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscribeInfo-needSilentReplayOnSubscribe?: boolean--><!--Device-NotificationSubscribeInfo-needSilentReplayOnSubscribe?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## pictureOptions

```TypeScript
pictureOptions?: PictureOptions
```

Image options of the live notification.

**Type:** [PictureOptions](arkts-notification-notificationsubscribeinfo-pictureoptions-i-sys.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscribeInfo-pictureOptions?: PictureOptions--><!--Device-NotificationSubscribeInfo-pictureOptions?: PictureOptions-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## slotTypes

```TypeScript
slotTypes?: Array<notificationManager.SlotType>
```

Types of the notification slots. If this parameter is not specified, the subscription defaults to notifications of all slot types.

**Type:** Array&lt;notificationManager.SlotType&gt;

**Since:** 23

<!--Device-NotificationSubscribeInfo-slotTypes?: Array<notificationManager.SlotType>--><!--Device-NotificationSubscribeInfo-slotTypes?: Array<notificationManager.SlotType>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## userId

```TypeScript
userId?: int
```

User ID. If this parameter is not specified, the subscription defaults to notifications from the current user ID.

**Type:** int

**Since:** 23

<!--Device-NotificationSubscribeInfo-userId?: int--><!--Device-NotificationSubscribeInfo-userId?: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## voiceContentOptions

```TypeScript
voiceContentOptions?: VoiceContentOptions
```

Configuration options for notification voice broadcast.

**Type:** [VoiceContentOptions](arkts-notification-notificationsubscribeinfo-voicecontentoptions-i-sys.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscribeInfo-voiceContentOptions?: VoiceContentOptions--><!--Device-NotificationSubscribeInfo-voiceContentOptions?: VoiceContentOptions-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

