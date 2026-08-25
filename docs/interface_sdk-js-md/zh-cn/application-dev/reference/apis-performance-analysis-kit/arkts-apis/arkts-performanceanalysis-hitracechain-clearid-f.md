# clearId

## 导入模块

```TypeScript
import { hiTraceChain } from 'kits/@kit.PerformanceAnalysisKit';
```

## clearId

```TypeScript
function clearId(): void
```

清除跟踪标识，同步接口。用于在需要切断当前跟踪链的场景，例如业务逻辑分支不再需要跟踪、任务完成后清理跟踪标识、或者在开始新的跟踪前清理旧的 跟踪标识。将当前线程TLS中的HiTraceId设置为无效。

**起始版本：** 8

**系统能力：** SystemCapability.HiviewDFX.HiTrace
