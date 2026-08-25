# createSpan

## 导入模块

```TypeScript
import { hiTraceChain } from 'kits/@kit.PerformanceAnalysisKit';
```

## createSpan

```TypeScript
function createSpan(): HiTraceId
```

创建跟踪分支，同步接口。用于在业务流程中标记重要的子流程，例如在请求处理过程中的关键步骤、服务端处理链中的各个阶段、或者需要重点关注的业务 分支。创建一个HiTraceId，使用当前线程TLS中的chainId、spanId初始化HiTraceId的chainId、parentSpanId，并为HiTraceId生成一个新的spanId， 返回该HiTraceId。

**起始版本：** 8

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**返回值：**

| 类型 |
| --- |
| [HiTraceId](arkts-performanceanalysis-hitracechain-hitraceid-i.md) |
