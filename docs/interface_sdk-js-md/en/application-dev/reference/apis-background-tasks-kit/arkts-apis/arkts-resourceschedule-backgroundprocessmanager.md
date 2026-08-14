# @ohos.resourceschedule.backgroundProcessManager(Background Child Process Management)

/*
 Copyright (c) 2025 Huawei Device Co., Ltd.
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


**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace backgroundProcessManager--><!--Device-unnamed-declare namespace backgroundProcessManager-End-->

**System capability:** SystemCapability.Resourceschedule.BackgroundProcessManager

## Modules to Import

```TypeScript
import { backgroundProcessManager } from 'backgroundProcessManager';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getPowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-getpowersavemode-f.md#getPowerSaveMode) | Obtains the power saving mode of a process. This API uses a promise to return the result. |
| [isPowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-ispowersavemode-f.md#isPowerSaveMode) | Queries whether the process is in power saving mode. This API uses a promise to return the result. |
| [resetProcessPriority](arkts-backgroundtasks-backgroundprocessmanager-resetprocesspriority-f.md#resetProcessPriority) | Unsuppresses the child process. In this case, the child process follows the scheduling policy of the main process. If the scheduling policy of the main process changes, for example, from the background to the foreground , the child process changes with the main process. The effect is the same as calling **resetProcessPriority**. |
| [setPowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-setpowersavemode-f.md#setPowerSaveMode) | Sets the power saving mode for a process. This API uses a promise to return the result. You can set to enter the power saving mode when: - The application is not focused, and there are no audio operations or UI updates. - The application cannot obtain the power lock through the system framework. - The application needs to perform time-consuming computing tasks, such as compression, decompression, and compilation, which are significantly restricted by CPU resources. (In this case, the power saving mode will be enabled forcibly.) |
| [setProcessPriority](arkts-backgroundtasks-backgroundprocessmanager-setprocesspriority-f.md#setProcessPriority) | Sets the child process priority. After a child process is suppressed, the CPU resources that can be obtained will be limited. If the scheduling policy of the main process changes, for example, from the background to the foreground, the child process changes with the main process. To suppress the child process, call this API again. |

### Enums

| Name | Description |
| --- | --- |
| [PowerSaveMode](arkts-backgroundtasks-backgroundprocessmanager-powersavemode-e.md) | Specifies the power saving mode. |
| [ProcessPriority](arkts-backgroundtasks-backgroundprocessmanager-processpriority-e.md) | Specifies the child process priority. |

