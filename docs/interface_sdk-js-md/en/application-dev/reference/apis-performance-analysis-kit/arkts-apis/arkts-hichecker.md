# @ohos.hichecker

The HiChecker module allows you to check issues that may be easily ignored during development of applications (including system-built and third-party applications). Such issues include calling of time-consuming functions by key application threads, event distribution and execution timeout in application processes, and ability resource leakage in application processes. The issues are recorded in logs or lead to process crashes explicitly so that you can find and rectify them.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.HiviewDFX.HiChecker

## Modules to Import

```TypeScript
import { hichecker } from '@kit.PerformanceAnalysisKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addCheckRule](arkts-performanceanalysis-hichecker-addcheckrule-f.md) |
| [addRule](arkts-performanceanalysis-hichecker-addrule-f.md) |
| [contains](arkts-performanceanalysis-hichecker-contains-f.md) |
| [containsCheckRule](arkts-performanceanalysis-hichecker-containscheckrule-f.md) |
| [getRule](arkts-performanceanalysis-hichecker-getrule-f.md) |
| [removeCheckRule](arkts-performanceanalysis-hichecker-removecheckrule-f.md) |
| [removeRule](arkts-performanceanalysis-hichecker-removerule-f.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RULE_CAUTION_PRINT_LOG](arkts-performanceanalysis-hichecker-con.md#rule_caution_print_log) |
| [RULE_CAUTION_TRIGGER_CRASH](arkts-performanceanalysis-hichecker-con.md#rule_caution_trigger_crash) |
| [RULE_CHECK_ABILITY_CONNECTION_LEAK](arkts-performanceanalysis-hichecker-con.md#rule_check_ability_connection_leak) |
| [RULE_CHECK_ARKUI_PERFORMANCE](arkts-performanceanalysis-hichecker-con.md#rule_check_arkui_performance) |
| [RULE_THREAD_CHECK_NETWORK_USAGE](arkts-performanceanalysis-hichecker-con.md#rule_thread_check_network_usage) |
| [RULE_THREAD_CHECK_SLOW_PROCESS](arkts-performanceanalysis-hichecker-con.md#rule_thread_check_slow_process) |
