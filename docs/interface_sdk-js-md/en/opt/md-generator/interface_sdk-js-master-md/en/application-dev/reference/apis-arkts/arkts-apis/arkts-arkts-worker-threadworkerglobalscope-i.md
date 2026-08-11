# ThreadWorkerGlobalScope

Implements communication between the Worker thread and the host thread. The postMessage API is used to send messages to the host thread, and the close API is used to terminate the Worker thread. The ThreadWorkerGlobalScope class inherits from GlobalScope9+.

**Inheritance/Implementation:** ThreadWorkerGlobalScope extends [GlobalScope](arkts-arkts-worker-globalscope-i.md)

**Since:** 9

<!--Device-unnamed-export interface ThreadWorkerGlobalScope extends GlobalScope--><!--Device-unnamed-export interface ThreadWorkerGlobalScope extends GlobalScope-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { MessageEvents, PostMessageOptions, MessageEvent, Priority, WorkerEventTarget, ThreadWorkerPriority, ThreadWorkerGlobalScope, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, WorkerOptions, EventTarget, WorkerEventListener } from 'kits/@kit.ArkTS';
```

## callGlobalCallObjectMethod

```TypeScript
callGlobalCallObjectMethod(instanceName: string, methodName: string, timeout: number, ...args: Object[]): Object
```

Calls a method of an object registered with the host thread. This API is called by the Worker thread.The invoking is synchronous for the Worker thread and asynchronous for the host thread. The return value is transferred through serialization.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThreadWorkerGlobalScope-callGlobalCallObjectMethod(instanceName: string, methodName: string, timeout: number, ...args: Object[]): Object--><!--Device-ThreadWorkerGlobalScope-callGlobalCallObjectMethod(instanceName: string, methodName: string, timeout: number, ...args: Object[]): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| instanceName | string | Yes |
| methodName | string | Yes |
| timeout | number | Yes |
| args | Object[] | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Object |

**Error codes:**

| Error Code ID |
| --- |
| [10200019](../errorcode-utils.md#10200019-failed-to-call-an-api-of-an-unregistered-object) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200021](../errorcode-utils.md#10200021-waiting-for-a-global-call-times-out) |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |
| [10200020](../errorcode-utils.md#10200020-failed-to-call-an-api-of-a-registered-object) |

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
// Call the following method when the component lifecycle ends:
// workerInstance.unregisterGlobalCallObject("myObj");
```

```TypeScript
// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
  try {
    // The method to call does not carry an input parameter.
    let res : string = workerPort.callGlobalCallObjectMethod("myObj", "getMessage", 0) as string;
    console.info("worker:", res); // worker: this is a message from TestObj
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

## close

```TypeScript
close(): void
```

Terminates the Worker thread to stop it from receiving messages.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorkerGlobalScope-close(): void--><!--Device-ThreadWorkerGlobalScope-close(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## Examples

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
```

```TypeScript
// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
    workerPort.close();
}
```

## onmessage

```TypeScript
onmessage?: (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void
```

