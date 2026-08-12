# removeAllSlots

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## removeAllSlots

```TypeScript
function removeAllSlots(callback: AsyncCallback<void>): void
```

删除当前应用所有通知渠道。使用callback异步回调。

删除后，当前应用的所有通知渠道及其配置将被永久移除，后续发布通知时系统将自动创建对应类型的渠道。已通过这些渠道发布的通知不受影响，仍可在通知中心查看。适用于需要一次性清除所有渠道配置的场景。

**起始版本：** 9

<!--Device-notificationManager-function removeAllSlots(callback: AsyncCallback<void>): void--><!--Device-notificationManager-function removeAllSlots(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

[addSlot](notificationManager.addSlot(slotType: SlotType,callback: AsyncCallback<void>): void) 创建通知频道。

[getSlot](notificationManager.getSlot(slotType: SlotType,callback: AsyncCallback<NotificationSlot>): void) 获取指定类型的通知渠道。

[removeSlot](notificationManager.removeSlot(slotType: SlotType,callback: AsyncCallback<void>): void) 删除所有通知渠道。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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

let removeAllSlotsCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to remove all slots. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in removing all slots.`);
  }
}
notificationManager.removeAllSlots(removeAllSlotsCallback);
```


## removeAllSlots

```TypeScript
function removeAllSlots(): Promise<void>
```

删除当前应用所有通知渠道。使用Promise异步回调。

删除后，当前应用的所有通知渠道及其配置将被永久移除，后续发布通知时系统将自动创建对应类型的渠道。已通过这些渠道发布的通知不受影响，仍可在通知中心查看。适用于需要一次性清除所有渠道配置的场景。

**起始版本：** 9

<!--Device-notificationManager-function removeAllSlots(): Promise<void>--><!--Device-notificationManager-function removeAllSlots(): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

[addSlot](notificationManager.addSlot(slotType: SlotType): Promise<void>) 创建通知频道。

[getSlot](notificationManager.getSlot(slotType: SlotType): Promise<NotificationSlot>) 获取指定类型的通知渠道。

[removeSlot](notificationManager.removeSlot(slotType: SlotType): Promise<void>) 删除指定类型的通知渠道。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.removeAllSlots().then(() => {
  console.info(`Succeeded in removing all slots.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to remove all slots. Code is ${err.code}, message is ${err.message}`);
});
```
