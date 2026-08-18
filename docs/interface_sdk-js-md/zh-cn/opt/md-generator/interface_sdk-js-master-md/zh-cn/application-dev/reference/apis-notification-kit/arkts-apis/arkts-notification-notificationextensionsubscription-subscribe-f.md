# subscribe

## 导入模块

```TypeScript
```

## subscribe

```TypeScript
function subscribe(info: NotificationExtensionSubscriptionInfo[]): Promise<void>
```

订阅通知扩展。使用蓝牙模块相关接口获取蓝牙设备的唯一地址后方可订阅。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.SUBSCRIBE_NOTIFICATION

<!--Device-notificationExtensionSubscription-function subscribe(info: NotificationExtensionSubscriptionInfo[]): Promise<void>--><!--Device-notificationExtensionSubscription-function subscribe(info: NotificationExtensionSubscriptionInfo[]): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

unsubscribe 取消通知扩展订阅。

getSubscribeInfo 获取应用通知扩展订阅信息。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [NotificationExtensionSubscriptionInfo[]](arkts-notification-notificationextensionsubscriptioninfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600023](../errorcode-notification.md#1600023-应用未实现notificationsubscriberextensionability) |

**示例**

```TypeScript
let infos: notificationExtensionSubscription.NotificationExtensionSubscriptionInfo[] = [
  {
    addr: '01:23:45:67:89:AB', // 使用动态获取的蓝牙地址
    type: notificationExtensionSubscription.SubscribeType.BLUETOOTH
  }
];
notificationExtensionSubscription.subscribe(infos).then(() => {
  console.info(`subscribe success`);
}).catch((err: BusinessError) => {
  console.error(`subscribe fail, code is ${err.code}, message is ${err.message}`);
});
```
