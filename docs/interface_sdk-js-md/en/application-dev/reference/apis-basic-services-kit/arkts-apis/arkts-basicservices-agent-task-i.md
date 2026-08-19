# Task

Implements an upload or download task. Before using this API, you must obtain a **Task** object, from a promise through [request.agent.create](arkts-basicservices-agent-create-f.md) or from a callback through [request.agent.create](arkts-basicservices-agent-create-f.md). &gt; **NOTE：**&gt; &gt; The **Task** object and its mounting callback function are released and automatically reclaimed by the system &gt; after the **remove** method is called.

**Since:** 23

<!--Device-agent-interface Task--><!--Device-agent-interface Task-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
import { cacheDownload } from '@kit.BasicServicesKit';
```

## offCompleted

```TypeScript
offCompleted(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

<!--Device-Task-offCompleted(callback?: ProgressCallback): void--><!--Device-Task-offCompleted(callback?: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | No | callback function with a `Progress` argument. |

## offFailed

```TypeScript
offFailed(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

<!--Device-Task-offFailed(callback?: ProgressCallback): void--><!--Device-Task-offFailed(callback?: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | No | callback function with a `Progress` argument. |

## offFaultOccur

```TypeScript
offFaultOccur(callback?: Callback<Faults>): void
```

Disables the 'faultOccur' callback.

**Since:** 23

<!--Device-Task-offFaultOccur(callback?: Callback<Faults>): void--><!--Device-Task-offFaultOccur(callback?: Callback<Faults>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | No | callback function with a `Faults` argument. |

## offPause

```TypeScript
offPause(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

<!--Device-Task-offPause(callback?: ProgressCallback): void--><!--Device-Task-offPause(callback?: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | No | callback function with a `Progress` argument. |

## offProgress

```TypeScript
offProgress(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

<!--Device-Task-offProgress(callback?: ProgressCallback): void--><!--Device-Task-offProgress(callback?: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | No | callback function with a `Progress` argument. |

## offRemove

```TypeScript
offRemove(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

<!--Device-Task-offRemove(callback?: ProgressCallback): void--><!--Device-Task-offRemove(callback?: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | No | callback function with a `Progress` argument. |

## offResponse

```TypeScript
offResponse(callback?: Callback<HttpResponse>): void
```

Disables the response callback.

**Since:** 23

<!--Device-Task-offResponse(callback?: Callback<HttpResponse>): void--><!--Device-Task-offResponse(callback?: Callback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;HttpResponse&gt; | No | callback function with an `HttpResponse` argument. |

## offResume

```TypeScript
offResume(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

<!--Device-Task-offResume(callback?: ProgressCallback): void--><!--Device-Task-offResume(callback?: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | No | callback function with a `Progress` argument. |

## offWait

```TypeScript
offWait(callback?: Callback<WaitingReason>): void
```

Disables the wait callback.

**Since:** 23

<!--Device-Task-offWait(callback?: Callback<WaitingReason>): void--><!--Device-Task-offWait(callback?: Callback<WaitingReason>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | No | callback function with an `WaitingReason` argument. |

## off_completed

```TypeScript
off(event: 'completed', callback?: (progress: Progress) => void): void
```

Unsubscribes from task completion events. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-off(event: 'completed', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'completed', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'completed' | Yes | Event type.<br>- **'completed'**: task completion. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task completion events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |

## off_failed

```TypeScript
off(event: 'failed', callback?: (progress: Progress) => void): void
```

Unsubscribes from task failure events. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-off(event: 'failed', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'failed', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'failed' | Yes | Event type.<br>- **'failed'**: task failure. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task failure events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |

## off_faultOccur

```TypeScript
off(event: 'faultOccur', callback?: Callback<Faults>): void
```

Unsubscribes from task failure events. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 20

<!--Device-Task-off(event: 'faultOccur', callback?: Callback<Faults>): void--><!--Device-Task-off(event: 'faultOccur', callback?: Callback<Faults>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'faultOccur' | Yes | Event type.<br>- **'faultOccur'**: task failure. |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## off_pause

```TypeScript
off(event: 'pause', callback?: (progress: Progress) => void): void
```

Unsubscribes from the foreground task pause event. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 11

<!--Device-Task-off(event: 'pause', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'pause', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'pause' | Yes | Event type.<br>- **'pause'**: task pause. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task pause events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## off_progress

```TypeScript
off(event: 'progress', callback?: (progress: Progress) => void): void
```

Unsubscribes from task progress events. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-off(event: 'progress', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'progress', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'progress' | Yes | Event type.<br>- **'progress'**: task progress. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task progress events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | task mode error.<br>**Applicable version:** 10 and later |

## off_remove

```TypeScript
off(event: 'remove', callback?: (progress: Progress) => void): void
```

Unsubscribes from the task removal event. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 11

<!--Device-Task-off(event: 'remove', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'remove', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'remove' | Yes | Event type.<br>- **'remove'**: task removal. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task removal events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. <br> 3. Parameter verification failed. |

## off_response

```TypeScript
off(event: 'response', callback?: Callback<HttpResponse>): void
```

Unsubscribes from task response headers. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Task-off(event: 'response', callback?: Callback<HttpResponse>): void--><!--Device-Task-off(event: 'response', callback?: Callback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'response' | Yes | Event type.<br>- **response**: task response. |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;HttpResponse&gt; | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## off_resume

```TypeScript
off(event: 'resume', callback?: (progress: Progress) => void): void
```

Unsubscribes from foreground task resume events. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 11

<!--Device-Task-off(event: 'resume', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'resume', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'resume' | Yes | Event type.<br>- **'resume'**: task resume. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task resume events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## off_wait

```TypeScript
off(event: 'wait', callback?: Callback<WaitingReason>): void
```

Unsubscribes from task waiting events. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 20

<!--Device-Task-off(event: 'wait', callback?: Callback<WaitingReason>): void--><!--Device-Task-off(event: 'wait', callback?: Callback<WaitingReason>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'wait' | Yes | Event type.<br>- 'wait': The task is waiting. |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## onCompleted

```TypeScript
onCompleted(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

<!--Device-Task-onCompleted(callback: ProgressCallback): void--><!--Device-Task-onCompleted(callback: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | Yes | callback function with a `Progress` argument. |

## onFailed

```TypeScript
onFailed(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

<!--Device-Task-onFailed(callback: ProgressCallback): void--><!--Device-Task-onFailed(callback: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | Yes | callback function with a `Progress` argument. |

## onFaultOccur

```TypeScript
onFaultOccur(callback: Callback<Faults>): void
```

Enables the 'faultOccur' callback. This callback is triggered when the task failed. The returned `Faults` will contain the reason why the task failed.

**Since:** 23

<!--Device-Task-onFaultOccur(callback: Callback<Faults>): void--><!--Device-Task-onFaultOccur(callback: Callback<Faults>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | Yes | callback function with a `Faults` argument. |

## onPause

```TypeScript
onPause(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

<!--Device-Task-onPause(callback: ProgressCallback): void--><!--Device-Task-onPause(callback: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | Yes | callback function with a `Progress` argument. |

## onProgress

```TypeScript
onProgress(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

<!--Device-Task-onProgress(callback: ProgressCallback): void--><!--Device-Task-onProgress(callback: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | Yes | callback function with a `Progress` argument. |

## onRemove

```TypeScript
onRemove(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

<!--Device-Task-onRemove(callback: ProgressCallback): void--><!--Device-Task-onRemove(callback: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | Yes | callback function with a `Progress` argument. |

## onResponse

```TypeScript
onResponse(callback: Callback<HttpResponse>): void
```

Enables the response callback.

**Since:** 23

<!--Device-Task-onResponse(callback: Callback<HttpResponse>): void--><!--Device-Task-onResponse(callback: Callback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;HttpResponse&gt; | Yes | callback function with an `HttpResponse` argument. |

## onResume

```TypeScript
onResume(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

<!--Device-Task-onResume(callback: ProgressCallback): void--><!--Device-Task-onResume(callback: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | Yes | callback function with a `Progress` argument. |

## onWait

```TypeScript
onWait(callback: Callback<WaitingReason>): void
```

Enables the wait callback. This callback is triggered when the task changes from other states to the waiting state. The returned `WaitingReason` will contain the reason why the task enters waiting state.

**Since:** 23

<!--Device-Task-onWait(callback: Callback<WaitingReason>): void--><!--Device-Task-onWait(callback: Callback<WaitingReason>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | Yes | callback function with an `WaitingReason` argument. |

## on_completed

```TypeScript
on(event: 'completed', callback: (progress: Progress) => void): void
```

Subscribes to task completion events. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-on(event: 'completed', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'completed', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'completed' | Yes | Event type.<br>- **'completed'**: task completion. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | task mode error.<br>**Applicable version:** 10 and later |

## on_failed

```TypeScript
on(event: 'failed', callback: (progress: Progress) => void): void
```

Subscribes to task failure events. This API uses an asynchronous callback to return the result. You can call [request.agent.show](arkts-basicservices-agent-show-f.md) to view the error cause. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-on(event: 'failed', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'failed', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'failed' | Yes | Event type.<br>- **'failed'**: task failure. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |

## on_faultOccur

```TypeScript
on(event: 'faultOccur', callback: Callback<Faults>): void
```

Subscribes to task failure events. This API uses a callback to return the result. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 20

<!--Device-Task-on(event: 'faultOccur', callback: Callback<Faults>): void--><!--Device-Task-on(event: 'faultOccur', callback: Callback<Faults>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'faultOccur' | Yes | Event type.<br>- **'faultOccur'**: task failure. |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | Yes | Callback used to return the failure cause of the task. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## on_pause

```TypeScript
on(event: 'pause', callback: (progress: Progress) => void): void
```

Subscribes to task pause events. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 11

<!--Device-Task-on(event: 'pause', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'pause', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'pause' | Yes | Event type.<br>- **'pause'**: task pause. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## on_progress

```TypeScript
on(event: 'progress', callback: (progress: Progress) => void): void
```

Subscribes to task progress changes. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-on(event: 'progress', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'progress', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'progress' | Yes | Event type.<br>- **'progress'**: task progress. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | task mode error.<br>**Applicable version:** 10 and later |

## on_remove

```TypeScript
on(event: 'remove', callback: (progress: Progress) => void): void
```

Subscribes to task removal events. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 11

<!--Device-Task-on(event: 'remove', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'remove', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'remove' | Yes | Event type.<br>- **'remove'**: task removal. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## on_response

```TypeScript
on(event: 'response', callback: Callback<HttpResponse>): void
```

Subscribes to task response headers. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Task-on(event: 'response', callback: Callback<HttpResponse>): void--><!--Device-Task-on(event: 'response', callback: Callback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'response' | Yes | Event type.<br>- **'response'**: task response. |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;HttpResponse&gt; | Yes | Callback used to return the data structure of the task response header. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## on_resume

```TypeScript
on(event: 'resume', callback: (progress: Progress) => void): void
```

Subscribes to task resume events. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 11

<!--Device-Task-on(event: 'resume', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'resume', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'resume' | Yes | Event type.<br>- **'resume'**: task resume. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## on_wait

```TypeScript
on(event: 'wait', callback: Callback<WaitingReason>): void
```

Subscribes to task wait events. This API uses a callback to return the result. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 20

<!--Device-Task-on(event: 'wait', callback: Callback<WaitingReason>): void--><!--Device-Task-on(event: 'wait', callback: Callback<WaitingReason>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'wait' | Yes | Event type.<br>- 'wait': The task is waiting. |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | Yes | Callback used to return the waiting reason of the task. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

Pauses a task that is waiting, running, or retrying. A paused task can be resumed by [resume](#resume). This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-Task-pause(callback: AsyncCallback<void>): void--><!--Device-Task-pause(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |

## pause

```TypeScript
pause(): Promise<void>
```

Pauses a task that is waiting, running, or retrying. A paused task can be resumed by [resume](#resume). This API uses a promise to return the result.

**Since:** 23

<!--Device-Task-pause(): Promise<void>--><!--Device-Task-pause(): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |

## resume

```TypeScript
resume(callback: AsyncCallback<void>): void
```

Resumes a paused task. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

<!--Device-Task-resume(callback: AsyncCallback<void>): void--><!--Device-Task-resume(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |

## resume

```TypeScript
resume(): Promise<void>
```

Resumes a paused task. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

<!--Device-Task-resume(): Promise<void>--><!--Device-Task-resume(): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [21900005](../errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |

## setMaxSpeed

```TypeScript
setMaxSpeed(speed: long): Promise<void>
```

Sets the maximum number of bytes that can be transmitted by a task per second. This API uses a promise to return the result.

**Since:** 23

<!--Device-Task-setMaxSpeed(speed: long): Promise<void>--><!--Device-Task-setMaxSpeed(speed: long): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speed | long | Yes | Maximum number of bytes that can be transmitted by a task per second, with a minimum of 16384 bytes. The value cannot be less than the minimum speed value specified by [MinSpeed](arkts-basicservices-agent-minspeed-i.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts a task. This API uses an asynchronous callback to return the result. Tasks in the following states can be started: 1. Task created by **request.agent.create**. 2. Download tasks that are created by **request.agent.create** but have failed or paused. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-start(callback: AsyncCallback<void>): void--><!--Device-Task-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |

## start

```TypeScript
start(): Promise<void>
```

Starts a task. This API uses a promise to return the result. Tasks in the following states can be started: 1. Task created by **request.agent.create**. 2. Download tasks that are created by **request.agent.create** but have failed or paused. &gt; **NOTE：**&gt; &gt; For details about how to obtain the context in the example, see &gt; [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) &gt; .

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-start(): Promise<void>--><!--Device-Task-start(): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops a task that is running, waiting, or retrying. A paused task can be resumed by [start](#start). This API uses an asynchronous callback to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-stop(callback: AsyncCallback<void>): void--><!--Device-Task-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |

## stop

```TypeScript
stop(): Promise<void>
```

Stops a task that is running, waiting, or retrying. A paused task can be resumed by [start](#start). This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-stop(): Promise<void>--><!--Device-Task-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [21900007](../errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [13400003](../errorcode-request.md#13400003-service-error) | Task service ability error. |

## config

```TypeScript
config: Config
```

Task configuration.

**Type:** Config

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-config: Config--><!--Device-Task-config: Config-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## tid

```TypeScript
readonly tid: string
```

Task ID, which is unique and automatically generated by the system.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-readonly tid: string--><!--Device-Task-readonly tid: string-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

