# check

## 导入模块

```TypeScript
import { jsLeakWatcher } from 'kits/@kit.PerformanceAnalysisKit';
```

## check

```TypeScript
function check(): string
```

获取已通过jsLeakWatcher.watch注册发生泄漏的对象列表，触发GC后未被回收的对象会被标记为泄漏。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**返回值：**

| 类型 |
| --- |
| string |
