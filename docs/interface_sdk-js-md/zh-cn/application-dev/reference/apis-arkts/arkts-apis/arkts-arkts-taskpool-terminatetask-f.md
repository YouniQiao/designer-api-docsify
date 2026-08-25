# terminateTask

## 导入模块

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## terminateTask

```TypeScript
function terminateTask(longTask: LongTask): void
```

终止任务池中的长时任务，在长时任务执行完成后调用。终止后，执行长时任务的线程可能会被回收。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| longTask | [LongTask](arkts-arkts-taskpool-longtask-c.md) | 是 |
