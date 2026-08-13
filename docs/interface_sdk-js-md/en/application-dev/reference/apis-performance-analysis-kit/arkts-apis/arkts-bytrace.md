# @ohos.bytrace(Performance Tracing)

/*
 Copyright (C) 2021 Huawei Device Co., Ltd.
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


**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 8

**Substitutes:** [hiTraceMeter](arkts-hitracemeter.md#@ohos.hiTraceMeter(Performance-Tracing))

<!--Device-unnamed-declare namespace bytrace--><!--Device-unnamed-declare namespace bytrace-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## Summary

### Functions

| Name | Description |
| --- | --- |
| [finishTrace](arkts-performanceanalysis-bytrace-finishtrace-f.md#finishTrace) | Marks the end of a timeslice trace task. > **NOTE：**> > To stop a trace task, the values of name and task ID in **finishTrace** must be the same as those in > **startTrace**. |
| [startTrace](arkts-performanceanalysis-bytrace-starttrace-f.md#startTrace) | Marks the start of a timeslice trace task. > **NOTE：**> > If multiple trace tasks with the same name need to be performed at the same time or a trace task needs to be > performed multiple times concurrently, different task IDs must be specified in **startTrace**. If the trace tasks > with the same name are not performed at the same time, the same task ID can be used. For details, see the > bytrace.finishTrace example. |
| [traceByValue](arkts-performanceanalysis-bytrace-tracebyvalue-f.md#traceByValue) | Defines a numeric variable that indicates the number of timeslice trace tasks. |

