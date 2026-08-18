# AudioRecorder

AudioRecorder is a class for audio recording management. It provides APIs to record audio. Before calling any API in AudioRecorder, you must use [createAudioRecorder()](arkts-media-media-createaudiorecorder-f.md#createaudiorecorder) to create an AudioRecorder instance.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [media](arkts-multimedia-media.md#ohosmultimediamedia)

<!--Device-media-interface AudioRecorder--><!--Device-media-interface AudioRecorder-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## Modules to Import

```TypeScript
```

## on_error

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to audio recording error events. After an error event is reported, you must handle the event and exit the recording.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avrecorder-i.md#onaudiocapturerchange)(type: 'error', callback: ErrorCallback)

<!--Device-AudioRecorder-on(type: 'error', callback: ErrorCallback): void--><!--Device-AudioRecorder-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

## on_pause

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avrecorder-i.md#onaudiocapturerchange)(type: 'stateChange', callback: OnAVRecorderStateChangeHandler)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|
| callback | () = & gt; void | Yes |

## on_prepare

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avrecorder-i.md#onaudiocapturerchange)(type: 'stateChange', callback: OnAVRecorderStateChangeHandler)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|
| callback | () = & gt; void | Yes |

## on_release

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avrecorder-i.md#onaudiocapturerchange)(type: 'stateChange', callback: OnAVRecorderStateChangeHandler)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|
| callback | () = & gt; void | Yes |

## on_reset

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avrecorder-i.md#onaudiocapturerchange)(type: 'stateChange', callback: OnAVRecorderStateChangeHandler)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|
| callback | () = & gt; void | Yes |

## on_resume

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avrecorder-i.md#onaudiocapturerchange)(type: 'stateChange', callback: OnAVRecorderStateChangeHandler)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|
| callback | () = & gt; void | Yes |

## on_start

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avrecorder-i.md#onaudiocapturerchange)(type: 'stateChange', callback: OnAVRecorderStateChangeHandler)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|
| callback | () = & gt; void | Yes |

## on_stop

```TypeScript
on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void
```

Subscribes to the audio recording events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avrecorder-i.md#onaudiocapturerchange)(type: 'stateChange', callback: OnAVRecorderStateChangeHandler)

<!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void--><!--Device-AudioRecorder-on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'prepare' \| 'start' \| 'pause' \| 'resume' \| 'stop' \| 'release' \| 'reset' | Yes | Event type. The following events are supported: 'prepare'\|'start'\| 'pause' \| 'resume' \|'stop'\|'release'\|
| callback | () = & gt; void | Yes |

## pause

```TypeScript
pause(): void
```

Pauses audio recording. This API can be called only after the **'start'** event is triggered.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [pause](arkts-media-media-avrecorder-i.md#pause)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioRecorder-pause(): void--><!--Device-AudioRecorder-pause(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## prepare

```TypeScript
prepare(config: AudioRecorderConfig): void
```

Prepares for recording.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [prepare](arkts-media-media-avrecorder-i.md#prepare)(config: AVRecorderConfig, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.MICROPHONE

<!--Device-AudioRecorder-prepare(config: AudioRecorderConfig): void--><!--Device-AudioRecorder-prepare(config: AudioRecorderConfig): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [AudioRecorderConfig](arkts-media-media-audiorecorderconfig-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## release

```TypeScript
release(): void
```

Releases the audio recording resources.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [release](arkts-media-media-avrecorder-i.md#release)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioRecorder-release(): void--><!--Device-AudioRecorder-release(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## reset

```TypeScript
reset(): void
```

Resets audio recording. Before resetting audio recording, you must call **stop()** to stop recording. After audio recording is reset, you must call **prepare()** to set the recording configurations for another recording.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [reset](arkts-media-media-avrecorder-i.md#reset)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioRecorder-reset(): void--><!--Device-AudioRecorder-reset(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## resume

```TypeScript
resume(): void
```

Resumes audio recording. This API can be called only after the **'pause'** event is triggered.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [resume](arkts-media-media-avrecorder-i.md#resume)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioRecorder-resume(): void--><!--Device-AudioRecorder-resume(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## start

```TypeScript
start(): void
```

Starts audio recording. This API can be called only after the **'prepare'** event is triggered.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [start](arkts-media-media-avrecorder-i.md#start)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioRecorder-start(): void--><!--Device-AudioRecorder-start(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

## stop

```TypeScript
stop(): void
```

Stops audio recording.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [stop](arkts-media-media-avrecorder-i.md#stop)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioRecorder-stop(): void--><!--Device-AudioRecorder-stop(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder
