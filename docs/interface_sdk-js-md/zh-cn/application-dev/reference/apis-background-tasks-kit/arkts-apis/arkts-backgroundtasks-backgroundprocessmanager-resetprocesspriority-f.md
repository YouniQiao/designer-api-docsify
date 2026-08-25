# resetProcessPriority

## 导入模块

```TypeScript
import { backgroundProcessManager } from 'kits/@kit.BackgroundTasksKit';
```

## resetProcessPriority

```TypeScript
function resetProcessPriority(pid: number): Promise<void>
```

为子进程解压制，即子进程策略恢复为主进程调度策略。若主进程调度策略发生变化，如从后台切至前台等， 子进程会跟随主进程一同变化，等效于执行一次resetProcessPriority动作。使用Promise异步回调。

**起始版本：** 17

**系统能力：** SystemCapability.Resourceschedule.BackgroundProcessManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pid | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
