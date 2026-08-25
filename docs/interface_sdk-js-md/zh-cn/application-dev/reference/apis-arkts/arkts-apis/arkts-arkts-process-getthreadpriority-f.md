# getThreadPriority

## 导入模块

```TypeScript
import { process } from '@kit.ArkTS';
```

## getThreadPriority

```TypeScript
function getThreadPriority(v: number): number
```

根据指定的 tid 获取线程优先级，优先级顺序取决于当前操作系统。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [getThreadPriority](arkts-arkts-process-processmanager-c.md#getthreadpriority)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| v | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
let tid = process.tid;
let pres = process.getThreadPriority(tid);
```

```TypeScript
// 创建ProcessManager实例
let processManager = new process.ProcessManager();
// 获取当前线程tid
let tid = process.tid;
// 根据tid获取线程优先级
let pres = processManager.getThreadPriority(tid);
```
