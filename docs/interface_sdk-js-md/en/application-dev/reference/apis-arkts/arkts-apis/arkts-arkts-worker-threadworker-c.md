# ThreadWorker

使用以下方法前，需先构造ThreadWorker实例。ThreadWorker类继承WorkerEventTarget。

使用Worker模块时，API version 18及之后的版本建议在宿主线程中注册onAllErrors回调，以捕获Worker线程生命周期内的各种异常。API version 18之前的版本应注册onerror回调。如果未注册onAllErrors或onerror回调，当Worker线程出现异常时会发生崩溃问题。注意，onerror接口仅能捕获onmessage回调中的同步异常，捕获异常后，Worker线程将进入销毁流程，无法继续使用。

onAllErrors接口与onerror接口之间的行为差异如下：

1. 异常捕获范围

 onAllErrors接口可以捕获Worker线程的onmessage回调、timer回调以及文件执行等流程中产生的全局异常。

 onerror接口仅能捕获Worker线程的onmessage回调中同步方法产生的异常，无法捕获多线程回调和模块化相关异常。

2. 异常捕获后的线程状态

 onAllErrors接口捕获异常后，Worker线程仍然存活并可以继续使用。这使开发者可以在捕获异常后执行其他操作，无需担心线程终止。

 onerror接口捕获异常后，Worker线程会进入销毁流程，无法继续使用。这意味着在onerror触发后，Worker线程将被终止，后续操作将无法进行。

3. 适用场景

 onAllErrors接口适用于捕获Worker线程中所有类型异常的场景，特别是确保异常发生后Worker线程仍能继续运行的复杂场景。

 onerror接口适用于只需要捕获onmessage回调中同步异常的简单场景。由于捕获异常后线程会被销毁，适用于不需要继续使用Worker线程的情况。

 推荐使用onAllErrors接口，因为它提供了更全面的异常捕获能力，并且不会导致线程终止。

