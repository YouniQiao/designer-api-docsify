# Task

Implements an upload or download task. Before using this API, you must obtain a **Task** object, from a promise through [request.agent.create](arkts-basicservices-agent-create-f.md) or from a callback through [request.agent.create](arkts-basicservices-agent-create-f.md).

> **NOTE：**
> 
> The **Task** object and its mounting callback function are released and automatically reclaimed by the system
> after the **remove** method is called.

**Since:** 10

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## off

```TypeScript
off(event: 'progress', callback?: (progress: Progress) => void): void
```

Unsubscribes from task progress events.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'progress' | Yes | Event type.   - **'progress'**: task progress. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task progress events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | task mode error.<br>**Applicable version:** 10 |

## off

```TypeScript
off(event: 'completed', callback?: (progress: Progress) => void): void
```

Unsubscribes from task completion events.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'completed' | Yes | Event type.   - **'completed'**: task completion. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task completion events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 |

## off

```TypeScript
off(event: 'failed', callback?: (progress: Progress) => void): void
```

Unsubscribes from task failure events.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'failed' | Yes | Event type.   - **'failed'**: task failure. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task failure events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 |

## off

```TypeScript
off(event: 'pause', callback?: (progress: Progress) => void): void
```

Unsubscribes from the foreground task pause event.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 11

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'pause' | Yes | Event type.   - **'pause'**: task pause. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task pause events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |

## off

```TypeScript
off(event: 'resume', callback?: (progress: Progress) => void): void
```

Unsubscribes from foreground task resume events.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 11

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'resume' | Yes | Event type.   - **'resume'**: task resume. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task resume events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |

## off

```TypeScript
off(event: 'remove', callback?: (progress: Progress) => void): void
```

Unsubscribes from the task removal event.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 11

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'remove' | Yes | Event type.   - **'remove'**: task removal. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task removal events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Mandatory parameters are left unspecified.   2. Incorrect parameter types.   3. Parameter verification failed. |

## off

```TypeScript
off(event: 'response', callback?: Callback<HttpResponse>): void
```

Unsubscribes from task response headers.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'response' | Yes | Event type.   - **response**: task response. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |

## off

```TypeScript
off(event: 'faultOccur', callback?: Callback<Faults>): void
```

Unsubscribes from task failure events.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 20

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'faultOccur' | Yes | Event type.   - **'faultOccur'**: task failure. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |

## off

```TypeScript
off(event: 'wait', callback?: Callback<WaitingReason>): void
```

Unsubscribes from task waiting events.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 20

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'wait' | Yes | Event type.   - 'wait': The task is waiting. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |

## on

```TypeScript
on(event: 'progress', callback: (progress: Progress) => void): void
```

Subscribes to task progress changes. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'progress' | Yes | Event type.   - **'progress'**: task progress. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | task mode error.<br>**Applicable version:** 10 |

## on

```TypeScript
on(event: 'completed', callback: (progress: Progress) => void): void
```

Subscribes to task completion events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'completed' | Yes | Event type.   - **'completed'**: task completion. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | task mode error.<br>**Applicable version:** 10 |

## on

```TypeScript
on(event: 'failed', callback: (progress: Progress) => void): void
```

Subscribes to task failure events. This API uses an asynchronous callback to return the result. You can call [request.agent.show](arkts-basicservices-agent-show-f.md) to view the error cause.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'failed' | Yes | Event type.   - **'failed'**: task failure. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 |

## on

```TypeScript
on(event: 'pause', callback: (progress: Progress) => void): void
```

Subscribes to task pause events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 11

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'pause' | Yes | Event type.   - **'pause'**: task pause. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |

## on

```TypeScript
on(event: 'resume', callback: (progress: Progress) => void): void
```

Subscribes to task resume events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 11

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'resume' | Yes | Event type.   - **'resume'**: task resume. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |

## on

```TypeScript
on(event: 'remove', callback: (progress: Progress) => void): void
```

Subscribes to task removal events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 11

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'remove' | Yes | Event type.   - **'remove'**: task removal. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |

## on

```TypeScript
on(event: 'response', callback: Callback<HttpResponse>): void
```

Subscribes to task response headers. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'response' | Yes | Event type.   - **'response'**: task response. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | Yes | Callback used to return the data structure of the task response header. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |

## on

```TypeScript
on(event: 'faultOccur', callback: Callback<Faults>): void
```

Subscribes to task failure events. This API uses a callback to return the result.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 20

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'faultOccur' | Yes | Event type.   - **'faultOccur'**: task failure. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | Yes | Callback used to return the failure cause of the task. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |

## on

```TypeScript
on(event: 'wait', callback: Callback<WaitingReason>): void
```

Subscribes to task wait events. This API uses a callback to return the result.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 20

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'wait' | Yes | Event type.   - 'wait': The task is waiting. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | Yes | Callback used to return the waiting reason of the task. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

