# Worker

The Worker class contains all Worker functions.

**Inheritance/Implementation:** Worker implements [EventTarget](arkts-arkts-worker-eventtarget-i.md)

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [ThreadWorker](arkts-arkts-worker-threadworker-c.md)

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import worker, { DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from '@kit.ArkTS';
```

## constructor

```TypeScript
constructor(scriptURL: string, options?: WorkerOptions)
```

Creates a worker instance

**Since:** 7

**Deprecated since:** 9

**Substitutes:** constructor

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scriptURL | string | Yes | scriptURL URL of the script to be executed by the worker |
| options | [WorkerOptions](arkts-arkts-worker-workeroptions-i.md) | No | Options that can be set for the worker |

**Examples**

The following uses the Index.ets file in the entry module of the stage model as an example to describe how to load the worker file. For details about how to use the library to load the Worker thread file, see [Precautions for File URLs](../../../arkts-utils/worker-introduction.md#precautions-for-file-urls).

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

// URL of the Worker file: "entry/src/main/ets/workers/worker.ets"
const workerInstance = new worker.ThreadWorker('entry/ets/workers/worker.ets', {name: "WorkerThread"});
```

The following uses the Index.ets file in the entry module of the stage model as an example to describe how to load the worker file. For details about how to use the library to load the Worker thread file, see [Precautions for File URLs](../../../arkts-utils/worker-introduction.md#precautions-for-file-urls).

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

// URL of the Worker file: "entry/src/main/ets/workers/worker.ets"
const workerInstance = new worker.Worker('entry/ets/workers/worker.ets', {name: "WorkerThread"});
```

## off

```TypeScript
off(type: string, listener?: EventListener): void
```

Removes an event listener to the worker.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** off

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Type of the event for which the event listener is removed. |
| listener | [EventListener](arkts-arkts-worker-eventlistener-i.md) | No | listener Callback of the event listener to remove. |

**Examples**

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
// Use on, once, or addEventListener to add a listener for the "alert" event, and use off to remove the listener.
workerInstance.off("alert");
```

## on

```TypeScript
on(type: string, listener: EventListener): void
```

Adds an event listener to the worker.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** on

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | type Adds an event listener to the worker. |
| listener | [EventListener](arkts-arkts-worker-eventlistener-i.md) | Yes | listener Callback to invoke when an event of the specified type occurs. |

**Examples**

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.on("alert", () => {
    console.info("alert listener callback");
})
```

## once

```TypeScript
once(type: string, listener: EventListener): void
```

Adds an event listener to the worker and removes the event listener automatically after it is invoked once.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** once

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Type of the event to listen for |
| listener | [EventListener](arkts-arkts-worker-eventlistener-i.md) | Yes | listener Callback to invoke when an event of the specified type occurs |

**Examples**

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.once("alert", () => {
    console.info("alert listener callback");
})
```

## onerror

```TypeScript
onerror?: (err: ErrorEvent) => void
```

The onerror attribute of the worker specifies the event handler to be called when an exception occurs during worker execution. The event handler is executed in the host thread.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** onerror

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | [ErrorEvent](arkts-arkts-worker-errorevent-i.md) | Yes |  |

## onexit

```TypeScript
onexit?: (code: number) => void
```

Called when the Worker thread exits. The event handler is executed in the host thread. In the callback function, the code value is of the number type, where the value 1 indicates abnormal exit and 0 indicates normal exit.The default value is undefined.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** onexit

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | number | Yes |  |

## onmessage

```TypeScript
onmessage?: (event: MessageEvent) => void
```

The onmessage attribute of the worker specifies the event handler to be called then the host thread receives a message created by itself and sent by the worker through the parentPort.postMessage. The event handler is executed in the host thread.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** onmessage

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [MessageEvent](arkts-arkts-worker-messageevent-i.md) | Yes |  |

## onmessageerror

```TypeScript
onmessageerror?: (event: MessageEvent) => void
```

The onmessage attribute of the worker specifies the event handler when the worker receives a message that cannot be serialized. The event handler is executed in the host thread.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** onmessageerror

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [MessageEvent](arkts-arkts-worker-messageevent-i.md) | Yes |  |

## postMessage

```TypeScript
postMessage(message: Object, transfer: ArrayBuffer[]): void
```

Sends a message to the worker thread. The data is transferred using the structured clone algorithm.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** postMessage

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | Object | Yes | Data to be sent to the worker |
| transfer | ArrayBuffer[] | Yes | transfer ArrayBuffer instance that can be transferred. The transferList array cannot contain null. |

**Examples**

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

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");

let buffer = new ArrayBuffer(8);
workerInstance.postMessage(buffer, [buffer]);
```

## postMessage

```TypeScript
postMessage(message: Object, options?: PostMessageOptions): void
```

Sends a message to the worker thread. The data is transferred using the structured clone algorithm.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** postMessage

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | Object | Yes | Data to be sent to the worker |
| options | [PostMessageOptions](arkts-arkts-worker-postmessageoptions-i.md) | No | Option can be set for postmessage. The transferList array cannot contain null. |

**Examples**

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

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");

workerInstance.postMessage("hello world");

let buffer = new ArrayBuffer(8);
workerInstance.postMessage(buffer, [buffer]);
```

## terminate

```TypeScript
terminate(): void
```

Terminates the worker thread to stop the worker from receiving messages

**Since:** 7

**Deprecated since:** 9

**Substitutes:** terminate

**System capability:** SystemCapability.Utils.Lang

**Examples**

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.terminate();
```

```TypeScript
// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.terminate();
```
