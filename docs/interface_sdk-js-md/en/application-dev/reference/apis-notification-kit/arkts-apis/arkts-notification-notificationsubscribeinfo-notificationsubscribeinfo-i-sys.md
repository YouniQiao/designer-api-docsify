# NotificationSubscribeInfo (System API)

通知发布者的信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationSubscribeInfo--><!--Device-unnamed-export interface NotificationSubscribeInfo-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## bundleNames

```TypeScript
bundleNames?: Array<string>
```

应用Bundle名称。 不传递该参数时，默认订阅所有应用的通知。

**Type:** Array&lt;string&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSubscribeInfo-bundleNames?: Array<string>--><!--Device-NotificationSubscribeInfo-bundleNames?: Array<string>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## deviceType

```TypeScript
deviceType?: string
```

设备类型。不传递该参数时，默认订阅当前设备的通知。根据[设备信息](../../apis-basic-service-kit/arkts-apis/arkts-deviceinfo.md/arkts-deviceinfo.md)获取。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NotificationSubscribeInfo-deviceType?: string--><!--Device-NotificationSubscribeInfo-deviceType?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## enableClassification

```TypeScript
enableClassification?: boolean
```

是否启用通知分类。  
- true：表示启用。  
- false：表示禁用。默认值为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscribeInfo-enableClassification?: boolean--><!--Device-NotificationSubscribeInfo-enableClassification?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## filterLimit

```TypeScript
filterLimit?: long
```

通知过滤范围。默认值为0。取值范围包括：

- 0：不进行任何过滤，订阅全部通知。   
- 1：将渠道类型为[SOCIAL_COMMUNICATION](arkts-notification-notificationmanager-slottype-e.md)且  
[userInput](arkts-notification-notificationactionbutton-notificationactionbutton-i.md)为空的通知过滤掉。  
- 2：将渠道类型为[SOCIAL_COMMUNICATION](arkts-notification-notificationmanager-slottype-e.md)且  
[userInput](arkts-notification-notificationactionbutton-notificationactionbutton-i.md)不为空的通知过滤掉。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-NotificationSubscribeInfo-filterLimit?: long--><!--Device-NotificationSubscribeInfo-filterLimit?: long-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## needSilentReplayOnSubscribe

```TypeScript
needSilentReplayOnSubscribe?: boolean
```

是否启用订阅时的静默重放。  
- true：表示启用。  
- false：表示禁用。默认值为false。  
启用后，首次订阅时会以静默方式重新推送历史通知，不会出现响铃和振动提醒。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscribeInfo-needSilentReplayOnSubscribe?: boolean--><!--Device-NotificationSubscribeInfo-needSilentReplayOnSubscribe?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## pictureOptions

```TypeScript
pictureOptions?: PictureOptions
```

实况通知图片配置项。

**Type:** [PictureOptions](arkts-notification-notificationsubscribeinfo-pictureoptions-i-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscribeInfo-pictureOptions?: PictureOptions--><!--Device-NotificationSubscribeInfo-pictureOptions?: PictureOptions-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## slotTypes

```TypeScript
slotTypes?: Array<notificationManager.SlotType>
```

通知渠道类型。 不传递该参数时，默认订阅所有渠道类型的通知。

**Type:** Array&lt;notificationManager.SlotType&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-NotificationSubscribeInfo-slotTypes?: Array<notificationManager.SlotType>--><!--Device-NotificationSubscribeInfo-slotTypes?: Array<notificationManager.SlotType>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## userId

```TypeScript
userId?: int
```

用户ID。 不传递该参数时，默认订阅当前用户ID的通知。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSubscribeInfo-userId?: int--><!--Device-NotificationSubscribeInfo-userId?: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## voiceContentOptions

```TypeScript
voiceContentOptions?: VoiceContentOptions
```

通知语音播报配置项。

**Type:** [VoiceContentOptions](arkts-notification-notificationsubscribeinfo-voicecontentoptions-i-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscribeInfo-voiceContentOptions?: VoiceContentOptions--><!--Device-NotificationSubscribeInfo-voiceContentOptions?: VoiceContentOptions-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

