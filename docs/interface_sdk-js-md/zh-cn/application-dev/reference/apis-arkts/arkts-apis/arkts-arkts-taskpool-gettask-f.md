# getTask

## 导入模块

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## getTask

```TypeScript
function getTask(taskId: number, taskName?: string): Task | undefined
```

通过taskId或taskId与taskName获取对应的Task实例。

> **说明：**&gt;
> - 如果传入的taskId查询不到对应的Task实例，则会返回undefined；&gt;
> - 如果传入的taskId能够查询到对应的Task实例，但是调用getTask方法的线程和创建Task实例的线程不一致，则会返回undefined；&gt;
> - 如果同时传入taskId和taskName，通过taskId查询到的Task实例的name和传入的taskName不一致，则会返回undefined。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| taskId | number | 是 |
| taskName | string | 否 |

**返回值：**

| 类型 |
| --- |
| Task \| undefined |
