# execute

## 导入模块

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## execute

```TypeScript
function execute(func: Function, ...args: Object[]): Promise<Object>
```

将待执行的函数放入taskpool的内部任务队列，函数不会立即执行，而是等待分发到工作线程执行。在当前执行模式下， 不支持取消任务。使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| func | Function | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;unknown & gt; |
| Promise & lt;Object & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200003](../errorcode-utils.md#10200003-worker初始化失败) |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) |


## execute

```TypeScript
function execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>
```

校验并发函数的参数类型和返回类型后，将函数添加到taskpool的任务队列。在当前执行模式下，不支持取消任务。使用Promise异步回调。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| func | (...args: A) = & gt; R \ | Promise & lt;R & gt; | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | A | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;R & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) |


## execute

```TypeScript
function execute(task: Task, priority?: Priority): Promise<Object>
```

将创建好的任务添加到taskpool的内部任务队列中，任务不会立即执行，而是等待分发到工作线程执行。当前模式支持设置任务优先级和通过cancel取消任务。使用Promise异步回调。

> **说明：**&gt;
> - 任务不能是任务组任务、串行队列任务或异步队列任务。
> - 长时任务只能调用一次，非长时任务可以多次调用执行。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | [Task](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | 是 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;unknown & gt; |
| Promise & lt;Object & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200003](../errorcode-utils.md#10200003-worker初始化失败) |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) |
| [10200051](../errorcode-utils.md#10200051-无法再次执行周期任务) |
| [10200057](../errorcode-utils.md#10200057-任务无法被两种api执行) |


## execute

```TypeScript
function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>
```

将创建好的泛型任务放入taskpool的内部任务队列，校验任务的参数类型和返回值类型。使用Promise异步回调。 execute任务的校验是结合**new GenericsTask**一起用的，参数、返回值类型需与**new GenericsTask**中的类型保持一致。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | 是 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;R & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) |
| [10200051](../errorcode-utils.md#10200051-无法再次执行周期任务) |
| [10200057](../errorcode-utils.md#10200057-任务无法被两种api执行) |


## execute

```TypeScript
function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>
```

将创建好的任务组放入taskpool内部任务队列，任务组中的任务不会立即执行，而是等待分发到工作线程执行。任务组中任务全部执行完成后， 结果数组统一返回。此模式适用于执行关联任务。使用Promise异步回调。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| group | [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) | 是 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Object[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |
| [10200059](../errorcode-utils.md#10200059-任务组不能重复执行) |


## execute

```TypeScript
function execute(task: Task, configs: Configs): Promise<Object>
```

将创建好的任务添加到taskpool的内部任务队列中，任务不会立即执行，而是等待分发到工作线程执行。当前模式支持设置任务优先级、设置超时时间和通过cancel取消任务。使用Promise异步回调。

> **说明：**&gt;
> - 不支持执行任务组任务。&gt;
> - 不支持执行串行队列任务。&gt;
> - 不支持执行异步队列任务。&gt;
> - 不支持执行周期性任务。&gt;
> - 不支持执行延迟任务。&gt;
> - 不支持执行存在依赖的任务。&gt;
> - 不支持任务重复执行。&gt;
> - 设置过超时的任务无法被其他任务依赖，也无法依赖其他任务。&gt;
> - 如果任务设置了失败监听，任务执行超时了，失败监听不会被触发。&gt;
> - 如果任务使用sendData来往宿主线程发消息，任务超时之后，宿主线程不再接收到消息。&gt;
> - 在抛出超时异常信息之后，执行中的任务还是会在线程中继续执行，但是最终不会返回执行结果。

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | [Task](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | 是 |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Object & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) |
| [10200051](../errorcode-utils.md#10200051-无法再次执行周期任务) |
| [10200057](../errorcode-utils.md#10200057-任务无法被两种api执行) |
| [10200058](../errorcode-utils.md#10200058-任务执行超时) |


## execute

```TypeScript
function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, configs: Configs): Promise<R>
```

将创建好的泛型任务放入taskpool的内部任务队列，使用Promise异步回调。 execute任务的类型校验与GenericsTask的构造类型相关联，参数类型和返回值类型需与new GenericsTask时指定的类型保持一致。

> **说明：**&gt;
> - 不支持执行任务组任务。&gt;
> - 不支持执行串行队列任务。&gt;
> - 不支持执行异步队列任务。&gt;
> - 不支持执行周期性任务。&gt;
> - 不支持执行延迟任务。&gt;
> - 不支持执行存在依赖的任务。&gt;
> - 不支持任务重复执行。&gt;
> - 设置过超时的任务无法被其他任务依赖，也无法依赖其他任务。&gt;
> - 如果任务设置了失败监听，任务执行超时了，失败监听不会被触发。&gt;
> - 如果任务使用sendData来往宿主线程发消息，任务超时之后，宿主线程不再接收到消息。&gt;
> - 在抛出超时异常信息之后，执行中的任务还是会在线程中继续执行，但是最终不会返回执行结果。

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | 是 |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;R & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |
| [10200014](../errorcode-utils.md#10200014-非concurrent函数错误) |
| [10200051](../errorcode-utils.md#10200051-无法再次执行周期任务) |
| [10200057](../errorcode-utils.md#10200057-任务无法被两种api执行) |
| [10200058](../errorcode-utils.md#10200058-任务执行超时) |


## execute

```TypeScript
function execute(group: TaskGroup, configs: Configs): Promise<Object[]>
```

将创建好的任务组放入taskpool内部任务队列，任务组中的任务不会立即执行，而是等待分发到工作线程执行。任务组中任务全部执行完成后，结果数组统一返回。此模式适用于执行关联任务。使用Promise异步回调。 configs配置里可以指定任务组执行的超时时间和优先级。指定的超时时间到了，但是任务组还未完成，则会抛出任务组超时的异常信息。

> **说明：**&gt;
> - 不支持任务组重复执行。&gt;
> - 在抛出超时异常信息之后，执行中的任务还是会在线程中继续执行，但是最终不会返回执行结果。

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| group | [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) | 是 |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Object[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |
| [10200059](../errorcode-utils.md#10200059-任务组不能重复执行) |
| [10200070](../errorcode-utils.md#10200070-任务组执行超时) |
