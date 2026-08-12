# getSlotNumByBundle（系统接口）

## getSlotNumByBundle

```TypeScript
function getSlotNumByBundle(bundle: BundleOption, callback: AsyncCallback<number>): void
```

获取指定应用的通知通道数量（Callback形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getSlotNumByBundle](ohos.notificationManager/notificationManager#getSlotNumByBundle)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getSlotNumByBundle(bundle: BundleOption, callback: AsyncCallback<number>): void--><!--Device-notification-function getSlotNumByBundle(bundle: BundleOption, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## getSlotNumByBundle

```TypeScript
function getSlotNumByBundle(bundle: BundleOption): Promise<number>
```

获取指定应用的通知通道数量（Promise形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getSlotNumByBundle](ohos.notificationManager/notificationManager#getSlotNumByBundle)

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getSlotNumByBundle(bundle: BundleOption): Promise<number>--><!--Device-notification-function getSlotNumByBundle(bundle: BundleOption): Promise<number>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