Pauses a task that is waiting, running, or retrying. A paused task can be resumed by [resume](#resume). This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |

**Examples**

```TypeScript
downloadTask.pause((err: BusinessError) => {
  if(err) {
    console.error(`Failed to pause the download task. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in pausing the download task.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskPauseTest',
  description: 'Sample code for pause the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.pause((err: BusinessError) => {
    if (err) {
      console.error(`Failed to pause the download task, Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in pausing a download task. `);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## pause

```TypeScript
pause(): Promise<void>
```

Pauses a task that is waiting, running, or retrying. A paused task can be resumed by [resume](#resume). This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |

**Examples**

```TypeScript
downloadTask.pause().then(() => {    
  console.info('Succeeded in pausing the download task.');
}).catch((err: BusinessError) => {
  console.error(`Failed to pause the download task. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskPauseTest',
  description: 'Sample code for pause the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.pause().then(() => {
    console.info(`Succeeded in pausing a download task. `);
  }).catch((err: BusinessError) => {
    console.error(`Failed to pause the download task, Code: ${err.code}, message: ${err.message}`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## resume

```TypeScript
resume(callback: AsyncCallback<void>): void
```

Resumes a paused task. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |

**Examples**

```TypeScript
downloadTask.resume((err: BusinessError) => {
  if (err) {
    console.error(`Failed to resume the download task. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in resuming the download task.');
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskResumeTest',
  description: 'Sample code for resume the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.pause();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.resume((err: BusinessError) => {
    if (err) {
      console.error(`Failed to resume the download task, Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in resuming a download task. `);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## resume

```TypeScript
resume(): Promise<void>
```

Resumes a paused task. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.INTERNET

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |

**Examples**

```TypeScript
downloadTask.resume().then(() => {
  console.info('Succeeded in resuming the download task.')
}).catch((err: BusinessError) => {
  console.error(`Failed to resume the download task. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskResumeTest',
  description: 'Sample code for resume the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.pause();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.resume().then(() => {
    console.info(`Succeeded in resuming a download task. `);
  }).catch((err: BusinessError) => {
    console.error(`Failed to resume the download task, Code: ${err.code}, message: ${err.message}`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## setMaxSpeed

```TypeScript
setMaxSpeed(speed: number): Promise<void>
```

Sets the maximum number of bytes that can be transmitted by a task per second. This API uses a promise to return the result.

**Since:** 18

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speed | number | Yes | Maximum number of bytes that can be transmitted by a task per second, with a minimum of 16384 bytes. The value cannot be less than the minimum speed value specified by [MinSpeed](arkts-basicservices-agent-minspeed-i.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes:   1. Missing mandatory parameters.   2. Incorrect parameter type.   3. Parameter verification failed. |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  saveas: "./",
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  // Set the maximum transmission speed.
  task.setMaxSpeed(10 * 1024 * 1024).then(() => {
    console.info(`Succeeded in setting the max speed of the task. result: ${task.tid}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the max speed of the task. result: ${task.tid}`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts a task. This API uses an asynchronous callback to return the result.

Tasks in the following states can be started:

1. Task created by **request.agent.create**.
2. Download tasks that are created by **request.agent.create** but have failed or paused.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 10

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskStartTest',
  description: 'Sample code for start the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.start((err: BusinessError) => {
    if (err) {
      console.error(`Failed to start the download task, Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in starting a download task.`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## start

```TypeScript
start(): Promise<void>
```

Starts a task. This API uses a promise to return the result.

Tasks in the following states can be started:

1. Task created by **request.agent.create**.
2. Download tasks that are created by **request.agent.create** but have failed or paused.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 10

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskStartTest',
  description: 'Sample code for start the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.start().then(() => {
    console.info(`Succeeded in starting a download task.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to start the download task, Code: ${err.code}, message: ${err.message}`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops a task that is running, waiting, or retrying. A paused task can be resumed by [start](#start). This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskStopTest',
  description: 'Sample code for stop the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop the download task, Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in stopping a download task. `);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## stop

```TypeScript
stop(): Promise<void>
```

Stops a task that is running, waiting, or retrying. A paused task can be resumed by [start](#start). This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // Replace the URL with the HTTP address of the real server.
  title: 'taskStopTest',
  description: 'Sample code for stop the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // Wait for 1 second before executing the next step to prevent asynchronous out-of-order.
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(),1000)
  })
  task.stop().then(() => {
    console.info(`Succeeded in stopping a download task. `);
  }).catch((err: BusinessError) => {
    console.error(`Failed to stop the download task, Code: ${err.code}, message: ${err.message}`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## config

```TypeScript
config: Config
```

Task configuration.

**Type:** Config

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Request.FileTransferAgent

## tid

```TypeScript
readonly tid: string
```

Task ID, which is unique and automatically generated by the system.

**Type:** string

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Request.FileTransferAgent
