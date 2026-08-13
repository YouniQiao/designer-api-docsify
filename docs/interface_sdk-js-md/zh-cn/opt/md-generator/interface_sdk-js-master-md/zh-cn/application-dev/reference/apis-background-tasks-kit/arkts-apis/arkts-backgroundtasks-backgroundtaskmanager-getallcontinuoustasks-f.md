# getAllContinuousTasks

## getAllContinuousTasks

```TypeScript
function getAllContinuousTasks(context: Context): Promise<ContinuousTaskInfo[]>
```

获取所有长时任务信息，如长时任务ID、长时任务类型等，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function getAllContinuousTasks(context: Context): Promise<ContinuousTaskInfo[]>--><!--Device-backgroundTaskManager-function getAllContinuousTasks(context: Context): Promise<ContinuousTaskInfo[]>-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ContinuousTaskInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskinfo-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [9800005](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800005-长时任务校验失败) |
| [9800004](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800002](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate() {
    try {
      // 如果当前没有申请长时任务，则获取到一个空数组
      backgroundTaskManager.getAllContinuousTasks(this.context).then((res: backgroundTaskManager.ContinuousTaskInfo[]) => {
        console.info(`Operation getAllContinuousTasks succeeded. data: ` + JSON.stringify(res));
      }).catch((error: BusinessError) => {
        console.error(`Operation getAllContinuousTasks failed. code is ${error.code} message is ${error.message}`);
      });
    } catch (error) {
      console.error(`Operation getAllContinuousTasks failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    }
  }
};
```


## getAllContinuousTasks

```TypeScript
function getAllContinuousTasks(context: Context, includeSuspended: boolean): Promise<ContinuousTaskInfo[]>
```

获取所有长时任务信息，如长时任务ID、长时任务类型等。可选择是否获取暂停的长时任务信息，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function getAllContinuousTasks(context: Context, includeSuspended: boolean): Promise<ContinuousTaskInfo[]>--><!--Device-backgroundTaskManager-function getAllContinuousTasks(context: Context, includeSuspended: boolean): Promise<ContinuousTaskInfo[]>-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| includeSuspended | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ContinuousTaskInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskinfo-i.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [9800005](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800005-长时任务校验失败) |
| [9800004](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800002](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate() {
    try {
      // 如果当前没有申请长时任务，则获取到一个空数组
      backgroundTaskManager.getAllContinuousTasks(this.context, false).then((res: backgroundTaskManager.ContinuousTaskInfo[]) => {
        console.info(`Operation getAllContinuousTasks succeeded. data: ` + JSON.stringify(res));
      }).catch((error: BusinessError) => {
        console.error(`Operation getAllContinuousTasks failed. code is ${error.code} message is ${error.message}`);
      });
    } catch (error) {
      console.error(`Operation getAllContinuousTasks failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    }
  }
};
```
