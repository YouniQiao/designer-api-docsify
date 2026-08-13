# Task

Implements an upload or download task. Before using this API, you must obtain a **Task** object, from a promise through [request.agent.create](arkts-basicservices-agent-create-f.md#create) or from a callback through [request.agent.create](arkts-basicservices-agent-create-f.md#create). > **NOTE：**> > The **Task** object and its mounting callback function are released and automatically reclaimed by the system > after the **remove** method is called.

**Since:** 23

**Deprecated since:** -1

<!--Device-agent-interface Task--><!--Device-agent-interface Task-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## offCompleted

```TypeScript
offCompleted(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-offCompleted(callback?: ProgressCallback): void--><!--Device-Task-offCompleted(callback?: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | No |

## offFailed

```TypeScript
offFailed(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-offFailed(callback?: ProgressCallback): void--><!--Device-Task-offFailed(callback?: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | No |

## offFaultOccur

```TypeScript
offFaultOccur(callback?: Callback<Faults>): void
```

Disables the 'faultOccur' callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-offFaultOccur(callback?: Callback<Faults>): void--><!--Device-Task-offFaultOccur(callback?: Callback<Faults>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | No |

## offPause

```TypeScript
offPause(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-offPause(callback?: ProgressCallback): void--><!--Device-Task-offPause(callback?: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | No |

## offProgress

```TypeScript
offProgress(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-offProgress(callback?: ProgressCallback): void--><!--Device-Task-offProgress(callback?: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | No |

## offRemove

```TypeScript
offRemove(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-offRemove(callback?: ProgressCallback): void--><!--Device-Task-offRemove(callback?: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | No |

## offResponse

```TypeScript
offResponse(callback?: Callback<HttpResponse>): void
```

Disables the response callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-offResponse(callback?: Callback<HttpResponse>): void--><!--Device-Task-offResponse(callback?: Callback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | No |

## offResume

```TypeScript
offResume(callback?: ProgressCallback): void
```

Disables the specified callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-offResume(callback?: ProgressCallback): void--><!--Device-Task-offResume(callback?: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | No |

## offWait

```TypeScript
offWait(callback?: Callback<WaitingReason>): void
```

Disables the wait callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-offWait(callback?: Callback<WaitingReason>): void--><!--Device-Task-offWait(callback?: Callback<WaitingReason>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | No |

## off_completed

```TypeScript
off(event: 'completed', callback?: (progress: Progress) => void): void
```

Unsubscribes from task completion events. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-off(event: 'completed', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'completed', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'completed' | Yes |
| callback | (progress: Progress) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |

## off_failed

```TypeScript
off(event: 'failed', callback?: (progress: Progress) => void): void
```

Unsubscribes from task failure events. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-off(event: 'failed', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'failed', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'failed' | Yes |
| callback | (progress: Progress) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |

## off_faultOccur

```TypeScript
off(event: 'faultOccur', callback?: Callback<Faults>): void
```

Unsubscribes from task failure events. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 20

**Deprecated since:** -1

<!--Device-Task-off(event: 'faultOccur', callback?: Callback<Faults>): void--><!--Device-Task-off(event: 'faultOccur', callback?: Callback<Faults>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'faultOccur' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_pause

```TypeScript
off(event: 'pause', callback?: (progress: Progress) => void): void
```

Unsubscribes from the foreground task pause event. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 11

**Deprecated since:** -1

<!--Device-Task-off(event: 'pause', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'pause', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'pause' | Yes |
| callback | (progress: Progress) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_progress

```TypeScript
off(event: 'progress', callback?: (progress: Progress) => void): void
```

Unsubscribes from task progress events. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-off(event: 'progress', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'progress', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'progress' | Yes |
| callback | (progress: Progress) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |

## off_remove

```TypeScript
off(event: 'remove', callback?: (progress: Progress) => void): void
```

Unsubscribes from the task removal event. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 11

**Deprecated since:** -1

<!--Device-Task-off(event: 'remove', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'remove', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'remove' | Yes |
| callback | (progress: Progress) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_response

```TypeScript
off(event: 'response', callback?: Callback<HttpResponse>): void
```

Unsubscribes from task response headers. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Task-off(event: 'response', callback?: Callback<HttpResponse>): void--><!--Device-Task-off(event: 'response', callback?: Callback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'response' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_resume

```TypeScript
off(event: 'resume', callback?: (progress: Progress) => void): void
```

Unsubscribes from foreground task resume events. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 11

**Deprecated since:** -1

<!--Device-Task-off(event: 'resume', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'resume', callback?: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'resume' | Yes |
| callback | (progress: Progress) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off_wait

```TypeScript
off(event: 'wait', callback?: Callback<WaitingReason>): void
```

Unsubscribes from task waiting events. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 20

**Deprecated since:** -1

<!--Device-Task-off(event: 'wait', callback?: Callback<WaitingReason>): void--><!--Device-Task-off(event: 'wait', callback?: Callback<WaitingReason>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'wait' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## onCompleted

```TypeScript
onCompleted(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-onCompleted(callback: ProgressCallback): void--><!--Device-Task-onCompleted(callback: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | Yes |

## onFailed

```TypeScript
onFailed(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-onFailed(callback: ProgressCallback): void--><!--Device-Task-onFailed(callback: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | Yes |

## onFaultOccur

```TypeScript
onFaultOccur(callback: Callback<Faults>): void
```

Enables the 'faultOccur' callback. This callback is triggered when the task failed. The returned `Faults` will contain the reason why the task failed.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-onFaultOccur(callback: Callback<Faults>): void--><!--Device-Task-onFaultOccur(callback: Callback<Faults>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | Yes |

## onPause

```TypeScript
onPause(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-onPause(callback: ProgressCallback): void--><!--Device-Task-onPause(callback: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | Yes |

## onProgress

```TypeScript
onProgress(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-onProgress(callback: ProgressCallback): void--><!--Device-Task-onProgress(callback: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | Yes |

## onRemove

```TypeScript
onRemove(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-onRemove(callback: ProgressCallback): void--><!--Device-Task-onRemove(callback: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | Yes |

## onResponse

```TypeScript
onResponse(callback: Callback<HttpResponse>): void
```

Enables the response callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-onResponse(callback: Callback<HttpResponse>): void--><!--Device-Task-onResponse(callback: Callback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | Yes |

## onResume

```TypeScript
onResume(callback: ProgressCallback): void
```

Enables the specified callback.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-onResume(callback: ProgressCallback): void--><!--Device-Task-onResume(callback: ProgressCallback): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | Yes |

## onWait

```TypeScript
onWait(callback: Callback<WaitingReason>): void
```

Enables the wait callback. This callback is triggered when the task changes from other states to the waiting state. The returned `WaitingReason` will contain the reason why the task enters waiting state.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-onWait(callback: Callback<WaitingReason>): void--><!--Device-Task-onWait(callback: Callback<WaitingReason>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | Yes |

## on_completed

```TypeScript
on(event: 'completed', callback: (progress: Progress) => void): void
```

Subscribes to task completion events. This API uses an asynchronous callback to return the result. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-on(event: 'completed', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'completed', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'completed' | Yes |
| callback | (progress: Progress) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |

## on_failed

```TypeScript
on(event: 'failed', callback: (progress: Progress) => void): void
```

Subscribes to task failure events. This API uses an asynchronous callback to return the result. You can call [request.agent.show](arkts-basicservices-agent-show-f.md#show) to view the error cause. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-on(event: 'failed', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'failed', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'failed' | Yes |
| callback | (progress: Progress) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |

## on_faultOccur

```TypeScript
on(event: 'faultOccur', callback: Callback<Faults>): void
```

Subscribes to task failure events. This API uses a callback to return the result. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 20

**Deprecated since:** -1

<!--Device-Task-on(event: 'faultOccur', callback: Callback<Faults>): void--><!--Device-Task-on(event: 'faultOccur', callback: Callback<Faults>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'faultOccur' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_pause

```TypeScript
on(event: 'pause', callback: (progress: Progress) => void): void
```

Subscribes to task pause events. This API uses an asynchronous callback to return the result. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 11

**Deprecated since:** -1

<!--Device-Task-on(event: 'pause', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'pause', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'pause' | Yes |
| callback | (progress: Progress) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_progress

```TypeScript
on(event: 'progress', callback: (progress: Progress) => void): void
```

Subscribes to task progress changes. This API uses an asynchronous callback to return the result. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-on(event: 'progress', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'progress', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'progress' | Yes |
| callback | (progress: Progress) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |

## on_remove

```TypeScript
on(event: 'remove', callback: (progress: Progress) => void): void
```

Subscribes to task removal events. This API uses an asynchronous callback to return the result. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 11

**Deprecated since:** -1

<!--Device-Task-on(event: 'remove', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'remove', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'remove' | Yes |
| callback | (progress: Progress) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_response

```TypeScript
on(event: 'response', callback: Callback<HttpResponse>): void
```

Subscribes to task response headers. This API uses an asynchronous callback to return the result. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Task-on(event: 'response', callback: Callback<HttpResponse>): void--><!--Device-Task-on(event: 'response', callback: Callback<HttpResponse>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'response' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_resume

```TypeScript
on(event: 'resume', callback: (progress: Progress) => void): void
```

Subscribes to task resume events. This API uses an asynchronous callback to return the result. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 11

**Deprecated since:** -1

<!--Device-Task-on(event: 'resume', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'resume', callback: (progress: Progress) => void): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'resume' | Yes |
| callback | (progress: Progress) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on_wait

```TypeScript
on(event: 'wait', callback: Callback<WaitingReason>): void
```

Subscribes to task wait events. This API uses a callback to return the result. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 20

**Deprecated since:** -1

<!--Device-Task-on(event: 'wait', callback: Callback<WaitingReason>): void--><!--Device-Task-on(event: 'wait', callback: Callback<WaitingReason>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'wait' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

Pauses a task that is waiting, running, or retrying. A paused task can be resumed by [resume](#resume). This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-pause(callback: AsyncCallback<void>): void--><!--Device-Task-pause(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |

## pause

```TypeScript
pause(): Promise<void>
```

Pauses a task that is waiting, running, or retrying. A paused task can be resumed by [resume](#resume). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-pause(): Promise<void>--><!--Device-Task-pause(): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |

## resume

```TypeScript
resume(callback: AsyncCallback<void>): void
```

Resumes a paused task. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERNET

<!--Device-Task-resume(callback: AsyncCallback<void>): void--><!--Device-Task-resume(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |

## resume

```TypeScript
resume(): Promise<void>
```

Resumes a paused task. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERNET

<!--Device-Task-resume(): Promise<void>--><!--Device-Task-resume(): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-task-mode-error) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |

## setMaxSpeed

```TypeScript
setMaxSpeed(speed: number): Promise<void>
```

Sets the maximum number of bytes that can be transmitted by a task per second. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-Task-setMaxSpeed(speed: long): Promise<void>--><!--Device-Task-setMaxSpeed(speed: long): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| speed | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts a task. This API uses an asynchronous callback to return the result. Tasks in the following states can be started: 1. Task created by **request.agent.create**. 2. Download tasks that are created by **request.agent.create** but have failed or paused. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-start(callback: AsyncCallback<void>): void--><!--Device-Task-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |

## start

```TypeScript
start(): Promise<void>
```

Starts a task. This API uses a promise to return the result. Tasks in the following states can be started: 1. Task created by **request.agent.create**. 2. Download tasks that are created by **request.agent.create** but have failed or paused. > **NOTE：**> > For details about how to obtain the context in the example, see > [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability) > .

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERNET

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-start(): Promise<void>--><!--Device-Task-start(): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops a task that is running, waiting, or retrying. A paused task can be resumed by [start](#start). This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-stop(callback: AsyncCallback<void>): void--><!--Device-Task-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |

## stop

```TypeScript
stop(): Promise<void>
```

Stops a task that is running, waiting, or retrying. A paused task can be resumed by [start](#start). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-stop(): Promise<void>--><!--Device-Task-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-operation-not-supported-by-the-task-state) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-service-error) |

## config

```TypeScript
config: Config
```

Task configuration.

**Type:** Config

**Since:** 23

**Deprecated since:** -1

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

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Task-readonly tid: string--><!--Device-Task-readonly tid: string-End-->

**System capability:** SystemCapability.Request.FileTransferAgent
