# SoundPool

Implements a sound pool that provides APIs for loading, unloading, playing, and stopping playing system sounds, setting the volume, and setting the number of loops. Before using these APIs, you must call [media.createSoundPool](../../../reference/apis-media-kit/arkts-apis-media-f.md) to create a SoundPool instance.

> **NOTE：**
> 
> - When using the SoundPool instance, you are advised to register the following callbacks to proactively obtain
> status changes:
> 
> - [on('loadComplete')](#onloadcomplete): listens for the
> event indicating that the resource loading is finished. You are advised to listen for this callback to ensure that
> the audio is played after being loaded.
> 
> -
> [on('playFinishedWithStreamId')](#onloadcomplete):
> listens for the event indicating that the playback is finished and returns the stream ID of the audio that finishes
> playing.
> 
> - [on('playFinished')](#onloadcomplete): listens
> for the event indicating that the playback is finished.
> 
> - [on('error')](#onloadcomplete): listens for error events.
> 
> - [on('errorOccurred')](#onloadcomplete): listens for
> error events and returns [errorInfo](arkts-media-soundpool-errorinfo-i.md).
> 
> - Currently, SoundPool does not support audio focus policies such as background playback and audio interruption, or
> skipping the silent frames at the beginning and end of an audio file. For details about low-latency playback using
> SoundPool, see
> [Using SoundPool to Play Short Sounds (ArkTS)](../../../media/media/using-soundpool-for-playback.md).

**Since:** 23

<!--Device-unnamed-export declare interface SoundPool--><!--Device-unnamed-export declare interface SoundPool-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## load

```TypeScript
load(uri: string, callback: AsyncCallback<int>): void
```

Loads a sound. This API uses an asynchronous callback to return the result.

This API uses an asynchronous callback to obtain the resource ID. The input parameter URL is a string starting with **fd://**, which is generated based on the file descriptor (FD) obtained.

This API cannot be used to load resources in the **rawfile** directory. Instead, use [load(fd: number, offset: number, length: number, callback: AsyncCallback\&lt;number&gt;): void](#load) or [load(fd: number, offset: number, length: number): Promise\&lt;number&gt;](#load) .

> **NOTE：**
> 
> - After the resource handle (in the form of an FD) or path description (in the form of a URI) is transferred to
> the player, do not use the resource handle or path description in read or write operations, including but not
> limited to transferring it to multiple players.
> 
> - Competition occurs when multiple players use the same resource handle or path description to read and write
> files at the same time, resulting in playback errors.

**Since:** 23

<!--Device-SoundPool-load(uri: string, callback: AsyncCallback<int>): void--><!--Device-SoundPool-load(uri: string, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the audio file to load. Generally, the URI starts with **fd://**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;int&gt; | Yes | Callback used to return the sound ID. A valid value must be greater than 0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400103](../errorcode-media.md#5400103-io-error) | I/O error. Return by callback. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## load

```TypeScript
load(uri: string): Promise<int>
```

Loads a sound. This API uses a promise to return the result.

This API uses a promise to obtain the resource ID. The input parameter URL is a string starting with **fd://**, which is generated based on the file descriptor (FD) obtained.

This API cannot be used to load resources in the **rawfile** directory. Instead, use [load(fd: number, offset: number, length: number, callback: AsyncCallback\&lt;number&gt;): void](#load) or [load(fd: number, offset: number, length: number): Promise\&lt;number&gt;](#load) .

> **NOTE：**
> 
> - After the resource handle (in the form of an FD) or path description (in the form of a URI) is transferred to
> the player, do not use the resource handle or path description in read or write operations, including but not
> limited to transferring it to multiple players.
> 
> - Competition occurs when multiple players use the same resource handle or path description to read and write
> files at the same time, resulting in playback errors.

**Since:** 23

<!--Device-SoundPool-load(uri: string): Promise<int>--><!--Device-SoundPool-load(uri: string): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the audio file to load. Generally, the URI starts with **fd://**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the sound ID. A valid value must be greater than 0 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-io-error) | I/O error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## load

```TypeScript
load(fd: int, offset: long, length: long, callback: AsyncCallback<int>): void
```

Loads a sound. This API uses an asynchronous callback to return the result.

This API uses an asynchronous callback to obtain the resource ID. For the input parameter, resource information can be passed in manually or acquired automatically by reading the application's built-in resources.

> **NOTE：**
> 
> - After the resource handle (in the form of an FD) or path description (in the form of a URI) is transferred to
> the player, do not use the resource handle or path description in read or write operations, including but not
> limited to transferring it to multiple players.
> 
> - Competition occurs when multiple players use the same resource handle or path description to read and write
> files at the same time, resulting in playback errors.

**Since:** 23

<!--Device-SoundPool-load(fd: int, offset: long, length: long, callback: AsyncCallback<int>): void--><!--Device-SoundPool-load(fd: int, offset: long, length: long, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | Resource handle, which is obtained by calling resourceManager.getRawFd. |
| offset | long | Yes | Resource offset, which needs to be entered based on the preset resource information. An invalid value causes a failure to parse audio and video resources. |
| length | long | Yes | Resource length, which needs to be entered based on the preset resource information. An invalid value causes a failure to parse audio and video resources. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;int&gt; | Yes | Callback used to return the sound ID. A valid value must be greater than 0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400103](../errorcode-media.md#5400103-io-error) | I/O error. Return by callback. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## load

```TypeScript
load(fd: int, offset: long, length: long): Promise<int>
```

Loads a sound. This API uses a promise to return the result.

This API uses a promise to obtain the resource ID. For the input parameter, resource information can be passed in manually or acquired automatically by reading the application's built-in resources.

> **NOTE：**
> 
> - After the resource handle (in the form of an FD) or path description (in the form of a URI) is transferred to
> the player, do not use the resource handle or path description in read or write operations, including but not
> limited to transferring it to multiple players.
> 
> - Competition occurs when multiple players use the same resource handle or path description to read and write
> files at the same time, resulting in playback errors.

**Since:** 23

<!--Device-SoundPool-load(fd: int, offset: long, length: long): Promise<int>--><!--Device-SoundPool-load(fd: int, offset: long, length: long): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | int | Yes | Resource handle, which is obtained by calling resourceManager.getRawFd |
| offset | long | Yes | Resource offset, which needs to be entered based on the preset resource information. An invalid value causes a failure to parse audio and video resources. |
| length | long | Yes | Resource length, which needs to be entered based on the preset resource information. An invalid value causes a failure to parse audio and video resources. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the sound ID. A valid value must be greater than 0 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-io-error) | I/O error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## offError

```TypeScript
offError(): void
```

Unsubscribes from error events of this **SoundPool** instance.

**Since:** 23

<!--Device-SoundPool-offError(): void--><!--Device-SoundPool-offError(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## offErrorOccurred

```TypeScript
offErrorOccurred(callback?: Callback<ErrorInfo>): void
```

Unsubscribes from errorOccurred events of this **SoundPool** instance.

**Since:** 23

<!--Device-SoundPool-offErrorOccurred(callback?: Callback<ErrorInfo>): void--><!--Device-SoundPool-offErrorOccurred(callback?: Callback<ErrorInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ErrorInfo](arkts-media-soundpool-errorinfo-i.md)&gt; | No | Callback used to listen for soundpool errorOccurred events. |

## offLoadComplete

```TypeScript
offLoadComplete(): void
```

Unsubscribes from events indicating that a sound finishes loading.

**Since:** 23

<!--Device-SoundPool-offLoadComplete(): void--><!--Device-SoundPool-offLoadComplete(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## offPlayFinished

```TypeScript
offPlayFinished(): void
```

Unsubscribes from events indicating that a sound finishes playing.

**Since:** 23

<!--Device-SoundPool-offPlayFinished(): void--><!--Device-SoundPool-offPlayFinished(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## offPlayFinishedWithStreamId

```TypeScript
offPlayFinishedWithStreamId(): void
```

Unsubscribes from events indicating that a sound finishes playing.

**Since:** 23

<!--Device-SoundPool-offPlayFinishedWithStreamId(): void--><!--Device-SoundPool-offPlayFinishedWithStreamId(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## off('error')

```TypeScript
off(type: 'error'): void
```

Unsubscribes from error events of a SoundPool instance.

**Since:** 10

<!--Device-SoundPool-off(type: 'error'): void--><!--Device-SoundPool-off(type: 'error'): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type, which is **'error'** in this case. |

## off('errorOccurred')

```TypeScript
off(type: 'errorOccurred', callback?: Callback<ErrorInfo>): void
```

Unsubscribes from error events of a SoundPool instance.

**Since:** 20

<!--Device-SoundPool-off(type: 'errorOccurred', callback?: Callback<ErrorInfo>): void--><!--Device-SoundPool-off(type: 'errorOccurred', callback?: Callback<ErrorInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'errorOccurred' | Yes | Event type, which is **'errorOccurred'** in this case. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ErrorInfo](arkts-media-soundpool-errorinfo-i.md)&gt; | No | Callback used to return [ErrorInfo](arkts-media-soundpool-errorinfo-i.md) if an error occurs during the use of the player. If the callback is not set, no related information is provided. |

## off('loadComplete')

```TypeScript
off(type: 'loadComplete'): void
```

Unsubscribes from events indicating that a sound finishes loading.

**Since:** 10

<!--Device-SoundPool-off(type: 'loadComplete'): void--><!--Device-SoundPool-off(type: 'loadComplete'): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'loadComplete' | Yes | Event type. The value is fixed at **'loadComplete'**. |

## off('playFinished')

```TypeScript
off(type: 'playFinished'): void
```

Unsubscribes from events indicating that a sound finishes playing.

**Since:** 10

<!--Device-SoundPool-off(type: 'playFinished'): void--><!--Device-SoundPool-off(type: 'playFinished'): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playFinished' | Yes | Event type. The value is fixed at **'playFinished'**. |

## off('playFinishedWithStreamId')

```TypeScript
off(type: 'playFinishedWithStreamId'): void
```

Unsubscribes from events indicating that a sound finishes playing.

**Since:** 18

<!--Device-SoundPool-off(type: 'playFinishedWithStreamId'): void--><!--Device-SoundPool-off(type: 'playFinishedWithStreamId'): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playFinishedWithStreamId' | Yes | Event type. The value is fixed at **'playFinishedWithStreamId'**. |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events of this **SoundPool** instance. This event is used only for error prompt. This event can be triggered by both user operations and the system.

**Since:** 23

<!--Device-SoundPool-onError(callback: ErrorCallback): void--><!--Device-SoundPool-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-errorcallback-t.md) | Yes | Callback used to return the error code ID and error message. |

## onErrorOccurred

```TypeScript
onErrorOccurred(callback: Callback<ErrorInfo>): void
```

Subscribes to errorOccurred events of this **SoundPool** instance.

**Since:** 23

<!--Device-SoundPool-onErrorOccurred(callback: Callback<ErrorInfo>): void--><!--Device-SoundPool-onErrorOccurred(callback: Callback<ErrorInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ErrorInfo](arkts-media-soundpool-errorinfo-i.md)&gt; | Yes | Callback used to listen for soundpool errorOccurred events. |

## onLoadComplete

```TypeScript
onLoadComplete(callback: Callback<int>): void
```

Subscribes to events indicating that a sound finishes loading. This event is triggered when a sound is loaded.

**Since:** 23

<!--Device-SoundPool-onLoadComplete(callback: Callback<int>): void--><!--Device-SoundPool-onLoadComplete(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;int&gt; | Yes | ID of the sound that has been loaded. |

## onPlayFinished

```TypeScript
onPlayFinished(callback: Callback<void>): void
```

Subscribes to events indicating that a sound finishes playing. This event is triggered when a sound finishes playing.

**Since:** 23

<!--Device-SoundPool-onPlayFinished(callback: Callback<void>): void--><!--Device-SoundPool-onPlayFinished(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

## onPlayFinishedWithStreamId

```TypeScript
onPlayFinishedWithStreamId(callback: Callback<int>): void
```

Subscribes to events indicating the completion of audio playback and returns the stream ID of the audio that finishes playing.

When only on('playFinished') or on('playFinishedWithStreamId') is subscribed to, the registered callback is triggered when the audio playback is complete.

When both on('playFinished') and on('playFinishedWithStreamId') are subscribed to, the 'playFinishedWithStreamId' callback is triggered, but the 'playFinished' callback is not triggered, when the audio playback is complete.

**Since:** 23

<!--Device-SoundPool-onPlayFinishedWithStreamId(callback: Callback<int>): void--><!--Device-SoundPool-onPlayFinishedWithStreamId(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;int&gt; | Yes | Callback used to return the result. Stream ID of the audio that finishes playing. |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to error events of a SoundPool instance. This event is used only for error prompt. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-on(type: 'error', callback: ErrorCallback): void--><!--Device-SoundPool-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type, which is **'error'** in this case. This event can be triggered by both user operations and the system. |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-errorcallback-t.md) | Yes | Callback used to return the error code ID and error message. |

## on('errorOccurred')

```TypeScript
on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void
```

Subscribes to error events of a SoundPool instance and returns [ErrorInfo](arkts-media-soundpool-errorinfo-i.md) that contains the error code, error stage, resource ID, and audio stream ID. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-SoundPool-on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void--><!--Device-SoundPool-on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'errorOccurred' | Yes | Event type, which is **'errorOccurred'** in this case. This event can be triggered by both user operations and the system. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ErrorInfo](arkts-media-soundpool-errorinfo-i.md)&gt; | Yes | Callback used to return [ErrorInfo](arkts-media-soundpool-errorinfo-i.md). |

## on('loadComplete')

```TypeScript
on(type: 'loadComplete', callback: Callback<int>): void
```

Subscribes to events indicating that a sound finishes loading. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-on(type: 'loadComplete', callback: Callback<int>): void--><!--Device-SoundPool-on(type: 'loadComplete', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'loadComplete' | Yes | Event type, which is **'loadComplete'** in this case. This event is triggered when a sound is loaded. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;int&gt; | Yes | Callback used to return the ID of the resource that has been loaded. |

## on('playFinished')

```TypeScript
on(type: 'playFinished', callback: Callback<void>): void
```

Subscribes to events indicating that a sound finishes playing. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-on(type: 'playFinished', callback: Callback<void>): void--><!--Device-SoundPool-on(type: 'playFinished', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playFinished' | Yes | Event type, which is **'playFinished'** in this case. This event is triggered when a sound finishes playing. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

## on('playFinishedWithStreamId')

```TypeScript
on(type: 'playFinishedWithStreamId', callback: Callback<int>): void
```

Subscribes to events indicating the completion of audio playback and returns the stream ID of the audio that finishes playing. This API uses an asynchronous callback to return the result.

When only [on('playFinished')](#onloadcomplete) or [on('playFinishedWithStreamId')](#onloadcomplete) is subscribed to, the registered callback is triggered when the audio playback is complete.

When both [on('playFinished')](#onloadcomplete) and [on('playFinishedWithStreamId')](#onloadcomplete) are subscribed to, the 'playFinishedWithStreamId' callback is triggered, but the 'playFinished' callback is not triggered, when the audio playback is complete.

**Since:** 18

<!--Device-SoundPool-on(type: 'playFinishedWithStreamId', callback: Callback<int>): void--><!--Device-SoundPool-on(type: 'playFinishedWithStreamId', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playFinishedWithStreamId' | Yes | Event type, which is **'playFinishedWithStreamId'** in this case. This event is triggered when an audio stream finishes playing, and the stream ID is returned. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;int&gt; | Yes | Callback used to return the stream ID of the audio that has finished playing. |

## play

```TypeScript
play(soundID: int, params: PlayParameters, callback: AsyncCallback<int>): void
```

Plays a sound and obtains the stream ID. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-SoundPool-play(soundID: int, params: PlayParameters, callback: AsyncCallback<int>): void--><!--Device-SoundPool-play(soundID: int, params: PlayParameters, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundID | int | Yes | Sound ID, which is obtained by calling **load()**. |
| params | [PlayParameters](arkts-media-soundpool-playparameters-i.md) | Yes | Playback parameters. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;int&gt; | Yes | Callback used to return the audio stream ID. A valid value must be greater than 0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## play

```TypeScript
play(soundID: int, callback: AsyncCallback<int>): void
```

Plays a sound using default parameters and obtains the stream ID. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-SoundPool-play(soundID: int, callback: AsyncCallback<int>): void--><!--Device-SoundPool-play(soundID: int, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundID | int | Yes | Sound ID, which is obtained by calling **load()**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;int&gt; | Yes | Callback used to return the audio stream ID. A valid value must be greater than 0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## play

```TypeScript
play(soundID: int, params?: PlayParameters): Promise<int>
```

Plays a sound and obtains the stream ID. This API uses a promise to return the result.

**Since:** 23

<!--Device-SoundPool-play(soundID: int, params?: PlayParameters): Promise<int>--><!--Device-SoundPool-play(soundID: int, params?: PlayParameters): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundID | int | Yes | Sound ID, which is obtained by calling **load()**. |
| params | [PlayParameters](arkts-media-soundpool-playparameters-i.md) | No | Playback parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the audio stream ID. A valid value must be greater than 0 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases a **SoundPool** instance. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-SoundPool-release(callback: AsyncCallback<void>): void--><!--Device-SoundPool-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## release

```TypeScript
release(): Promise<void>
```

Releases a **SoundPool** instance. This API uses a promise to return the result.

**Since:** 23

<!--Device-SoundPool-release(): Promise<void>--><!--Device-SoundPool-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## setInterruptMode

```TypeScript
setInterruptMode(interruptMode: media.SoundInterruptMode): void
```

Sets the interruption mode of the audio files with the same ID during playback. After the **SoundPool** is created, this API is valid only when the **Play** function of the **SoundPool** is called for the first time. You can set the interruption mode for multiple times. If the interruption mode is not set, the [SAME_SOUND_INTERRUPT](../../../reference/apis-media-kit/arkts-apis-media-e.md) mode is used by default. That is , if the former audio file is not completely played, the latter audio file with the same ID interrupts the former audio file.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-SoundPool-setInterruptMode(interruptMode: media.SoundInterruptMode): void--><!--Device-SoundPool-setInterruptMode(interruptMode: media.SoundInterruptMode): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| interruptMode | media.SoundInterruptMode | Yes | Interruption mode of the audio files with the same ID during playback, which is obtained through the **media.SoundInterruptMode** enum. |

## setLoop

```TypeScript
setLoop(streamID: int, loop: int, callback: AsyncCallback<void>): void
```

Sets the loop mode. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-SoundPool-setLoop(streamID: int, loop: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setLoop(streamID: int, loop: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| loop | int | Yes | Number of loops.<br>If this parameter is set to a value greater than or equal to 0, the number of times the content is actually played is the value of **loop** plus 1.<br> If this parameter is set to a value less than 0, the content is played repeatedly. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## setLoop

```TypeScript
setLoop(streamID: int, loop: int): Promise<void>
```

Sets the loop mode. This API uses a promise to return the result.

**Since:** 23

<!--Device-SoundPool-setLoop(streamID: int, loop: int): Promise<void>--><!--Device-SoundPool-setLoop(streamID: int, loop: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| loop | int | Yes | Number of loops.<br>If this parameter is set to a value greater than or equal to 0, the number of times the content is actually played is the value of **loop** plus 1.<br> If this parameter is set to a value less than 0, the content is played repeatedly. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## setPriority

```TypeScript
setPriority(streamID: int, priority: int, callback: AsyncCallback<void>): void
```

Sets the priority for an audio stream. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-SoundPool-setPriority(streamID: int, priority: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setPriority(streamID: int, priority: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| priority | int | Yes | Priority. The value **0** means the lowest priority. The value is an integer greater than or equal to 0. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## setPriority

```TypeScript
setPriority(streamID: int, priority: int): Promise<void>
```

Sets the priority for an audio stream. This API uses a promise to return the result.

**Since:** 23

<!--Device-SoundPool-setPriority(streamID: int, priority: int): Promise<void>--><!--Device-SoundPool-setPriority(streamID: int, priority: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| priority | int | Yes | Priority. The value **0** means the lowest priority. The value is an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## setRate

```TypeScript
setRate(streamID: int, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void
```

Sets the playback rate for an audio stream. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| rate | audio.AudioRendererRate | Yes | Playback rate. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## setRate

```TypeScript
setRate(streamID: int, rate: audio.AudioRendererRate): Promise<void>
```

Sets the playback rate for an audio stream. This API uses a promise to return the result.

**Since:** 23

<!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate): Promise<void>--><!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| rate | audio.AudioRendererRate | Yes | Playback rate. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## setVolume

```TypeScript
setVolume(streamID: int, leftVolume: double, rightVolume: double, callback: AsyncCallback<void>): void
```

Sets the volume for an audio stream. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| leftVolume | double | Yes | Volume of the left channel. The value range is [0.0, 1.0]. |
| rightVolume | double | Yes | Volume of the right channel. The value range is [0.0, 1.0]. Currently, setting the volume for the right channel does not take effect. The volume set for the left channel is used. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## setVolume

```TypeScript
setVolume(streamID: int, leftVolume: double, rightVolume: double): Promise<void>
```

Sets the volume for an audio stream. This API uses a promise to return the result.

**Since:** 23

<!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double): Promise<void>--><!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| leftVolume | double | Yes | Volume of the left channel. The value range is [0.0, 1.0]. |
| rightVolume | double | Yes | Volume of the right channel. The value range is [0.0, 1.0]. Currently, setting the volume for the right channel does not take effect. The volume set for the left channel is used. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## stop

```TypeScript
stop(streamID: int, callback: AsyncCallback<void>): void
```

Stops audio playback. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-SoundPool-stop(streamID: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-stop(streamID: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## stop

```TypeScript
stop(streamID: int): Promise<void>
```

Stops audio playback. This API uses a promise to return the result.

**Since:** 23

<!--Device-SoundPool-stop(streamID: int): Promise<void>--><!--Device-SoundPool-stop(streamID: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | int | Yes | Audio stream ID, which is obtained by calling **play()**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## unload

```TypeScript
unload(soundID: int, callback: AsyncCallback<void>): void
```

Unloads a sound. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-SoundPool-unload(soundID: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-unload(soundID: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundID | int | Yes | Sound ID, which is obtained by calling **load()**. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400103](../errorcode-media.md#5400103-io-error) | I/O error. Return by callback. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## unload

```TypeScript
unload(soundID: int): Promise<void>
```

Unloads a sound. This API uses a promise to return the result.

**Since:** 23

<!--Device-SoundPool-unload(soundID: int): Promise<void>--><!--Device-SoundPool-unload(soundID: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundID | int | Yes | Sound ID, which is obtained by calling **load()**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../errorcode-media.md#5400103-io-error) | I/O error. Return by promise. |
| [5400105](../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

