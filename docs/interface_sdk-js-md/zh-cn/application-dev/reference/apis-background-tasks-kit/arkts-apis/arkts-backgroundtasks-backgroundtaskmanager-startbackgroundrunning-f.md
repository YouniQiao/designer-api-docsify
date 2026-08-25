# startBackgroundRunning

## 导入模块

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## startBackgroundRunning

```TypeScript
function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void
```

申请长时任务，支持申请一种类型，使用callback异步回调。长时任务申请成功后，会有通知栏消息，没有提示音。一个UIAbility（FA模型则为ServiceAbility）同一时刻仅支持通过本接口支持申请一个长时任务，可以通过 API version 21新增接口 [startBackgroundRunning](#startbackgroundrunning) 申请多个长时任务。

**起始版本：** 9

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| bgMode | [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-e.md) | 是 |
| wantAgent | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-内存操作失败) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |
| [9800003](../errorcode-backgroundTaskMgr.md#9800003-ipc通信失败) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-长时任务校验失败) |
| [9800006](../errorcode-backgroundTaskMgr.md#9800006-长时任务通知信息校验失败) |
| [9800007](../errorcode-backgroundTaskMgr.md#9800007-长时任务信息存储失败) |


## startBackgroundRunning

```TypeScript
function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>
```

申请长时任务，支持申请一种类型，使用Promise异步回调。长时任务申请成功后，会有通知栏消息，没有提示音。一个UIAbility（FA模型则为ServiceAbility）同一时刻仅支持通过本接口支持申请一个长时任务，可以通过 API version 21新增接口 [startBackgroundRunning](#startbackgroundrunning) 申请多个长时任务。

**起始版本：** 9

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| bgMode | [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-e.md) | 是 |
| wantAgent | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9800001](../errorcode-backgroundTaskMgr.md#9800001-内存操作失败) |
| [9800002](../errorcode-backgroundTaskMgr.md#9800002-parcel读写操作失败) |
| [9800003](../errorcode-backgroundTaskMgr.md#9800003-ipc通信失败) |
| [9800004](../errorcode-backgroundTaskMgr.md#9800004-系统服务失败) |
| [9800005](../errorcode-backgroundTaskMgr.md#9800005-长时任务校验失败) |
| [9800006](../errorcode-backgroundTaskMgr.md#9800006-长时任务通知信息校验失败) |
| [9800007](../errorcode-backgroundTaskMgr.md#9800007-长时任务信息存储失败) |


## startBackgroundRunning

```TypeScript
function startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent): Promise<ContinuousTaskNotification>
```

申请长时任务，支持申请多种类型，使用Promise异步回调。长时任务申请成功后，会有通知栏消息，没有提示音。一个UIAbility（FA模型则为ServiceAbility）同一时刻仅支持通过本接口支持申请一个长时任务，可以通过 API version 21新增接口 [startBackgroundRunning](#startbackgroundrunning) 申请多个长时任务。

**起始版本：** 12

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| bgModes | string[] | 是 |
| wantAgent | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | 是 |

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


## startBackgroundRunning

```TypeScript
function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>
```

申请长时任务，一个UIAbility（FA模型则为ServiceAbility）下支持通过本接口申请多个长时任务，使用Promise异步回调。通过本接口申请长时任务时，支持与已存在的长时任务合并通知，具体请参考 [ContinuousTaskRequest](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskrequest-c.md)。&lt;/br&gt;同一时间最多可存在10个长时任务，长时任务申请成功后，会有通知栏消息， 没有提示音。&lt;/br&gt;如果通过本接口申请的一个长时任务中同时包含多种类型，且包含数据传输类型，则在通知栏会发送2个长时任务通知，一个为数据传输类型，另一个为其他类型的合并通知。任意一个通知被移除时，长时任务取消，且另一个通知也会同 步移除。接口返回的长时任务通知Id为数据传输类型的Id，主要用于数据传输的进度更新。

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
