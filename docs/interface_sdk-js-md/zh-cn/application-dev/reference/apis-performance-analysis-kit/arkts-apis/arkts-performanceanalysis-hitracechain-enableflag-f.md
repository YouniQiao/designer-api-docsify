# enableFlag

## 导入模块

```TypeScript
import { hiTraceChain } from 'kits/@kit.PerformanceAnalysisKit';
```

## enableFlag

```TypeScript
function enableFlag(id: HiTraceId, flag: HiTraceFlag): void
```

启用HiTraceId中指定的跟踪标志，同步接口。用于在业务流程中动态调整跟踪行为，例如在调试时启用TP_INFO标志以打印埋点信息、在需要跟踪异步调用时 启用INCLUDE_ASYNC标志、在需要禁用日志关联时启用DISABLE_LOG标志。

**起始版本：** 8

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | [HiTraceId](arkts-performanceanalysis-hitracechain-hitraceid-i.md) | 是 |
| flag | [HiTraceFlag](arkts-performanceanalysis-hitracechain-hitraceflag-e.md) | 是 |
