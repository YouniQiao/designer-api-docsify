# distributeOperation（系统接口）

## 导入模块

```TypeScript
import { notificationSubscribe } from '@kit.NotificationKit';
```

## distributeOperation

```TypeScript
function distributeOperation(hashcode: string, operationInfo?: OperationInfo): Promise<void>
```

触发指定通知的跨设备协同操作（例如通知跨设备点击跳转、通知跨设备快捷回复等）。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function distributeOperation(hashcode: string, operationInfo?: OperationInfo): Promise<void>--><!--Device-notificationSubscribe-function distributeOperation(hashcode: string, operationInfo?: OperationInfo): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hashcode | string | 是 |
| [operationInfo](../../apis-ability-kit/arkts-apis/arkts-ability-abilitytoolaccessctrl-permissionquery-i-sys.md) | [OperationInfo](arkts-notification-notificationsubscribe-operationinfo-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [1600010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600010-分布式操作失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [1600021](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600021-跨设备通信超时) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let hashcode: string = 'hashcode';
let operationInfo: notificationSubscribe.OperationInfo = {
  actionName: 'actionName',
  userInput: 'userInput',
  operationType: 1,
  buttonIndex: 1,
};
notificationSubscribe.distributeOperation(hashcode, operationInfo).then(() => {
  console.info('distributeOperation success');
}).catch((err: BusinessError) => {
  console.error(`distributeOperation fail, code is ${err.code}, message is ${err.message}`);
});
```
