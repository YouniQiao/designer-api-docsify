# isNotificationSlotEnabledByBundles（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## isNotificationSlotEnabledByBundles

```TypeScript
function isNotificationSlotEnabledByBundles(bundles: Array<BundleOption>, type: SlotType): Promise<Map<BundleOption, boolean>>
```

批量获取多个应用的指定渠道类型的使能状态。使用Promise异步回调。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function isNotificationSlotEnabledByBundles(bundles: Array<BundleOption>, type: SlotType): Promise<Map<BundleOption, boolean>>--><!--Device-notificationManager-function isNotificationSlotEnabledByBundles(bundles: Array<BundleOption>, type: SlotType): Promise<Map<BundleOption, boolean>>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundles | Array & lt;BundleOption & gt; | 是 |
| type | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Map & lt;BundleOption, boolean & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 批量查询多个应用的实况窗开关状态
const bundles: Array<notificationManager.BundleOption> = [
    { bundle: 'com.example.app1', uid: 10001 },
    { bundle: 'com.example.app2', uid: 10002 },
];

notificationManager.isNotificationSlotEnabledByBundles(
    bundles, notificationManager.SlotType.LIVE_VIEW).then((data) => {
    data.forEach((value: boolean, key: notificationManager.BundleOption) => {
        console.info(`bundle: ${key.bundle}, enabled: ${value}`);
    });
}).catch((err: BusinessError) => {
    console.error(`isNotificationSlotEnabledByBundles failed, code is ${err.code}, message is ${err.message}`);
});
```
