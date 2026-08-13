# enableDistributedByBundle（系统接口）

## enableDistributedByBundle

```TypeScript
function enableDistributedByBundle(bundle: BundleOption, enable: boolean, callback: AsyncCallback<void>): void
```

设置指定应用是否支持分布式通知（Callback形式）。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setDistributedEnableByBundle](arkts-notification-notificationmanager-setdistributedenablebybundle-f-sys.md#setDistributedEnableByBundle（系统接口）)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function enableDistributedByBundle(bundle: BundleOption, enable: boolean, callback: AsyncCallback<void>): void--><!--Device-notification-function enableDistributedByBundle(bundle: BundleOption, enable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| enable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## enableDistributedByBundle

```TypeScript
function enableDistributedByBundle(bundle: BundleOption, enable: boolean): Promise<void>
```

设置指定应用是否支持分布式通知（Promise形式）。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setDistributedEnableByBundle](arkts-notification-notificationmanager-setdistributedenablebybundle-f-sys.md#setDistributedEnableByBundle（系统接口）)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function enableDistributedByBundle(bundle: BundleOption, enable: boolean): Promise<void>--><!--Device-notification-function enableDistributedByBundle(bundle: BundleOption, enable: boolean): Promise<void>-End-->

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
