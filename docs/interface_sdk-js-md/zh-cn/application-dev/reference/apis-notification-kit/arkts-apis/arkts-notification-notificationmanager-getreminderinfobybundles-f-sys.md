# getReminderInfoByBundles（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getReminderInfoByBundles

```TypeScript
function getReminderInfoByBundles(bundles: Array<BundleOption>) : Promise<Array<NotificationReminderInfo>>
```

批量获取指定应用提醒信息。使用Promise异步回调。

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getReminderInfoByBundles(bundles: Array<BundleOption>) : Promise<Array<NotificationReminderInfo>>--><!--Device-notificationManager-function getReminderInfoByBundles(bundles: Array<BundleOption>) : Promise<Array<NotificationReminderInfo>>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundles | Array&lt;BundleOption&gt; | 是 | 待获取应用提醒信息的应用包信息数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;NotificationReminderInfo&gt;&gt; | Promise对象，返回包含应用提醒信息的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1600012 | No memory space. |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundles: Array<notificationManager.BundleOption> = [
    {
        bundle: 'bundleName',
    },
    {
        bundle: 'bundleName1',
    }
];
notificationManager.getReminderInfoByBundles(bundles).then((data: Array<notificationManager.NotificationReminderInfo>) => {
    console.info(`Reminder data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`GetReminderInfoByBundles failed, code is ${err.code}, message is ${err.message}`);
});
```

