# Task

上传或下载任务。使用该方法前需要先获取Task对象，promise形式通过 [request.agent.create](arkts-basicservices-agent-create-f.md#create)获取， callback形式通过 [request.agent.create](arkts-basicservices-agent-create-f.md#create)获取。 > **说明：** > > Task对象及其挂载回调函数会在调用remove方法后释放并被系统自动回收。

**起始版本：** 23

**废弃版本：** -1

<!--Device-agent-interface Task--><!--Device-agent-interface Task-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

## offCompleted

```TypeScript
offCompleted(callback?: ProgressCallback): void
```

Disables the specified callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-offCompleted(callback?: ProgressCallback): void--><!--Device-Task-offCompleted(callback?: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 否 |

## offFailed

```TypeScript
offFailed(callback?: ProgressCallback): void
```

Disables the specified callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-offFailed(callback?: ProgressCallback): void--><!--Device-Task-offFailed(callback?: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 否 |

## offFaultOccur

```TypeScript
offFaultOccur(callback?: Callback<Faults>): void
```

Disables the 'faultOccur' callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-offFaultOccur(callback?: Callback<Faults>): void--><!--Device-Task-offFaultOccur(callback?: Callback<Faults>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | 否 |

## offPause

```TypeScript
offPause(callback?: ProgressCallback): void
```

Disables the specified callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-offPause(callback?: ProgressCallback): void--><!--Device-Task-offPause(callback?: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 否 |

## offProgress

```TypeScript
offProgress(callback?: ProgressCallback): void
```

Disables the specified callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-offProgress(callback?: ProgressCallback): void--><!--Device-Task-offProgress(callback?: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 否 |

## offRemove

```TypeScript
offRemove(callback?: ProgressCallback): void
```

Disables the specified callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-offRemove(callback?: ProgressCallback): void--><!--Device-Task-offRemove(callback?: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 否 |

## offResponse

```TypeScript
offResponse(callback?: Callback<HttpResponse>): void
```

Disables the response callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-offResponse(callback?: Callback<HttpResponse>): void--><!--Device-Task-offResponse(callback?: Callback<HttpResponse>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[HttpResponse](arkts-basicservices-agent-httpresponse-i.md)&gt; | 否 |

## offResume

```TypeScript
offResume(callback?: ProgressCallback): void
```

Disables the specified callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-offResume(callback?: ProgressCallback): void--><!--Device-Task-offResume(callback?: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 否 |

## offWait

```TypeScript
offWait(callback?: Callback<WaitingReason>): void
```

Disables the wait callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-offWait(callback?: Callback<WaitingReason>): void--><!--Device-Task-offWait(callback?: Callback<WaitingReason>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | 否 |

## off_completed

```TypeScript
off(event: 'completed', callback?: (progress: Progress) => void): void
```

取消订阅任务完成事件。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-off(event: 'completed', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'completed', callback?: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'completed' | 是 |
| callback | (progress: Progress) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-任务模式错误) |

## off_failed

```TypeScript
off(event: 'failed', callback?: (progress: Progress) => void): void
```

取消订阅任务失败事件。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-off(event: 'failed', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'failed', callback?: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'failed' | 是 |
| callback | (progress: Progress) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-任务模式错误) |

## off_faultOccur

```TypeScript
off(event: 'faultOccur', callback?: Callback<Faults>): void
```

取消订阅任务失败原因相关的事件。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 20

**废弃版本：** -1

<!--Device-Task-off(event: 'faultOccur', callback?: Callback<Faults>): void--><!--Device-Task-off(event: 'faultOccur', callback?: Callback<Faults>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'faultOccur' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off_pause

```TypeScript
off(event: 'pause', callback?: (progress: Progress) => void): void
```

取消订阅任务暂停事件。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 11

**废弃版本：** -1

<!--Device-Task-off(event: 'pause', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'pause', callback?: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'pause' | 是 |
| callback | (progress: Progress) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off_progress

```TypeScript
off(event: 'progress', callback?: (progress: Progress) => void): void
```

取消订阅任务进度事件。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-off(event: 'progress', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'progress', callback?: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'progress' | 是 |
| callback | (progress: Progress) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-任务模式错误) |

## off_remove

```TypeScript
off(event: 'remove', callback?: (progress: Progress) => void): void
```

取消订阅任务移除事件。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 11

**废弃版本：** -1

<!--Device-Task-off(event: 'remove', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'remove', callback?: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'remove' | 是 |
| callback | (progress: Progress) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off_response

```TypeScript
off(event: 'response', callback?: Callback<HttpResponse>): void
```

取消订阅任务响应事件。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Task-off(event: 'response', callback?: Callback<HttpResponse>): void--><!--Device-Task-off(event: 'response', callback?: Callback<HttpResponse>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'response' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[HttpResponse](arkts-basicservices-agent-httpresponse-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off_resume

```TypeScript
off(event: 'resume', callback?: (progress: Progress) => void): void
```

取消订阅任务恢复事件。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 11

**废弃版本：** -1

<!--Device-Task-off(event: 'resume', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'resume', callback?: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'resume' | 是 |
| callback | (progress: Progress) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off_wait

```TypeScript
off(event: 'wait', callback?: Callback<WaitingReason>): void
```

取消订阅任务等待原因相关的事件。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 20

**废弃版本：** -1

<!--Device-Task-off(event: 'wait', callback?: Callback<WaitingReason>): void--><!--Device-Task-off(event: 'wait', callback?: Callback<WaitingReason>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'wait' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## onCompleted

```TypeScript
onCompleted(callback: ProgressCallback): void
```

Enables the specified callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-onCompleted(callback: ProgressCallback): void--><!--Device-Task-onCompleted(callback: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 是 |

## onFailed

```TypeScript
onFailed(callback: ProgressCallback): void
```

Enables the specified callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-onFailed(callback: ProgressCallback): void--><!--Device-Task-onFailed(callback: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 是 |

## onFaultOccur

```TypeScript
onFaultOccur(callback: Callback<Faults>): void
```

Enables the 'faultOccur' callback. This callback is triggered when the task failed. The returned `Faults` will contain the reason why the task failed.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-onFaultOccur(callback: Callback<Faults>): void--><!--Device-Task-onFaultOccur(callback: Callback<Faults>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | 是 |

## onPause

```TypeScript
onPause(callback: ProgressCallback): void
```

Enables the specified callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-onPause(callback: ProgressCallback): void--><!--Device-Task-onPause(callback: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 是 |

## onProgress

```TypeScript
onProgress(callback: ProgressCallback): void
```

Enables the specified callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-onProgress(callback: ProgressCallback): void--><!--Device-Task-onProgress(callback: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 是 |

## onRemove

```TypeScript
onRemove(callback: ProgressCallback): void
```

Enables the specified callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-onRemove(callback: ProgressCallback): void--><!--Device-Task-onRemove(callback: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 是 |

## onResponse

```TypeScript
onResponse(callback: Callback<HttpResponse>): void
```

Enables the response callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-onResponse(callback: Callback<HttpResponse>): void--><!--Device-Task-onResponse(callback: Callback<HttpResponse>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[HttpResponse](arkts-basicservices-agent-httpresponse-i.md)&gt; | 是 |

## onResume

```TypeScript
onResume(callback: ProgressCallback): void
```

Enables the specified callback.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-onResume(callback: ProgressCallback): void--><!--Device-Task-onResume(callback: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 是 |

## onWait

```TypeScript
onWait(callback: Callback<WaitingReason>): void
```

Enables the wait callback. This callback is triggered when the task changes from other states to the waiting state. The returned `WaitingReason` will contain the reason why the task enters waiting state.

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-onWait(callback: Callback<WaitingReason>): void--><!--Device-Task-onWait(callback: Callback<WaitingReason>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | 是 |

## on_completed

```TypeScript
on(event: 'completed', callback: (progress: Progress) => void): void
```

订阅任务完成事件，使用callback异步回调。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-on(event: 'completed', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'completed', callback: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'completed' | 是 |
| callback | (progress: Progress) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-任务模式错误) |

## on_failed

```TypeScript
on(event: 'failed', callback: (progress: Progress) => void): void
```

订阅任务失败事件，使用callback异步回调。可通过调用 [request.agent.show](arkts-basicservices-agent-show-f.md#show)查看错误原因 。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-on(event: 'failed', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'failed', callback: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'failed' | 是 |
| callback | (progress: Progress) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-任务模式错误) |

## on_faultOccur

```TypeScript
on(event: 'faultOccur', callback: Callback<Faults>): void
```

订阅任务失败原因，使用callback形式返回结果。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 20

**废弃版本：** -1

<!--Device-Task-on(event: 'faultOccur', callback: Callback<Faults>): void--><!--Device-Task-on(event: 'faultOccur', callback: Callback<Faults>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'faultOccur' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on_pause

```TypeScript
on(event: 'pause', callback: (progress: Progress) => void): void
```

订阅任务暂停事件，使用callback异步回调。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 11

**废弃版本：** -1

<!--Device-Task-on(event: 'pause', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'pause', callback: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'pause' | 是 |
| callback | (progress: Progress) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on_progress

```TypeScript
on(event: 'progress', callback: (progress: Progress) => void): void
```

订阅任务进度的事件，使用callback异步回调。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-on(event: 'progress', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'progress', callback: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'progress' | 是 |
| callback | (progress: Progress) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-任务模式错误) |

## on_remove

```TypeScript
on(event: 'remove', callback: (progress: Progress) => void): void
```

订阅任务移除事件，使用callback异步回调。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 11

**废弃版本：** -1

<!--Device-Task-on(event: 'remove', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'remove', callback: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'remove' | 是 |
| callback | (progress: Progress) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on_response

```TypeScript
on(event: 'response', callback: Callback<HttpResponse>): void
```

订阅任务响应头，使用callback异步回调。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Task-on(event: 'response', callback: Callback<HttpResponse>): void--><!--Device-Task-on(event: 'response', callback: Callback<HttpResponse>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'response' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[HttpResponse](arkts-basicservices-agent-httpresponse-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on_resume

```TypeScript
on(event: 'resume', callback: (progress: Progress) => void): void
```

订阅任务恢复事件，使用callback异步回调。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 11

**废弃版本：** -1

<!--Device-Task-on(event: 'resume', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'resume', callback: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'resume' | 是 |
| callback | (progress: Progress) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on_wait

```TypeScript
on(event: 'wait', callback: Callback<WaitingReason>): void
```

订阅任务等待原因，使用callback形式返回结果。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 20

**废弃版本：** -1

<!--Device-Task-on(event: 'wait', callback: Callback<WaitingReason>): void--><!--Device-Task-on(event: 'wait', callback: Callback<WaitingReason>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | 'wait' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

暂停任务，可以暂停正在等待/正在运行/正在重试的任务，已暂停的任务可被 [resume](#resume)恢复。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-pause(callback: AsyncCallback<void>): void--><!--Device-Task-pause(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-在不支持的状态上的操作) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-任务模式错误) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |

## pause

```TypeScript
pause(): Promise<void>
```

暂停任务，可以暂停正在等待/正在运行/正在重试的任务，已暂停的任务可被 [resume](#resume)恢复。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-pause(): Promise<void>--><!--Device-Task-pause(): Promise<void>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-在不支持的状态上的操作) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-任务模式错误) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |

## resume

```TypeScript
resume(callback: AsyncCallback<void>): void
```

重新启动任务，可以恢复被暂停的任务。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.INTERNET

<!--Device-Task-resume(callback: AsyncCallback<void>): void--><!--Device-Task-resume(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-在不支持的状态上的操作) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-任务模式错误) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |

## resume

```TypeScript
resume(): Promise<void>
```

重新启动任务，可以恢复被暂停的任务。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.INTERNET

<!--Device-Task-resume(): Promise<void>--><!--Device-Task-resume(): Promise<void>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-在不支持的状态上的操作) |
| [21900005](../../apis-basic-services-kit/errorcode-request.md#21900005-任务模式错误) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |

## setMaxSpeed

```TypeScript
setMaxSpeed(speed: number): Promise<void>
```

设置任务每秒能传输的字节数上限。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Task-setMaxSpeed(speed: long): Promise<void>--><!--Device-Task-setMaxSpeed(speed: long): Promise<void>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| speed | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

启动一个任务。使用callback异步回调。 以下状态的任务可以被启动： 1. 刚被request.agent.create接口创建的任务。 2. 使用request.agent.create接口创建的已经失败或者停止的下载任务。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-start(callback: AsyncCallback<void>): void--><!--Device-Task-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-在不支持的状态上的操作) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |

## start

```TypeScript
start(): Promise<void>
```

启动一个任务。使用Promise异步回调。 以下状态的任务可以被启动： 1. 刚被request.agent.create接口创建的任务。 2. 使用request.agent.create接口创建的已经失败或者停止的下载任务。 > **说明：** > > 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-start(): Promise<void>--><!--Device-Task-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-在不支持的状态上的操作) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止任务，可以停止正在运行/正在等待/正在重试的任务，已停止的任务可被 [start](#start)恢复。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-stop(callback: AsyncCallback<void>): void--><!--Device-Task-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-在不支持的状态上的操作) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |

## stop

```TypeScript
stop(): Promise<void>
```

停止任务，可以停止正在运行/正在等待/正在重试的任务，已停止的任务可被 [start](#start)恢复。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-stop(): Promise<void>--><!--Device-Task-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [21900007](../../apis-basic-services-kit/errorcode-request.md#21900007-在不支持的状态上的操作) |
| [13400003](../../apis-basic-services-kit/errorcode-request.md#13400003-服务异常) |

## config

```TypeScript
config: Config
```

任务的配置信息。

**类型：** Config

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-config: Config--><!--Device-Task-config: Config-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

## tid

```TypeScript
readonly tid: string
```

任务id，由系统自动生成且唯一。

**类型：** string

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-readonly tid: string--><!--Device-Task-readonly tid: string-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent
