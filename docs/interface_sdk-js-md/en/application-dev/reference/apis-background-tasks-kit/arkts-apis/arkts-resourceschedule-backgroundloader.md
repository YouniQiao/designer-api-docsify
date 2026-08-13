# @ohos.resourceschedule.backgroundLoader

/*
 Copyright (c) 2026 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace backgroundLoader--><!--Device-unnamed-declare namespace backgroundLoader-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## Modules to Import

```TypeScript
import { backgroundLoader } from '@kit.BackgroundTasksKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [finishTask](arkts-backgroundtasks-backgroundloader-finishtask-f.md#finishTask) | Finish background load task. |
| [getTaskInfo](arkts-backgroundtasks-backgroundloader-gettaskinfo-f.md#getTaskInfo) | Obtains the information of a background load task. This API returns the result via a promise. |
| [registerTask](arkts-backgroundtasks-backgroundloader-registertask-f.md#registerTask) | Register background load task. |
| [unregisterTask](arkts-backgroundtasks-backgroundloader-unregistertask-f.md#unregisterTask) | Unregister background load task. |

### Interfaces

| Name | Description |
| --- | --- |
| [TaskInfo](arkts-backgroundtasks-backgroundloader-taskinfo-i.md) | Represents the background load task information, which is used to register task. |
| [TaskStopInfo](arkts-backgroundtasks-backgroundloader-taskstopinfo-i.md) | Represents the background load task stop information, which is used to ON_STOP function. |

### Enums

| Name | Description |
| --- | --- |
| [StopCode](arkts-backgroundtasks-backgroundloader-stopcode-e.md) | Enumerates the stop code, which is used to ON_STOP function. |

### Constants

| Name | Description |
| --- | --- |
| [ON_START](arkts-backgroundtasks-backgroundloader-con.md#ON_START) | Start task method. |
| [ON_STOP](arkts-backgroundtasks-backgroundloader-con.md#ON_STOP) | Stop task method. |

