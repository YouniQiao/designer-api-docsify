# getId

## 导入模块

```TypeScript
import { hiTraceChain } from 'kits/@kit.PerformanceAnalysisKit';
```

## getId

```TypeScript
function getId(): HiTraceId
```

获取跟踪标识，同步接口。用于在需要传递当前跟踪标识的场景，例如将跟踪标识传递给子线程、传递给其他进程、或者在日志中记录当前跟踪标识。获取当前线程TLS中的HiTraceId。若当前线程TLS中不存在有效的HiTraceId，返回各属性值均为0的无效HiTraceId。

**起始版本：** 8

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**返回值：**

| 类型 |
| --- |
| [HiTraceId](arkts-performanceanalysis-hitracechain-hitraceid-i.md) |
