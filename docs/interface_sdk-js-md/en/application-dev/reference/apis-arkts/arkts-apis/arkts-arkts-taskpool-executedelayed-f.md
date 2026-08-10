# executeDelayed

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## executeDelayed

```TypeScript
function executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>
```

延时执行任务。当前执行模式可以设置任务优先级，可通过cancel取消任务。使用Promise异步回调。

> **说明：**
> 
> - 该任务不能是任务组任务、串行队列任务、异步队列任务或周期任务。
> - 如果任务不是长时任务，可以多次调用executeDelayed执行。
> - 如果是长时任务，则仅支持执行一次。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-taskpool-function executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>--><!--Device-taskpool-function executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delayTime | number | Yes | 延时时间。单位：ms。delayTime值必须要大于等于0。 |
| task | [Task](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes | 需要延时执行的任务。 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No | 延时执行的任务的优先级，该参数默认值为**taskpool.Priority.MEDIUM**。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Object&gt; | Promise对象，返回任务函数的执行结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200057 | The task cannot be executed by two APIs.<br>**Applicable version:** 18 and later |
| 10200014 | The function is not marked as concurrent.<br>**Applicable version:** 12 and later |
| 10200028 | The delayTime is less than zero. |
| 10200051 | The periodic task cannot be executed again.<br>**Applicable version:** 12 and later |
| 10200006 | An exception occurred during serialization.<br>**Applicable version:** 12 and later |

## Examples

```TypeScript
// import BusinessError
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function printArgs(args: number): void {
    console.info("printArgs: " + args);
}

let t: number = Date.now();
console.info("taskpool start time is: " + t);
let task: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
taskpool.executeDelayed(1000, task).then(() => { // 1000: delayTime is 1000ms
  console.info("taskpool execute success");
}).catch((e: BusinessError) => {
  console.error(`taskpool execute: Code: ${e.code}, message: ${e.message}`);
})
```


## executeDelayed

```TypeScript
function executeDelayed<A extends Array<Object>, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise<R>
```

延时执行泛型任务，使用Promise异步回调。executeDelayed任务的类型校验与GenericsTask的构造类型相关联，参数类型和返回值类型需与new GenericsTask时指定的类型保持一致。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-taskpool-function executeDelayed<A extends Array<Object>, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise<R>--><!--Device-taskpool-function executeDelayed<A extends Array<Object>, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise<R>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| delayTime | number | Yes | 延时时间。单位：ms。delayTime值必须要大于等于0。 |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | Yes | 需要延时执行的泛型任务。 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No | 延时执行的任务的优先级，默认值为**taskpool.Priority.MEDIUM**。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;R&gt; | Promise对象，返回任务函数的执行结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200057 | The task cannot be executed by two APIs.<br>**Applicable version:** 18 and later |
| 10200028 | The delayTime is less than zero. |
| 10200051 | The periodic task cannot be executed again. |

## Examples

```TypeScript
// import BusinessError
import { BusinessError } from '@kit.BasicServicesKit'

@Concurrent
function printArgs(args: number): string {
    console.info("printArgs: " + args);
    return "success";
}

let task: taskpool.Task = new taskpool.GenericsTask<[number], string>(printArgs, 100); // 100: test number
taskpool.executeDelayed<[number], string>(1000, task).then((res: string) => { // 1000: delayTime is 1000ms
  console.info("taskpool execute success");
}).catch((e: BusinessError) => {
  console.error(`taskpool execute: Code: ${e.code}, message: ${e.message}`);
})
```

