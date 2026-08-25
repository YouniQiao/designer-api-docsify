# getBackgroundTaskState（系统接口）

## 导入模块

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

## getBackgroundTaskState

```TypeScript
function getBackgroundTaskState(stateInfo: BackgroundTaskStateInfo): UserAuthResult
```

获取长时任务授权信息。

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为24。

**需要权限：** ohos.permission.SET_BACKGROUND_TASK_STATE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| stateInfo | [BackgroundTaskStateInfo](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskstateinfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [UserAuthResult](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-userauthresult-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-长时任务校验失败) |

**示例**

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 请开发者根据实际情况更新参数
  let backgroundTaskStateInfo: backgroundTaskManager.BackgroundTaskStateInfo = {
    userId: 100,
    bundleName: 'com.example.continuoustask',
    appIndex: 0
  };
  let auth = backgroundTaskManager.getBackgroundTaskState(backgroundTaskStateInfo);
  console.info('Operation getBackgroundTaskState succeeded. data: ' + JSON.stringify(auth));
} catch (error) {
  console.error(`Operation getBackgroundTaskState failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
}
```
