# SoundPool

Implements a sound pool that provides APIs for loading, unloading, playing, and stopping playing system sounds, setting the volume, and setting the number of loops. Before using these APIs, you must call   
[media.createSoundPool](../../../reference/apis-media-kit/arkts-apis-media-f.md)to create a SoundPool instance.

> **NOTE：**
> 
> - When using the SoundPool instance, you are advised to register the following callbacks to proactively obtain
> status changes:
> > - [on('loadComplete')](SoundPool.on(type: 'loadComplete', callback: Callback&lt;int&gt;)): listens for the
> event indicating that the resource loading is finished. You are advised to listen for this callback to ensure that
> the audio is played after being loaded.
> > -
> [on('playFinishedWithStreamId')](SoundPool.on(type: 'playFinishedWithStreamId', callback: Callback&lt;int&gt;)):
> listens for the event indicating that the playback is finished and returns the stream ID of the audio that finishes
> playing.
> > - [on('playFinished')](SoundPool.on(type: 'playFinishedWithStreamId', callback: Callback&lt;int&gt;)): listens
> for the event indicating that the playback is finished.
> > - [on('error')](SoundPool.on(type: 'error', callback: ErrorCallback)): listens for error events.
> > - [on('errorOccurred')](SoundPool.on(type: 'errorOccurred', callback: Callback&lt;ErrorInfo&gt;)): listens for
> error events and returns [errorInfo](arkts-media-soundpool-errorinfo-i.md).
> 
> - Currently, SoundPool does not support audio focus policies such as background playback and audio interruption, or
> skipping the silent frames at the beginning and end of an audio file. For details about low-latency playback using
> SoundPool, see
> [Using SoundPool to Play Short Sounds (ArkTS)](../../../media/media/using-soundpool-for-playback.md).

**Since:** 10

<!--Device-unnamed-export declare interface SoundPool--><!--Device-unnamed-export declare interface SoundPool-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## load

```TypeScript
load(uri: string, callback: AsyncCallback<number>): void
```

Loads a sound. This API uses an asynchronous callback to return the result.

This API uses an asynchronous callback to obtain the resource ID. The input parameter URL is a string starting with  
**fd://**, which is generated based on the file descriptor (FD) obtained.

