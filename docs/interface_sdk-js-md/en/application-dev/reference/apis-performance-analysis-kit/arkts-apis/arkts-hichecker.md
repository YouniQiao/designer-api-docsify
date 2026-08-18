# @ohos.hichecker

/*
 Copyright (c) 2022 Huawei Device Co., Ltd.
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

<!--Device-unnamed-declare namespace hichecker--><!--Device-unnamed-declare namespace hichecker-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

## Modules to Import

```TypeScript
import { hichecker } from '@kit.PerformanceAnalysisKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addCheckRule](arkts-performanceanalysis-hichecker-addcheckrule-f.md#addcheckrule) | Adds one or more check rules. HiChecker detects unexpected operations or gives feedback based on the added rules. You can use **grep HiChecker** to check for the application running information in the hilog. |
| [addRule](arkts-performanceanalysis-hichecker-addrule-f.md#addrule) | Adds one or more rules. HiChecker detects unexpected operations or gives feedback based on the added rules. |
| [contains](arkts-performanceanalysis-hichecker-contains-f.md#contains) | Checks whether the specified rule exists in the collection of added rules. If the rule is of the thread level, this operation is performed only on the current thread. |
| [containsCheckRule](arkts-performanceanalysis-hichecker-containscheckrule-f.md#containscheckrule) | Checks whether the specified rule exists in the collection of added rules. If the rule is of the thread level, this operation is performed only on the current thread. |
| [getRule](arkts-performanceanalysis-hichecker-getrule-f.md#getrule) | Obtains a collection of thread, process, and alarm rules that have been added. |
| [removeCheckRule](arkts-performanceanalysis-hichecker-removecheckrule-f.md#removecheckrule) | Removes one or more rules. The removed rules will become ineffective. |
| [removeRule](arkts-performanceanalysis-hichecker-removerule-f.md#removerule) | Removes one or more rules. The removed rules will become ineffective. |

### Constants

| Name | Description |
| --- | --- |
| [RULE_CAUTION_PRINT_LOG](arkts-performanceanalysis-hichecker-con.md#rulecautionprintlog) | Alarm rule, which is programmed to print a log when an alarm is generated. |
| [RULE_CAUTION_TRIGGER_CRASH](arkts-performanceanalysis-hichecker-con.md#rulecautiontriggercrash) | Alarm rule, which is programmed to force the application to exit when an alarm is generated. |
| [RULE_CHECK_ABILITY_CONNECTION_LEAK](arkts-performanceanalysis-hichecker-con.md#rulecheckabilityconnectionleak) | Caution rule, which is programmed to detect whether ability leakage has occurred. |
| [RULE_CHECK_ARKUI_PERFORMANCE](arkts-performanceanalysis-hichecker-con.md#rulecheckarkuiperformance) | Caution rule, which is programmed to detect the ArkUI performance. |
| [RULE_THREAD_CHECK_NETWORK_USAGE](arkts-performanceanalysis-hichecker-con.md#rulethreadchecknetworkusage) | The thread rule check network usage. |
| [RULE_THREAD_CHECK_SLOW_PROCESS](arkts-performanceanalysis-hichecker-con.md#rulethreadcheckslowprocess) | Caution rule, which is programmed to detect whether any time-consuming function is invoked. |

