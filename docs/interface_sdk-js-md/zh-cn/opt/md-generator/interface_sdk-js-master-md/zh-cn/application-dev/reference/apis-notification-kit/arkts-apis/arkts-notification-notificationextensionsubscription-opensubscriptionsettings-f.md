# openSubscriptionSettings

## 导入模块

```TypeScript
import { notificationExtensionSubscription } from '@kit.NotificationKit';
```

## openSubscriptionSettings

```TypeScript
function openSubscriptionSettings(context: UIAbilityContext): Promise<void>
```

打开应用的通知扩展订阅授权页面，以半模态弹窗形式显示。用户可在该页面授权“允许获取本机通知”开关与“已获取的本机通知”应用开关。 使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SUBSCRIBE_NOTIFICATION

<!--Device-notificationExtensionSubscription-function openSubscriptionSettings(context: UIAbilityContext): Promise<void>--><!--Device-notificationExtensionSubscription-function openSubscriptionSettings(context: UIAbilityContext): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600018](../errorcode-notification.md#1600018-通知设置页面已经拉起) |
| [1600023](../errorcode-notification.md#1600023-应用未实现notificationsubscriberextensionability) |

## 示例

```TypeScript
import { common } from '@kit.AbilityKit';

try {
  // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  notificationExtensionSubscription.openSubscriptionSettings(context).then(() => {
    console.info(`openSubscriptionSettings success`);
  }).catch((e: Error) => {
    let error = e as BusinessError
    console.error(`failed to call openSubscriptionSettings, code is ${error.code}, message is ${error.message}`)
  });
} catch (error) {
  console.error(`failed to call openSubscriptionSettings, code is ${error.code}, message is ${error.message}`)
}
```
