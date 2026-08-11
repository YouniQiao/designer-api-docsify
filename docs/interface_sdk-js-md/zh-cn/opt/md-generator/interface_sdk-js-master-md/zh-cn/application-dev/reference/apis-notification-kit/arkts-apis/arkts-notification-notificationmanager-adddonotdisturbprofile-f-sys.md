# addDoNotDisturbProfile（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## addDoNotDisturbProfile

```TypeScript
function addDoNotDisturbProfile(templates: Array<DoNotDisturbProfile>): Promise<void>
```

添加勿扰模式配置信息。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function addDoNotDisturbProfile(templates: Array<DoNotDisturbProfile>): Promise<void>--><!--Device-notificationManager-function addDoNotDisturbProfile(templates: Array<DoNotDisturbProfile>): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| templates | Array&lt;DoNotDisturbProfile&gt; | 是 |

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let trustlist: Array<notificationManager.BundleOption> = [
  {
    bundle: 'com.example.bundleName',
    uid: 0
  },
  {
    bundle: 'com.example.bundleName1',
    uid: 1
  }
]
let templates: Array<notificationManager.DoNotDisturbProfile> = [
  {
    id: 3,
    name: '工作模式',
    trustlist: trustlist
  }
]

notificationManager.addDoNotDisturbProfile(templates).then(() => {
  console.info('addDoNotDisturbProfile success.');
}).catch((err: BusinessError) => {
  console.error(`addDoNotDisturbProfile failed, code is ${err.code}, message is ${err.message}`);
});
```


## addDoNotDisturbProfile

```TypeScript
function addDoNotDisturbProfile(templates: Array<DoNotDisturbProfile>, userId: number): Promise<void>
```

向指定用户添加勿扰模式配置信息。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-notificationManager-function addDoNotDisturbProfile(templates: Array<DoNotDisturbProfile>, userId: int): Promise<void>--><!--Device-notificationManager-function addDoNotDisturbProfile(templates: Array<DoNotDisturbProfile>, userId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| templates | Array&lt;DoNotDisturbProfile&gt; | 是 |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600008](../errorcode-notification.md#1600008-用户不存在) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userId : number = 100;
let trustlist: Array<notificationManager.BundleOption> = [
  {
    // 需根据实际情况进行替换
    bundle: 'bundleName',
    uid: 0
  },
  {
    // 需根据实际情况进行替换
    bundle: 'bundleName1',
    uid: 1
  }
]
let templates: Array<notificationManager.DoNotDisturbProfile> = [
  {
    id: 3,
    name: '工作模式',
    trustlist: trustlist
  }
]

notificationManager.addDoNotDisturbProfile(templates, userId).then(() => {
  console.info('addDoNotDisturbProfile success.');
}).catch((err: BusinessError) => {
  console.error(`addDoNotDisturbProfile failed, code is ${err.code}, message is ${err.message}`);
});
```
