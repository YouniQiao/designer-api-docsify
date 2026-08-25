# setMinLogLevel

## 导入模块

```TypeScript
import { hilog } from 'kits/@kit.PerformanceAnalysisKit';
```

## setMinLogLevel

```TypeScript
function setMinLogLevel(level: LogLevel): void
```

设置应用日志打印的最低日志级别，用于拦截低级别日志打印。

> **注意：**&gt;
> 如果设置的日志级别低于[全局日志级别](../../../dfx/hilog.md#查看和设置日志级别)，设置不生效。&gt;
> debug版本应用下，此函数不生效。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| level | [LogLevel](arkts-performanceanalysis-hilog-loglevel-e.md) | 是 |
