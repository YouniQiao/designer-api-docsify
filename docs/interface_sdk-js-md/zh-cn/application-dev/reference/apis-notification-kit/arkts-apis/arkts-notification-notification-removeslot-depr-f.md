# removeSlot

## 导入模块

```TypeScript
```

## removeSlot

```TypeScript
function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void
```

删除指定类型的通知通道（callback形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [removeSlot](arkts-notification-notificationmanager-removeslot-f.md)

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## removeSlot

```TypeScript
function removeSlot(slotType: SlotType): Promise<void>
```

删除指定类型的通知通道（Promise形式）。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [removeSlot](arkts-notification-notificationmanager-removeslot-f.md)

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
