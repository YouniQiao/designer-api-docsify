# isDistributedEnabled

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## isDistributedEnabled

```TypeScript
function isDistributedEnabled(callback: AsyncCallback<boolean>): void
```

查询设备是否支持跨设备协同通知。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 26.0.0

**替代接口：** [notificationManager.isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f.md#isdistributedenabled)(deviceType:

<!--Device-notificationManager-function isDistributedEnabled(callback: AsyncCallback<boolean>): void--><!--Device-notificationManager-function isDistributedEnabled(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1600010](../errorcode-notification.md#1600010-分布式操作失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let isDistributedEnabledCallback = (err: BusinessError, data: boolean): void => {
  if (err) {
    console.error(`isDistributedEnabled failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`isDistributedEnabled success ${JSON.stringify(data)}`);
  }
};
notificationManager.isDistributedEnabled(isDistributedEnabledCallback);
```


## isDistributedEnabled

```TypeScript
function isDistributedEnabled(): Promise<boolean>
```

查询设备是否支持跨设备协同通知。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 26.0.0

**替代接口：** [notificationManager.isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f.md#isdistributedenabled)(deviceType:

<!--Device-notificationManager-function isDistributedEnabled(): Promise<boolean>--><!--Device-notificationManager-function isDistributedEnabled(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.Notification

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1600010](../errorcode-notification.md#1600010-分布式操作失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.isDistributedEnabled().then((data: boolean) => {
  console.info(`isDistributedEnabled success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`isDistributedEnabled failed, code is ${err.code}, message is ${err.message}`);
});
```
