# executePeriodically

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## executePeriodically

```TypeScript
function executePeriodically(period: number, task: Task, priority?: Priority): void
```

周期任务每隔period时长执行一次。当前执行模式支持设置任务优先级，可通过cancel取消任务。

> **说明：**
> 
> - 周期任务不能是任务组任务、串行队列任务或异步队列任务。
> - 同一个周期任务不能多次调用该接口。
> - 执行的任务不能拥有依赖关系。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-taskpool-function executePeriodically(period: number, task: Task, priority?: Priority): void--><!--Device-taskpool-function executePeriodically(period: number, task: Task, priority?: Priority): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| period | number | Yes | 周期时长。单位：ms。period值必须要大于等于0。 |
| task | [Task](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes | 需要周期执行的任务。 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No | 周期执行的任务的优先级，该参数默认值为**taskpool.Priority.MEDIUM**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200057 | The task cannot be executed by two APIs.<br>**Applicable version:** 18 and later |
| 10200014 | The function is not marked as concurrent. |
| 10200028 | The period is less than zero. |
| 10200050 | The concurrent task has been executed and cannot be executed periodically. |
| 10200006 | An exception occurred during serialization. |

## Examples

```TypeScript
@Concurrent
function printArgs(args: number): void {
  console.info("printArgs: " + args);
}

@Concurrent
function testExecutePeriodically(args: number): void {
  let t = Date.now();
  while ((Date.now() - t) < args) {
    continue;
  }
  taskpool.Task.sendData(args); // Send a message to the host thread.
}

function printResult(data: number): void {
  console.info("taskpool: data is: " + data);
}

function taskpoolTest() {
  try {
    let task: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
    taskpool.executePeriodically(1000, task); // 1000: period is 1000ms
  } catch (e) {
    console.error(`taskpool execute-1: Code: ${e.code}, message: ${e.message}`);
  }

  try {
    let periodicTask: taskpool.Task = new taskpool.Task(testExecutePeriodically, 200); // 200: test number
    periodicTask.onReceiveData(printResult);
    taskpool.executePeriodically(1000, periodicTask); // 1000: period is 1000ms
  } catch (e) {
    console.error(`taskpool execute-2: Code: ${e.code}, message: ${e.message}`);
  }
}

taskpoolTest();
```


## executePeriodically

```TypeScript
function executePeriodically<A extends Array<Object>, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void
```

周期执行泛型任务，使用Promise异步回调。executePeriodically任务的类型校验与GenericsTask的构造类型相关联，参数类型和返回值类型需与new GenericsTask时指定的类型保持一致。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-taskpool-function executePeriodically<A extends Array<Object>, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void--><!--Device-taskpool-function executePeriodically<A extends Array<Object>, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| period | number | Yes | 周期时长。单位：ms。period值必须要大于等于0。 |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | Yes | 需要周期执行的泛型任务。 |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No | 周期执行的任务的优先级，该参数默认值为**taskpool.Priority.MEDIUM**。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200057 | The task cannot be executed by two APIs.<br>**Applicable version:** 18 and later |
| 10200014 | The function is not marked as concurrent. |
| 10200028 | The period is less than zero. |
| 10200050 | The concurrent task has been executed and cannot be executed periodically. |
| 10200006 | An exception occurred during serialization. |

## Examples

```TypeScript
@Concurrent
function printArgs(args: number): void {
  console.info("printArgs: " + args);
}

@Concurrent
function testExecutePeriodically(args: number): void {
  let t = Date.now();
  while ((Date.now() - t) < args) {
    continue;
  }
  taskpool.Task.sendData(args); // Send a message to the host thread.
}

function printResult(data: number): void {
  console.info("taskpool: data is: " + data);
}

function taskpoolTest() {
  try {
    let task: taskpool.Task = new taskpool.GenericsTask<[number], void>(printArgs, 100); // 100: test number
    taskpool.executePeriodically<[number], void>(1000, task); // 1000: period is 1000ms
  } catch (e) {
    console.error(`taskpool execute-1: Code: ${e.code}, message: ${e.message}`);
  }

  try {
    let periodicTask: taskpool.Task = new taskpool.GenericsTask<[number], void>(testExecutePeriodically, 200); // 200: test number
    periodicTask.onReceiveData(printResult);
    taskpool.executePeriodically<[number], void>(1000, periodicTask); // 1000: period is 1000ms
  } catch (e) {
    console.error(`taskpool execute-2: Code: ${e.code}, message: ${e.message}`);
  }
}

taskpoolTest();
```

