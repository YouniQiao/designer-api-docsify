# @ohos.hiviewdfx.hiRetrieval

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

<!--Device-unnamed-declare namespace hiRetrieval--><!--Device-unnamed-declare namespace hiRetrieval-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

## Modules to Import

```TypeScript
import { hiRetrieval } from 'hiRetrieval';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getCurrentConfig](arkts-performanceanalysis-hiretrieval-getcurrentconfig-f.md#getcurrentconfig) | Query the current HiRetrieval config. |
| [getLastParticipationTimestamp](arkts-performanceanalysis-hiretrieval-getlastparticipationtimestamp-f.md#getlastparticipationtimestamp) | Query the UNIX timestamp of the last participating time. |
| [init](arkts-performanceanalysis-hiretrieval-init-f.md#init) | Init the HiRetrieval functionality. |
| [isParticipant](arkts-performanceanalysis-hiretrieval-isparticipant-f.md#isparticipant) | Query if the app is participating the HiRetrieval project. |
| [participate](arkts-performanceanalysis-hiretrieval-participate-f.md#participate) | Participate the HiRetrieval project with given HiRetrievalConfig. |
| [quit](arkts-performanceanalysis-hiretrieval-quit-f.md#quit) | Quit the HiRetrieval project. This operation clears the current HiRetrieval config. Invoking init function again is required after invoking quit function. |
| [run](arkts-performanceanalysis-hiretrieval-run-f.md#run) | Trigger the HiRetrieval functionality, make it start working. |

### Interfaces

| Name | Description |
| --- | --- |
| [HiRetrievalConfig](arkts-performanceanalysis-hiretrieval-hiretrievalconfig-i.md) | HiRetrieval functionality config. |

