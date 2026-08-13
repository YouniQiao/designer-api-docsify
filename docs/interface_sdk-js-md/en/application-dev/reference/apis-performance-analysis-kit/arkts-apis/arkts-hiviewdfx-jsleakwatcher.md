# @ohos.hiviewdfx.jsLeakWatcher

/*
 Copyright (c) 2024 Huawei Device Co., Ltd.
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


**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace jsLeakWatcher--><!--Device-unnamed-declare namespace jsLeakWatcher-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

## Modules to Import

```TypeScript
import { jsLeakWatcher } from '@kit.PerformanceAnalysisKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [check](arkts-performanceanalysis-jsleakwatcher-check-f.md#check) | Obtains the list of objects that are leaked and registered using **jsLeakWatcher.watch()**. Objects that are not reclaimed after GC is triggered are marked as leaked. |
| [dump](arkts-performanceanalysis-jsleakwatcher-dump-f.md#dump) | Dumps the list of leaked objects and VM memory snapshot. |
| [enable](arkts-performanceanalysis-jsleakwatcher-enable-f.md#enable) | Enables the detection for JS object leaks. This function is disabled by default. |
| [enableLeakWatcher](arkts-performanceanalysis-jsleakwatcher-enableleakwatcher-f.md#enableLeakWatcher) | Enables the detection for JS object leaks. This function is disabled by default. This API can detect the JS object memory leak, which is simpler than the method that needs to call the **enable**, **watch**, **check**, and **dump** functions. If a memory leak occurs, the leaked file is returned through the callback. |
| [enableLeakWatcher](arkts-performanceanalysis-jsleakwatcher-enableleakwatcher-f.md#enableLeakWatcher) | Enables the ArkTS object leak detection. This API can detect memory leaks of ArkTS objects with a single call, which is simpler than the previous method that requires four functions (**enable**, **watch**, **check**, and **dump**). You can use the **configs** parameter to customize the properties of monitoring items, greatly improving the leak detection performance. |
| [watch](arkts-performanceanalysis-jsleakwatcher-watch-f.md#watch) | Registers the object to be checked. |

### Interfaces

| Name | Description |
| --- | --- |
| [LeakWatcherConfig](arkts-performanceanalysis-jsleakwatcher-leakwatcherconfig-i.md) | Defines the **LeakWatcherConfig** object, which contains multiple configurable properties for memory leak monitoring. |

### Enums

| Name | Description |
| --- | --- |
| [MonitorObjectType](arkts-performanceanalysis-jsleakwatcher-monitorobjecttype-e.md) | Enumerates the types of component objects to be monitored. |

