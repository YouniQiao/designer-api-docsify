# @ohos.faultLogger(故障日志获取)

应用可以使用faultLogger接口查询系统侧缓存的当前应用的故障日志。接口以应用包名和系统分配的UID作为唯一键值。系统侧保存的应用故障日志数量受系统日志的压力限制， 推荐使用[@ohos.hiviewdfx.hiAppEvent](arkts-performanceanalysis-hiappevent-n.md) 订阅APP_CRASH及APP_FREEZE等故障事件。详见： - [从Faultlogger接口迁移崩溃事件](../../../dfx/hiappevent-watcher-crash-events-arkts.md#从faultlogger接口迁移崩溃事件) - [从Faultlogger接口迁移应用冻屏事件](../../../dfx/hiappevent-watcher-freeze-events-arkts.md#从faultlogger接口迁移应用冻屏事件)

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 18

**替代接口：** hiAppEvent

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

## 导入模块

```TypeScript
import { FaultLogger } from '@kit.PerformanceAnalysisKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [query(故障日志获取)](arkts-performanceanalysis-faultlogger-query-f.md) |
| [query(故障日志获取)](arkts-performanceanalysis-faultlogger-query-f.md) |
| [querySelfFaultLog(故障日志获取)](arkts-performanceanalysis-faultlogger-queryselffaultlog-f.md) |
| [querySelfFaultLog(故障日志获取)](arkts-performanceanalysis-faultlogger-queryselffaultlog-f.md) |

### 接口

| 名称 |
| --- |
| [FaultLogInfo(故障日志获取)](arkts-performanceanalysis-faultlogger-faultloginfo-i.md) |

### 枚举

| 名称 |
| --- |
| [FaultType(故障日志获取)](arkts-performanceanalysis-faultlogger-faulttype-e.md) |
