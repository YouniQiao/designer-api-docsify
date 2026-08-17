# BackgroundTaskStateInfo (System API)

Defines the authorization information of a continuous task.

**Since:** 24

<!--Device-backgroundTaskManager-interface BackgroundTaskStateInfo--><!--Device-backgroundTaskManager-interface BackgroundTaskStateInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'backgroundTaskManager';
```

## appIndex

```TypeScript
appIndex: int
```

AppIndex of the application applying for special continuous task.

**Type:** int

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundTaskStateInfo-appIndex: int--><!--Device-BackgroundTaskStateInfo-appIndex: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

## authResult

```TypeScript
authResult?: UserAuthResult
```

Type of user authorization status.

**Type:** UserAuthResult

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundTaskStateInfo-authResult?: UserAuthResult--><!--Device-BackgroundTaskStateInfo-authResult?: UserAuthResult-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

BundleName of the application applying for special continuous task.

**Type:** string

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundTaskStateInfo-bundleName: string--><!--Device-BackgroundTaskStateInfo-bundleName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

## userId

```TypeScript
userId: int
```

UserId of the application applying for special continuous task

**Type:** int

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundTaskStateInfo-userId: int--><!--Device-BackgroundTaskStateInfo-userId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

