# cancelGroup

## 导入模块

```TypeScript
```

## cancelGroup

```TypeScript
function cancelGroup(groupName: string, callback: AsyncCallback<void>): void
```

取消本应用指定组下的通知（Callback形式）。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [cancelGroup](arkts-notification-notificationmanager-cancelgroup-f.md)

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| groupName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## cancelGroup

```TypeScript
function cancelGroup(groupName: string): Promise<void>
```

取消本应用指定组下的通知（Promise形式）。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [cancelGroup](arkts-notification-notificationmanager-cancelgroup-f.md)

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| groupName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
