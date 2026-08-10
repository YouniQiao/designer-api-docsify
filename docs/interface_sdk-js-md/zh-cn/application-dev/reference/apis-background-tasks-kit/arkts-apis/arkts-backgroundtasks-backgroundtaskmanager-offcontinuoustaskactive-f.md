# offContinuousTaskActive

## 导入模块

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## offContinuousTaskActive

```TypeScript
function offContinuousTaskActive(callback?: Callback<ContinuousTaskActiveInfo>): void
```

取消长时任务激活的监听，使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function offContinuousTaskActive(callback?: Callback<ContinuousTaskActiveInfo>): void--><!--Device-backgroundTaskManager-function offContinuousTaskActive(callback?: Callback<ContinuousTaskActiveInfo>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ContinuousTaskActiveInfo&gt; | 否 | the callback of continuous task active. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 9800005 | Continuous task verification failed. |
| 201 | Permission denied. |

