# updateBackgroundRunning

## 导入模块

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## updateBackgroundRunning

```TypeScript
function updateBackgroundRunning(context: Context, bgModes: string[]): Promise<ContinuousTaskNotification>
```

更新长时任务类型，使用Promise异步回调。长时任务更新成功后，会有通知栏消息，没有提示音。&lt;/br&gt;更新长时任务前，可以通过 [getAllContinuousTasks](arkts-backgroundtasks-backgroundtaskmanager-getallcontinuoustasks-f.md)接口获取当前所有长时任务信息，如果当前没有已经 存在的长时任务，会更新失败。&lt;/br&gt;该接口仅支持更新如下三个接口申请的长时任务：&lt;/br&gt; [startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback:AsyncCallback&lt;void&gt;): void](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md) &lt;/br&gt; [startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise&lt;void&gt;]{@linkbackgroundTaskManager.startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent)} &lt;/br&gt; [startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent):Promise&lt;ContinuousTaskNotification&gt;][startBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md)

**起始版本：** 12

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| bgModes | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ContinuousTaskNotification](arkts-backgroundtasks-backgroundtaskmanager-continuoustasknotification-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-内存操作失败) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |
| [9800003](../errorcode-backgroundTaskMgr.md#9800003-ipc通信失败) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-长时任务校验失败) |
| [9800006](../errorcode-backgroundTaskMgr.md#9800006-长时任务通知信息校验失败) |
| [9800007](../errorcode-backgroundTaskMgr.md#9800007-长时任务信息存储失败) |


## updateBackgroundRunning

```TypeScript
function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>
```

更新长时任务，使用Promise异步回调。长时任务更新成功后，会有通知栏消息，没有提示音。更新长时任务还存在如下约束限制：
1. 本接口仅支持更新如下接口申请的长时任务：[startBackgroundRunning(context: Context, request: ContinuousTaskRequest):Promise&lt;ContinuousTaskNotification&gt;](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md)。
2. 已经合并的长时任务，且后台任务主类型和子类型均相同，仅支持更新ContinuousTaskRequest.wantAgent中的wants信息（abilityName等），如果类型不同，更新失败。
3. 如果待更新的长时任务或指定的更新类型中包含数据传输类型，直接返回失败。

**起始版本：** 21

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| request | [ContinuousTaskRequest](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskrequest-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ContinuousTaskNotification](arkts-backgroundtasks-backgroundtaskmanager-continuoustasknotification-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-内存操作失败) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-长时任务校验失败) |
| [9800006](../errorcode-backgroundTaskMgr.md#9800006-长时任务通知信息校验失败) |
| [9800007](../errorcode-backgroundTaskMgr.md#9800007-长时任务信息存储失败) |
