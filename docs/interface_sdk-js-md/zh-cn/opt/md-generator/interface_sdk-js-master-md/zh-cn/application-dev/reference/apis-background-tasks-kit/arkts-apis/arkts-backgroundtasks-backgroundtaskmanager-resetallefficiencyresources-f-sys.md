# resetAllEfficiencyResources（系统接口）

## resetAllEfficiencyResources

```TypeScript
function resetAllEfficiencyResources(): void
```

释放已申请的全部能效资源。

**起始版本：** 23

**废弃版本：** -1

<!--Device-backgroundTaskManager-function resetAllEfficiencyResources(): void--><!--Device-backgroundTaskManager-function resetAllEfficiencyResources(): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
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

try {
    backgroundTaskManager.resetAllEfficiencyResources();
} catch (error) {
    console.error(`resetAllEfficiencyResources failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```
