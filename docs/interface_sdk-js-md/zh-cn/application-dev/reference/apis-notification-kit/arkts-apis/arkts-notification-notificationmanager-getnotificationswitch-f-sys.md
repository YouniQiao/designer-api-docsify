# getNotificationSwitch（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getNotificationSwitch

```TypeScript
function getNotificationSwitch(switchName: string, userId: int): Promise<SwitchState>
```

获取通知开关状态。使用Promise异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-notificationManager-function getNotificationSwitch(switchName: string, userId: int): Promise<SwitchState>--><!--Device-notificationManager-function getNotificationSwitch(switchName: string, userId: int): Promise<SwitchState>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| switchName | string | 是 | 通知开关名称。取值为：DEAL（交易类通知聚合开关）、LOGISTICS（物流类通知聚合开关）。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 用户ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;SwitchState&gt; | Promise对象，返回通知开关状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1600008 | The user does not exist. |
| 1600012 | No memory space. |
| 201 | Permission denied. |
| 1600001 | Internal error. Database operation failed. |
| 202 | Not system application to call the interface. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let switchName: string = 'DEAL';
let userId: number = 100;

notificationManager.getNotificationSwitch(switchName, userId).then((data: notificationManager.SwitchState) => {
    console.info(`getNotificationSwitch success, switchState: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getNotificationSwitch failed, code is ${err.code}, message is ${err.message}`);
});
```

