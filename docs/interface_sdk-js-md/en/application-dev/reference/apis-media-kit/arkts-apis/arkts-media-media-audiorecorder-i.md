# AudioRecorder

AudioRecorder is a class for audio recording management. It provides APIs to record audio. Before calling any API in AudioRecorder, you must use [createAudioRecorder()](arkts-media-media-createaudiorecorder-f.md#createAudioRecorder) to create an AudioRecorder instance.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [media](arkts-multimedia-media.md#media)

<!--Device-media-interface AudioRecorder--><!--Device-media-interface AudioRecorder-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## on('prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset')

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [on](@ohos.multimedia.media:media.AVRecorder.on(type:)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|'reset'&lt;br&gt;- ' prepare': triggered when the **prepare()** API is called and the audio recording parameters are set.&lt;br&gt;- ' start': triggered when the **start()** API is called and audio recording starts.&lt;br&gt;- 'pause': triggered when the **pause()** API is called and audio recording is paused.&lt;br&gt;- 'resume': triggered when the **resume()** API is called and audio recording is resumed.&lt;br&gt;- 'stop': triggered when the **stop()** API is called and audio recording stops.&lt;br&gt;- 'release': triggered when the **release()** API is called and the recording resources are released.&lt;br&gt;- 'reset': triggered when the **reset()** API is called and audio recording is reset. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset')

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [on](@ohos.multimedia.media:media.AVRecorder.on(type:)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|'reset'&lt;br&gt;- ' prepare': triggered when the **prepare()** API is called and the audio recording parameters are set.&lt;br&gt;- ' start': triggered when the **start()** API is called and audio recording starts.&lt;br&gt;- 'pause': triggered when the **pause()** API is called and audio recording is paused.&lt;br&gt;- 'resume': triggered when the **resume()** API is called and audio recording is resumed.&lt;br&gt;- 'stop': triggered when the **stop()** API is called and audio recording stops.&lt;br&gt;- 'release': triggered when the **release()** API is called and the recording resources are released.&lt;br&gt;- 'reset': triggered when the **reset()** API is called and audio recording is reset. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset')

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [on](@ohos.multimedia.media:media.AVRecorder.on(type:)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|'reset'&lt;br&gt;- ' prepare': triggered when the **prepare()** API is called and the audio recording parameters are set.&lt;br&gt;- ' start': triggered when the **start()** API is called and audio recording starts.&lt;br&gt;- 'pause': triggered when the **pause()** API is called and audio recording is paused.&lt;br&gt;- 'resume': triggered when the **resume()** API is called and audio recording is resumed.&lt;br&gt;- 'stop': triggered when the **stop()** API is called and audio recording stops.&lt;br&gt;- 'release': triggered when the **release()** API is called and the recording resources are released.&lt;br&gt;- 'reset': triggered when the **reset()** API is called and audio recording is reset. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset')

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [on](@ohos.multimedia.media:media.AVRecorder.on(type:)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|'reset'&lt;br&gt;- ' prepare': triggered when the **prepare()** API is called and the audio recording parameters are set.&lt;br&gt;- ' start': triggered when the **start()** API is called and audio recording starts.&lt;br&gt;- 'pause': triggered when the **pause()** API is called and audio recording is paused.&lt;br&gt;- 'resume': triggered when the **resume()** API is called and audio recording is resumed.&lt;br&gt;- 'stop': triggered when the **stop()** API is called and audio recording stops.&lt;br&gt;- 'release': triggered when the **release()** API is called and the recording resources are released.&lt;br&gt;- 'reset': triggered when the **reset()** API is called and audio recording is reset. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset')

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [on](@ohos.multimedia.media:media.AVRecorder.on(type:)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|'reset'&lt;br&gt;- ' prepare': triggered when the **prepare()** API is called and the audio recording parameters are set.&lt;br&gt;- ' start': triggered when the **start()** API is called and audio recording starts.&lt;br&gt;- 'pause': triggered when the **pause()** API is called and audio recording is paused.&lt;br&gt;- 'resume': triggered when the **resume()** API is called and audio recording is resumed.&lt;br&gt;- 'stop': triggered when the **stop()** API is called and audio recording stops.&lt;br&gt;- 'release': triggered when the **release()** API is called and the recording resources are released.&lt;br&gt;- 'reset': triggered when the **reset()** API is called and audio recording is reset. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset')

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [on](@ohos.multimedia.media:media.AVRecorder.on(type:)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|'reset'&lt;br&gt;- ' prepare': triggered when the **prepare()** API is called and the audio recording parameters are set.&lt;br&gt;- ' start': triggered when the **start()** API is called and audio recording starts.&lt;br&gt;- 'pause': triggered when the **pause()** API is called and audio recording is paused.&lt;br&gt;- 'resume': triggered when the **resume()** API is called and audio recording is resumed.&lt;br&gt;- 'stop': triggered when the **stop()** API is called and audio recording stops.&lt;br&gt;- 'release': triggered when the **release()** API is called and the recording resources are released.&lt;br&gt;- 'reset': triggered when the **reset()** API is called and audio recording is reset. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset')

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [on](@ohos.multimedia.media:media.AVRecorder.on(type:)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|'reset'&lt;br&gt;- ' prepare': triggered when the **prepare()** API is called and the audio recording parameters are set.&lt;br&gt;- ' start': triggered when the **start()** API is called and audio recording starts.&lt;br&gt;- 'pause': triggered when the **pause()** API is called and audio recording is paused.&lt;br&gt;- 'resume': triggered when the **resume()** API is called and audio recording is resumed.&lt;br&gt;- 'stop': triggered when the **stop()** API is called and audio recording stops.&lt;br&gt;- 'release': triggered when the **release()** API is called and the recording resources are released.&lt;br&gt;- 'reset': triggered when the **reset()** API is called and audio recording is reset. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to audio recording error events. After an error event is reported, you must handle the event and exit the recording.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [on](@ohos.multimedia.media:media.AVRecorder.on(type:)

<!--Device-AudioRecorder-on(type: 'error', callback: ErrorCallback): void--><!--Device-AudioRecorder-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type, which is **'error'** in this case.&lt;br&gt;This event is triggered when an error occurs during audio recording. |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-errorcallback-t.md) | Yes | Callback invoked when the event is triggered. |

## pause

```TypeScript
pause(): void
```

Pauses audio recording. This API can be called only after the **'start'** event is triggered.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [pause](@ohos.multimedia.media:media.AVRecorder.pause(callback:)

<!--Device-AudioRecorder-pause(): void--><!--Device-AudioRecorder-pause(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## prepare

```TypeScript
prepare(config: AudioRecorderConfig): void
```

Prepares for recording.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [prepare](@ohos.multimedia.media:media.AVRecorder.prepare(config:)

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-AudioRecorder-prepare(config: AudioRecorderConfig): void--><!--Device-AudioRecorder-prepare(config: AudioRecorderConfig): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [AudioRecorderConfig](arkts-media-media-audiorecorderconfig-i.md) | Yes | Audio recording parameters, including the audio output URI, encoding format, sample rate, audio channel count, and output format. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | permission denied.<br>**Applicable version:** 12 and later |

## release

```TypeScript
release(): void
```

Releases the audio recording resources.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [release](@ohos.multimedia.media:media.AVRecorder.release(callback:)

<!--Device-AudioRecorder-release(): void--><!--Device-AudioRecorder-release(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## reset

```TypeScript
reset(): void
```

Resets audio recording.

Before resetting audio recording, you must call **stop()** to stop recording. After audio recording is reset, you must call **prepare()** to set the recording configurations for another recording.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [reset](@ohos.multimedia.media:media.AVRecorder.reset(callback:)

<!--Device-AudioRecorder-reset(): void--><!--Device-AudioRecorder-reset(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## resume

```TypeScript
resume(): void
```

Resumes audio recording. This API can be called only after the **'pause'** event is triggered.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [resume](@ohos.multimedia.media:media.AVRecorder.resume(callback:)

<!--Device-AudioRecorder-resume(): void--><!--Device-AudioRecorder-resume(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## start

```TypeScript
start(): void
```

Starts audio recording. This API can be called only after the **'prepare'** event is triggered.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [start](@ohos.multimedia.media:media.AVRecorder.start(callback:)

<!--Device-AudioRecorder-start(): void--><!--Device-AudioRecorder-start(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## stop

```TypeScript
stop(): void
```

Stops audio recording.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [stop](@ohos.multimedia.media:media.AVRecorder.stop(callback:)

<!--Device-AudioRecorder-stop(): void--><!--Device-AudioRecorder-stop(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

