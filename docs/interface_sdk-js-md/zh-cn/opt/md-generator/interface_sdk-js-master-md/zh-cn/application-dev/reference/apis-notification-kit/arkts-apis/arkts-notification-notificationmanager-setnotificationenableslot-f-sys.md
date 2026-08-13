# setNotificationEnableSlot（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## setNotificationEnableSlot

```TypeScript
function setNotificationEnableSlot(
    bundle: BundleOption,
    type: SlotType,
    enable: boolean,
    callback: AsyncCallback<void>
  ): void
```

设置指定应用的指定渠道类型的使能状态。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setNotificationEnableSlot(    bundle: BundleOption,    type: SlotType,    enable: boolean,    callback: AsyncCallback<void>  ): void--><!--Device-notificationManager-function setNotificationEnableSlot(    bundle: BundleOption,    type: SlotType,    enable: boolean,    callback: AsyncCallback<void>  ): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| type | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |
| enable | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// setNotificationEnableSlot
let setNotificationEnableSlotCallback = (err: BusinessError): void => {
    if (err) {
        console.error(`setNotificationEnableSlot failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info('setNotificationEnableSlot success');
    }
};
notificationManager.setNotificationEnableSlot(
    { bundle: 'ohos.samples.notification', },
    notificationManager.SlotType.SOCIAL_COMMUNICATION,
    true,
    setNotificationEnableSlotCallback);
```


## setNotificationEnableSlot

```TypeScript
function setNotificationEnableSlot(
    bundle: BundleOption,
    type: SlotType,
    enable: boolean,
    isForceControl: boolean,
    callback: AsyncCallback<void>,
  ): void
```

设置指定应用的指定渠道类型的使能状态。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setNotificationEnableSlot(    bundle: BundleOption,    type: SlotType,    enable: boolean,    isForceControl: boolean,    callback: AsyncCallback<void>,  ): void--><!--Device-notificationManager-function setNotificationEnableSlot(    bundle: BundleOption,    type: SlotType,    enable: boolean,    isForceControl: boolean,    callback: AsyncCallback<void>,  ): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| type | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |
| enable | boolean | 是 |
| isForceControl | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-指定的bundlename不存在) |


## setNotificationEnableSlot

```TypeScript
function setNotificationEnableSlot(bundle: BundleOption, type: SlotType, enable: boolean, isForceControl?: boolean): Promise<void>
```

设置指定应用的指定渠道类型的使能状态。使用promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setNotificationEnableSlot(bundle: BundleOption, type: SlotType, enable: boolean, isForceControl?: boolean): Promise<void>--><!--Device-notificationManager-function setNotificationEnableSlot(bundle: BundleOption, type: SlotType, enable: boolean, isForceControl?: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| type | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |
| enable | boolean | 是 |
| isForceControl | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// setNotificationEnableSlot
notificationManager.setNotificationEnableSlot(
    { bundle: 'ohos.samples.notification', },
    notificationManager.SlotType.SOCIAL_COMMUNICATION,
    true).then(() => {
        console.info('setNotificationEnableSlot success');
    }).catch((err: BusinessError) => {
        console.error(`setNotificationEnableSlot failed, code is ${err.code}, message is ${err.message}`);
    });
```
