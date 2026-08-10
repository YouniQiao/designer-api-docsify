# @ohos.faultLogger(故障日志获取)

应用可以使用faultLogger接口查询系统侧缓存的当前应用的故障日志。接口以应用包名和系统分配的UID作为唯一键值。

系统侧保存的应用故障日志数量受系统日志的压力限制，推荐使用[@ohos.hiviewdfx.hiAppEvent](arkts-performanceanalysis-hiappevent-n.md)订阅APP_CRASH及APP_FREEZE等故障事件。

> **说明：**
> 
> 本模块接口从API version 18开始废弃使用, 该接口不再维护。后续版本推荐使用
> [@ohos.hiviewdfx.hiAppEvent](arkts-performanceanalysis-hiappevent-n.md)订阅APP_CRASH，APP_FREEZE事件。
> 
> 查阅[从Faultlogger接口迁移崩溃事件](../../../dfx/hiappevent-watcher-crash-events-arkts.md#从faultlogger接口迁移崩溃事件)，
> 了解使用hiAppEvent订阅APP_CRASH的具体信息。
> 
> 查阅[从Faultlogger接口迁移应用冻屏事件](../../../dfx/hiappevent-watcher-freeze-events-arkts.md#从faultlogger接口迁移应用冻屏事件)，
> 了解使用hiAppEvent订阅APP_FREEZE的具体信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** ohos.hiviewdfx.hiAppEvent

<!--Device-unnamed-declare namespace FaultLogger--><!--Device-unnamed-declare namespace FaultLogger-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

## Modules to Import

```TypeScript
import { FaultLogger } from 'kits/@kit.PerformanceAnalysisKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [query](arkts-performanceanalysis-faultlogger-query-f.md#query) | 获取当前应用故障信息，该方法通过回调方式获取故障信息数组，故障信息数组内最多上报10份故障信息。 |
| [query](arkts-performanceanalysis-faultlogger-query-f.md#query-1) | 获取当前应用故障信息，该方法通过Promise方式返回故障信息数组，故障信息数组内最多上报10份故障信息。 |
| [querySelfFaultLog](arkts-performanceanalysis-faultlogger-queryselffaultlog-f.md#queryselffaultlog) | 获取当前应用故障信息，该方法通过回调方式获取故障信息数组，故障信息数组内最多上报10份故障信息。 |
| [querySelfFaultLog](arkts-performanceanalysis-faultlogger-queryselffaultlog-f.md#queryselffaultlog-1) | 获取当前应用故障信息，该方法通过Promise方式返回故障信息数组，故障信息数组内最多上报10份故障信息。 |

### Interfaces

| Name | Description |
| --- | --- |
| [FaultLogInfo](arkts-performanceanalysis-faultlogger-faultloginfo-i.md) | 故障信息数据结构，获取到的故障信息的数据结构。 |

### Enums

| Name | Description |
| --- | --- |
| [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | 故障类型枚举。 |