**Inheritance/Implementation:** ThreadWorker implements [WorkerEventTarget](arkts-arkts-worker-workereventtarget-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-worker-class ThreadWorker implements WorkerEventTarget--><!--Device-worker-class ThreadWorker implements WorkerEventTarget-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from 'kits/@kit.ArkTS';
```

## addEventListener

```TypeScript
addEventListener(type: string, listener: WorkerEventListener): void
```

向宿主线程的Worker实例对象添加一个事件监听，该接口与on9+接口功能一致。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThreadWorker-addEventListener(type: string, listener: WorkerEventListener): void--><!--Device-ThreadWorker-addEventListener(type: string, listener: WorkerEventListener): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 监听的事件类型。 |
| listener | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | Yes | 当指定类型的事件发生时调用的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200005 | The called API is not supported in the worker thread. |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", () => {
  console.info("alert listener callback");
})

// Execute the callback of the alert type.
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.
```

## constructor

```TypeScript
constructor(scriptURL: string, options?: WorkerOptions)
```

ThreadWorker构造函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorker-constructor(scriptURL: string, options?: WorkerOptions)--><!--Device-ThreadWorker-constructor(scriptURL: string, options?: WorkerOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scriptURL | string | Yes | Worker线程文件的路径。路径规则详细参考文件路径注意事项。 |
| options | [WorkerOptions](arkts-arkts-worker-workeroptions-i.md) | No | Worker构造的选项。此参数不填时，对应各属性取其默认值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200003 | Worker initialization failed. |
| 10200007 | The worker file path is invalid. |

## Examples

The following uses the Index.ets file in the entry module of the stage model as an example to describe how to load the worker file. For details about how to use the library to load the Worker thread file, see [Precautions for File URLs](../../arkts-utils/worker-introduction.md#precautions-for-file-urls).

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

// URL of the Worker file: "entry/src/main/ets/workers/worker.ets"
const workerInstance = new worker.ThreadWorker('entry/ets/workers/worker.ets', {name: "WorkerThread"});
```

## dispatchEvent

```TypeScript
dispatchEvent(event: Event): boolean
```

分发定义在Worker线程的事件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThreadWorker-dispatchEvent(event: Event): boolean--><!--Device-ThreadWorker-dispatchEvent(event: Event): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Event](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-event-c.md) | Yes | 需要分发的事件。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", () => {
  console.info("alert listener callback");
})

let result: Boolean = workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

console.info("dispatchEvent result is: ", result);
```

## off

```TypeScript
off(type: string, listener?: WorkerEventListener): void
```

移除宿主线程的Worker实例对象中类型为type的事件监听，该接口与removeEventListener9+接口功能一致。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThreadWorker-off(type: string, listener?: WorkerEventListener): void--><!--Device-ThreadWorker-off(type: string, listener?: WorkerEventListener): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 需要移除的事件类型。 |
| listener | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | No | listener 要移除的事件监听的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200005 | The called API is not supported in the worker thread. |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

const handler1 = () => console.info("Handler 1");
const handler2 = () => console.info("Handler 2");

// Register two listeners.
workerInstance.on("alert", handler1);
workerInstance.on("alert", handler2);

// First trigger: Both listeners are executed.
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

// Remove the handler1 listener.
workerInstance.off("alert", handler1);

// Second trigger: Only handler2 is executed.
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

// Remove all listeners of the alert type.
workerInstance.off("alert");
```

## on

```TypeScript
on(type: string, listener: WorkerEventListener): void
```

向宿主线程的Worker实例对象添加一个事件监听，该接口与addEventListener9+接口功能一致。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThreadWorker-on(type: string, listener: WorkerEventListener): void--><!--Device-ThreadWorker-on(type: string, listener: WorkerEventListener): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 监听的事件类型。 |
| listener | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | Yes | 当指定类型的事件发生时调用的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200005 | The called API is not supported in the worker thread. |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.on("alert", () => {
    console.info("alert listener callback");
})

// Event listeners added using on can be executed multiple times.
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.
```

## onAllErrors

```TypeScript
onAllErrors?: ErrorCallback
```

回调函数。表示Worker线程生命周期内发生异常被调用的事件处理程序，处理程序在宿主线程中执行。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ThreadWorker-onAllErrors?: ErrorCallback--><!--Device-ThreadWorker-onAllErrors?: ErrorCallback-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200005 | The called API is not supported in the worker thread. |
| 10200004 | The Worker instance is not running. |

## once

```TypeScript
once(type: string, listener: WorkerEventListener): void
```

向宿主线程的Worker实例对象添加一个事件监听，该事件监听只执行一次，执行完后会自动删除。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThreadWorker-once(type: string, listener: WorkerEventListener): void--><!--Device-ThreadWorker-once(type: string, listener: WorkerEventListener): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 监听的事件类型。 |
| listener | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | Yes | listener 当指定类型的事件发生时调用的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200005 | The called API is not supported in the worker thread. |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.once("alert", () => {
  console.info("alert listener callback");
})

workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

// Event listeners added using once are automatically removed after being executed once and cannot be executed multiple times.
// workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.
```

## onerror

```TypeScript
onerror?: (err: ErrorEvent) => void
```

回调函数，用于处理onmessage回调函数中同步代码产生的异常，处理程序在宿主线程中执行。回调函数的err类型为ErrorEvent，表示收到的异常数据。默认值为undefined。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorker-onerror?: (err: ErrorEvent) => void--><!--Device-ThreadWorker-onerror?: (err: ErrorEvent) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | [ErrorEvent](arkts-arkts-worker-errorevent-i.md) | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200005 | The called API is not supported in the worker thread. |
| 10200004 | The Worker instance is not running. |

## onexit

```TypeScript
onexit?: (code: number) => void
```

回调函数。表示Worker线程销毁时被调用的事件处理程序，该处理程序在宿主线程中执行。回调函数的code参数类型为number，异常退出时code为1，正常退出时code为0。默认值为undefined。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorker-onexit?: (code: number) => void--><!--Device-ThreadWorker-onexit?: (code: number) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | number | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200005 | The called API is not supported in the worker thread. |
| 10200004 | The Worker instance is not running. |

## onmessage

```TypeScript
onmessage?: (event: MessageEvents) => void
```

回调函数。表示宿主线程接收到来自其创建的Worker通过workerPort.postMessage或workerPort.postMessageWithSharedSendable接口发送的消息时被调用的事件处理程序，处理程序在宿主线程中执行。其中回调函数中event类型为MessageEvents，表示收到的Worker线程发送的消息数据。默认值为undefined。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorker-onmessage?: (event: MessageEvents) => void--><!--Device-ThreadWorker-onmessage?: (event: MessageEvents) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [MessageEvents](arkts-arkts-worker-messageevents-i.md) | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200005 | The called API is not supported in the worker thread. |
| 10200004 | The Worker instance is not running. |

## onmessageerror

```TypeScript
onmessageerror?: (event: MessageEvents) => void
```

回调函数。用于处理Worker对象接收到的无法被序列化的消息。该处理程序在宿主线程中执行，event类型为MessageEvents，表示收到的Worker消息数据。默认值为undefined。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorker-onmessageerror?: (event: MessageEvents) => void--><!--Device-ThreadWorker-onmessageerror?: (event: MessageEvents) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [MessageEvents](arkts-arkts-worker-messageevents-i.md) | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200005 | The called API is not supported in the worker thread. |
| 10200004 | The Worker instance is not running. |

## postMessage

```TypeScript
postMessage(message: Object, transfer: ArrayBuffer[]): void
```

宿主线程通过转移对象所有权的方式向Worker线程发送消息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorker-postMessage(message: Object, transfer: ArrayBuffer[]): void--><!--Device-ThreadWorker-postMessage(message: Object, transfer: ArrayBuffer[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | Object | Yes | 发送至Worker的数据，该数据对象必须是可序列化对象。 支持的参数类型请参考序列化支持类型。 |
| transfer | ArrayBuffer[] | Yes | 表示可转移的ArrayBuffer实例对象数组，该数组中对象的所有权 会被转移到Worker线程，在宿主线程中将会变为不可用，仅在Worker线程中可用。该数组不可传入null。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200006 | An exception occurred during serialization. |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
// Worker.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

// Create an object in the Worker thread for communicating with the host thread.
const workerPort = worker.workerPort;

// The Worker thread receives information from the host thread.
workerPort.onmessage = (e: MessageEvents): void => {
  // data carries the information sent by the host thread.
  let data: ArrayBuffer = e.data;
  // Write data to the received buffer.
  const view = new Int8Array(data).fill(3);
  // The Worker thread sends information to the host thread.
  workerPort.postMessage(view);
}

// Trigger a callback when an error occurs in the Worker thread.
workerPort.onerror = (err: ErrorEvent) => {
  console.error("worker.ets onerror" + err.message);
}
```

```TypeScript
// Index.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // Create a Worker instance in the host thread.
            const workerInstance = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
            // The host thread transfers information to the Worker thread.
            const buffer = new ArrayBuffer(8);
            workerInstance.postMessage(buffer, [buffer]);

            // The ownership of the buffer is transferred to the Worker thread and is unavailable in the host thread.
            // const view = new Int8Array(buffer).fill(3);

            // The host thread receives information from the Worker thread.
            workerInstance.onmessage = (e: MessageEvents): void => {
              // data carries the information sent by the Worker thread.
              let data: Int8Array = e.data;
              console.info("main thread data is  " + data);
              // Terminate the Worker instance.
              workerInstance.terminate();
            }
            // Call onexit().
            workerInstance.onexit = (code) => {
              console.info("main thread terminate");
            }
            // Listen for Worker errors.
            workerInstance.onAllErrors = (err: ErrorEvent) => {
              console.error("main error message " + err.message);
            }
          })
      }
      .width('100%')
      .height('100%')
    }
  }
}
```

## postMessage

```TypeScript
postMessage(message: Object, options?: PostMessageOptions): void
```

宿主线程可以通过转移对象所有权或拷贝数据的方式向Worker线程发送消息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorker-postMessage(message: Object, options?: PostMessageOptions): void--><!--Device-ThreadWorker-postMessage(message: Object, options?: PostMessageOptions): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | Object | Yes | 发送至Worker的数据，该数据对象必须是可序列化对象。 支持的参数类型请参考序列化支持类型。 |
| options | [PostMessageOptions](arkts-arkts-worker-postmessageoptions-i.md) | No | 当填入该参数时，其作用与传入ArrayBuffer[]相同， 该数组中对象的所有权会被转移到Worker线程，在宿主线程中将变为不可用，仅在Worker线程中可用。 若不填入该参数，默认设置为undefined，通过拷贝数据的方式传输信息到Worker线程。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200006 | An exception occurred during serialization. |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.postMessage("hello world");

let buffer = new ArrayBuffer(8);

// When the options parameter is specified, the ownership of the buffer is transferred to the Worker thread and will no longer be accessible from the host thread.
workerInstance.postMessage(buffer, [buffer]);

// When the options parameter is not provided, it defaults to undefined, and the buffer is sent to the Worker thread by copying the data.
workerInstance.postMessage(buffer);
```

## postMessageWithSharedSendable

```TypeScript
postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void
```

宿主线程向Worker线程发送消息，消息中的Sendable对象通过引用传递，非Sendable对象通过拷贝数据的方式传递。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThreadWorker-postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void--><!--Device-ThreadWorker-postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | Object | Yes | 发送至Worker线程的数据，该数据对象必须是可序列化或可共享。 支持的序列化类型请参考序列化支持类型。 支持的共享类型请参考Sendable支持的数据类型。 |
| transfer | ArrayBuffer[] | No | 表示可转移的ArrayBuffer实例对象数组，该数组中对象的所有权 会被转移到Worker线程，转移后该对象仅在Worker线程中可用。该数组不可传入null。默认值为空数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200006 | An exception occurred during serialization. |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
// Index.ets
// Create a SendableObject instance and pass it to the Worker thread through the host thread.

import { worker } from '@kit.ArkTS';
import { SendableObject } from './sendable';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
let object: SendableObject = new SendableObject();
workerInstance.postMessageWithSharedSendable(object);

// Use the postMessage API to pass Sendable objects by copying the data.
workerInstance.postMessage(object);
```

```TypeScript
// sendable.ets
// Define SendableObject.

@Sendable
export class SendableObject {
  a:number = 45;
}
```

```TypeScript
// The worker file path is entry/src/main/ets/workers/Worker.ets.
// Worker.ets
// Receive and access the data passed from the host thread to the Worker thread.

import { SendableObject } from '../pages/sendable';
import { worker, ThreadWorkerGlobalScope, MessageEvents, ErrorEvent } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let obj: SendableObject = e.data;
  console.info("sendable obj is: " + obj.a);
}
```

## registerGlobalCallObject

```TypeScript
registerGlobalCallObject(instanceName: string, globalCallObject: Object): void
```

在宿主线程的ThreadWorker实例上注册一个对象，该对象的方法可在Worker线程中通过callGlobalCallObjectMethod调用。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThreadWorker-registerGlobalCallObject(instanceName: string, globalCallObject: Object): void--><!--Device-ThreadWorker-registerGlobalCallObject(instanceName: string, globalCallObject: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instanceName | string | Yes | 注册对象时使用的键，调用时通过该键值找到被注册的对象。 |
| globalCallObject | Object | Yes | 被注册的对象，ThreadWorker实例会持有该对象的强引用。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
//Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
class TestObj {
  private message : string = "this is a message from TestObj";
  public getMessage() : string {
    return this.message;
  }
  public getMessageWithInput(str : string) : string {
    return this.message + " with input: " + str;
  }
}
let registerObj = new TestObj();
// Register registerObj with the ThreadWorker instance.
workerInstance.registerGlobalCallObject("myObj", registerObj);
workerInstance.postMessage("start worker");
```

```TypeScript
// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
  try {
    // The method to call does not carry an input parameter.
    let res : string = workerPort.callGlobalCallObjectMethod("myObj", "getMessage", 0) as string;
    console.info("worker:", res) // worker: this is a message from TestObj
  } catch (error) {
    // Exception handling.
    console.error("worker: error code is " + error.code + " error message is " + error.message);
  }
  try {
    // The method to call carries input parameters.
    let res : string = workerPort.callGlobalCallObjectMethod("myObj", "getMessageWithInput", 0, "hello there!") as string;
    console.info("worker:", res); //worker: this is a message from TestObj with input: hello there!
  } catch (error) {
    // Exception handling.
    console.error("worker: error code is " + error.code + " error message is " + error.message);
  }
}
```

## removeAllListener

```TypeScript
removeAllListener(): void
```

移除宿主线程中Worker实例对象的所有事件监听。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThreadWorker-removeAllListener(): void--><!--Device-ThreadWorker-removeAllListener(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.addEventListener("alert", () => {
    console.info("alert listener callback");
})
workerInstance.removeAllListener();
```

## removeEventListener

```TypeScript
removeEventListener(type: string, callback?: WorkerEventListener): void
```

移除宿主线程的Worker实例对象中类型为type的事件监听，该接口与off9+接口功能一致。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThreadWorker-removeEventListener(type: string, callback?: WorkerEventListener): void--><!--Device-ThreadWorker-removeEventListener(type: string, callback?: WorkerEventListener): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 需要移除的事件类型。 |
| callback | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | No | 移除监听事件后执行的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", () => {
  console.info("alert listener callback");
})

workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

workerInstance.removeEventListener("alert");
```

## terminate

```TypeScript
terminate(): void
```

销毁Worker线程，终止Worker接收消息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorker-terminate(): void--><!--Device-ThreadWorker-terminate(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.terminate();
```

## unregisterGlobalCallObject

```TypeScript
unregisterGlobalCallObject(instanceName?: string): void
```

取消在宿主线程ThreadWorker实例上注册的对象，该方法会释放ThreadWorker实例与目标对象之间的强引用。如果无匹配对象，该方法不会报错。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThreadWorker-unregisterGlobalCallObject(instanceName?: string): void--><!--Device-ThreadWorker-unregisterGlobalCallObject(instanceName?: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instanceName | string | No | 注册对象时使用的键。此参数不填时， 会释放ThreadWorker实例中所有已注册的对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200004 | The Worker instance is not running. |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
class TestObj {
  private message : string = "this is a message from TestObj";
  public getMessage() : string {
    return this.message;
  }
  public getMessageWithInput(str : string) : string {
    return this.message + " with input: " + str;
  }
}
let registerObj = new TestObj();
workerInstance.registerGlobalCallObject("myObj", registerObj);
// Unregister the object.
workerInstance.unregisterGlobalCallObject("myObj");
// Unregister all objects from the ThreadWorker instance.
//workerInstance.unregisterGlobalCallObject();
workerInstance.postMessage("start worker");
```

