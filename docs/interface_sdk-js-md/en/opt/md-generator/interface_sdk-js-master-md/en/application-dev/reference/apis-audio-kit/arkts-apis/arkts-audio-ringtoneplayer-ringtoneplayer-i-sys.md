# RingtonePlayer (System API)

Provides APIs for setting and obtaining ringtone parameters as well as playing and stopping ringtones. Before calling any API in RingtonePlayer, you must use   
[getRingtonePlayer](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#getringtoneplayer)to obtain a RingtonePlayer instance.

**Since:** 10

<!--Device-unnamed-export interface RingtonePlayer--><!--Device-unnamed-export interface RingtonePlayer-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

## configure

```TypeScript
configure(options: RingtoneOptions, callback: AsyncCallback<void>): void
```

Sets ringtone parameters. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-RingtonePlayer-configure(options: RingtoneOptions, callback: AsyncCallback<void>): void--><!--Device-RingtonePlayer-configure(options: RingtoneOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RingtoneOptions](arkts-audio-systemsoundmanager-ringtoneoptions-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## configure

```TypeScript
configure(options: RingtoneOptions): Promise<void>
```

Sets ringtone parameters. This API uses a promise to return the result.

**Since:** 10

<!--Device-RingtonePlayer-configure(options: RingtoneOptions): Promise<void>--><!--Device-RingtonePlayer-configure(options: RingtoneOptions): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RingtoneOptions](arkts-audio-systemsoundmanager-ringtoneoptions-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## getAudioRendererInfo

```TypeScript
getAudioRendererInfo(callback: AsyncCallback<audio.AudioRendererInfo>): void
```

Obtains the information about the audio renderer used by the ringtone. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-RingtonePlayer-getAudioRendererInfo(callback: AsyncCallback<audio.AudioRendererInfo>): void--><!--Device-RingtonePlayer-getAudioRendererInfo(callback: AsyncCallback<audio.AudioRendererInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;audio.AudioRendererInfo&gt; | Yes |

## getAudioRendererInfo

```TypeScript
getAudioRendererInfo(): Promise<audio.AudioRendererInfo>
```

Obtains the information about the audio renderer used by the ringtone. This API uses a promise to return the result.

**Since:** 10

<!--Device-RingtonePlayer-getAudioRendererInfo(): Promise<audio.AudioRendererInfo>--><!--Device-RingtonePlayer-getAudioRendererInfo(): Promise<audio.AudioRendererInfo>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;audio.AudioRendererInfo&gt; |

## getTitle

```TypeScript
getTitle(callback: AsyncCallback<string>): void
```

Obtains the title of the ringtone. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-RingtonePlayer-getTitle(callback: AsyncCallback<string>): void--><!--Device-RingtonePlayer-getTitle(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getTitle

```TypeScript
getTitle(): Promise<string>
```

Obtains the title of the ringtone. This API uses a promise to return the result.

**Since:** 10

<!--Device-RingtonePlayer-getTitle(): Promise<string>--><!--Device-RingtonePlayer-getTitle(): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

## off('audioInterrupt')

```TypeScript
off(type: 'audioInterrupt'): void
```

Unsubscribes from the audio interruption event.

**Since:** 10

<!--Device-RingtonePlayer-off(type: 'audioInterrupt'): void--><!--Device-RingtonePlayer-off(type: 'audioInterrupt'): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioInterrupt' | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void
```

Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-RingtonePlayer-on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void--><!--Device-RingtonePlayer-on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioInterrupt' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;audio.InterruptEvent&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases the ringtone player. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-RingtonePlayer-release(callback: AsyncCallback<void>): void--><!--Device-RingtonePlayer-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## release

```TypeScript
release(): Promise<void>
```

Releases the ringtone player. This API uses a promise to return the result.

**Since:** 10

<!--Device-RingtonePlayer-release(): Promise<void>--><!--Device-RingtonePlayer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

Starts playing the ringtone. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-RingtonePlayer-start(callback: AsyncCallback<void>): void--><!--Device-RingtonePlayer-start(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## start

```TypeScript
start(): Promise<void>
```

Starts playing the ringtone. This API uses a promise to return the result.

**Since:** 10

<!--Device-RingtonePlayer-start(): Promise<void>--><!--Device-RingtonePlayer-start(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops playing the ringtone. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-RingtonePlayer-stop(callback: AsyncCallback<void>): void--><!--Device-RingtonePlayer-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## stop

```TypeScript
stop(): Promise<void>
```

Stops playing the ringtone. This API uses a promise to return the result.

**Since:** 10

<!--Device-RingtonePlayer-stop(): Promise<void>--><!--Device-RingtonePlayer-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## state

```TypeScript
readonly state: media.AVPlayerState
```

Gets player state.

**Type:** media.AVPlayerState

**Since:** 10

<!--Device-RingtonePlayer-readonly state: media.AVPlayerState--><!--Device-RingtonePlayer-readonly state: media.AVPlayerState-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.
