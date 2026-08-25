# getTaskPoolInfo

## 导入模块

```TypeScript
import { taskpool } from '@kit.ArkTS';
```

## getTaskPoolInfo

```TypeScript
function getTaskPoolInfo(): TaskPoolInfo
```

获取任务池的线程信息和任务信息。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [TaskPoolInfo](arkts-arkts-taskpool-taskpoolinfo-c.md) |

**示例**

```TypeScript
let taskpoolInfo: taskpool.TaskPoolInfo = taskpool.getTaskPoolInfo();
```
