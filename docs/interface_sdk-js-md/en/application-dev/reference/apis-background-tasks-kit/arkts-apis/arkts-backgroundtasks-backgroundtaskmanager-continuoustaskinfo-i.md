# ContinuousTaskInfo

长时任务信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-backgroundTaskManager-interface ContinuousTaskInfo--><!--Device-backgroundTaskManager-interface ContinuousTaskInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## abilityId

```TypeScript
abilityId: int
```

UIAbility ID.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskInfo-abilityId: int--><!--Device-ContinuousTaskInfo-abilityId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## abilityName

```TypeScript
abilityName: string
```

UIAbility名称。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskInfo-abilityName: string--><!--Device-ContinuousTaskInfo-abilityName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## appIndex

```TypeScript
appIndex?: int
```

应用分身ID。取值范围为全体整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 24.

<!--Device-ContinuousTaskInfo-appIndex?: int--><!--Device-ContinuousTaskInfo-appIndex?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## backgroundModes

```TypeScript
backgroundModes: string[]
```

[长时任务类型](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-e.md)。

**Type:** string[]

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskInfo-backgroundModes: string[]--><!--Device-ContinuousTaskInfo-backgroundModes: string[]-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## backgroundSubModes

```TypeScript
backgroundSubModes: string[]
```

[长时任务子类型](arkts-backgroundtasks-backgroundtaskmanager-backgroundsubmode-e.md)。

**Type:** string[]

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskInfo-backgroundSubModes: string[]--><!--Device-ContinuousTaskInfo-backgroundSubModes: string[]-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## bundleName

```TypeScript
bundleName?: string
```

应用包名。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn since version 23; ArkTS-Sta since version 24.

<!--Device-ContinuousTaskInfo-bundleName?: string--><!--Device-ContinuousTaskInfo-bundleName?: string-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## continuousTaskId

```TypeScript
continuousTaskId: int
```

长时任务ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskInfo-continuousTaskId: int--><!--Device-ContinuousTaskInfo-continuousTaskId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## isFromWebView

```TypeScript
isFromWebView: boolean
```

是否通过Webview方式申请，即通过系统代理应用申请长时任务。true表示通过Webview方式申请，false表示不通过Webview方式申请。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskInfo-isFromWebView: boolean--><!--Device-ContinuousTaskInfo-isFromWebView: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## notificationId

```TypeScript
notificationId: int
```

通知 Id。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskInfo-notificationId: int--><!--Device-ContinuousTaskInfo-notificationId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## pid

```TypeScript
pid: int
```

应用进程的PID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskInfo-pid: int--><!--Device-ContinuousTaskInfo-pid: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## suspendState

```TypeScript
suspendState: boolean
```

申请的长时任务是否处于暂停状态。true表示处于暂停状态，false表示处于激活状态。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskInfo-suspendState: boolean--><!--Device-ContinuousTaskInfo-suspendState: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## uid

```TypeScript
uid: int
```

应用的UID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskInfo-uid: int--><!--Device-ContinuousTaskInfo-uid: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## wantAgentAbilityName

```TypeScript
wantAgentAbilityName: string
```

[WantAgent](../../apis-ability-kit/arkts-apis/arkts-app-ability-wantagent.md/arkts-app-ability-wantagent.md) 配置的ability名称。WantAgent为通知参数，用于指定点击长时任务通知后跳转的界面，在申请长时任务时作为参数传入。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskInfo-wantAgentAbilityName: string--><!--Device-ContinuousTaskInfo-wantAgentAbilityName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## wantAgentBundleName

```TypeScript
wantAgentBundleName: string
```

[WantAgent](../../apis-ability-kit/arkts-apis/arkts-app-ability-wantagent.md/arkts-app-ability-wantagent.md) 配置的包名。WantAgent为通知参数，用于指定点击长时任务通知后跳转的界面，在申请长时任务时作为参数传入。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskInfo-wantAgentBundleName: string--><!--Device-ContinuousTaskInfo-wantAgentBundleName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

