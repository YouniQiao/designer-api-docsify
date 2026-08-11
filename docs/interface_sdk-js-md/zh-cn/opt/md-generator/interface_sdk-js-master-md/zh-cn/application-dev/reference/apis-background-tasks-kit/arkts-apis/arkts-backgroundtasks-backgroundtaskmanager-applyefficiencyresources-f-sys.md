# applyEfficiencyResources（系统接口）

## applyEfficiencyResources

```TypeScript
function applyEfficiencyResources(request: EfficiencyResourcesRequest): void
```

申请能效资源。

**起始版本：** 9

<!--Device-backgroundTaskManager-function applyEfficiencyResources(request: EfficiencyResourcesRequest): void--><!--Device-backgroundTaskManager-function applyEfficiencyResources(request: EfficiencyResourcesRequest): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [EfficiencyResourcesRequest](arkts-backgroundtasks-backgroundtaskmanager-efficiencyresourcesrequest-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [9800004](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800001-内存操作失败) |
| [9800003](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800003-ipc通信失败) |
| [9800002](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [18700001](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#18700001-资源申请接口信息校验失败) |

## 示例

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';  
import { BusinessError } from '@kit.BasicServicesKit';

let request: backgroundTaskManager.EfficiencyResourcesRequest = {
    resourceTypes: backgroundTaskManager.ResourceType.CPU, // 申请CPU资源
    isApply: true, // 申请资源
    timeOut: 0, // 资源使用时间（ms）
    reason: 'apply', // 申请资源原因
    isPersist: true, // 永久持有资源
    isProcess: false, // 应用申请
    cpuLevel: backgroundTaskManager.EfficiencyResourcesCpuLevel.SMALL_CPU // 运行在小核，从API version 23开始支持。
};
try {
    backgroundTaskManager.applyEfficiencyResources(request);
    console.info('applyEfficiencyResources success.');
} catch (error) {
    console.error(`applyEfficiencyResources failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```
