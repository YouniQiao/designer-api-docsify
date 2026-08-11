# unsubscribe

## 导入模块

```TypeScript
import { notificationExtensionSubscription } from 'kits/@kit.NotificationKit';
```

## unsubscribe

```TypeScript
function unsubscribe(): Promise<void>
```

取消通知扩展的订阅。使用Promise异步回调。

**起始版本：** 22

**需要权限：** ohos.permission.SUBSCRIBE_NOTIFICATION

<!--Device-notificationExtensionSubscription-function unsubscribe(): Promise<void>--><!--Device-notificationExtensionSubscription-function unsubscribe(): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
notificationExtensionSubscription.unsubscribe().then(() => {
  console.info(`unsubscribe success`);
}).catch((err: BusinessError) => {
  console.error(`unsubscribe fail, code is ${err.code}, message is ${err.message}`);
});
```
