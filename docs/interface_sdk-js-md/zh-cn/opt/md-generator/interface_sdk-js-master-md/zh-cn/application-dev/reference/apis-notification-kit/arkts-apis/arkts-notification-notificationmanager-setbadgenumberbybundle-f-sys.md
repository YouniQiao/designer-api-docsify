# setBadgeNumberByBundle（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## setBadgeNumberByBundle

```TypeScript
function setBadgeNumberByBundle(bundle: BundleOption, badgeNumber: number): Promise<void>
```

代理其他应用设定角标个数。使用Promise异步回调。

**起始版本：** 12

<!--Device-notificationManager-function setBadgeNumberByBundle(bundle: BundleOption, badgeNumber: int): Promise<void>--><!--Device-notificationManager-function setBadgeNumberByBundle(bundle: BundleOption, badgeNumber: int): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| badgeNumber | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600017](../errorcode-notification.md#1600017-没有对应的代理关系配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundle: notificationManager.BundleOption = {
    bundle: 'com.example.bundleName',
};
let badgeNumber: number = 10;

notificationManager.setBadgeNumberByBundle(bundle, badgeNumber).then(() => {
    console.info('setBadgeNumberByBundle success');
}).catch((err: BusinessError) => {
    console.error(`setBadgeNumberByBundle failed, code is ${err.code}, message is ${err.message}`);
});
```
