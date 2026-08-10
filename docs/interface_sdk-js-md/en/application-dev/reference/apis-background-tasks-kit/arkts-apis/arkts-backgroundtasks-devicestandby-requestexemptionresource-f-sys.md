# requestExemptionResource (System API)

## Modules to Import

```TypeScript
import { deviceStandby } from 'kits/@kit.BackgroundTasksKit';
```

## requestExemptionResource

```TypeScript
function requestExemptionResource(request: ResourceRequest): void
```

应用订阅申请豁免，使应用临时不进入待机管控。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.DEVICE_STANDBY_EXEMPTION

<!--Device-deviceStandby-function requestExemptionResource(request: ResourceRequest): void--><!--Device-deviceStandby-function requestExemptionResource(request: ResourceRequest): void-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [ResourceRequest](arkts-backgroundtasks-devicestandby-resourcerequest-i-sys.md) | Yes | 资源请求。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 9800004 | Failed to get device standby service. Possible cause: A necessary system service is not ready. |
| 9800001 | Memory operation failed. |
| 9800003 | Failed to complete inner transaction. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters. |
| 201 | Permission denied. |
| 202 | Not System App. |
| 18700001 | Caller information verification failed. |

## Examples

```TypeScript
import { deviceStandby } from '@kit.BackgroundTasksKit';

let resRequest: deviceStandby.ResourceRequest = {
  resourceTypes: deviceStandby.ResourceType.TIMER,
  uid:10003,
  name:"com.example.app",
  duration:10,
  reason:"apply",
};
deviceStandby.requestExemptionResource(resRequest);
```

