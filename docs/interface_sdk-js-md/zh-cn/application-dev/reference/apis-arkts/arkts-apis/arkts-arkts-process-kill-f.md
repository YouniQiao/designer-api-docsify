# kill

## 导入模块

```TypeScript
import { process } from '@kit.ArkTS';
```

## kill

```TypeScript
function kill(signal: number, pid: number): boolean
```

发送信号到指定进程，结束该进程。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [kill](arkts-arkts-process-processmanager-c.md#kill)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [signal](arkts-arkts-locks-asynclockoptions-c.md) | number | 是 |
| pid | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
let pid = process.pid;
let result = process.kill(28, pid);
```

```TypeScript
// 创建ProcessManager实例
let processManager = new process.ProcessManager();
// 获取当前进程pid
let pres = process.pid;
// 发送信号28结束当前进程
let result = processManager.kill(28, pres);
```
