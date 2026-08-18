# isNotificationEnabled（系统接口）

## 导入模块

```TypeScript
```

## isNotificationEnabled

```TypeScript
function isNotificationEnabled(bundle: BundleOption, callback: AsyncCallback<boolean>): void
```

获取指定应用的通知使能状态（Callback形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled系统接口)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function isNotificationEnabled(bundle: BundleOption, callback: AsyncCallback<boolean>): void--><!--Device-notification-function isNotificationEnabled(bundle: BundleOption, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(bundle: BundleOption): Promise<boolean>
```

获取指定应用的通知使能状态（Promise形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled系统接口)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function isNotificationEnabled(bundle: BundleOption): Promise<boolean>--><!--Device-notification-function isNotificationEnabled(bundle: BundleOption): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(callback: AsyncCallback<boolean>): void
```

获取通知使能状态（Callback形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled系统接口)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function isNotificationEnabled(callback: AsyncCallback<boolean>): void--><!--Device-notification-function isNotificationEnabled(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(): Promise<boolean>
```

获取通知使能状态（Promise形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled系统接口)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function isNotificationEnabled(): Promise<boolean>--><!--Device-notification-function isNotificationEnabled(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(userId: number, callback: AsyncCallback<boolean>): void
```

获取指定用户ID下的通知使能状态。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled系统接口)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function isNotificationEnabled(userId: number, callback: AsyncCallback<boolean>): void--><!--Device-notification-function isNotificationEnabled(userId: number, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(userId: number): Promise<boolean>
```

获取指定用户下的通知使能状态。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled系统接口)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function isNotificationEnabled(userId: number): Promise<boolean>--><!--Device-notification-function isNotificationEnabled(userId: number): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
