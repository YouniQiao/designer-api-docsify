# getAllEfficiencyResources（系统接口）

## 导入模块

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

## getAllEfficiencyResources

```TypeScript
function getAllEfficiencyResources(): Promise<EfficiencyResourcesInfo[]>
```

获取已申请的所有能效资源信息，如能效资源类型等，使用Promise异步回调。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.EfficiencyResourcesApply

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[EfficiencyResourcesInfo](arkts-backgroundtasks-backgroundtaskmanager-efficiencyresourcesinfo-i-sys.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [18700001](../errorcode-backgroundTaskMgr.md#18700001-资源申请接口信息校验失败) |
| [18700002](../errorcode-backgroundTaskMgr.md#18700002-parcel读写操作失败) |
| [18700004](../errorcode-backgroundTaskMgr.md#18700004-系统服务失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  backgroundTaskManager.getAllEfficiencyResources().then((res: backgroundTaskManager.EfficiencyResourcesInfo[]) => {
    console.info(`Operation getAllEfficiencyResources succeeded. data: ` + JSON.stringify(res));
  }).catch((error: BusinessError) => {
    console.error(`Operation getAllEfficiencyResources failed. code is ${error.code} message is ${error.message}`);
  });
} catch (error) {
  console.error(`Operation getAllEfficiencyResources failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  backgroundTaskManager.getAllEfficiencyResources().then((res: backgroundTaskManager.EfficiencyResourcesInfo[]) => {
    console.info(`Operation getAllEfficiencyResources succeeded. data: ` + JSON.stringify(res));
  }).catch((error) => {
    console.error(`Operation getAllEfficiencyResources failed. code is ${error.code} message is ${error.message}`);
  });
} catch (error) {
  console.error(`Operation getAllEfficiencyResources failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```
