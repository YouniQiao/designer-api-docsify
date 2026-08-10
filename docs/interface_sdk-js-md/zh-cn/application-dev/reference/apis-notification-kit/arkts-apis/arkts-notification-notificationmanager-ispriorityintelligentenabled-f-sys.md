# isPriorityIntelligentEnabled（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## isPriorityIntelligentEnabled

```TypeScript
function isPriorityIntelligentEnabled(): Promise<boolean>
```

获取优先通知智能服务使能状态。使用Promise异步回调。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-notificationManager-function isPriorityIntelligentEnabled(): Promise<boolean>--><!--Device-notificationManager-function isPriorityIntelligentEnabled(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回包含优先通知智能服务使能状态的Promise对象。 &lt;br&gt; - true：优先通知智能服务为打开状态。 &lt;br&gt; - false：优先通知智能服务为关闭状态。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1600012 | No memory space. |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600003 | Failed to connect to the service. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

notificationManager.isPriorityIntelligentEnabled().then((result: boolean) => {
  hilog.info(0x0000, 'testTag', `isPriorityIntelligentEnabled result: ${result}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', `isPriorityIntelligentEnabled failed, code is ${err.code}, message is ${err.message}`);
});
```

