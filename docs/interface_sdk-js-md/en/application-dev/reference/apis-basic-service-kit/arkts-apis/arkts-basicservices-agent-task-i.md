# Task

Implements an upload or download task. Before using this API, you must obtain a **Task** object, from a promise through   
[request.agent.create](arkts-basicservices-agent-create-f.md#create) or from a callback through   
[request.agent.create](arkts-basicservices-agent-create-f.md#create).

> **NOTE：**
> 
> The **Task** object and its mounting callback function are released and automatically reclaimed by the system
> after the **remove** method is called.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-agent-interface Task--><!--Device-agent-interface Task-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
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

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-off(event: 'progress', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'progress', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'progress' | Yes | Event type.&lt;br&gt;- **'progress'**: task progress. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task progress events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) | task mode error.<br>**Applicable version:** 10 and later |

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

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-off(event: 'completed', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'completed', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'completed' | Yes | Event type.&lt;br&gt;- **'completed'**: task completion. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task completion events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |

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

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-off(event: 'failed', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'failed', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'failed' | Yes | Event type.&lt;br&gt;- **'failed'**: task failure. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task failure events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |

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

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-Task-off(event: 'pause', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'pause', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'pause' | Yes | Event type.&lt;br&gt;- **'pause'**: task pause. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task pause events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-Task-off(event: 'resume', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'resume', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'resume' | Yes | Event type.&lt;br&gt;- **'resume'**: task resume. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task resume events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-Task-off(event: 'remove', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'remove', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'remove' | Yes | Event type.&lt;br&gt;- **'remove'**: task removal. |
| callback | (progress: Progress) =&gt; void | No | Callback to be invoked when the specified event occurs. If this parameter is not specified, all callbacks of the task removal events are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameter types. &lt;br&gt; 3. Parameter verification failed. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Task-off(event: 'response', callback?: Callback<HttpResponse>): void--><!--Device-Task-off(event: 'response', callback?: Callback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'response' | Yes | Event type.&lt;br&gt;- **response**: task response. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Task-off(event: 'faultOccur', callback?: Callback<Faults>): void--><!--Device-Task-off(event: 'faultOccur', callback?: Callback<Faults>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'faultOccur' | Yes | Event type.&lt;br&gt;- **'faultOccur'**: task failure. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Faults&gt; | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Task-off(event: 'wait', callback?: Callback<WaitingReason>): void--><!--Device-Task-off(event: 'wait', callback?: Callback<WaitingReason>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'wait' | Yes | Event type.&lt;br&gt;- 'wait': The task is waiting. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;WaitingReason&gt; | No | Callback to unregister. If this parameter is not specified, all callbacks of the current type will be unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |

## offCompleted

```TypeScript
offCompleted(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Task-offFaultOccur(callback?: Callback<Faults>): void--><!--Device-Task-offFaultOccur(callback?: Callback<Faults>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Faults&gt; | No | callback function with a `Faults` argument. |

## offPause

```TypeScript
offPause(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Task-offResponse(callback?: Callback<HttpResponse>): void--><!--Device-Task-offResponse(callback?: Callback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | No | callback function with an `HttpResponse` argument. |

## offResume

```TypeScript
offResume(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Task-offWait(callback?: Callback<WaitingReason>): void--><!--Device-Task-offWait(callback?: Callback<WaitingReason>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;WaitingReason&gt; | No | callback function with an `WaitingReason` argument. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-on(event: 'progress', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'progress', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'progress' | Yes | Event type.&lt;br&gt;- **'progress'**: task progress. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) | task mode error.<br>**Applicable version:** 10 and later |

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

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-on(event: 'completed', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'completed', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'completed' | Yes | Event type.&lt;br&gt;- **'completed'**: task completion. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) | task mode error.<br>**Applicable version:** 10 and later |

## on

```TypeScript
on(event: 'failed', callback: (progress: Progress) => void): void
```

Subscribes to task failure events. This API uses an asynchronous callback to return the result. You can call   
[request.agent.show](arkts-basicservices-agent-show-f.md#show) to view the error cause.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-on(event: 'failed', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'failed', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'failed' | Yes | Event type.&lt;br&gt;- **'failed'**: task failure. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |

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

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-Task-on(event: 'pause', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'pause', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'pause' | Yes | Event type.&lt;br&gt;- **'pause'**: task pause. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-Task-on(event: 'resume', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'resume', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'resume' | Yes | Event type.&lt;br&gt;- **'resume'**: task resume. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-Task-on(event: 'remove', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'remove', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'remove' | Yes | Event type.&lt;br&gt;- **'remove'**: task removal. |
| callback | (progress: Progress) =&gt; void | Yes | Callback to be invoked when the specified event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Task-on(event: 'response', callback: Callback<HttpResponse>): void--><!--Device-Task-on(event: 'response', callback: Callback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'response' | Yes | Event type.&lt;br&gt;- **'response'**: task response. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | Yes | Callback used to return the data structure of the task response header. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Task-on(event: 'faultOccur', callback: Callback<Faults>): void--><!--Device-Task-on(event: 'faultOccur', callback: Callback<Faults>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'faultOccur' | Yes | Event type.&lt;br&gt;- **'faultOccur'**: task failure. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Faults&gt; | Yes | Callback used to return the failure cause of the task. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-Task-on(event: 'wait', callback: Callback<WaitingReason>): void--><!--Device-Task-on(event: 'wait', callback: Callback<WaitingReason>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'wait' | Yes | Event type.&lt;br&gt;- 'wait': The task is waiting. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;WaitingReason&gt; | Yes | Callback used to return the waiting reason of the task. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |

## onCompleted

```TypeScript
onCompleted(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

Enables the 'faultOccur' callback.This callback is triggered when the task failed.The returned `Faults` will contain the reason why the task failed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Task-onFaultOccur(callback: Callback<Faults>): void--><!--Device-Task-onFaultOccur(callback: Callback<Faults>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Faults&gt; | Yes | callback function with a `Faults` argument. |

## onPause

```TypeScript
onPause(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Task-onResponse(callback: Callback<HttpResponse>): void--><!--Device-Task-onResponse(callback: Callback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | Yes | callback function with an `HttpResponse` argument. |

## onResume

```TypeScript
onResume(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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

Enables the wait callback.This callback is triggered when the task changes from other states to the waiting state.The returned `WaitingReason` will contain the reason why the task enters waiting state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Task-onWait(callback: Callback<WaitingReason>): void--><!--Device-Task-onWait(callback: Callback<WaitingReason>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;WaitingReason&gt; | Yes | callback function with an `WaitingReason` argument. |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

Pauses a task that is waiting, running, or retrying. A paused task can be resumed by   
[resume](arkts-basicservices-agent-task-i.md#resume). This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Task-pause(callback: AsyncCallback<void>): void--><!--Device-Task-pause(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) | Task service ability error. |

## pause

```TypeScript
pause(): Promise<void>
```

Pauses a task that is waiting, running, or retrying. A paused task can be resumed by   
[resume](arkts-basicservices-agent-task-i.md#resume). This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Task-pause(): Promise<void>--><!--Device-Task-pause(): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) | Task service ability error. |

## resume

```TypeScript
resume(callback: AsyncCallback<void>): void
```

Resumes a paused task. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERNET

<!--Device-Task-resume(callback: AsyncCallback<void>): void--><!--Device-Task-resume(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) | Task service ability error. |

## resume

```TypeScript
resume(): Promise<void>
```

Resumes a paused task. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

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
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) | Operation with wrong task mode.<br>**Applicable version:** 10 and later |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) | Task service ability error. |

## setMaxSpeed

ArkTS-Dyn:
```TypeScript
setMaxSpeed(speed: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setMaxSpeed(speed: long): Promise<void>
```

Sets the maximum number of bytes that can be transmitted by a task per second. This API uses a promise to return the result.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-Task-setMaxSpeed(speed: long): Promise<void>--><!--Device-Task-setMaxSpeed(speed: long): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speed | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | Maximum number of bytes that can be transmitted by a task per second, with a minimum of 16384 bytes. The value cannot be less than the minimum speed value specified by [MinSpeed](arkts-basicservices-agent-minspeed-i.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Missing mandatory parameters. &lt;br&gt; 2. Incorrect parameter type. &lt;br&gt; 3. Parameter verification failed. |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) | Task service ability error. |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts a task. This API uses an asynchronous callback to return the result.

Tasks in the following states can be started:

1. Task created by **request.agent.create**.2. Download tasks that are created by **request.agent.create** but have failed or paused.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-start(callback: AsyncCallback<void>): void--><!--Device-Task-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) | Task service ability error. |

## start

```TypeScript
start(): Promise<void>
```

Starts a task. This API uses a promise to return the result.

Tasks in the following states can be started:

1. Task created by **request.agent.create**.2. Download tasks that are created by **request.agent.create** but have failed or paused.

> **NOTE：**
> 
> For details about how to obtain the context in the example, see
> [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability)
> .

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

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
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) | Task service ability error. |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops a task that is running, waiting, or retrying. A paused task can be resumed by   
[start](arkts-basicservices-agent-task-i.md#start). This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-stop(callback: AsyncCallback<void>): void--><!--Device-Task-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) | Task service ability error. |

## stop

```TypeScript
stop(): Promise<void>
```

Stops a task that is running, waiting, or retrying. A paused task can be resumed by   
[start](arkts-basicservices-agent-task-i.md#start). This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

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
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) | Operation with wrong task state. |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) | Task service ability error. |

## config

```TypeScript
config: Config
```

Task configuration.

**Type:** [Config](arkts-basicservices-agent-config-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-config: Config--><!--Device-Task-config: Config-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## tid

```TypeScript
readonly tid: string
```

Task ID, which is unique and automatically generated by the system.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-readonly tid: string--><!--Device-Task-readonly tid: string-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

