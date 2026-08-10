# releaseExemptionResource（系统接口）

## 导入模块

```TypeScript
import { deviceStandby } from 'kits/@kit.BackgroundTasksKit';
```

## releaseExemptionResource

```TypeScript
function releaseExemptionResource(request: ResourceRequest): void
```

取消应用订阅申请豁免。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.DEVICE_STANDBY_EXEMPTION

<!--Device-deviceStandby-function releaseExemptionResource(request: ResourceRequest): void--><!--Device-deviceStandby-function releaseExemptionResource(request: ResourceRequest): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.DeviceStandby

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [ResourceRequest](arkts-backgroundtasks-devicestandby-resourcerequest-i-sys.md) | 是 | 资源请求 。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 9800004 | Failed to get device standby service. Possible cause: A necessary system service is not ready. |
| 9800001 | Memory operation failed. |
| 9800003 | Failed to complete inner transaction. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters. |
| 201 | Permission denied. |
| 202 | Not System App. |
| 18700001 | Caller information verification failed. |

## 示例

```TypeScript
import { deviceStandby } from '@kit.BackgroundTasksKit';

let resRequest: deviceStandby.ResourceRequest = {
  resourceTypes: deviceStandby.ResourceType.TIMER,
  uid:10003,
  name:"com.demo.app",
  duration:10,
  reason:"unapply",
};
deviceStandby.releaseExemptionResource(resRequest);
```

