# @ohos.app.ability.appMemoryOptimizer

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace appMemoryOptimizer--><!--Device-unnamed-declare namespace appMemoryOptimizer-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { appMemoryOptimizer } from '@kit.AbilityKit';
import { appMemoryOptimizer } from '@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [evictFilePages](arkts-ability-appmemoryoptimizer-evictfilepages-f.md#evictfilepages) | Sends a request to the system to release file page cache of specified files. The system determines whether to actually perform the release based on the current memory status, and success is not guaranteed. |
| [evictModuleFilePages](arkts-ability-appmemoryoptimizer-evictmodulefilepages-f.md#evictmodulefilepages) | Sends a request to the system to release file page cache of specified modules. The system determines whether to actually perform the release based on the current memory status, and success is not guaranteed. The system reads the memory_optimizer.json configuration file of the corresponding module, obtains the evictFilePages array, and performs file page cache eviction on the files in the array. Configuration file path: {Module directory}/src/main/resources/rawfile/memory_optimizer.json File names in the evictFilePages array of the configuration file must end with .so, .hap, or .hsp. |

