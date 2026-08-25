# NotificationSubscriber（系统接口）

提供订阅者接收到新通知、取消通知等的回调方法。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

## onBadgeChanged

```TypeScript
onBadgeChanged?:(data: BadgeNumberCallbackData) => void
```

回调返回监听到的应用角标数量变化。

**起始版本：** 10

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [BadgeNumberCallbackData](arkts-notification-notificationsubscriber-badgenumbercallbackdata-i-sys.md) | 是 |

## onBatchCancel

```TypeScript
onBatchCancel?: (data: Array<SubscribeCallbackData>) => void
```

批量删除的通知信息。

**起始版本：** 11

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Array&lt;[SubscribeCallbackData](arkts-notification-notificationsubscriber-subscribecallbackdata-i-sys.md)&gt; | 是 |

## onCancel

```TypeScript
onCancel?:(data: SubscribeCallbackData) => void
```

需要取消的通知信息。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [SubscribeCallbackData](arkts-notification-notificationsubscriber-subscribecallbackdata-i-sys.md) | 是 |

## onConnect

```TypeScript
onConnect?:() => void
```

订阅完成的回调。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

## onConsume

```TypeScript
onConsume?:(data: SubscribeCallbackData) => void
```

新接收到的通知信息。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [SubscribeCallbackData](arkts-notification-notificationsubscriber-subscribecallbackdata-i-sys.md) | 是 |

## onDestroy

```TypeScript
onDestroy?:() => void
```

服务失联的回调。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

## onDisconnect

```TypeScript
onDisconnect?:() => void
```

取消订阅的回调。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

## onDoNotDisturbChanged

```TypeScript
onDoNotDisturbChanged?: (mode: notificationManager.DoNotDisturbDate) => void
```

回调返回免打扰时间选项变更。

**起始版本：** 11

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | notificationManager.DoNotDisturbDate | 是 |

## onDoNotDisturbDateChange

```TypeScript
onDoNotDisturbDateChange?: (mode: notification.DoNotDisturbDate) => void
```

回调返回免打扰时间选项变更。

**起始版本：** 8

**废弃版本：** 11

**替代接口：** [onDoNotDisturbChanged](#ondonotdisturbchanged)

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | notification.DoNotDisturbDate | 是 |

## onEnabledNotificationChanged

```TypeScript
onEnabledNotificationChanged?:(callbackData: EnabledNotificationCallbackData) => void
```

回调返回监听到的应用信息。

**起始版本：** 8

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackData | [EnabledNotificationCallbackData](arkts-notification-notificationsubscriber-enablednotificationcallbackdata-i-sys.md) | 是 |

## onEnabledPriorityByBundleChanged

```TypeScript
onEnabledPriorityByBundleChanged?: (callbackData: EnabledPriorityNotificationByBundleCallbackData) => void
```

返回应用通知优先级开关状态。

**起始版本：** 23

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackData | [EnabledPriorityNotificationByBundleCallbackData](arkts-notification-notificationsubscriber-enabledprioritynotificationbybundlecallbackdata-i-sys.md) | 是 |

## onEnabledPriorityChanged

```TypeScript
onEnabledPriorityChanged?: (callbackData: EnabledPriorityNotificationCallbackData) => void
```

返回通知优先级总开关状态。

**起始版本：** 23

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callbackData | [EnabledPriorityNotificationCallbackData](arkts-notification-notificationsubscriber-enabledprioritynotificationcallbackdata-i-sys.md) | 是 |

## onEnabledSilentReminderChanged

```TypeScript
onEnabledSilentReminderChanged?: EnabledSilentReminderChangedCallback
```

返回应用通知静默提醒的使能状态变化。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

## onNotificationSwitchChanged

```TypeScript
onNotificationSwitchChanged?: NotificationSwitchChangedCallback
```

返回由[notificationManager.setNotificationSwitch]{@link../@ohos.notificationManager:notificationManager.setNotificationSwitch}接口设置的通知开关状态变化。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

## onSystemUpdate

```TypeScript
onSystemUpdate?: SystemUpdateCallback
```

返回携带系统属性值的通知信息。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

## onUpdate

```TypeScript
onUpdate?:(data: NotificationSortingMap) => void
```

最新的通知排序列表。

**起始版本：** 7

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | [NotificationSortingMap](arkts-notification-notificationsortingmap-notificationsortingmap-i-sys.md) | 是 |

## onBadgeEnabledChanged

```TypeScript
onBadgeEnabledChanged?: BadgeEnabledChangedCallback
```

返回应用角标的使能状态变化。

**类型：** [BadgeEnabledChangedCallback](arkts-notification-notificationsubscriber-badgeenabledchangedcallback-i-sys.md)

**起始版本：** 12

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。
