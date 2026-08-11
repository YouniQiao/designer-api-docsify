# cancel（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## cancel

```TypeScript
function cancel(representativeBundle: BundleOption, id: number): Promise<void>
```

代理取消当前用户其他应用的通知。使用Promise异步回调。

需要当前应用与其他应用存在代理关系，或者当前应用有ohos.permission.NOTIFICATION_AGENT_CONTROLLER权限。

**起始版本：** 12

<!--Device-notificationManager-function cancel(representativeBundle: BundleOption, id: int): Promise<void>--><!--Device-notificationManager-function cancel(representativeBundle: BundleOption, id: int): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| representativeBundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600017](../errorcode-notification.md#1600017-没有对应的代理关系配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600007](../errorcode-notification.md#1600007-通知不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundle: notificationManager.BundleOption = {
  bundle: 'bundleName'
};
let id: number = 1;
notificationManager.cancel(bundle, id).then(() => {
  console.info('cancel success');
}).catch((err: BusinessError) => {
  console.error(`cancel failed, code is ${err.code}, message is ${err.message}`);
});
```
