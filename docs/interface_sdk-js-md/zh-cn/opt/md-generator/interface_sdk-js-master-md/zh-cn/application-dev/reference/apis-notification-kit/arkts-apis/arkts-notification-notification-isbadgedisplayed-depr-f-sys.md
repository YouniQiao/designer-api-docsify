# isBadgeDisplayed（系统接口）

## isBadgeDisplayed

```TypeScript
function isBadgeDisplayed(bundle: BundleOption, callback: AsyncCallback<boolean>): void
```

获取指定应用的角标使能状态（Callback形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.notificationManager/notificationManager#isBadgeDisplayed

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function isBadgeDisplayed(bundle: BundleOption, callback: AsyncCallback<boolean>): void--><!--Device-notification-function isBadgeDisplayed(bundle: BundleOption, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isBadgeDisplayed

```TypeScript
function isBadgeDisplayed(bundle: BundleOption): Promise<boolean>
```

获取指定应用的角标使能状态（Promise形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** ohos.notificationManager/notificationManager#isBadgeDisplayed

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function isBadgeDisplayed(bundle: BundleOption): Promise<boolean>--><!--Device-notification-function isBadgeDisplayed(bundle: BundleOption): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |
