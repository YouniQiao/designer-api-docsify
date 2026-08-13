# removeNotificationSlot

## removeNotificationSlot

```TypeScript
function removeNotificationSlot(slotType: notification.SlotType, callback: AsyncCallback<void>): void
```

删除指定的通知渠道类型，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-reminderAgentManager-function removeNotificationSlot(slotType: notification.SlotType, callback: AsyncCallback<void>): void--><!--Device-reminderAgentManager-function removeNotificationSlot(slotType: notification.SlotType, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | notification.SlotType | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.removeNotificationSlot(notificationManager.SlotType.CONTENT_INFORMATION,
  (err: BusinessError) => {
  if (err.code) {
    console.error("callback err code:" + err.code + " message:" + err.message);
  } else {
    console.info("removeNotificationSlot callback");
  }
});
```


## removeNotificationSlot

```TypeScript
function removeNotificationSlot(slotType: notification.SlotType): Promise<void>
```

删除指定的通知渠道类型，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-reminderAgentManager-function removeNotificationSlot(slotType: notification.SlotType): Promise<void>--><!--Device-reminderAgentManager-function removeNotificationSlot(slotType: notification.SlotType): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.ReminderAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | notification.SlotType | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';

reminderAgentManager.removeNotificationSlot(notificationManager.SlotType.CONTENT_INFORMATION).then(() => {
  console.info("removeNotificationSlot promise");
}).catch((err: BusinessError) => {
  console.error("promise err code:" + err.code + " message:" + err.message);
});
```
