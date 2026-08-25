# execute

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## execute

```TypeScript
function execute(func: Function, ...args: Object[]): Promise<Object>
```

Places a function to be executed in the internal queue of the task pool. The function is not executed immediately. It waits to be distributed to the worker thread for execution. In this mode, the function cannot be canceled. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| func | Function | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;unknown & gt; |
| Promise & lt;Object & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200003](../errorcode-utils.md#10200003-failed-to-initialize-the-worker-instance) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) |


## execute

```TypeScript
function execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>
```

Verifies the passed-in parameter types and return value type of a concurrent function, and places the function in the queue of the task pool. This API uses a promise to return the result.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| func | (...args: A) = & gt; R \ | Promise & lt;R & gt; | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | A | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;R & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) |


## execute

```TypeScript
function execute(task: Task, priority?: Priority): Promise<Object>
```

Places a task in the internal queue of the task pool. The task will not be executed immediately; instead, it waits to be distributed to a worker thread for execution. In the current mode, you can set the task priority and cancel the task. Note that the task cannot belong to a task group, serial queue, or asynchronous queue. For non-continuous tasks, this API can be called multiple times. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [Task](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;unknown & gt; |
| Promise & lt;Object & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200003](../errorcode-utils.md#10200003-failed-to-initialize-the-worker-instance) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) |


## execute

```TypeScript
function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>
```

Places the generic task in the internal queue of the task pool. The parameter type and return value type of the task are not verified. This API uses a promise to return the result. The verification of the **execute** task works in conjunction with **new GenericsTask**, requiring that the parameter and return value types match those specified in **new GenericsTask**.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | Yes |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;R & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) |


## execute

```TypeScript
function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>
```

Places a task group in the internal queue of the task pool. The tasks in the task group are not executed immediately. They wait to be distributed to the worker thread for execution. After all tasks in the task group are executed, a result array is returned. This mode is applicable to the execution of associated tasks. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| group | [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) | Yes |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Object[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| 10200059 |


## execute

```TypeScript
function execute(task: Task, configs: Configs): Promise<Object>
```

Execute a concurrent task with Configs.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [Task](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Object & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) |
| 10200058 |


## execute

```TypeScript
function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, configs: Configs): Promise<R>
```

Execute a concurrent generics task with Configs.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | Yes |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;R & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) |
| 10200058 |


## execute

```TypeScript
function execute(group: TaskGroup, configs: Configs): Promise<Object[]>
```

Execute a concurrent task group with Configs.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| group | [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) | Yes |
| configs | [Configs](arkts-arkts-taskpool-configs-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Object[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| 10200059 |
| 10200070 |
