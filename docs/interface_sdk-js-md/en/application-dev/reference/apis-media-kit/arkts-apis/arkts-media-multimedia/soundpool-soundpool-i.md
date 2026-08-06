# SoundPool

Implements a sound pool that provides APIs for loading, unloading, playing, and stopping playing system sounds,setting the volume, and setting the number of loops. Before using these APIs, you must call  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_to create a SoundPool instance.
    **NOTE**  
    
    - When using the SoundPool instance, you are advised to register the following callbacks to proactively obtain  
    status changes:  
        - [on('loadComplete')]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_: listens for the  
    event indicating that the resource loading is finished. You are advised to listen for this callback to ensure that  
    the audio is played after being loaded.  
        -  
    [on('playFinishedWithStreamId')]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_:  
    listens for the event indicating that the playback is finished and returns the stream ID of the audio that finishes  
    playing.  
        - [on('playFinished')]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_: listens  
    for the event indicating that the playback is finished.  
        - [on('error')]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_: listens for error events.  
        - [on('errorOccurred')]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_: listens for  
    error events and returns [errorInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_.  
    
    - Currently, SoundPool does not support audio focus policies such as background playback and audio interruption, or  
    skipping the silent frames at the beginning and end of an audio file. For details about low-latency playback using  
    SoundPool, see  
    \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface SoundPool--><!--Device-unnamed-export declare interface SoundPool-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## load

ArkTS-Dyn:
```TypeScript
load(uri: string, callback: AsyncCallback<number>): void
```

ArkTS-Sta:
```TypeScript
load(uri: string, callback: AsyncCallback<int>): void
```

Loads a sound. This API uses an asynchronous callback to return the result.

This API uses an asynchronous callback to obtain the resource ID. The input parameter URL is a string starting with  
**fd://**, which is generated based on the file descriptor (FD) obtained.

This API cannot be used to load resources in the **rawfile** directory. Instead, use  
[load(fd: number, offset: number, length: number, callback: AsyncCallback\_\_\_ESCAPED\_UNDERSCORE\_DESC\_\_\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_): void]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_or  
[load(fd: number, offset: number, length: number): Promise\_\_\_ESCAPED\_UNDERSCORE\_DESC\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.
    **NOTE**  
    
    - After the resource handle (in the form of an FD) or path description (in the form of a URI) is transferred to  
    the player, do not use the resource handle or path description in read or write operations, including but not  
    limited to transferring it to multiple players.  
    
    - Competition occurs when multiple players use the same resource handle or path description to read and write  
    files at the same time, resulting in playback errors.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-load(uri: string, callback: AsyncCallback<int>): void--><!--Device-SoundPool-load(uri: string, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the audio file to load. Generally, the URI starts with **fd://**. |
| callback | ArkTS-Dyn: \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_2\_\_\_ArkTS-Sta：\_\_\_MD\_LINK\_USD\_1\_\_\_&lt;int&gt; | Yes | Callback used to return the sound ID. A valid value must be greater than 0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400103](../../errorcode-media.md#5400103-io-error) | I/O error. Return by callback. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## load

ArkTS-Dyn:
```TypeScript
load(uri: string): Promise<number>
```

ArkTS-Sta:
```TypeScript
load(uri: string): Promise<int>
```

Loads a sound. This API uses a promise to return the result.

This API uses a promise to obtain the resource ID. The input parameter URL is a string starting with **fd://**,which is generated based on the file descriptor (FD) obtained.

This API cannot be used to load resources in the **rawfile** directory. Instead, use  
[load(fd: number, offset: number, length: number, callback: AsyncCallback\_\_\_ESCAPED\_UNDERSCORE\_DESC\_\_\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_): void]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_or  
[load(fd: number, offset: number, length: number): Promise\_\_\_ESCAPED\_UNDERSCORE\_DESC\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.
    **NOTE**  
    
    - After the resource handle (in the form of an FD) or path description (in the form of a URI) is transferred to  
    the player, do not use the resource handle or path description in read or write operations, including but not  
    limited to transferring it to multiple players.  
    
    - Competition occurs when multiple players use the same resource handle or path description to read and write  
    files at the same time, resulting in playback errors.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-load(uri: string): Promise<int>--><!--Device-SoundPool-load(uri: string): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI of the audio file to load. Generally, the URI starts with **fd://**. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Promise&lt;int&gt; | Promise used to return the sound ID. A valid value must be greater than 0 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../../errorcode-media.md#5400103-io-error) | I/O error. Return by promise. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## load

ArkTS-Dyn:
```TypeScript
load(fd: number, offset: number, length: number, callback: AsyncCallback<number>): void
```

ArkTS-Sta:
```TypeScript
load(fd: int, offset: long, length: long, callback: AsyncCallback<int>): void
```

Loads a sound. This API uses an asynchronous callback to return the result.

This API uses an asynchronous callback to obtain the resource ID. For the input parameter, resource information can be passed in manually or acquired automatically by reading the application's built-in resources.
    **NOTE**  
    
    - After the resource handle (in the form of an FD) or path description (in the form of a URI) is transferred to  
    the player, do not use the resource handle or path description in read or write operations, including but not  
    limited to transferring it to multiple players.  
    
    - Competition occurs when multiple players use the same resource handle or path description to read and write  
    files at the same time, resulting in playback errors.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-load(fd: int, offset: long, length: long, callback: AsyncCallback<int>): void--><!--Device-SoundPool-load(fd: int, offset: long, length: long, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Resource handle, which is obtained by calling \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| offset | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | Resource offset, which needs to be entered based on the preset resource information. An invalid value causes a failure to parse audio and video resources. |
| length | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | Resource length, which needs to be entered based on the preset resource information. An invalid value causes a failure to parse audio and video resources. |
| callback | ArkTS-Dyn: \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_2\_\_\_ArkTS-Sta：\_\_\_MD\_LINK\_USD\_1\_\_\_&lt;int&gt; | Yes | Callback used to return the sound ID. A valid value must be greater than 0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400103](../../errorcode-media.md#5400103-io-error) | I/O error. Return by callback. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## load

ArkTS-Dyn:
```TypeScript
load(fd: number, offset: number, length: number): Promise<number>
```

ArkTS-Sta:
```TypeScript
load(fd: int, offset: long, length: long): Promise<int>
```

Loads a sound. This API uses a promise to return the result.

This API uses a promise to obtain the resource ID. For the input parameter, resource information can be passed in manually or acquired automatically by reading the application's built-in resources.
    **NOTE**  
    
    - After the resource handle (in the form of an FD) or path description (in the form of a URI) is transferred to  
    the player, do not use the resource handle or path description in read or write operations, including but not  
    limited to transferring it to multiple players.  
    
    - Competition occurs when multiple players use the same resource handle or path description to read and write  
    files at the same time, resulting in playback errors.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-load(fd: int, offset: long, length: long): Promise<int>--><!--Device-SoundPool-load(fd: int, offset: long, length: long): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Resource handle, which is obtained by calling \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ |
| offset | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | Resource offset, which needs to be entered based on the preset resource information. An invalid value causes a failure to parse audio and video resources. |
| length | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | Resource length, which needs to be entered based on the preset resource information. An invalid value causes a failure to parse audio and video resources. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Promise&lt;int&gt; | Promise used to return the sound ID. A valid value must be greater than 0 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../../errorcode-media.md#5400103-io-error) | I/O error. Return by promise. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## off('loadComplete')

```TypeScript
off(type: 'loadComplete'): void
```

Unsubscribes from events indicating that a sound finishes loading.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-SoundPool-off(type: 'loadComplete'): void--><!--Device-SoundPool-off(type: 'loadComplete'): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'loadComplete' | Yes | Event type. The value is fixed at **'loadComplete'**. |

## off('playFinishedWithStreamId')

```TypeScript
off(type: 'playFinishedWithStreamId'): void
```

Unsubscribes from events indicating that a sound finishes playing.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-SoundPool-off(type: 'playFinishedWithStreamId'): void--><!--Device-SoundPool-off(type: 'playFinishedWithStreamId'): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playFinishedWithStreamId' | Yes | Event type. The value is fixed at **'playFinishedWithStreamId'**. |

## off('playFinished')

```TypeScript
off(type: 'playFinished'): void
```

Unsubscribes from events indicating that a sound finishes playing.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-SoundPool-off(type: 'playFinished'): void--><!--Device-SoundPool-off(type: 'playFinished'): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playFinished' | Yes | Event type. The value is fixed at **'playFinished'**. |

## off('error')

```TypeScript
off(type: 'error'): void
```

Unsubscribes from error events of a SoundPool instance.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

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

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-SoundPool-off(type: 'errorOccurred', callback?: Callback<ErrorInfo>): void--><!--Device-SoundPool-off(type: 'errorOccurred', callback?: Callback<ErrorInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'errorOccurred' | Yes | Event type, which is **'errorOccurred'** in this case. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | No | Callback used to return [ErrorInfo]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ if an error occurs during the use of the player. If the callback is not set, no related information is provided. |

## offError

```TypeScript
offError(): void
```

Unsubscribes from error events of this **SoundPool** instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SoundPool-offError(): void--><!--Device-SoundPool-offError(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## offErrorOccurred

```TypeScript
offErrorOccurred(callback?: Callback<ErrorInfo>): void
```

Unsubscribes from errorOccurred events of this **SoundPool** instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SoundPool-offErrorOccurred(callback?: Callback<ErrorInfo>): void--><!--Device-SoundPool-offErrorOccurred(callback?: Callback<ErrorInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | No | Callback used to listen for soundpool errorOccurred events. |

## offLoadComplete

```TypeScript
offLoadComplete(): void
```

Unsubscribes from events indicating that a sound finishes loading.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SoundPool-offLoadComplete(): void--><!--Device-SoundPool-offLoadComplete(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## offPlayFinished

```TypeScript
offPlayFinished(): void
```

Unsubscribes from events indicating that a sound finishes playing.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SoundPool-offPlayFinished(): void--><!--Device-SoundPool-offPlayFinished(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## offPlayFinishedWithStreamId

```TypeScript
offPlayFinishedWithStreamId(): void
```

Unsubscribes from events indicating that a sound finishes playing.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SoundPool-offPlayFinishedWithStreamId(): void--><!--Device-SoundPool-offPlayFinishedWithStreamId(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## on('loadComplete')

```TypeScript
on(type: 'loadComplete', callback: Callback<int>): void
```

Subscribes to events indicating that a sound finishes loading. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-SoundPool-on(type: 'loadComplete', callback: Callback<int>): void--><!--Device-SoundPool-on(type: 'loadComplete', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'loadComplete' | Yes | Event type, which is **'loadComplete'** in this case. This event is triggered when a sound is loaded. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback used to return the ID of the resource that has been loaded. |

## on('playFinishedWithStreamId')

```TypeScript
on(type: 'playFinishedWithStreamId', callback: Callback<int>): void
```

Subscribes to events indicating the completion of audio playback and returns the stream ID of the audio that finishes playing. This API uses an asynchronous callback to return the result.

When only [on('playFinished')]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or  
[on('playFinishedWithStreamId')]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ is subscribed to, the registered callback is triggered when the audio playback is complete.

When both [on('playFinished')]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ and  
[on('playFinishedWithStreamId')]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ are subscribed to, the 'playFinishedWithStreamId' callback is triggered, but the 'playFinished' callback is not triggered, when the audio playback is complete.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-SoundPool-on(type: 'playFinishedWithStreamId', callback: Callback<int>): void--><!--Device-SoundPool-on(type: 'playFinishedWithStreamId', callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playFinishedWithStreamId' | Yes | Event type, which is **'playFinishedWithStreamId'** in this case. This event is triggered when an audio stream finishes playing, and the stream ID is returned. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback used to return the stream ID of the audio that has finished playing. |

## on('playFinished')

```TypeScript
on(type: 'playFinished', callback: Callback<void>): void
```

Subscribes to events indicating that a sound finishes playing. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-SoundPool-on(type: 'playFinished', callback: Callback<void>): void--><!--Device-SoundPool-on(type: 'playFinished', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playFinished' | Yes | Event type, which is **'playFinished'** in this case. This event is triggered when a sound finishes playing. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to error events of a  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ instance. This event is used only for error prompt. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-SoundPool-on(type: 'error', callback: ErrorCallback): void--><!--Device-SoundPool-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type, which is **'error'** in this case. This event can be triggered by both user operations and the system. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to return the error code ID and error message. |

## on('errorOccurred')

```TypeScript
on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void
```

Subscribes to error events of a  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ instance and returns [ErrorInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ that contains the error code, error stage, resource ID, and audio stream ID.This API uses an asynchronous callback to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-SoundPool-on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void--><!--Device-SoundPool-on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'errorOccurred' | Yes | Event type, which is **'errorOccurred'** in this case. This event can be triggered by both user operations and the system. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | Yes | Callback used to return [ErrorInfo]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

## onError

```TypeScript
onError(callback: ErrorCallback): void
```

Subscribes to error events of this **SoundPool** instance. This event is used only for error prompt.This event can be triggered by both user operations and the system.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SoundPool-onError(callback: ErrorCallback): void--><!--Device-SoundPool-onError(callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to return the error code ID and error message. |

## onErrorOccurred

```TypeScript
onErrorOccurred(callback: Callback<ErrorInfo>): void
```

Subscribes to errorOccurred events of this **SoundPool** instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SoundPool-onErrorOccurred(callback: Callback<ErrorInfo>): void--><!--Device-SoundPool-onErrorOccurred(callback: Callback<ErrorInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | Yes | Callback used to listen for soundpool errorOccurred events. |

## onLoadComplete

```TypeScript
onLoadComplete(callback: Callback<int>): void
```

Subscribes to events indicating that a sound finishes loading.This event is triggered when a sound is loaded.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SoundPool-onLoadComplete(callback: Callback<int>): void--><!--Device-SoundPool-onLoadComplete(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | ID of the sound that has been loaded. |

## onPlayFinished

```TypeScript
onPlayFinished(callback: Callback<void>): void
```

Subscribes to events indicating that a sound finishes playing.This event is triggered when a sound finishes playing.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SoundPool-onPlayFinished(callback: Callback<void>): void--><!--Device-SoundPool-onPlayFinished(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |

## onPlayFinishedWithStreamId

```TypeScript
onPlayFinishedWithStreamId(callback: Callback<int>): void
```

Subscribes to events indicating the completion of audio playback and returns the stream ID of the audio that finishes playing.

When only on('playFinished') or on('playFinishedWithStreamId') is subscribed to, the registered callback is triggered when the audio playback is complete.

When both on('playFinished') and on('playFinishedWithStreamId') are subscribed to,the 'playFinishedWithStreamId' callback is triggered, but the 'playFinished' callback is not triggered,when the audio playback is complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-SoundPool-onPlayFinishedWithStreamId(callback: Callback<int>): void--><!--Device-SoundPool-onPlayFinishedWithStreamId(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;int&gt; | Yes | Callback used to return the result. Stream ID of the audio that finishes playing. |

## play

ArkTS-Dyn:
```TypeScript
play(soundID: number, params: PlayParameters, callback: AsyncCallback<number>): void
```

ArkTS-Sta:
```TypeScript
play(soundID: int, params: PlayParameters, callback: AsyncCallback<int>): void
```

Plays a sound and obtains the stream ID. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-play(soundID: int, params: PlayParameters, callback: AsyncCallback<int>): void--><!--Device-SoundPool-play(soundID: int, params: PlayParameters, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Sound ID, which is obtained by calling **load()**. |
| params | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Playback parameters. |
| callback | ArkTS-Dyn: \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_2\_\_\_ArkTS-Sta：\_\_\_MD\_LINK\_USD\_1\_\_\_&lt;int&gt; | Yes | Callback used to return the audio stream ID. A valid value must be greater than 0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## play

ArkTS-Dyn:
```TypeScript
play(soundID: number, callback: AsyncCallback<number>): void
```

ArkTS-Sta:
```TypeScript
play(soundID: int, callback: AsyncCallback<int>): void
```

Plays a sound using default parameters and obtains the stream ID. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-play(soundID: int, callback: AsyncCallback<int>): void--><!--Device-SoundPool-play(soundID: int, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Sound ID, which is obtained by calling **load()**. |
| callback | ArkTS-Dyn: \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_2\_\_\_ArkTS-Sta：\_\_\_MD\_LINK\_USD\_1\_\_\_&lt;int&gt; | Yes | Callback used to return the audio stream ID. A valid value must be greater than 0. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## play

ArkTS-Dyn:
```TypeScript
play(soundID: number, params?: PlayParameters): Promise<number>
```

ArkTS-Sta:
```TypeScript
play(soundID: int, params?: PlayParameters): Promise<int>
```

Plays a sound and obtains the stream ID. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-play(soundID: int, params?: PlayParameters): Promise<int>--><!--Device-SoundPool-play(soundID: int, params?: PlayParameters): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Sound ID, which is obtained by calling **load()**. |
| params | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Playback parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Promise&lt;int&gt; | Promise used to return the audio stream ID. A valid value must be greater than 0 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases a **SoundPool** instance. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-release(callback: AsyncCallback<void>): void--><!--Device-SoundPool-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## release

```TypeScript
release(): Promise<void>
```

Releases a **SoundPool** instance. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-release(): Promise<void>--><!--Device-SoundPool-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## setInterruptMode

```TypeScript
setInterruptMode(interruptMode: media.SoundInterruptMode): void
```

Sets the interruption mode of the audio files with the same ID during playback. After the **SoundPool** is created,this API is valid only when the **Play** function of the **SoundPool** is called for the first time. You can set the interruption mode for multiple times. If the interruption mode is not set, the  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ mode is used by default. That is, if the former audio file is not completely played, the latter audio file with the same ID interrupts the former audio file.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SoundPool-setInterruptMode(interruptMode: media.SoundInterruptMode): void--><!--Device-SoundPool-setInterruptMode(interruptMode: media.SoundInterruptMode): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| interruptMode | media.SoundInterruptMode | Yes | Interruption mode of the audio files with the same ID during playback, which is obtained through the **media.SoundInterruptMode** enum. |

## setLoop

ArkTS-Dyn:
```TypeScript
setLoop(streamID: number, loop: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
setLoop(streamID: int, loop: int, callback: AsyncCallback<void>): void
```

Sets the loop mode. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-setLoop(streamID: int, loop: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setLoop(streamID: int, loop: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| loop | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Number of loops.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_If this parameter is set to a value greater than or equal to 0, the number of times the content is actually played is the value of **loop** plus 1.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ If this parameter is set to a value less than 0, the content is played repeatedly. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## setLoop

ArkTS-Dyn:
```TypeScript
setLoop(streamID: number, loop: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setLoop(streamID: int, loop: int): Promise<void>
```

Sets the loop mode. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-setLoop(streamID: int, loop: int): Promise<void>--><!--Device-SoundPool-setLoop(streamID: int, loop: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| loop | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Number of loops.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_If this parameter is set to a value greater than or equal to 0, the number of times the content is actually played is the value of **loop** plus 1.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ If this parameter is set to a value less than 0, the content is played repeatedly. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## setPriority

ArkTS-Dyn:
```TypeScript
setPriority(streamID: number, priority: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
setPriority(streamID: int, priority: int, callback: AsyncCallback<void>): void
```

Sets the priority for an audio stream. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-setPriority(streamID: int, priority: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setPriority(streamID: int, priority: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| priority | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Priority. The value **0** means the lowest priority. The value is an integer greater than or equal to 0. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## setPriority

ArkTS-Dyn:
```TypeScript
setPriority(streamID: number, priority: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setPriority(streamID: int, priority: int): Promise<void>
```

Sets the priority for an audio stream. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-setPriority(streamID: int, priority: int): Promise<void>--><!--Device-SoundPool-setPriority(streamID: int, priority: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| priority | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Priority. The value **0** means the lowest priority. The value is an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## setRate

ArkTS-Dyn:
```TypeScript
setRate(streamID: number, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
setRate(streamID: int, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void
```

Sets the playback rate for an audio stream. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| rate | audio.AudioRendererRate | Yes | Playback rate. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## setRate

ArkTS-Dyn:
```TypeScript
setRate(streamID: number, rate: audio.AudioRendererRate): Promise<void>
```

ArkTS-Sta:
```TypeScript
setRate(streamID: int, rate: audio.AudioRendererRate): Promise<void>
```

Sets the playback rate for an audio stream. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate): Promise<void>--><!--Device-SoundPool-setRate(streamID: int, rate: audio.AudioRendererRate): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| rate | audio.AudioRendererRate | Yes | Playback rate. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## setVolume

ArkTS-Dyn:
```TypeScript
setVolume(streamID: number, leftVolume: number, rightVolume: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
setVolume(streamID: int, leftVolume: double, rightVolume: double, callback: AsyncCallback<void>): void
```

Sets the volume for an audio stream. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double, callback: AsyncCallback<void>): void--><!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| leftVolume | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Volume of the left channel. The value range is [0.0, 1.0]. |
| rightVolume | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Volume of the right channel. The value range is [0.0, 1.0]. Currently, setting the volume for the right channel does not take effect. The volume set for the left channel is used. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## setVolume

ArkTS-Dyn:
```TypeScript
setVolume(streamID: number, leftVolume: number, rightVolume: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setVolume(streamID: int, leftVolume: double, rightVolume: double): Promise<void>
```

Sets the volume for an audio stream. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double): Promise<void>--><!--Device-SoundPool-setVolume(streamID: int, leftVolume: double, rightVolume: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| leftVolume | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Volume of the left channel. The value range is [0.0, 1.0]. |
| rightVolume | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：double | Yes | Volume of the right channel. The value range is [0.0, 1.0]. Currently, setting the volume for the right channel does not take effect. The volume set for the left channel is used. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## stop

ArkTS-Dyn:
```TypeScript
stop(streamID: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
stop(streamID: int, callback: AsyncCallback<void>): void
```

Stops audio playback. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-stop(streamID: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-stop(streamID: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Audio stream ID, which is obtained by calling **play()**. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## stop

ArkTS-Dyn:
```TypeScript
stop(streamID: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
stop(streamID: int): Promise<void>
```

Stops audio playback. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-stop(streamID: int): Promise<void>--><!--Device-SoundPool-stop(streamID: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Audio stream ID, which is obtained by calling **play()**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

## unload

ArkTS-Dyn:
```TypeScript
unload(soundID: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
unload(soundID: int, callback: AsyncCallback<void>): void
```

Unloads a sound. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-unload(soundID: int, callback: AsyncCallback<void>): void--><!--Device-SoundPool-unload(soundID: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Sound ID, which is obtained by calling **load()**. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback function. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by callback. |
| [5400103](../../errorcode-media.md#5400103-io-error) | I/O error. Return by callback. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by callback. |

## unload

ArkTS-Dyn:
```TypeScript
unload(soundID: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
unload(soundID: int): Promise<void>
```

Unloads a sound. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-SoundPool-unload(soundID: int): Promise<void>--><!--Device-SoundPool-unload(soundID: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundID | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Sound ID, which is obtained by calling **load()**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5400102](../../errorcode-media.md#5400102-unsupported-operation) | Operation not allowed. Return by promise. |
| [5400103](../../errorcode-media.md#5400103-io-error) | I/O error. Return by promise. |
| [5400105](../../errorcode-media.md#5400105-play-service-dead) | Service died. Return by promise. |

