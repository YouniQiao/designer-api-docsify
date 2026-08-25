# @ohos.hichecker

HiChecker可以作为应用开发阶段使用的检测工具，用于检测代码运行过程中部分易忽略的问题，如应用线程出现耗时调用、应用进程中Ability资源泄露等问题。开发者可以通过日志记录或进程crash等形式查看具体问题并进行修改，提升应用 的使用体验。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.HiviewDFX.HiChecker

## 导入模块

```TypeScript
import { hichecker } from '@kit.PerformanceAnalysisKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addCheckRule](arkts-performanceanalysis-hichecker-addcheckrule-f.md) |
| [addRule](arkts-performanceanalysis-hichecker-addrule-f.md) |
| [contains](arkts-performanceanalysis-hichecker-contains-f.md) |
| [containsCheckRule](arkts-performanceanalysis-hichecker-containscheckrule-f.md) |
| [getRule](arkts-performanceanalysis-hichecker-getrule-f.md) |
| [removeCheckRule](arkts-performanceanalysis-hichecker-removecheckrule-f.md) |
| [removeRule](arkts-performanceanalysis-hichecker-removerule-f.md) |

### 常量

| 名称 |
| --- |
| [RULE_CAUTION_PRINT_LOG](arkts-performanceanalysis-hichecker-con.md#rule_caution_print_log) |
| [RULE_CAUTION_TRIGGER_CRASH](arkts-performanceanalysis-hichecker-con.md#rule_caution_trigger_crash) |
| [RULE_CHECK_ABILITY_CONNECTION_LEAK](arkts-performanceanalysis-hichecker-con.md#rule_check_ability_connection_leak) |
| [RULE_CHECK_ARKUI_PERFORMANCE](arkts-performanceanalysis-hichecker-con.md#rule_check_arkui_performance) |
| [RULE_THREAD_CHECK_NETWORK_USAGE](arkts-performanceanalysis-hichecker-con.md#rule_thread_check_network_usage) |
| [RULE_THREAD_CHECK_SLOW_PROCESS](arkts-performanceanalysis-hichecker-con.md#rule_thread_check_slow_process) |
