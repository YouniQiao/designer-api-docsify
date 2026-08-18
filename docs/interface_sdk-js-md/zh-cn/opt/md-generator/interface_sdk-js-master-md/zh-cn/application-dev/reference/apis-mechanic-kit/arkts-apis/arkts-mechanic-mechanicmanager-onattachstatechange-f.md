# onAttachStateChange

## 导入模块

```TypeScript
```

## onAttachStateChange

```TypeScript
function onAttachStateChange(callback: Callback<AttachStateChangeInfo>): void
```

Subscribes to device attachment state change events.

**起始版本：** 23

<!--Device-mechanicManager-function onAttachStateChange(callback: Callback<AttachStateChangeInfo>): void--><!--Device-mechanicManager-function onAttachStateChange(callback: Callback<AttachStateChangeInfo>): void-End-->

**系统能力：** SystemCapability.Mechanic.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AttachStateChangeInfo](arkts-mechanic-mechanicmanager-attachstatechangeinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [33300001](../errorcode-mechanic.md#33300001-系统错误) |
