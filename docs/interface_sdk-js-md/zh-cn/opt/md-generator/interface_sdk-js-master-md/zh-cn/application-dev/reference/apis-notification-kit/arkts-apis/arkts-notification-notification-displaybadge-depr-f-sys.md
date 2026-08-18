# displayBadge（系统接口）

## 导入模块

```TypeScript
```

## displayBadge

```TypeScript
function displayBadge(bundle: BundleOption, enable: boolean, callback: AsyncCallback<void>): void
```

设定指定应用的角标使能状态（Callback形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [displayBadge](arkts-notification-notificationmanager-displaybadge-f-sys.md#displaybadge系统接口)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function displayBadge(bundle: BundleOption, enable: boolean, callback: AsyncCallback<void>): void--><!--Device-notification-function displayBadge(bundle: BundleOption, enable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| enable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## displayBadge

```TypeScript
function displayBadge(bundle: BundleOption, enable: boolean): Promise<void>
```

设定指定应用的角标使能状态（Promise形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [displayBadge](arkts-notification-notificationmanager-displaybadge-f-sys.md#displaybadge系统接口)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function displayBadge(bundle: BundleOption, enable: boolean): Promise<void>--><!--Device-notification-function displayBadge(bundle: BundleOption, enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
