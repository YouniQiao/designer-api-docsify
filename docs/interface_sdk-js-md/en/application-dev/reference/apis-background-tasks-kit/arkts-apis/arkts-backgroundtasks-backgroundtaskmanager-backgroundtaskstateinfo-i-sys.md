# BackgroundTaskStateInfo (System API)

Defines the authorization information of a continuous task.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

<!--Device-backgroundTaskManager-interface BackgroundTaskStateInfo--><!--Device-backgroundTaskManager-interface BackgroundTaskStateInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## appIndex

```TypeScript
appIndex: int
```

AppIndex of the application applying for special continuous task.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundTaskStateInfo-appIndex: int--><!--Device-BackgroundTaskStateInfo-appIndex: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

## authResult

```TypeScript
authResult?: UserAuthResult
```

Type of user authorization status.

**Type:** [UserAuthResult](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-userauthresult-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

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

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundTaskStateInfo-bundleName: string--><!--Device-BackgroundTaskStateInfo-bundleName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

## userId

```TypeScript
userId: int
```

UserId of the application applying for special continuous task

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundTaskStateInfo-userId: int--><!--Device-BackgroundTaskStateInfo-userId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**System API:** This is a system API.

