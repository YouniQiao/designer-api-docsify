# executeDelayed

## 导入模块

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## executeDelayed

```TypeScript
function executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>
```

延时执行任务。当前执行模式可以设置任务优先级，可通过cancel取消任务。使用Promise异步回调。

> **说明：**&gt;
> - 该任务不能是任务组任务、串行队列任务、异步队列任务或周期任务。
> - 如果任务不是长时任务，可以多次调用executeDelayed执行。
> - 如果是长时任务，则仅支持执行一次。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| delayTime | number | 是 |
| task | [Task](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | 是 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Object & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200028](../errorcode-utils.md#10200028-延时时间小于零) |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) |
| [10200051](../errorcode-utils.md#10200051-无法再次执行周期任务) |
| [10200057](../errorcode-utils.md#10200057-任务无法被两种api执行) |


## executeDelayed

```TypeScript
function executeDelayed<A extends Array<Object>, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise<R>
```

延时执行泛型任务，使用Promise异步回调。 executeDelayed任务的类型校验与GenericsTask的构造类型相关联，参数类型和返回值类型需与new GenericsTask时指定的类型保持一致。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| delayTime | number | 是 |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | 是 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;R & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200028](../errorcode-utils.md#10200028-延时时间小于零) |
| [10200051](../errorcode-utils.md#10200051-无法再次执行周期任务) |
| [10200057](../errorcode-utils.md#10200057-任务无法被两种api执行) |
