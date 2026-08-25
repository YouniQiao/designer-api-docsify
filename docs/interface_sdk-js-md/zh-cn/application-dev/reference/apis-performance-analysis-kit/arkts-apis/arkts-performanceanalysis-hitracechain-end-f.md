# end

## 导入模块

```TypeScript
import { hiTraceChain } from 'kits/@kit.PerformanceAnalysisKit';
```

## end

```TypeScript
function end(id: HiTraceId): void
```

结束跟踪，同步接口。用于在业务流程的结束节点终止分布式跟踪，例如在请求处理完成返回结果、用户操作流程结束、后台任务执行完毕等场景。若给定的HiTraceId有效，且等于当前线程TLS中的HiTraceId，结束跟踪并将当前线程TLS中的HiTraceId设置为无效。若给定的HiTraceId无效，或不等于当前线程TLS中的HiTraceId，结束跟踪失败，打印结束跟踪失败hilog日志。

**起始版本：** 8

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | [HiTraceId](arkts-performanceanalysis-hitracechain-hitraceid-i.md) | 是 |
