# isDebugState

## 导入模块

```TypeScript
```

## isDebugState

```TypeScript
function isDebugState(): boolean
```

获取应用进程的调试状态。

**起始版本：** 23

<!--Device-hidebug-function isDebugState(): boolean--><!--Device-hidebug-function isDebugState(): boolean-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

console.info(`isDebugState = ${hidebug.isDebugState()}`)
```
