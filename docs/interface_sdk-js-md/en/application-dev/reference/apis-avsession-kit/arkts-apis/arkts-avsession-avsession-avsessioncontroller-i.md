# AVSessionController

Session controller,used to control media playback and get media information

**Since:** 23

<!--Device-avSession-interface AVSessionController--><!--Device-avSession-interface AVSessionController-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from 'avSession';
```

## destroy

```TypeScript
destroy(callback: AsyncCallback<void>): void
```

Destroy the server controller

**Since:** 23

<!--Device-AVSessionController-destroy(callback: AsyncCallback<void>): void--><!--Device-AVSessionController-destroy(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The asyncCallback triggered when the command is executed successfully. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## destroy

```TypeScript
destroy(): Promise<void>
```

Destroy the server controller

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-destroy(): Promise<void>--><!--Device-AVSessionController-destroy(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVCallState

```TypeScript
getAVCallState(callback: AsyncCallback<AVCallState>): void
```

Get the call status of the current session

**Since:** 23

<!--Device-AVSessionController-getAVCallState(callback: AsyncCallback<AVCallState>): void--><!--Device-AVSessionController-getAVCallState(callback: AsyncCallback<AVCallState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVCallState](arkts-avsession-avsession-avcallstate-i.md)&gt; | Yes | The triggered asyncCallback when (getAVCallState). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVCallState

```TypeScript
getAVCallState(): Promise<AVCallState>
```

Get the call status of the current session

**Since:** 23

<!--Device-AVSessionController-getAVCallState(): Promise<AVCallState>--><!--Device-AVSessionController-getAVCallState(): Promise<AVCallState>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AVCallState](arkts-avsession-avsession-avcallstate-i.md)&gt; | (AVCallState) returned through promise |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVMetadata

```TypeScript
getAVMetadata(callback: AsyncCallback<AVMetadata>): void
```

Get the metadata of the current session

**Since:** 23

<!--Device-AVSessionController-getAVMetadata(callback: AsyncCallback<AVMetadata>): void--><!--Device-AVSessionController-getAVMetadata(callback: AsyncCallback<AVMetadata>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;AVMetadata&gt; | Yes | The triggered asyncCallback when (getAVMetadata). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVMetadata

```TypeScript
getAVMetadata(): Promise<AVMetadata>
```

Get the metadata of the current session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getAVMetadata(): Promise<AVMetadata>--><!--Device-AVSessionController-getAVMetadata(): Promise<AVMetadata>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AVMetadata&gt; | (AVMetadata) returned through promise |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVMetadataSync

```TypeScript
getAVMetadataSync(): AVMetadata
```

Get the metadata of the current session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getAVMetadataSync(): AVMetadata--><!--Device-AVSessionController-getAVMetadataSync(): AVMetadata-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| AVMetadata | (AVMetadata) returned |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVPlaybackState

```TypeScript
getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void
```

Get the playback status of the current session

**Since:** 23

<!--Device-AVSessionController-getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void--><!--Device-AVSessionController-getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md)&gt; | Yes | The triggered asyncCallback when (getAVPlaybackState). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVPlaybackState

```TypeScript
getAVPlaybackState(): Promise<AVPlaybackState>
```

Get the playback status of the current session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getAVPlaybackState(): Promise<AVPlaybackState>--><!--Device-AVSessionController-getAVPlaybackState(): Promise<AVPlaybackState>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md)&gt; | (AVPlaybackState) returned through promise |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVPlaybackStateSync

```TypeScript
getAVPlaybackStateSync(): AVPlaybackState
```

Get the playback status of the current session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getAVPlaybackStateSync(): AVPlaybackState--><!--Device-AVSessionController-getAVPlaybackStateSync(): AVPlaybackState-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md) | (AVPlaybackState) returned |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVQueueItems

```TypeScript
getAVQueueItems(callback: AsyncCallback<Array<AVQueueItem>>): void
```

Get the playlist of the current session

**Since:** 23

<!--Device-AVSessionController-getAVQueueItems(callback: AsyncCallback<Array<AVQueueItem>>): void--><!--Device-AVSessionController-getAVQueueItems(callback: AsyncCallback<Array<AVQueueItem>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt;&gt; | Yes | The triggered asyncCallback when (getAVQueueItems). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVQueueItems

```TypeScript
getAVQueueItems(): Promise<Array<AVQueueItem>>
```

Get the playlist of the current session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getAVQueueItems(): Promise<Array<AVQueueItem>>--><!--Device-AVSessionController-getAVQueueItems(): Promise<Array<AVQueueItem>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt;&gt; | (Array&lt;AVQueueItem&gt;) returned through promise |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVQueueItemsSync

```TypeScript
getAVQueueItemsSync(): Array<AVQueueItem>
```

Get the playlist of the current session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getAVQueueItemsSync(): Array<AVQueueItem>--><!--Device-AVSessionController-getAVQueueItemsSync(): Array<AVQueueItem>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt; | (Array&lt;AVQueueItem&gt;) returned |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVQueueTitle

```TypeScript
getAVQueueTitle(callback: AsyncCallback<string>): void
```

Get the name of the playlist of the current session

**Since:** 23

<!--Device-AVSessionController-getAVQueueTitle(callback: AsyncCallback<string>): void--><!--Device-AVSessionController-getAVQueueTitle(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | The triggered asyncCallback when (getAVQueueTitle). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVQueueTitle

```TypeScript
getAVQueueTitle(): Promise<string>
```

Get the name of the playlist of the current session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getAVQueueTitle(): Promise<string>--><!--Device-AVSessionController-getAVQueueTitle(): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | (string) returned through promise |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getAVQueueTitleSync

```TypeScript
getAVQueueTitleSync(): string
```

Get the name of the playlist of the current session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getAVQueueTitleSync(): string--><!--Device-AVSessionController-getAVQueueTitleSync(): string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | (string) returned |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getCallMetadata

```TypeScript
getCallMetadata(callback: AsyncCallback<CallMetadata>): void
```

Get the call metadata of the current session

**Since:** 23

<!--Device-AVSessionController-getCallMetadata(callback: AsyncCallback<CallMetadata>): void--><!--Device-AVSessionController-getCallMetadata(callback: AsyncCallback<CallMetadata>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CallMetadata](arkts-avsession-avsession-callmetadata-i.md)&gt; | Yes | The triggered asyncCallback when (getCallMetadata). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getCallMetadata

```TypeScript
getCallMetadata(): Promise<CallMetadata>
```

Get the call metadata of the current session

**Since:** 23

<!--Device-AVSessionController-getCallMetadata(): Promise<CallMetadata>--><!--Device-AVSessionController-getCallMetadata(): Promise<CallMetadata>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[CallMetadata](arkts-avsession-avsession-callmetadata-i.md)&gt; | (CallMetadata) returned through promise |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getDesktopLyricState

```TypeScript
getDesktopLyricState(): Promise<DesktopLyricState>
```

Get desktop lyric state such as lock state for this session.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-getDesktopLyricState(): Promise<DesktopLyricState>--><!--Device-AVSessionController-getDesktopLyricState(): Promise<DesktopLyricState>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DesktopLyricState](arkts-avsession-avsession-desktoplyricstate-i.md)&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600110](../errorcode-avsession.md#6600110-desktop-lyrics-not-enabled-for-the-application) | The desktop lyrics feature of this application is not enabled. |
| [6600111](../errorcode-avsession.md#6600111-desktop-lyrics-not-supported-for-the-current-device) | The desktop lyrics feature is not supported. |

## getExtras

```TypeScript
getExtras(callback: AsyncCallback<{[key: string]: Object}>): void
```

Get custom media packets provided by the corresponding session

**Since:** 10

<!--Device-AVSessionController-getExtras(callback: AsyncCallback<{[key: string]: Object}>): void--><!--Device-AVSessionController-getExtras(callback: AsyncCallback<{[key: string]: Object}>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;{[key: string]: Object}&gt; | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |
| [6600107](../errorcode-avsession.md#6600107-too-many-commands-or-events) | Too many commands or events. |

## getExtras

```TypeScript
getExtras(callback: AsyncCallback<Record<string, Object>>): void
```

Get custom media packets provided by the corresponding session

**Since:** 23

<!--Device-AVSessionController-getExtras(callback: AsyncCallback<Record<string, Object>>): void--><!--Device-AVSessionController-getExtras(callback: AsyncCallback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Record&lt;string, Object&gt;&gt; | Yes | The triggered asyncCallback when (getExtras). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |
| [6600107](../errorcode-avsession.md#6600107-too-many-commands-or-events) | Too many commands or events. |

## getExtras

```TypeScript
getExtras(): Promise<{[key: string]: Object}>
```

Get custom media packets provided by the corresponding session

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getExtras(): Promise<{[key: string]: Object}>--><!--Device-AVSessionController-getExtras(): Promise<{[key: string]: Object}>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;{[key: string]: Object}&gt; | > } the parameters of extras |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |
| [6600107](../errorcode-avsession.md#6600107-too-many-commands-or-events) | Too many commands or events. |

## getExtras

```TypeScript
getExtras(): Promise<Record<string, Object>>
```

Get custom media packets provided by the corresponding session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVSessionController-getExtras(): Promise<Record<string, Object>>--><!--Device-AVSessionController-getExtras(): Promise<Record<string, Object>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Record&lt;string, Object&gt;&gt; | the parameters of extras |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |
| [6600107](../errorcode-avsession.md#6600107-too-many-commands-or-events) | Too many commands or events. |

## getExtrasWithEvent

```TypeScript
getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>
```

Get extra information for remote device, such as volume level, connected devices.

**Since:** 23

<!--Device-AVSessionController-getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>--><!--Device-AVSessionController-getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| extraEvent | string | Yes | the event name to get |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ExtraInfo](arkts-avsession-avsession-extrainfo-t.md)&gt; | the value returned for such event |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |

## getLaunchAbility

```TypeScript
getLaunchAbility(callback: AsyncCallback<WantAgent>): void
```

Get the WantAgent of this session that can launch the session ability

**Since:** 23

<!--Device-AVSessionController-getLaunchAbility(callback: AsyncCallback<WantAgent>): void--><!--Device-AVSessionController-getLaunchAbility(callback: AsyncCallback<WantAgent>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md)&gt; | Yes | The asyncCallback triggered when getting the WantAgent. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getLaunchAbility

```TypeScript
getLaunchAbility(): Promise<WantAgent>
```

Get the WantAgent of this session that can launch the session ability

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getLaunchAbility(): Promise<WantAgent>--><!--Device-AVSessionController-getLaunchAbility(): Promise<WantAgent>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md)&gt; | WantAgent promise |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getMediaCenterControlType

```TypeScript
getMediaCenterControlType(): Promise<Array<AVMediaCenterControlType>>
```

Get media control type that the can be displayed on the media center.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-getMediaCenterControlType(): Promise<Array<AVMediaCenterControlType>>--><!--Device-AVSessionController-getMediaCenterControlType(): Promise<Array<AVMediaCenterControlType>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[AVMediaCenterControlType](arkts-avsession-avsession-avmediacentercontroltype-t.md)&gt;&gt; | The control types that the app sets to be displayed on the media center. The default value is empty, indicating that the types of the customized display control is not set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getOutputDevice

```TypeScript
getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void
```

Get output device information

**Since:** 23

<!--Device-AVSessionController-getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void--><!--Device-AVSessionController-getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md)&gt; | Yes | The triggered asyncCallback when (getOutputDevice). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 600101 | Session service exception. |
| 600103 | The session controller does not exist. |

## getOutputDevice

```TypeScript
getOutputDevice(): Promise<OutputDeviceInfo>
```

Get output device information

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getOutputDevice(): Promise<OutputDeviceInfo>--><!--Device-AVSessionController-getOutputDevice(): Promise<OutputDeviceInfo>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md)&gt; | (OutputDeviceInfo) returned through promise |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 600101 | Session service exception. |
| 600103 | The session controller does not exist. |

## getOutputDeviceSync

```TypeScript
getOutputDeviceSync(): OutputDeviceInfo
```

Get output device information

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getOutputDeviceSync(): OutputDeviceInfo--><!--Device-AVSessionController-getOutputDeviceSync(): OutputDeviceInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md) | (OutputDeviceInfo) returned |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getRealPlaybackPositionSync

```TypeScript
getRealPlaybackPositionSync(): long
```

Get the adjusted playback position. The time automatically calculated by the system taking into account factors such as playback status, playback speed, and application update time.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getRealPlaybackPositionSync(): long--><!--Device-AVSessionController-getRealPlaybackPositionSync(): long-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| long | current playback position in ms.Note that the returns value of each call will be different. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getSupportedLoopModes

```TypeScript
getSupportedLoopModes(): Promise<Array<LoopMode>>
```

Get supported loop modes supplied by application.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVSessionController-getSupportedLoopModes(): Promise<Array<LoopMode>>--><!--Device-AVSessionController-getSupportedLoopModes(): Promise<Array<LoopMode>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[LoopMode](arkts-avsession-avsession-loopmode-e.md)&gt;&gt; | supported loop modes returned through promise |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getSupportedPlaySpeeds

```TypeScript
getSupportedPlaySpeeds(): Promise<Array<double>>
```

Get supported speeds supplied by application.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVSessionController-getSupportedPlaySpeeds(): Promise<Array<double>>--><!--Device-AVSessionController-getSupportedPlaySpeeds(): Promise<Array<double>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;double&gt;&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getValidCommands

```TypeScript
getValidCommands(callback: AsyncCallback<Array<AVControlCommandType>>): void
```

Get commands supported by the current session

**Since:** 23

<!--Device-AVSessionController-getValidCommands(callback: AsyncCallback<Array<AVControlCommandType>>): void--><!--Device-AVSessionController-getValidCommands(callback: AsyncCallback<Array<AVControlCommandType>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AVControlCommandType](arkts-avsession-avsession-avcontrolcommandtype-t.md)&gt;&gt; | Yes | The triggered asyncCallback when ( getValidCommands). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getValidCommands

```TypeScript
getValidCommands(): Promise<Array<AVControlCommandType>>
```

Get commands supported by the current session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getValidCommands(): Promise<Array<AVControlCommandType>>--><!--Device-AVSessionController-getValidCommands(): Promise<Array<AVControlCommandType>>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[AVControlCommandType](arkts-avsession-avsession-avcontrolcommandtype-t.md)&gt;&gt; | array of AVControlCommandType promise |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## getValidCommandsSync

```TypeScript
getValidCommandsSync(): Array<AVControlCommandType>
```

Get commands supported by the current session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-getValidCommandsSync(): Array<AVControlCommandType>--><!--Device-AVSessionController-getValidCommandsSync(): Array<AVControlCommandType>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[AVControlCommandType](arkts-avsession-avsession-avcontrolcommandtype-t.md)&gt; | array of AVControlCommandType |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## isActive

```TypeScript
isActive(callback: AsyncCallback<boolean>): void
```

Check if the current session is active

**Since:** 23

<!--Device-AVSessionController-isActive(callback: AsyncCallback<boolean>): void--><!--Device-AVSessionController-isActive(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | The triggered asyncCallback when (isActive). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## isActive

```TypeScript
isActive(): Promise<boolean>
```

Check if the current session is active

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-isActive(): Promise<boolean>--><!--Device-AVSessionController-isActive(): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | boolean promise |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## isActiveSync

```TypeScript
isActiveSync(): boolean
```

Check if the current session is active

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-isActiveSync(): boolean--><!--Device-AVSessionController-isActiveSync(): boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | boolean |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## isDesktopLyricEnabled

```TypeScript
isDesktopLyricEnabled(): Promise<boolean>
```

Query desktop lyric enabled state for this session.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-isDesktopLyricEnabled(): Promise<boolean>--><!--Device-AVSessionController-isDesktopLyricEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | return the enabled status |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600111](../errorcode-avsession.md#6600111-desktop-lyrics-not-supported-for-the-current-device) | The desktop lyrics feature is not supported. |

## isDesktopLyricVisible

```TypeScript
isDesktopLyricVisible(): Promise<boolean>
```

Query desktop lyric visible state for this session.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-isDesktopLyricVisible(): Promise<boolean>--><!--Device-AVSessionController-isDesktopLyricVisible(): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | return desktop lyric visible state |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600110](../errorcode-avsession.md#6600110-desktop-lyrics-not-enabled-for-the-application) | The desktop lyrics feature of this application is not enabled. |
| [6600111](../errorcode-avsession.md#6600111-desktop-lyrics-not-supported-for-the-current-device) | The desktop lyrics feature is not supported. |

## offActiveStateChange

```TypeScript
offActiveStateChange(callback?: Callback<boolean>): void
```

Unregister the active state of this session changed callback

**Since:** 23

<!--Device-AVSessionController-offActiveStateChange(callback?: Callback<boolean>): void--><!--Device-AVSessionController-offActiveStateChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | The callback used to handle the active state of this session changed event. The callback function provides the changed session state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offCallMetadataChange

```TypeScript
offCallMetadataChange(callback?: Callback<CallMetadata>): void
```

Unregister call metadata changed callback

**Since:** 23

<!--Device-AVSessionController-offCallMetadataChange(callback?: Callback<CallMetadata>): void--><!--Device-AVSessionController-offCallMetadataChange(callback?: Callback<CallMetadata>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallMetadata](arkts-avsession-avsession-callmetadata-i.md)&gt; | No | The callback used to handle call metadata changed event. The callback function provides the [CallMetadata](arkts-avsession-avsession-callmetadata-i.md#callmetadata) parameter. It only contains the properties set in the filter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offCallStateChange

```TypeScript
offCallStateChange(callback?: Callback<AVCallState>): void
```

Unregister playback state changed callback

**Since:** 23

<!--Device-AVSessionController-offCallStateChange(callback?: Callback<AVCallState>): void--><!--Device-AVSessionController-offCallStateChange(callback?: Callback<AVCallState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCallState](arkts-avsession-avsession-avcallstate-i.md)&gt; | No | The callback used to handle call state changed event. The callback function provides the [AVCallState](arkts-avsession-avsession-avcallstate-i.md#avcallstate) parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offCustomDataChange

```TypeScript
offCustomDataChange(callback?: Callback<Record<string, Object>>): void
```

Unregister listener for custom data.

**Since:** 23

<!--Device-AVSessionController-offCustomDataChange(callback?: Callback<Record<string, Object>>): void--><!--Device-AVSessionController-offCustomDataChange(callback?: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | No | Callback used to retrieve custom data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offDesktopLyricEnabled

```TypeScript
offDesktopLyricEnabled(callback?: Callback<boolean>): void
```

Unregister desktop lyric enable state change callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-offDesktopLyricEnabled(callback?: Callback<boolean>): void--><!--Device-AVSessionController-offDesktopLyricEnabled(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | a callback to receive desktop lyric enable state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offDesktopLyricStateChanged

```TypeScript
offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void
```

Unregister desktop lyric state changed callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void--><!--Device-AVSessionController-offDesktopLyricStateChanged(callback?: Callback<DesktopLyricState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DesktopLyricState](arkts-avsession-avsession-desktoplyricstate-i.md)&gt; | No | a callback to receive desktop lyric state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offDesktopLyricVisibilityChanged

```TypeScript
offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void
```

Unregister desktop lyric visible state change callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void--><!--Device-AVSessionController-offDesktopLyricVisibilityChanged(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | a callback to receive desktop lyric window visible state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offExtrasChange

```TypeScript
offExtrasChange(callback?: Callback<Record<string, Object>>): void
```

Unregister the custom media packets change callback

**Since:** 23

<!--Device-AVSessionController-offExtrasChange(callback?: Callback<Record<string, Object>>): void--><!--Device-AVSessionController-offExtrasChange(callback?: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | No | Used to handle custom media packets changed. The callback provides the new media packets. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offMediaCenterControlTypeChanged

```TypeScript
offMediaCenterControlTypeChanged(callback?: Callback<Array<AVMediaCenterControlType>>): void
```

Unregister media center control type changed callback.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-offMediaCenterControlTypeChanged(callback?: Callback<Array<AVMediaCenterControlType>>): void--><!--Device-AVSessionController-offMediaCenterControlTypeChanged(callback?: Callback<Array<AVMediaCenterControlType>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVMediaCenterControlType](arkts-avsession-avsession-avmediacentercontroltype-t.md)&gt;&gt; | No | Callback to receive the changed control types. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offMetadataChange

```TypeScript
offMetadataChange(callback?: Callback<AVMetadata>): void
```

Unregister metadata changed callback

**Since:** 23

<!--Device-AVSessionController-offMetadataChange(callback?: Callback<AVMetadata>): void--><!--Device-AVSessionController-offMetadataChange(callback?: Callback<AVMetadata>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVMetadata&gt; | No | The callback used to handle metadata changed event. The callback function provides the [AVMetadata](arkts-avsession-avsession-avmetadata-i.md#avmetadata) parameter. It only contains the properties set in the filter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offOutputDeviceChange

```TypeScript
offOutputDeviceChange(callback?: ConnectionEvent): void
```

Unregister session output device change callback

**Since:** 23

<!--Device-AVSessionController-offOutputDeviceChange(callback?: ConnectionEvent): void--><!--Device-AVSessionController-offOutputDeviceChange(callback?: ConnectionEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ConnectionEvent](arkts-avsession-avsession-connectionevent-t.md) | No | Used to handle output device changed. The callback provide the new device info [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md#outputdeviceinfo) and related connection state [ConnectionState](arkts-avsession-avsession-connectionstate-e.md#connectionstate). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist |

## offPlaybackStateChange

```TypeScript
offPlaybackStateChange(callback?: Callback<AVPlaybackState>): void
```

Unregister playback state changed callback

**Since:** 23

<!--Device-AVSessionController-offPlaybackStateChange(callback?: Callback<AVPlaybackState>): void--><!--Device-AVSessionController-offPlaybackStateChange(callback?: Callback<AVPlaybackState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md)&gt; | No | The callback used to handle playback state changed event. The callback function provides the [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md#avplaybackstate) parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offQueueItemsChange

```TypeScript
offQueueItemsChange(callback?: Callback<Array<AVQueueItem>>): void
```

Unregister session playlist change callback

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVSessionController-offQueueItemsChange(callback?: Callback<Array<AVQueueItem>>): void--><!--Device-AVSessionController-offQueueItemsChange(callback?: Callback<Array<AVQueueItem>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt;&gt; | No | Used to handle playlist changed. The callback provides the new array of AVQueueItem [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md#avqueueitem) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offQueueTitleChange

```TypeScript
offQueueTitleChange(callback?: Callback<string>): void
```

Unregister the name of session playlist change callback

**Since:** 23

<!--Device-AVSessionController-offQueueTitleChange(callback?: Callback<string>): void--><!--Device-AVSessionController-offQueueTitleChange(callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No | Used to handle name of playlist changed. The callback provides the new name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offSessionDestroy

```TypeScript
offSessionDestroy(callback?: NoParamCallback): void
```

Unregister current session destroyed callback

**Since:** 23

<!--Device-AVSessionController-offSessionDestroy(callback?: NoParamCallback): void--><!--Device-AVSessionController-offSessionDestroy(callback?: NoParamCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | No | The callback used to handle current session destroyed event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offSessionEvent

```TypeScript
offSessionEvent(callback?: EventProcess): void
```

Unregister session event callback

**Since:** 23

<!--Device-AVSessionController-offSessionEvent(callback?: EventProcess): void--><!--Device-AVSessionController-offSessionEvent(callback?: EventProcess): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [EventProcess](arkts-avsession-avsession-eventprocess-t.md) | No | Used to cancel a specific listener The callback function provides the event string and key-value pair parameters. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offSupportedLoopModesChange

```TypeScript
offSupportedLoopModesChange(callback?: Callback<Array<LoopMode>>): void
```

Unregister listener for supported loop modes.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVSessionController-offSupportedLoopModesChange(callback?: Callback<Array<LoopMode>>): void--><!--Device-AVSessionController-offSupportedLoopModesChange(callback?: Callback<Array<LoopMode>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[LoopMode](arkts-avsession-avsession-loopmode-e.md)&gt;&gt; | No | Callback used to retrieve supported loop modes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offSupportedPlaySpeedsChange

```TypeScript
offSupportedPlaySpeedsChange(callback?: Callback<Array<double>>): void
```

Unregister listener for supported play speeds.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVSessionController-offSupportedPlaySpeedsChange(callback?: Callback<Array<double>>): void--><!--Device-AVSessionController-offSupportedPlaySpeedsChange(callback?: Callback<Array<double>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;double&gt;&gt; | No | Callback used to retrieve supported play speeds. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## offValidCommandChange

```TypeScript
offValidCommandChange(callback?: Callback<Array<AVControlCommandType>>): void
```

Unregister the valid commands of the session changed callback

**Since:** 23

<!--Device-AVSessionController-offValidCommandChange(callback?: Callback<Array<AVControlCommandType>>): void--><!--Device-AVSessionController-offValidCommandChange(callback?: Callback<Array<AVControlCommandType>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVControlCommandType](arkts-avsession-avsession-avcontrolcommandtype-t.md)&gt;&gt; | No | The callback used to handle the changes. The callback function provides an array of AVControlCommandType. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## off_activeStateChange

```TypeScript
off(type: 'activeStateChange', callback?: (isActive: boolean) => void)
```

Unregister the active state of this session changed callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-off(type: 'activeStateChange', callback?: (isActive: boolean) => void)--><!--Device-AVSessionController-off(type: 'activeStateChange', callback?: (isActive: boolean) => void)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'activeStateChange' | Yes | 'activeStateChange' |
| callback | (isActive: boolean) =&gt; void | No | The callback used to handle the active state of this session changed event. The callback function provides the changed session state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## off_callMetadataChange

```TypeScript
off(type: 'callMetadataChange', callback?: Callback<CallMetadata>): void
```

Unregister call metadata changed callback

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-off(type: 'callMetadataChange', callback?: Callback<CallMetadata>): void--><!--Device-AVSessionController-off(type: 'callMetadataChange', callback?: Callback<CallMetadata>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'callMetadataChange' | Yes | 'callMetadataChange' |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallMetadata](arkts-avsession-avsession-callmetadata-i.md)&gt; | No | The callback used to handle call metadata changed event. The callback function provides the [CallMetadata](arkts-avsession-avsession-callmetadata-i.md#callmetadata) parameter. It only contains the properties set in the filter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## off_callStateChange

```TypeScript
off(type: 'callStateChange', callback?: Callback<AVCallState>): void
```

Unregister playback state changed callback

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-off(type: 'callStateChange', callback?: Callback<AVCallState>): void--><!--Device-AVSessionController-off(type: 'callStateChange', callback?: Callback<AVCallState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'callStateChange' | Yes | 'callStateChange' |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCallState](arkts-avsession-avsession-avcallstate-i.md)&gt; | No | The callback used to handle call state changed event. The callback function provides the [AVCallState](arkts-avsession-avsession-avcallstate-i.md#avcallstate) parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## off_customDataChange

```TypeScript
off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void
```

Unregister listener for custom data.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVSessionController-off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void--><!--Device-AVSessionController-off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'customDataChange' | Yes | Type of the 'customDataChange' to listen for. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | No | Callback used to retrieve custom data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## off_extrasChange

```TypeScript
off(type: 'extrasChange', callback?: (extras: {[key: string]: Object}) => void): void
```

Unregister the custom media packets change callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-off(type: 'extrasChange', callback?: (extras: {[key: string]: Object}) => void): void--><!--Device-AVSessionController-off(type: 'extrasChange', callback?: (extras: {[key: string]: Object}) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'extrasChange' | Yes | Registration Type 'extrasChange' |
| callback | (extras: {[key: string]: Object}) =&gt; void | No | Used to handle custom media packets changed. The callback provides the new media packets. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## off_metadataChange

```TypeScript
off(type: 'metadataChange', callback?: (data: AVMetadata) => void)
```

Unregister metadata changed callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-off(type: 'metadataChange', callback?: (data: AVMetadata) => void)--><!--Device-AVSessionController-off(type: 'metadataChange', callback?: (data: AVMetadata) => void)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'metadataChange' | Yes |  |
| callback | (data: AVMetadata) =&gt; void | No | The callback used to handle metadata changed event. The callback function provides the [AVMetadata](arkts-avsession-avsession-avmetadata-i.md#avmetadata) parameter. It only contains the properties set in the filter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## off_outputDeviceChange

```TypeScript
off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void
```

Unregister session output device change callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void--><!--Device-AVSessionController-off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'outputDeviceChange' | Yes | Registration Type 'outputDeviceChange' |
| callback | (state: ConnectionState, device: OutputDeviceInfo) =&gt; void | No | Used to handle output device changed. The callback provide the new device info [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md#outputdeviceinfo) and related connection state [ConnectionState](arkts-avsession-avsession-connectionstate-e.md#connectionstate). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist |

## off_playbackStateChange

```TypeScript
off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void)
```

Unregister playback state changed callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void)--><!--Device-AVSessionController-off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playbackStateChange' | Yes |  |
| callback | (state: AVPlaybackState) =&gt; void | No | The callback used to handle playback state changed event. The callback function provides the [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md#avplaybackstate) parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## off_queueItemsChange

```TypeScript
off(type: 'queueItemsChange', callback?: (items: Array<AVQueueItem>) => void): void
```

Unregister session playlist change callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-off(type: 'queueItemsChange', callback?: (items: Array<AVQueueItem>) => void): void--><!--Device-AVSessionController-off(type: 'queueItemsChange', callback?: (items: Array<AVQueueItem>) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'queueItemsChange' | Yes | Registration Type 'queueItemsChange' |
| callback | (items: Array&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt;) =&gt; void | No | Used to handle playlist changed. The callback provides the new array of AVQueueItem [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md#avqueueitem) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## off_queueTitleChange

```TypeScript
off(type: 'queueTitleChange', callback?: (title: string) => void): void
```

Unregister the name of session playlist change callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-off(type: 'queueTitleChange', callback?: (title: string) => void): void--><!--Device-AVSessionController-off(type: 'queueTitleChange', callback?: (title: string) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'queueTitleChange' | Yes | Registration Type 'queueTitleChange' |
| callback | (title: string) =&gt; void | No | Used to handle name of playlist changed. The callback provides the new name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## off_sessionDestroy

```TypeScript
off(type: 'sessionDestroy', callback?: () => void)
```

Unregister current session destroyed callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-off(type: 'sessionDestroy', callback?: () => void)--><!--Device-AVSessionController-off(type: 'sessionDestroy', callback?: () => void)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sessionDestroy' | Yes | 'sessionDestroy' |
| callback | () =&gt; void | No | The callback used to handle current session destroyed event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## off_sessionEvent

```TypeScript
off(type: 'sessionEvent', callback?: (sessionEvent: string, args: {[key: string]: Object}) => void): void
```

Unregister session event callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-off(type: 'sessionEvent', callback?: (sessionEvent: string, args: {[key: string]: Object}) => void): void--><!--Device-AVSessionController-off(type: 'sessionEvent', callback?: (sessionEvent: string, args: {[key: string]: Object}) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sessionEvent' | Yes | 'sessionEvent' |
| callback | (sessionEvent: string, args: {[key: string]: Object}) =&gt; void | No | Used to cancel a specific listener The callback function provides the event string and key-value pair parameters. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## off_validCommandChange

```TypeScript
off(type: 'validCommandChange', callback?: (commands: Array<AVControlCommandType>) => void)
```

Unregister the valid commands of the session changed callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-off(type: 'validCommandChange', callback?: (commands: Array<AVControlCommandType>) => void)--><!--Device-AVSessionController-off(type: 'validCommandChange', callback?: (commands: Array<AVControlCommandType>) => void)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'validCommandChange' | Yes | 'validCommandChange' |
| callback | (commands: Array&lt;[AVControlCommandType](arkts-avsession-avsession-avcontrolcommandtype-t.md)&gt;) =&gt; void | No | The callback used to handle the changes. The callback function provides an array of AVControlCommandType. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onActiveStateChange

```TypeScript
onActiveStateChange(callback: Callback<boolean>): void
```

Register the active state of this session changed callback

**Since:** 23

<!--Device-AVSessionController-onActiveStateChange(callback: Callback<boolean>): void--><!--Device-AVSessionController-onActiveStateChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes | The callback used to handle the active state of this session changed event. The callback function provides the changed session state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onCallMetadataChange

```TypeScript
onCallMetadataChange(filter: Array<string>, callback: Callback<CallMetadata>): void
```

Register call metadata changed callback

**Since:** 23

<!--Device-AVSessionController-onCallMetadataChange(filter: Array<string>, callback: Callback<CallMetadata>): void--><!--Device-AVSessionController-onCallMetadataChange(filter: Array<string>, callback: Callback<CallMetadata>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | Array&lt;string&gt; | Yes | The properties of [CallMetadata](arkts-avsession-avsession-callmetadata-i.md#callmetadata) that you cared about |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallMetadata](arkts-avsession-avsession-callmetadata-i.md)&gt; | Yes | The callback used to handle call metadata changed event. The callback function provides the [CallMetadata](arkts-avsession-avsession-callmetadata-i.md#callmetadata) parameter. It only contains the properties set in the filter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onCallMetadataChangeAll

```TypeScript
onCallMetadataChangeAll(callback: Callback<CallMetadata>): void
```

Registers a callback for all call metadata changes

**Since:** 23

<!--Device-AVSessionController-onCallMetadataChangeAll(callback: Callback<CallMetadata>): void--><!--Device-AVSessionController-onCallMetadataChangeAll(callback: Callback<CallMetadata>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallMetadata](arkts-avsession-avsession-callmetadata-i.md)&gt; | Yes | The callback used to handle call metadata changed event. The callback function provides the [CallMetadata](arkts-avsession-avsession-callmetadata-i.md#callmetadata) parameter. It only contains the properties set in the filter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onCallStateChange

```TypeScript
onCallStateChange(filter: Array<string>, callback: Callback<AVCallState>): void
```

Register call state changed callback

**Since:** 23

<!--Device-AVSessionController-onCallStateChange(filter: Array<string>, callback: Callback<AVCallState>): void--><!--Device-AVSessionController-onCallStateChange(filter: Array<string>, callback: Callback<AVCallState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | Array&lt;string&gt; | Yes | The properties of [AVCallState](arkts-avsession-avsession-avcallstate-i.md#avcallstate) that you cared about |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCallState](arkts-avsession-avsession-avcallstate-i.md)&gt; | Yes | The callback used to handle call state changed event. The callback function provides the [AVCallState](arkts-avsession-avsession-avcallstate-i.md#avcallstate) parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onCallStateChangeAll

```TypeScript
onCallStateChangeAll(callback: Callback<AVCallState>): void
```

Register a callback for all call attribute changes

**Since:** 23

<!--Device-AVSessionController-onCallStateChangeAll(callback: Callback<AVCallState>): void--><!--Device-AVSessionController-onCallStateChangeAll(callback: Callback<AVCallState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCallState](arkts-avsession-avsession-avcallstate-i.md)&gt; | Yes | The callback used to handle call state changed event. The callback function provides the [AVCallState](arkts-avsession-avsession-avcallstate-i.md#avcallstate) parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onCustomDataChange

```TypeScript
onCustomDataChange(callback: Callback<Record<string, Object>>): void
```

Register listener for custom data.

**Since:** 23

<!--Device-AVSessionController-onCustomDataChange(callback: Callback<Record<string, Object>>): void--><!--Device-AVSessionController-onCustomDataChange(callback: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | Yes | Callback used to retrieve custom data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onDesktopLyricEnabled

```TypeScript
onDesktopLyricEnabled(callback: Callback<boolean>): void
```

Register desktop lyric enable state change callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-onDesktopLyricEnabled(callback: Callback<boolean>): void--><!--Device-AVSessionController-onDesktopLyricEnabled(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes | a callback to receive desktop lyric enable state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onDesktopLyricStateChanged

```TypeScript
onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void
```

Register desktop lyric state changed callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void--><!--Device-AVSessionController-onDesktopLyricStateChanged(callback: Callback<DesktopLyricState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DesktopLyricState](arkts-avsession-avsession-desktoplyricstate-i.md)&gt; | Yes | a callback to receive desktop lyric state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onDesktopLyricVisibilityChanged

```TypeScript
onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void
```

Register desktop lyric visible state change callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void--><!--Device-AVSessionController-onDesktopLyricVisibilityChanged(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes | a callback to receive desktop lyric window visible state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onExtrasChange

```TypeScript
onExtrasChange(callback: Callback<Record<string, Object>>): void
```

Register the custom media packets change callback

**Since:** 23

<!--Device-AVSessionController-onExtrasChange(callback: Callback<Record<string, Object>>): void--><!--Device-AVSessionController-onExtrasChange(callback: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | Yes | Used to handle custom media packets changed. The callback provides the new media packets. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onMediaCenterControlTypeChanged

```TypeScript
onMediaCenterControlTypeChanged(callback: Callback<Array<AVMediaCenterControlType>>): void
```

Register media center control type changed callback.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-onMediaCenterControlTypeChanged(callback: Callback<Array<AVMediaCenterControlType>>): void--><!--Device-AVSessionController-onMediaCenterControlTypeChanged(callback: Callback<Array<AVMediaCenterControlType>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVMediaCenterControlType](arkts-avsession-avsession-avmediacentercontroltype-t.md)&gt;&gt; | Yes | Callback to receive the changed control types. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onMetadataChange

```TypeScript
onMetadataChange(filter: Array<string>, callback: Callback<AVMetadata>): void
```

Register metadata changed callback

**Since:** 23

<!--Device-AVSessionController-onMetadataChange(filter: Array<string>, callback: Callback<AVMetadata>): void--><!--Device-AVSessionController-onMetadataChange(filter: Array<string>, callback: Callback<AVMetadata>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | Array&lt;string&gt; | Yes | The properties of [AVMetadata](arkts-avsession-avsession-avmetadata-i.md#avmetadata) that you cared about |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVMetadata&gt; | Yes | The callback used to handle metadata changed event. The callback function provides the [AVMetadata](arkts-avsession-avsession-avmetadata-i.md#avmetadata) parameter. It only contains the properties set in the filter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onMetadataChangeAll

```TypeScript
onMetadataChangeAll(callback: Callback<AVMetadata>): void
```

Registers a callback to be invoked whenever any metadata changes

**Since:** 23

<!--Device-AVSessionController-onMetadataChangeAll(callback: Callback<AVMetadata>): void--><!--Device-AVSessionController-onMetadataChangeAll(callback: Callback<AVMetadata>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVMetadata&gt; | Yes | The callback used to handle metadata changed event. The callback function provides the [AVMetadata](arkts-avsession-avsession-avmetadata-i.md#avmetadata) parameter. It only contains the properties set in the filter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onOutputDeviceChange

```TypeScript
onOutputDeviceChange(callback: ConnectionEvent): void
```

Register session output device change callback

**Since:** 23

<!--Device-AVSessionController-onOutputDeviceChange(callback: ConnectionEvent): void--><!--Device-AVSessionController-onOutputDeviceChange(callback: ConnectionEvent): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ConnectionEvent](arkts-avsession-avsession-connectionevent-t.md) | Yes | Used to handle output device changed. The callback provide the new device info [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md#outputdeviceinfo) and related connection state [ConnectionState](arkts-avsession-avsession-connectionstate-e.md#connectionstate). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist |

## onPlaybackStateChange

```TypeScript
onPlaybackStateChange(filter: Array<string>, callback: Callback<AVPlaybackState>): void
```

Register playback state changed callback

**Since:** 23

<!--Device-AVSessionController-onPlaybackStateChange(filter: Array<string>, callback: Callback<AVPlaybackState>): void--><!--Device-AVSessionController-onPlaybackStateChange(filter: Array<string>, callback: Callback<AVPlaybackState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | Array&lt;string&gt; | Yes | The properties of [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md#avplaybackstate) that you cared about |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md)&gt; | Yes | The callback used to handle playback state changed event. The callback function provides the [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md#avplaybackstate) parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onPlaybackStateChangeAll

```TypeScript
onPlaybackStateChangeAll(callback: Callback<AVPlaybackState>): void
```

Registers a callback to be invoked whenever the playback state changes

**Since:** 23

<!--Device-AVSessionController-onPlaybackStateChangeAll(callback: Callback<AVPlaybackState>): void--><!--Device-AVSessionController-onPlaybackStateChangeAll(callback: Callback<AVPlaybackState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md)&gt; | Yes | The callback used to handle playback state changed event. The callback function provides the [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md#avplaybackstate) parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onQueueItemsChange

```TypeScript
onQueueItemsChange(callback: Callback<Array<AVQueueItem>>): void
```

Register session playlist change callback

**Since:** 23

<!--Device-AVSessionController-onQueueItemsChange(callback: Callback<Array<AVQueueItem>>): void--><!--Device-AVSessionController-onQueueItemsChange(callback: Callback<Array<AVQueueItem>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt;&gt; | Yes | Used to handle playlist changed. The callback provides the new array of AVQueueItem [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md#avqueueitem) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onQueueTitleChange

```TypeScript
onQueueTitleChange(callback: Callback<string>): void
```

Register the name of session playlist change callback

**Since:** 23

<!--Device-AVSessionController-onQueueTitleChange(callback: Callback<string>): void--><!--Device-AVSessionController-onQueueTitleChange(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | Used to handle name of playlist changed. The callback provides the new name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onSessionDestroy

```TypeScript
onSessionDestroy(callback: NoParamCallback): void
```

Register current session destroyed callback

**Since:** 23

<!--Device-AVSessionController-onSessionDestroy(callback: NoParamCallback): void--><!--Device-AVSessionController-onSessionDestroy(callback: NoParamCallback): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | Yes | The callback used to handle current session destroyed event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onSessionEvent

```TypeScript
onSessionEvent(callback: EventProcess): void
```

Register session event callback

**Since:** 23

<!--Device-AVSessionController-onSessionEvent(callback: EventProcess): void--><!--Device-AVSessionController-onSessionEvent(callback: EventProcess): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [EventProcess](arkts-avsession-avsession-eventprocess-t.md) | Yes | The callback used to handle session event changed event. The callback function provides the event string and key-value pair parameters. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onSupportedLoopModesChange

```TypeScript
onSupportedLoopModesChange(callback: Callback<Array<LoopMode>>): void
```

Register listener for supported loop modes.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVSessionController-onSupportedLoopModesChange(callback: Callback<Array<LoopMode>>): void--><!--Device-AVSessionController-onSupportedLoopModesChange(callback: Callback<Array<LoopMode>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[LoopMode](arkts-avsession-avsession-loopmode-e.md)&gt;&gt; | Yes | Callback used to retrieve supported loop modes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onSupportedPlaySpeedsChange

```TypeScript
onSupportedPlaySpeedsChange(callback: Callback<Array<double>>): void
```

Register listener for supported play speeds.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AVSessionController-onSupportedPlaySpeedsChange(callback: Callback<Array<double>>): void--><!--Device-AVSessionController-onSupportedPlaySpeedsChange(callback: Callback<Array<double>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;double&gt;&gt; | Yes | Callback used to retrieve supported play speeds. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## onValidCommandChange

```TypeScript
onValidCommandChange(callback: Callback<Array<AVControlCommandType>>): void
```

Register the valid commands of the session changed callback

**Since:** 23

<!--Device-AVSessionController-onValidCommandChange(callback: Callback<Array<AVControlCommandType>>): void--><!--Device-AVSessionController-onValidCommandChange(callback: Callback<Array<AVControlCommandType>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVControlCommandType](arkts-avsession-avsession-avcontrolcommandtype-t.md)&gt;&gt; | Yes | The callback used to handle the changes. The callback function provides an array of AVControlCommandType. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## on_activeStateChange

```TypeScript
on(type: 'activeStateChange', callback: (isActive: boolean) => void)
```

Register the active state of this session changed callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-on(type: 'activeStateChange', callback: (isActive: boolean) => void)--><!--Device-AVSessionController-on(type: 'activeStateChange', callback: (isActive: boolean) => void)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'activeStateChange' | Yes | 'activeStateChange' |
| callback | (isActive: boolean) =&gt; void | Yes | The callback used to handle the active state of this session changed event. The callback function provides the changed session state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## on_callMetadataChange

```TypeScript
on(type: 'callMetadataChange', filter: Array<keyof CallMetadata> | 'all', callback: Callback<CallMetadata>): void
```

Register call metadata changed callback

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-on(type: 'callMetadataChange', filter: Array<keyof CallMetadata> | 'all', callback: Callback<CallMetadata>): void--><!--Device-AVSessionController-on(type: 'callMetadataChange', filter: Array<keyof CallMetadata> | 'all', callback: Callback<CallMetadata>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'callMetadataChange' | Yes | 'callMetadataChange' |
| filter | Array&lt;keyof CallMetadata&gt; \| 'all' | Yes | The properties of [CallMetadata](arkts-avsession-avsession-callmetadata-i.md#callmetadata) that you cared about |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallMetadata](arkts-avsession-avsession-callmetadata-i.md)&gt; | Yes | The callback used to handle call metadata changed event. The callback function provides the [CallMetadata](arkts-avsession-avsession-callmetadata-i.md#callmetadata) parameter. It only contains the properties set in the filter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## on_callStateChange

```TypeScript
on(type: 'callStateChange', filter: Array<keyof AVCallState> | 'all', callback: Callback<AVCallState>): void
```

Register call state changed callback

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-on(type: 'callStateChange', filter: Array<keyof AVCallState> | 'all', callback: Callback<AVCallState>): void--><!--Device-AVSessionController-on(type: 'callStateChange', filter: Array<keyof AVCallState> | 'all', callback: Callback<AVCallState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'callStateChange' | Yes | 'callStateChange' |
| filter | Array&lt;keyof AVCallState&gt; \| 'all' | Yes | The properties of [AVCallState](arkts-avsession-avsession-avcallstate-i.md#avcallstate) that you cared about |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCallState](arkts-avsession-avsession-avcallstate-i.md)&gt; | Yes | The callback used to handle call state changed event. The callback function provides the [AVCallState](arkts-avsession-avsession-avcallstate-i.md#avcallstate) parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## on_customDataChange

```TypeScript
on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void
```

Register listener for custom data.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AVSessionController-on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void--><!--Device-AVSessionController-on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'customDataChange' | Yes | Type of the 'customDataChange' to listen for. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Object&gt;&gt; | Yes | Callback used to retrieve custom data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## on_extrasChange

```TypeScript
on(type: 'extrasChange', callback: (extras: {[key: string]: Object}) => void): void
```

Register the custom media packets change callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-on(type: 'extrasChange', callback: (extras: {[key: string]: Object}) => void): void--><!--Device-AVSessionController-on(type: 'extrasChange', callback: (extras: {[key: string]: Object}) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'extrasChange' | Yes | Registration Type 'extrasChange' |
| callback | (extras: {[key: string]: Object}) =&gt; void | Yes | Used to handle custom media packets changed. The callback provides the new media packets. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## on_metadataChange

```TypeScript
on(type: 'metadataChange', filter: Array<keyof AVMetadata> | 'all', callback: (data: AVMetadata) => void)
```

Register metadata changed callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-on(type: 'metadataChange', filter: Array<keyof AVMetadata> | 'all', callback: (data: AVMetadata) => void)--><!--Device-AVSessionController-on(type: 'metadataChange', filter: Array<keyof AVMetadata> | 'all', callback: (data: AVMetadata) => void)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'metadataChange' | Yes |  |
| filter | Array&lt;keyof AVMetadata&gt; \| 'all' | Yes | The properties of [AVMetadata](arkts-avsession-avsession-avmetadata-i.md#avmetadata) that you cared about |
| callback | (data: AVMetadata) =&gt; void | Yes | The callback used to handle metadata changed event. The callback function provides the [AVMetadata](arkts-avsession-avsession-avmetadata-i.md#avmetadata) parameter. It only contains the properties set in the filter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## on_outputDeviceChange

```TypeScript
on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void
```

Register session output device change callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void--><!--Device-AVSessionController-on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'outputDeviceChange' | Yes | Registration Type 'outputDeviceChange' |
| callback | (state: ConnectionState, device: OutputDeviceInfo) =&gt; void | Yes | Used to handle output device changed. The callback provide the new device info [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md#outputdeviceinfo) and related connection state [ConnectionState](arkts-avsession-avsession-connectionstate-e.md#connectionstate). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist |

## on_playbackStateChange

```TypeScript
on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void)
```

Register playback state changed callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void)--><!--Device-AVSessionController-on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playbackStateChange' | Yes |  |
| filter | Array&lt;keyof AVPlaybackState&gt; \| 'all' | Yes | The properties of [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md#avplaybackstate) that you cared about |
| callback | (state: AVPlaybackState) =&gt; void | Yes | The callback used to handle playback state changed event. The callback function provides the [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md#avplaybackstate) parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## on_queueItemsChange

```TypeScript
on(type: 'queueItemsChange', callback: (items: Array<AVQueueItem>) => void): void
```

Register session playlist change callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-on(type: 'queueItemsChange', callback: (items: Array<AVQueueItem>) => void): void--><!--Device-AVSessionController-on(type: 'queueItemsChange', callback: (items: Array<AVQueueItem>) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'queueItemsChange' | Yes | Registration Type 'queueItemsChange' |
| callback | (items: Array&lt;[AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md)&gt;) =&gt; void | Yes | Used to handle playlist changed. The callback provides the new array of AVQueueItem [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md#avqueueitem) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## on_queueTitleChange

```TypeScript
on(type: 'queueTitleChange', callback: (title: string) => void): void
```

Register the name of session playlist change callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-on(type: 'queueTitleChange', callback: (title: string) => void): void--><!--Device-AVSessionController-on(type: 'queueTitleChange', callback: (title: string) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'queueTitleChange' | Yes | Registration Type 'queueTitleChange' |
| callback | (title: string) =&gt; void | Yes | Used to handle name of playlist changed. The callback provides the new name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## on_sessionDestroy

```TypeScript
on(type: 'sessionDestroy', callback: () => void)
```

Register current session destroyed callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-on(type: 'sessionDestroy', callback: () => void)--><!--Device-AVSessionController-on(type: 'sessionDestroy', callback: () => void)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sessionDestroy' | Yes |  |
| callback | () =&gt; void | Yes | The callback used to handle current session destroyed event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## on_sessionEvent

```TypeScript
on(type: 'sessionEvent', callback: (sessionEvent: string, args: {[key: string]: Object}) => void): void
```

Register session event callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-on(type: 'sessionEvent', callback: (sessionEvent: string, args: {[key: string]: Object}) => void): void--><!--Device-AVSessionController-on(type: 'sessionEvent', callback: (sessionEvent: string, args: {[key: string]: Object}) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sessionEvent' | Yes | 'sessionEvent' |
| callback | (sessionEvent: string, args: {[key: string]: Object}) =&gt; void | Yes | The callback used to handle session event changed event. The callback function provides the event string and key-value pair parameters. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## on_validCommandChange

```TypeScript
on(type: 'validCommandChange', callback: (commands: Array<AVControlCommandType>) => void)
```

Register the valid commands of the session changed callback

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-on(type: 'validCommandChange', callback: (commands: Array<AVControlCommandType>) => void)--><!--Device-AVSessionController-on(type: 'validCommandChange', callback: (commands: Array<AVControlCommandType>) => void)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'validCommandChange' | Yes | 'validCommandChange' |
| callback | (commands: Array&lt;[AVControlCommandType](arkts-avsession-avsession-avcontrolcommandtype-t.md)&gt;) =&gt; void | Yes | The callback used to handle the changes. The callback function provides an array of AVControlCommandType. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## sendAVKeyEvent

```TypeScript
sendAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void
```

Send media key event to this session

**Since:** 23

<!--Device-AVSessionController-sendAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void--><!--Device-AVSessionController-sendAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md) | Yes | The KeyEvent |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The asyncCallback triggered when the command is executed successfully. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 600105 | Invalid session command. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 600106 | The session is not activated. |
| 600101 | Session service exception. |
| 600103 | The session controller does not exist. |
| 600102 | The session does not exist. |

## sendAVKeyEvent

```TypeScript
sendAVKeyEvent(event: KeyEvent): Promise<void>
```

Send media key event to this session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-sendAVKeyEvent(event: KeyEvent): Promise<void>--><!--Device-AVSessionController-sendAVKeyEvent(event: KeyEvent): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md) | Yes | The KeyEvent |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 600105 | Invalid session command. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 600106 | The session is not activated. |
| 600101 | Session service exception. |
| 600103 | The session controller does not exist. |
| 600102 | The session does not exist. |

## sendCommonCommand

```TypeScript
sendCommonCommand(command: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void
```

Send common commands to this session

**Since:** 10

<!--Device-AVSessionController-sendCommonCommand(command: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void--><!--Device-AVSessionController-sendCommonCommand(command: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | string | Yes | The command name to be sent. |
| args | {[key: string]: Object} | Yes | The parameters of session event |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The asyncCallback triggered when the command is executed successfully. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |
| [6600106](../errorcode-avsession.md#6600106-session-not-activated) | The session is not activated. |
| [6600107](../errorcode-avsession.md#6600107-too-many-commands-or-events) | Too many commands or events. |

## sendCommonCommand

```TypeScript
sendCommonCommand(command: string, args: Record<string, Object>, callback: AsyncCallback<void>): void
```

Send common commands to this session

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-sendCommonCommand(command: string, args: Record<string, Object>, callback: AsyncCallback<void>): void--><!--Device-AVSessionController-sendCommonCommand(command: string, args: Record<string, Object>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | string | Yes | The command name to be sent. |
| args | Record&lt;string, Object&gt; | Yes | The parameters of session event |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The asyncCallback triggered when the command is executed successfully. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |
| [6600106](../errorcode-avsession.md#6600106-session-not-activated) | The session is not activated. |
| [6600107](../errorcode-avsession.md#6600107-too-many-commands-or-events) | Too many commands or events. |

## sendCommonCommand

```TypeScript
sendCommonCommand(command: string, args: {[key: string]: Object}): Promise<void>
```

Send common commands to this session

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-sendCommonCommand(command: string, args: {[key: string]: Object}): Promise<void>--><!--Device-AVSessionController-sendCommonCommand(command: string, args: {[key: string]: Object}): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | string | Yes | The command name to be sent. |
| args | {[key: string]: Object} | Yes | The parameters of session event |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |
| [6600106](../errorcode-avsession.md#6600106-session-not-activated) | The session is not activated. |
| [6600107](../errorcode-avsession.md#6600107-too-many-commands-or-events) | Too many commands or events. |

## sendCommonCommand

```TypeScript
sendCommonCommand(command: string, args: Record<string, Object>): Promise<void>
```

Send common commands to this session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVSessionController-sendCommonCommand(command: string, args: Record<string, Object>): Promise<void>--><!--Device-AVSessionController-sendCommonCommand(command: string, args: Record<string, Object>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | string | Yes | The command name to be sent. |
| args | Record&lt;string, Object&gt; | Yes | The parameters of session event |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |
| [6600106](../errorcode-avsession.md#6600106-session-not-activated) | The session is not activated. |
| [6600107](../errorcode-avsession.md#6600107-too-many-commands-or-events) | Too many commands or events. |

## sendControlCommand

```TypeScript
sendControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void
```

Send control commands to this session

**Since:** 23

<!--Device-AVSessionController-sendControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void--><!--Device-AVSessionController-sendControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | [AVControlCommand](arkts-avsession-avsession-avcontrolcommand-i.md) | Yes | The command to be sent. See [AVControlCommand](arkts-avsession-avsession-avcontrolcommand-i.md#avcontrolcommand) |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The asyncCallback triggered when the command is executed successfully. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |
| [6600106](../errorcode-avsession.md#6600106-session-not-activated) | The session is not activated. |
| [6600107](../errorcode-avsession.md#6600107-too-many-commands-or-events) | Too many commands or events. |

## sendControlCommand

```TypeScript
sendControlCommand(command: AVControlCommand): Promise<void>
```

Send control commands to this session

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-sendControlCommand(command: AVControlCommand): Promise<void>--><!--Device-AVSessionController-sendControlCommand(command: AVControlCommand): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| command | [AVControlCommand](arkts-avsession-avsession-avcontrolcommand-i.md) | Yes | The command to be sent. See [AVControlCommand](arkts-avsession-avsession-avcontrolcommand-i.md#avcontrolcommand) |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600105](../errorcode-avsession.md#6600105-invalid-session-command) | Invalid session command. |
| [6600106](../errorcode-avsession.md#6600106-session-not-activated) | The session is not activated. |
| [6600107](../errorcode-avsession.md#6600107-too-many-commands-or-events) | Too many commands or events. |

## sendCustomData

```TypeScript
sendCustomData(data: Record<string, Object>): Promise<void>
```

Send custom data to this avsession.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVSessionController-sendCustomData(data: Record<string, Object>): Promise<void>--><!--Device-AVSessionController-sendCustomData(data: Record<string, Object>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Record&lt;string, Object&gt; | Yes | The custom data populated by application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void result promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## setDesktopLyricState

```TypeScript
setDesktopLyricState(state: DesktopLyricState): Promise<void>
```

Set desktop lyric state such as lock state for this session.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-setDesktopLyricState(state: DesktopLyricState): Promise<void>--><!--Device-AVSessionController-setDesktopLyricState(state: DesktopLyricState): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [DesktopLyricState](arkts-avsession-avsession-desktoplyricstate-i.md) | Yes | The desktop lyric state |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600110](../errorcode-avsession.md#6600110-desktop-lyrics-not-enabled-for-the-application) | The desktop lyrics feature of this application is not enabled. |
| [6600111](../errorcode-avsession.md#6600111-desktop-lyrics-not-supported-for-the-current-device) | The desktop lyrics feature is not supported. |

## setDesktopLyricVisible

```TypeScript
setDesktopLyricVisible(visible: boolean): Promise<void>
```

Set desktop lyric visible state for this session.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVSessionController-setDesktopLyricVisible(visible: boolean): Promise<void>--><!--Device-AVSessionController-setDesktopLyricVisible(visible: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| visible | boolean | Yes | make desktop lyric window visible or not |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |
| [6600110](../errorcode-avsession.md#6600110-desktop-lyrics-not-enabled-for-the-application) | The desktop lyrics feature of this application is not enabled. |
| [6600111](../errorcode-avsession.md#6600111-desktop-lyrics-not-supported-for-the-current-device) | The desktop lyrics feature is not supported. |

## skipToQueueItem

```TypeScript
skipToQueueItem(itemId: int, callback: AsyncCallback<void>): void
```

Set the item in the playlist to be played

**Since:** 23

<!--Device-AVSessionController-skipToQueueItem(itemId: int, callback: AsyncCallback<void>): void--><!--Device-AVSessionController-skipToQueueItem(itemId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemId | int | Yes | The serial number of the item to be played |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The asyncCallback triggered when the command is executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## skipToQueueItem

```TypeScript
skipToQueueItem(itemId: int): Promise<void>
```

Set the item in the playlist to be played

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-skipToQueueItem(itemId: int): Promise<void>--><!--Device-AVSessionController-skipToQueueItem(itemId: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemId | int | Yes | The serial number of the item to be played |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |
| [6600102](../errorcode-avsession.md#6600102-session-does-not-exist) | The session does not exist. |
| [6600103](../errorcode-avsession.md#6600103-session-controller-does-not-exist) | The session controller does not exist. |

## sessionId

```TypeScript
readonly sessionId: string
```

Unique session Id

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVSessionController-readonly sessionId: string--><!--Device-AVSessionController-readonly sessionId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

