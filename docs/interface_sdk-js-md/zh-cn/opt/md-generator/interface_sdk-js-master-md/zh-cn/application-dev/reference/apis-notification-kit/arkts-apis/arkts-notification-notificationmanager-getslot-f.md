# getSlot

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getSlot

```TypeScript
function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void
```

获取指定类型的通知渠道。使用callback异步回调。

用于查询已创建的通知渠道的详细配置信息，包括提醒方式、级别、锁屏显示等设置。需先通过addSlot创建对应类型的通知渠道，否则获取结果为空。

**起始版本：** 9

<!--Device-notificationManager-function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void--><!--Device-notificationManager-function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

[addSlot](notificationManager.addSlot(slotType: SlotType,callback: AsyncCallback<void>): void) 创建通知频道。

[removeSlot](notificationManager.removeSlot(slotType: SlotType, AsyncCallback<void>): void) 删除指定类型的通知渠道。

[removeAllSlots](notificationManager.removeAllSlots(callback: AsyncCallback): void) 删除所有通知渠道。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NotificationSlot&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// getSlot回调
let getSlotCallback = (err: BusinessError, data: notificationManager.NotificationSlot): void => {
  if (err) {
    console.error(`Failed to get slot. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in getting slot, data is ${JSON.stringify(data)}`);
  }
}
let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
notificationManager.getSlot(slotType, getSlotCallback);
```


## getSlot

```TypeScript
function getSlot(slotType: SlotType): Promise<NotificationSlot>
```

获取指定类型的通知渠道。使用Promise异步回调。

用于查询已创建的通知渠道的详细配置信息，包括提醒方式、级别、锁屏显示等设置。需先通过addSlot创建对应类型的通知渠道，否则获取结果为空。

**起始版本：** 9

<!--Device-notificationManager-function getSlot(slotType: SlotType): Promise<NotificationSlot>--><!--Device-notificationManager-function getSlot(slotType: SlotType): Promise<NotificationSlot>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

[addSlot](notificationManager.addSlot(slotType: SlotType): Promise<void>) 创建通知频道。

[removeSlot](notificationManager.removeSlot(slotType: SlotType): Promise<void>) 删除指定类型的通知渠道。

[removeAllSlots](notificationManager.removeAllSlots(): Promise<void>) 删除所有通知渠道。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;NotificationSlot & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
notificationManager.getSlot(slotType).then((data: notificationManager.NotificationSlot) => {
  console.info(`Succeeded in getting slot, data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get slot. Code is ${err.code}, message is ${err.message}`);
});
```
