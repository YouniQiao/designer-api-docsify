# NotificationFilter (System API)

描述查询普通实况窗时的筛选条件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationFilter--><!--Device-unnamed-export interface NotificationFilter-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## bundle

```TypeScript
bundle: BundleOption
```

实况通知的包信息。

**Type:** [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationFilter-bundle: BundleOption--><!--Device-NotificationFilter-bundle: BundleOption-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## extraInfoKeys

```TypeScript
extraInfoKeys?: Array<string>
```

筛选附加信息的键值列表。不填表示查询所有的附加信息。

**Type:** Array&lt;string&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationFilter-extraInfoKeys?: Array<string>--><!--Device-NotificationFilter-extraInfoKeys?: Array<string>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## notificationKey

```TypeScript
notificationKey: notificationSubscribe.NotificationKey
```

通知信息，包含通知ID和通知标签。

**Type:** notificationSubscribe.NotificationKey

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationFilter-notificationKey: notificationSubscribe.NotificationKey--><!--Device-NotificationFilter-notificationKey: notificationSubscribe.NotificationKey-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