This API cannot be used to load resources in the **rawfile** directory. Instead, use   
[load(fd: number, offset: number, length: number, callback: AsyncCallback\&lt;number&gt;): void](arkts-media-soundpool-soundpool-i.md#load)or   
[load(fd: number, offset: number, length: number): Promise\&lt;number&gt;](arkts-media-soundpool-soundpool-i.md#load).

> **NOTE：**
> 
> - After the resource handle (in the form of an FD) or path description (in the form of a URI) is transferred to
> the player, do not use the resource handle or path description in read or write operations, including but not
> limited to transferring it to multiple players.
> 
> - Competition occurs when multiple players use the same resource handle or path description to read and write
> files at the same time, resulting in playback errors.

**Since:** 10

<!--Device-SoundPool-load(uri: string, callback: AsyncCallback<int>): void--><!--Device-SoundPool-load(uri: string, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## load

```TypeScript
load(uri: string): Promise<number>
```

Loads a sound. This API uses a promise to return the result.

This API uses a promise to obtain the resource ID. The input parameter URL is a string starting with **fd://**, which is generated based on the file descriptor (FD) obtained.

This API cannot be used to load resources in the **rawfile** directory. Instead, use   
[load(fd: number, offset: number, length: number, callback: AsyncCallback\&lt;number&gt;): void](arkts-media-soundpool-soundpool-i.md#load)or   
[load(fd: number, offset: number, length: number): Promise\&lt;number&gt;](arkts-media-soundpool-soundpool-i.md#load).

> **NOTE：**
> 
> - After the resource handle (in the form of an FD) or path description (in the form of a URI) is transferred to
> the player, do not use the resource handle or path description in read or write operations, including but not
> limited to transferring it to multiple players.
> 
> - Competition occurs when multiple players use the same resource handle or path description to read and write
> files at the same time, resulting in playback errors.

**Since:** 10

<!--Device-SoundPool-load(uri: string): Promise<int>--><!--Device-SoundPool-load(uri: string): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## load

```TypeScript
load(fd: number, offset: number, length: number, callback: AsyncCallback<number>): void
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

**Since:** 10

<!--Device-SoundPool-load(fd: int, offset: long, length: long, callback: AsyncCallback<int>): void--><!--Device-SoundPool-load(fd: int, offset: long, length: long, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| offset | number | Yes |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## load

```TypeScript
load(fd: number, offset: number, length: number): Promise<number>
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

**Since:** 10

<!--Device-SoundPool-load(fd: int, offset: long, length: long): Promise<int>--><!--Device-SoundPool-load(fd: int, offset: long, length: long): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |
| offset | number | Yes |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## off('loadComplete')

```TypeScript
off(type: 'loadComplete'): void
```

Unsubscribes from events indicating that a sound finishes loading.

**Since:** 10

<!--Device-SoundPool-off(type: 'loadComplete'): void--><!--Device-SoundPool-off(type: 'loadComplete'): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'loadComplete' | Yes |

## off('playFinishedWithStreamId')

```TypeScript
off(type: 'playFinishedWithStreamId'): void
```

Unsubscribes from events indicating that a sound finishes playing.

**Since:** 18

<!--Device-SoundPool-off(type: 'playFinishedWithStreamId'): void--><!--Device-SoundPool-off(type: 'playFinishedWithStreamId'): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playFinishedWithStreamId' | Yes |

## off('playFinished')

```TypeScript
off(type: 'playFinished'): void
```

Unsubscribes from events indicating that a sound finishes playing.

**Since:** 10

<!--Device-SoundPool-off(type: 'playFinished'): void--><!--Device-SoundPool-off(type: 'playFinished'): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playFinished' | Yes |

## off('error')

```TypeScript
off(type: 'error'): void
```

Unsubscribes from error events of a SoundPool instance.

**Since:** 10

<!--Device-SoundPool-off(type: 'error'): void--><!--Device-SoundPool-off(type: 'error'): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |

## off('errorOccurred')

```TypeScript
off(type: 'errorOccurred', callback?: Callback<ErrorInfo>): void
```

Unsubscribes from error events of a SoundPool instance.

**Since:** 20

<!--Device-SoundPool-off(type: 'errorOccurred', callback?: Callback<ErrorInfo>): void--><!--Device-SoundPool-off(type: 'errorOccurred', callback?: Callback<ErrorInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'errorOccurred' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ErrorInfo&gt; | No |

## on('loadComplete')

```TypeScript
on(type: 'loadComplete', callback: Callback<number>): void
```

Subscribes to events indicating that a sound finishes loading. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-on(type: 'loadComplete', callback: Callback<int>): void--><!--Device-SoundPool-on(type: 'loadComplete', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'loadComplete' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## on('playFinishedWithStreamId')

```TypeScript
on(type: 'playFinishedWithStreamId', callback: Callback<number>): void
```

Subscribes to events indicating the completion of audio playback and returns the stream ID of the audio that finishes playing. This API uses an asynchronous callback to return the result.

When only [on('playFinished')](SoundPool.on(type: 'playFinishedWithStreamId', callback: Callback&lt;int&gt;)) or   
[on('playFinishedWithStreamId')](SoundPool.on(type: 'playFinishedWithStreamId', callback: Callback&lt;int&gt;)) is subscribed to, the registered callback is triggered when the audio playback is complete.

When both [on('playFinished')](SoundPool.on(type: 'playFinishedWithStreamId', callback: Callback&lt;int&gt;)) and   
[on('playFinishedWithStreamId')](SoundPool.on(type: 'playFinishedWithStreamId', callback: Callback&lt;int&gt;)) are subscribed to, the 'playFinishedWithStreamId' callback is triggered, but the 'playFinished' callback is not triggered, when the audio playback is complete.

**Since:** 18

<!--Device-SoundPool-on(type: 'playFinishedWithStreamId', callback: Callback<int>): void--><!--Device-SoundPool-on(type: 'playFinishedWithStreamId', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playFinishedWithStreamId' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

## on('playFinished')

```TypeScript
on(type: 'playFinished', callback: Callback<void>): void
```

Subscribes to events indicating that a sound finishes playing. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-on(type: 'playFinished', callback: Callback<void>): void--><!--Device-SoundPool-on(type: 'playFinished', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'playFinished' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to error events of a   
[SoundPool](../../../reference/apis-media-kit/js-apis-inner-multimedia-soundPool.md#soundpool) instance. This event is used only for error prompt. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-on(type: 'error', callback: ErrorCallback): void--><!--Device-SoundPool-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

## on('errorOccurred')

```TypeScript
on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void
```

Subscribes to error events of a   
[SoundPool](../../../reference/apis-media-kit/js-apis-inner-multimedia-soundPool.md#soundpool) instance and returns [ErrorInfo](arkts-media-soundpool-errorinfo-i.md) that contains the error code, error stage, resource ID, and audio stream ID. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-SoundPool-on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void--><!--Device-SoundPool-on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'errorOccurred' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ErrorInfo&gt; | Yes |

## play

```TypeScript
play(soundID: number, params: PlayParameters, callback: AsyncCallback<number>): void
```

Plays a sound and obtains the stream ID. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-play(soundID: int, params: PlayParameters, callback: AsyncCallback<int>): void--><!--Device-SoundPool-play(soundID: int, params: PlayParameters, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| soundID | number | Yes |
| params | [PlayParameters](arkts-media-media-playparameters-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## play

```TypeScript
play(soundID: number, callback: AsyncCallback<number>): void
```

Plays a sound using default parameters and obtains the stream ID. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-play(soundID: int, callback: AsyncCallback<int>): void--><!--Device-SoundPool-play(soundID: int, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| soundID | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## play

```TypeScript
play(soundID: number, params?: PlayParameters): Promise<number>
```

Plays a sound and obtains the stream ID. This API uses a promise to return the result.

**Since:** 10

<!--Device-SoundPool-play(soundID: int, params?: PlayParameters): Promise<int>--><!--Device-SoundPool-play(soundID: int, params?: PlayParameters): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| soundID | number | Yes |
| params | [PlayParameters](arkts-media-media-playparameters-t.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases a **SoundPool** instance. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-release(callback: AsyncCallback<void>): void--><!--Device-SoundPool-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## release

```TypeScript
release(): Promise<void>
```

Releases a **SoundPool** instance. This API uses a promise to return the result.

**Since:** 10

<!--Device-SoundPool-release(): Promise<void>--><!--Device-SoundPool-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## setInterruptMode

```TypeScript
setInterruptMode(interruptMode: media.SoundInterruptMode): void
```

Sets the interruption mode of the audio files with the same ID during playback. After the **SoundPool** is created,this API is valid only when the **Play** function of the **SoundPool** is called for the first time. You can set the interruption mode for multiple times. If the interruption mode is not set, the   
[SAME_SOUND_INTERRUPT](../../../reference/apis-media-kit/arkts-apis-media-e.md) mode is used by default. That is, if the former audio file is not completely played, the latter audio file with the same ID interrupts the former audio file.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-SoundPool-setInterruptMode(interruptMode: media.SoundInterruptMode): void--><!--Device-SoundPool-setInterruptMode(interruptMode: media.SoundInterruptMode): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| interruptMode | media.SoundInterruptMode | Yes |

## setLoop

```TypeScript
setLoop(streamID: number, loop: number, callback: AsyncCallback<void>): void
```

Sets the loop mode. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-setLoop(streamID: int, loop: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setLoop(streamID: int, loop: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamID | number | Yes |
| loop | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## setLoop

```TypeScript
setLoop(streamID: number, loop: number): Promise<void>
```

Sets the loop mode. This API uses a promise to return the result.

**Since:** 10

<!--Device-SoundPool-setLoop(streamID: int, loop: int): Promise<void>--><!--Device-SoundPool-setLoop(streamID: int, loop: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamID | number | Yes |
| loop | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## setPriority

```TypeScript
setPriority(streamID: number, priority: number, callback: AsyncCallback<void>): void
```

Sets the priority for an audio stream. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-setPriority(streamID: int, priority: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setPriority(streamID: int, priority: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamID | number | Yes |
| priority | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## setPriority

```TypeScript
setPriority(streamID: number, priority: number): Promise<void>
```

Sets the priority for an audio stream. This API uses a promise to return the result.

**Since:** 10

<!--Device-SoundPool-setPriority(streamID: int, priority: int): Promise<void>--><!--Device-SoundPool-setPriority(streamID: int, priority: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamID | number | Yes |
| priority | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## setRate

```TypeScript
setRate(streamID: number, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void
```

Sets the playback rate for an audio stream. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamID | number | Yes |
| rate | audio.AudioRendererRate | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## setRate

```TypeScript
setRate(streamID: number, rate: audio.AudioRendererRate): Promise<void>
```

Sets the playback rate for an audio stream. This API uses a promise to return the result.

**Since:** 10

<!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate): Promise<void>--><!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamID | number | Yes |
| rate | audio.AudioRendererRate | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## setVolume

```TypeScript
setVolume(streamID: number, leftVolume: number, rightVolume: number, callback: AsyncCallback<void>): void
```

Sets the volume for an audio stream. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamID | number | Yes |
| leftVolume | number | Yes |
| rightVolume | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## setVolume

```TypeScript
setVolume(streamID: number, leftVolume: number, rightVolume: number): Promise<void>
```

Sets the volume for an audio stream. This API uses a promise to return the result.

**Since:** 10

<!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double): Promise<void>--><!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamID | number | Yes |
| leftVolume | number | Yes |
| rightVolume | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## stop

```TypeScript
stop(streamID: number, callback: AsyncCallback<void>): void
```

Stops audio playback. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-stop(streamID: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-stop(streamID: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamID | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## stop

```TypeScript
stop(streamID: number): Promise<void>
```

Stops audio playback. This API uses a promise to return the result.

**Since:** 10

<!--Device-SoundPool-stop(streamID: int): Promise<void>--><!--Device-SoundPool-stop(streamID: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| streamID | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## unload

```TypeScript
unload(soundID: number, callback: AsyncCallback<void>): void
```

Unloads a sound. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-SoundPool-unload(soundID: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-unload(soundID: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| soundID | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |

## unload

```TypeScript
unload(soundID: number): Promise<void>
```

Unloads a sound. This API uses a promise to return the result.

**Since:** 10

<!--Device-SoundPool-unload(soundID: int): Promise<void>--><!--Device-SoundPool-unload(soundID: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| soundID | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../errorcode-media.md#5400103-io-error) |
| [5400105](../errorcode-media.md#5400105-play-service-dead) |