Called when the Worker thread receives a message sent by the host thread through postMessage.The event handler is executed in the Worker thread. In the callback function, this indicates the caller's ThreadWorkerGlobalScope, and the ev type is MessageEvents, indicating the received message data.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorkerGlobalScope-onmessage?: (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void--><!--Device-ThreadWorkerGlobalScope-onmessage?: (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | [ThreadWorkerGlobalScope](arkts-arkts-worker-threadworkerglobalscope-i.md) | Yes |
| ev | [MessageEvents](arkts-arkts-worker-messageevents-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200005](../errorcode-utils.md#10200005-api-not-supported-in-the-worker-thread) |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## onmessageerror

```TypeScript
onmessageerror?: (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void
```

Called when the Worker thread receives a message that cannot be deserialized. The event handler is executed in the Worker thread. In the callback function, this indicates the caller's ThreadWorkerGlobalScope,and the ev type is MessageEvents, indicating the received message data.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorkerGlobalScope-onmessageerror?: (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void--><!--Device-ThreadWorkerGlobalScope-onmessageerror?: (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | [ThreadWorkerGlobalScope](arkts-arkts-worker-threadworkerglobalscope-i.md) | Yes |
| ev | [MessageEvents](arkts-arkts-worker-messageevents-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200005](../errorcode-utils.md#10200005-api-not-supported-in-the-worker-thread) |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## postMessage

```TypeScript
postMessage(messageObject: Object, transfer: ArrayBuffer[]): void
```

Sends a message from the Worker thread to the host thread by transferring object ownership.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorkerGlobalScope-postMessage(messageObject: Object, transfer: ArrayBuffer[]): void--><!--Device-ThreadWorkerGlobalScope-postMessage(messageObject: Object, transfer: ArrayBuffer[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| messageObject | Object | Yes |
| transfer | ArrayBuffer[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## Examples

```TypeScript
// Index.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (e: MessageEvents): void => {
    console.info("receive data from worker.ets");
}
```

```TypeScript
// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
    let buffer = new ArrayBuffer(8);
    workerPort.postMessage(buffer, [buffer]);
}
```

## postMessage

```TypeScript
postMessage(messageObject: Object, options?: PostMessageOptions): void
```

Sends a message from the Worker thread to the host thread by transferring object ownership or copying data.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadWorkerGlobalScope-postMessage(messageObject: Object, options?: PostMessageOptions): void--><!--Device-ThreadWorkerGlobalScope-postMessage(messageObject: Object, options?: PostMessageOptions): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| messageObject | Object | Yes |
| options | [PostMessageOptions](arkts-arkts-worker-postmessageoptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## Examples

```TypeScript
// Index.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (e: MessageEvents): void => {
    console.info("receive data from worker.ets");
}
```

```TypeScript
// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
    workerPort.postMessage("receive data from main thread");
}
```

## postMessageAtFront

```TypeScript
postMessageAtFront?(message: Object, priority: Priority, transfer?: ArrayBuffer[]): void
```

Sends a message from the Worker thread to the main thread by transferring object ownership,and inserted into the head of the corresponding priority queue.Except for the worker thread to the main thread,this interface has the same function as postMessage.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ThreadWorkerGlobalScope-postMessageAtFront?(message: Object, priority: Priority, transfer?: ArrayBuffer[]): void--><!--Device-ThreadWorkerGlobalScope-postMessageAtFront?(message: Object, priority: Priority, transfer?: ArrayBuffer[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | Object | Yes |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | Yes |
| transfer | ArrayBuffer[] | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## postMessageWithSharedSendable

```TypeScript
postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void
```

Sends a message from the Worker thread to the host thread. In the message, a sendable object is passed by reference,and a non-sendable object is passed by serialization.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ThreadWorkerGlobalScope-postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void--><!--Device-ThreadWorkerGlobalScope-postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | Object | Yes |
| transfer | ArrayBuffer[] | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200004](../errorcode-utils.md#10200004-worker-instance-is-not-running) |

## Examples

```TypeScript
// The worker file path is entry/src/main/ets/workers/Worker.ets.
// Worker.ets
// Create a SendableObject instance and pass it to the host thread through the Worker thread.

import { SendableObject } from '../pages/sendable';
import { worker, ThreadWorkerGlobalScope, MessageEvents, ErrorEvent } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = new SendableObject();
  workerPort.postMessageWithSharedSendable(object);
}
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
// Index.ets
// Receive the data passed from the Worker thread to the host thread and access its properties.

import { worker, MessageEvents } from '@kit.ArkTS';
import { SendableObject } from './sendable';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
workerInstance.postMessage(1);
workerInstance.onmessage = (e: MessageEvents) => {
  let obj: SendableObject = e.data;
  console.info("sendable index obj is: " + obj.a);
}
```
