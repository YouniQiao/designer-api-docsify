# check

## 导入模块

```TypeScript
import { jsLeakWatcher } from '@kit.PerformanceAnalysisKit';
```

## check

```TypeScript
function check(): string
```

获取已通过jsLeakWatcher.watch注册发生泄漏的对象列表，触发GC后未被回收的对象会被标记为泄漏。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为26.1.0。

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
let leakObjlist:string = jsLeakWatcher.check();
```
