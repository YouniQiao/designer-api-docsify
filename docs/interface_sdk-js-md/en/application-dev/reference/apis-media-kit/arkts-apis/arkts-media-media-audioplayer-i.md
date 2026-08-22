# AudioPlayer

AudioPlayer is a class for audio playback management. It provides APIs to manage and play audio. Before calling any API in AudioPlayer, you must use [createAudioPlayer()](arkts-media-media-createaudioplayer-f.md) to create an AudioPlayer instance.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [media](arkts-multimedia-media.md)

<!--Device-media-interface AudioPlayer--><!--Device-media-interface AudioPlayer-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## getTrackDescription

```TypeScript
getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void
```

Obtains the audio track information. It can be called only after the **'dataLoad'** event is triggered. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)(callback: AsyncCallback&lt;Array&lt;MediaDescription&gt;&gt;)

<!--Device-AudioPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void--><!--Device-AudioPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MediaDescription](arkts-media-media-mediadescription-i.md)&gt;&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the MediaDescription array obtained; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
  if (arrList != null) {
    console.info('Succeeded in getting TrackDescription');
  } else {
    console.error(`Failed to get TrackDescription, error:${error}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

audioPlayer.getTrackDescription().then((arrList: Array<media.MediaDescription>) => {
  console.info('Succeeded in getting TrackDescription');
}).catch((error: BusinessError) => {
  console.error(`Failed to get TrackDescription, error:${error}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the prepared, playing, or paused state before proceeding.
  avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
    if ((arrList) != null) {
      console.info('Succeeded in doing getTrackDescription');
    } else {
      console.error(`Failed to do getTrackDescription, error:${error}`);
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the prepared, playing, or paused state before proceeding.
  avPlayer.getTrackDescription().then((arrList: Array<media.MediaDescription>) => {
    console.info('Succeeded in getting TrackDescription');
  }).catch((error: BusinessError) => {
    console.error(`Failed to get TrackDescription, error:${error}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
  if ((arrList) != null) {
    console.info('Succeeded in getting TrackDescription');
  } else {
    console.error(`Failed to get TrackDescription, error:${error}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.getTrackDescription().then((arrList: Array<media.MediaDescription>) => {
  if (arrList != null) {
    console.info('Succeeded in getting TrackDescription');
  } else {
    console.error('Failed to get TrackDescription');
  }
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## getTrackDescription

```TypeScript
getTrackDescription(): Promise<Array<MediaDescription>>
```

Obtains the audio track information. It can be called only after the **'dataLoad'** event is triggered. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)()

<!--Device-AudioPlayer-getTrackDescription(): Promise<Array<MediaDescription>>--><!--Device-AudioPlayer-getTrackDescription(): Promise<Array<MediaDescription>>-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[MediaDescription](arkts-media-media-mediadescription-i.md)&gt;&gt; | Promise used to return a **MediaDescription** array, which records the audio track information. |

**Examples**

See [getTrackDescription](#gettrackdescription)

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void
```

Subscribes to the audio interruption event. For details, see [audio.InterruptEvent](../../apis-audio-kit/arkts-apis/arkts-audio-audio-interruptevent-i.md).

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'audioInterrupt', callback: Callback&lt;audio.InterruptEvent&gt;)

<!--Device-AudioPlayer-on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void--><!--Device-AudioPlayer-on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | Yes | Event type, which is **'audioInterrupt'** in this case. |
| callback | (info: audio.InterruptEvent) =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('bufferingUpdate')

```TypeScript
on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void
```

Subscribes to the audio buffering update event. This API works only under online playback.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler)

<!--Device-AudioPlayer-on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void--><!--Device-AudioPlayer-on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'bufferingUpdate' | Yes | Event type, which is **'bufferingUpdate'** in this case. |
| callback | (infoType: BufferingInfoType, value: number) =&gt; void | Yes | Callback invoked when the event is triggered.<br>The value of [BufferingInfoType](arkts-media-media-bufferinginfotype-e.md) is fixed at **0**. |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes | Event type. The following events are supported:<br>- 'play': triggered when the [play()](#play) API is called and audio playback starts.<br>- 'pause': triggered when the [pause()](#pause) API is called and audio playback is paused.<br>- 'stop': triggered when the [stop()](#stop) API is called and audio playback stops.<br>- 'reset': triggered when the [reset()](#reset) API is called and audio playback is reset.<br>- 'dataLoad': triggered when the audio data is loaded, that is, when the **src** property is configured.<br>- 'finish': triggered when the audio playback is finished.<br>- 'volumeChange': triggered when the [setVolume()](#setvolume) API is called and the playback volume is changed. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to audio playback error events. After an error event is reported, you must handle the event and exit the playback.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'error', callback: ErrorCallback)

<!--Device-AudioPlayer-on(type: 'error', callback: ErrorCallback): void--><!--Device-AudioPlayer-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type, which is **'error'** in this case.<br>This event is triggered when an error occurs during audio playback. |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback invoked when the event is triggered. |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes | Event type. The following events are supported:<br>- 'play': triggered when the [play()](#play) API is called and audio playback starts.<br>- 'pause': triggered when the [pause()](#pause) API is called and audio playback is paused.<br>- 'stop': triggered when the [stop()](#stop) API is called and audio playback stops.<br>- 'reset': triggered when the [reset()](#reset) API is called and audio playback is reset.<br>- 'dataLoad': triggered when the audio data is loaded, that is, when the **src** property is configured.<br>- 'finish': triggered when the audio playback is finished.<br>- 'volumeChange': triggered when the [setVolume()](#setvolume) API is called and the playback volume is changed. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes | Event type. The following events are supported:<br>- 'play': triggered when the [play()](#play) API is called and audio playback starts.<br>- 'pause': triggered when the [pause()](#pause) API is called and audio playback is paused.<br>- 'stop': triggered when the [stop()](#stop) API is called and audio playback stops.<br>- 'reset': triggered when the [reset()](#reset) API is called and audio playback is reset.<br>- 'dataLoad': triggered when the audio data is loaded, that is, when the **src** property is configured.<br>- 'finish': triggered when the audio playback is finished.<br>- 'volumeChange': triggered when the [setVolume()](#setvolume) API is called and the playback volume is changed. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes | Event type. The following events are supported:<br>- 'play': triggered when the [play()](#play) API is called and audio playback starts.<br>- 'pause': triggered when the [pause()](#pause) API is called and audio playback is paused.<br>- 'stop': triggered when the [stop()](#stop) API is called and audio playback stops.<br>- 'reset': triggered when the [reset()](#reset) API is called and audio playback is reset.<br>- 'dataLoad': triggered when the audio data is loaded, that is, when the **src** property is configured.<br>- 'finish': triggered when the audio playback is finished.<br>- 'volumeChange': triggered when the [setVolume()](#setvolume) API is called and the playback volume is changed. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes | Event type. The following events are supported:<br>- 'play': triggered when the [play()](#play) API is called and audio playback starts.<br>- 'pause': triggered when the [pause()](#pause) API is called and audio playback is paused.<br>- 'stop': triggered when the [stop()](#stop) API is called and audio playback stops.<br>- 'reset': triggered when the [reset()](#reset) API is called and audio playback is reset.<br>- 'dataLoad': triggered when the audio data is loaded, that is, when the **src** property is configured.<br>- 'finish': triggered when the audio playback is finished.<br>- 'volumeChange': triggered when the [setVolume()](#setvolume) API is called and the playback volume is changed. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes | Event type. The following events are supported:<br>- 'play': triggered when the [play()](#play) API is called and audio playback starts.<br>- 'pause': triggered when the [pause()](#pause) API is called and audio playback is paused.<br>- 'stop': triggered when the [stop()](#stop) API is called and audio playback stops.<br>- 'reset': triggered when the [reset()](#reset) API is called and audio playback is reset.<br>- 'dataLoad': triggered when the audio data is loaded, that is, when the **src** property is configured.<br>- 'finish': triggered when the audio playback is finished.<br>- 'volumeChange': triggered when the [setVolume()](#setvolume) API is called and the playback volume is changed. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('timeUpdate')

```TypeScript
on(type: 'timeUpdate', callback: Callback<number>): void
```

Subscribes to the **'timeUpdate'** event. This event is reported every second when the audio playback is in progress.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'timeUpdate', callback: Callback&lt;int&gt;)

<!--Device-AudioPlayer-on(type: 'timeUpdate', callback: Callback<number>): void--><!--Device-AudioPlayer-on(type: 'timeUpdate', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'timeUpdate' | Yes | Event type, which is **'timeUpdate'** in this case.<br>The **'timeUpdate'** event is triggered when the audio playback starts after an audio playback timestamp update. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes | Callback invoked when the event is triggered. The input parameter is the updated timestamp. |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

Subscribes to the audio playback events.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | Yes | Event type. The following events are supported:<br>- 'play': triggered when the [play()](#play) API is called and audio playback starts.<br>- 'pause': triggered when the [pause()](#pause) API is called and audio playback is paused.<br>- 'stop': triggered when the [stop()](#stop) API is called and audio playback stops.<br>- 'reset': triggered when the [reset()](#reset) API is called and audio playback is reset.<br>- 'dataLoad': triggered when the audio data is loaded, that is, when the **src** property is configured.<br>- 'finish': triggered when the audio playback is finished.<br>- 'volumeChange': triggered when the [setVolume()](#setvolume) API is called and the playback volume is changed. |
| callback | () =&gt; void | Yes | Callback invoked when the event is triggered. |

## pause

```TypeScript
pause(): void
```

Pauses audio playback.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [pause](arkts-media-media-avplayer-i.md#pause)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioPlayer-pause(): void--><!--Device-AudioPlayer-pause(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.pause((err: BusinessError) => {
  if (err == null) {
    console.info('pause videorecorder success');
  } else {
    console.error('pause videorecorder failed and error is ' + err.message);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.pause().then(() => {
  console.info('pause videorecorder success');
}).catch((err: BusinessError) => {
  console.error('pause videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioPlayer.on('pause', () => {    // Set the 'pause' event callback.
  console.info('audio pause called');
});
audioPlayer.pause();
```

```TypeScript
audioRecorder.on('pause', () => {    // Set the 'pause' event callback.
  console.info('audio recorder pause called');
});
audioRecorder.pause();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the playing state before proceeding.
  avPlayer.pause((err: BusinessError) => {
    if (err) {
      console.error('Failed to pause,error message is :' + err.message);
    } else {
      console.info('Succeeded in pausing');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the playing state before proceeding.
  avPlayer.pause().then(() => {
    console.info('Succeeded in pausing');
  }, (err: BusinessError) => {
    console.error('Failed to pause,error message is :' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.pause((err: BusinessError) => {
  if (err) {
    console.error(`Failed to pause AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in pausing');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.pause().then(() => {
  console.info('Succeeded in pausing');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to pause AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVTranscoder instance.
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.pause().then(() => {
    console.info('pause AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('pause AVTranscoder failed and catch error is ' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.pause((err: BusinessError) => {
  if (err) {
    console.error('Failed to pause!');
  } else {
    console.info('Succeeded in pausing!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.pause().then(() => {
  console.info('Succeeded in pausing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## play

```TypeScript
play(): void
```

Starts to play an audio asset. This API can be called only after the **'dataLoad'** event is triggered.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [play](arkts-media-media-avplayer-i.md#play)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioPlayer-play(): void--><!--Device-AudioPlayer-play(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Examples**

```TypeScript
audioPlayer.on('play', () => {    // Set the 'play' event callback.
  console.info('audio play called');
});
audioPlayer.play();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the prepared, paused, or completed state before proceeding.
  avPlayer.play((err: BusinessError) => {
    if (err) {
      console.error('Failed to play,error message is :' + err.message);
    } else {
      console.info('Succeeded in playing');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the prepared, paused, or completed state before proceeding.
  avPlayer.play().then(() => {
    console.info('Succeeded in playing');
  }, (err: BusinessError) => {
    console.error('Failed to play,error message is :' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.play((err: BusinessError) => {
  if (err) {
    console.error('Failed to play!');
  } else {
    console.info('Succeeded in playing!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.play().then(() => {
  console.info('Succeeded in playing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## release

```TypeScript
release(): void
```

Releases the audio playback resources.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [release](arkts-media-media-avplayer-i.md#release)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioPlayer-release(): void--><!--Device-AudioPlayer-release(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.release((err: BusinessError) => {
  if (err == null) {
    console.info('release videorecorder success');
  } else {
    console.error('release videorecorder failed and error is ' + err.message);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.release().then(() => {
  console.info('release videorecorder success');
}).catch((err: BusinessError) => {
  console.error('release videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioPlayer.release();
audioPlayer = undefined;
```

```TypeScript
audioRecorder.on('release', () => {    // Set the 'release' event callback.
  console.info('audio recorder release called');
});
audioRecorder.release();
audioRecorder = undefined;
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;

// Release the resources.
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator != null) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.release((error: BusinessError) => {
      if (error) {
        console.error(`Failed to release, err = ${JSON.stringify(error)}`);
        return;
      }
      console.info(`Succeeded in releasing`);
    });
  } else {
    console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;

// Release the resources.
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator != null) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.release().then(() => {
      console.info(`Succeeded in releasing.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to release, error message:${error.message}`);
    });
  } else {
    console.error(`Failed to create AVImageGenerator, error message:${err.message}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVMetadataExtractor instance.
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.release((error: BusinessError) => {
    if (error) {
      console.error(`Failed to release, err = ${JSON.stringify(error)}`);
      return;
    }
    console.info(`Succeeded in releasing.`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVMetadataExtractor instance.
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.release().then(() => {
    console.info(`Succeeded in releasing.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to release, error message:${error.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach a state other than released before proceeding.
  avPlayer.release((err: BusinessError) => {
    if (err) {
      console.error('Failed to release,error message is :' + err.message);
    } else {
      console.info('Succeeded in releasing');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach a state other than released before proceeding.
  avPlayer.release().then(() => {
    console.info('Succeeded in releasing');
  }, (err: BusinessError) => {
    console.error('Failed to release,error message is :' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.release((err: BusinessError) => {
  if (err) {
    console.error(`Failed to release AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in releasing AVRecorder');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.release().then(() => {
  console.info('Succeeded in releasing AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to release AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
});

// Other processes.

// Call the release method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.release().then(() => {
    console.info('Succeeded in releasing avScreenCaptureRecorder');
  }).catch((err: BusinessError) => {
    console.error(`Failed to release avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVTranscoder instance.
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.release().then(() => {
    console.info('release AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('release AVTranscoder failed and catch error is ' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release((err: BusinessError) => {
  if (err) {
    console.error('Failed to release!');
  } else {
    console.info('Succeeded in releasing!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release().then(() => {
  console.info('Succeeded in releasing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## reset

```TypeScript
reset(): void
```

Resets the audio asset to be played.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [reset](arkts-media-media-avplayer-i.md#reset)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioPlayer-reset(): void--><!--Device-AudioPlayer-reset(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.reset((err: BusinessError) => {
  if (err == null) {
    console.info('reset videorecorder success');
  } else {
    console.error('reset videorecorder failed and error is ' + err.message);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.reset().then(() => {
  console.info('reset videorecorder success');
}).catch((err: BusinessError) => {
  console.error('reset videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioPlayer.on('reset', () => {    // Set the 'reset' event callback.
  console.info('audio reset called');
});
audioPlayer.reset();
```

```TypeScript
audioRecorder.on('reset', () => {    // Set the 'reset' event callback.
  console.info('audio recorder reset called');
});
audioRecorder.reset();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the initialized, prepared, playing, paused, completed, stopped, or error state before proceeding.
  avPlayer.reset((err: BusinessError) => {
    if (err) {
      console.error('Failed to reset,error message is :' + err.message);
    } else {
      console.info('Succeeded in resetting');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the initialized, prepared, playing, paused, completed, stopped, or error state before proceeding.
  avPlayer.reset().then(() => {
    console.info('Succeeded in resetting');
  }, (err: BusinessError) => {
    console.error('Failed to reset,error message is :' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.reset((err: BusinessError) => {
  if (err) {
    console.error(`Failed to reset AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in resetting AVRecorder');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.reset().then(() => {
  console.info('Succeeded in resetting AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to reset AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.reset((err: BusinessError) => {
  if (err) {
    console.error('Failed to reset!');
  } else {
    console.info('Succeeded in resetting!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.reset().then(() => {
  console.info('Succeeded in resetting');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## seek

```TypeScript
seek(timeMs: number): void
```

Seeks to the specified playback position.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [seek](arkts-media-media-avplayer-i.md#seek)

<!--Device-AudioPlayer-seek(timeMs: number): void--><!--Device-AudioPlayer-seek(timeMs: number): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeMs | number | Yes | Position to seek to, in ms. The value range is [0, duration]. |

**Examples**

```TypeScript
audioPlayer.on('timeUpdate', (seekDoneTime: number) => {    // Set the 'timeUpdate' event callback.
  if (seekDoneTime == null) {
    console.error('Failed to seek');
    return;
  }
  console.info('Succeeded in seek. seekDoneTime: ' + seekDoneTime);
});
audioPlayer.seek(30000); // Seek to 30000 ms.
```

```TypeScript
async function  test(){
  let avPlayer = await media.createAVPlayer();
  let seekTime: number = 1000;
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the prepared, playing, paused, or completed state before proceeding.
  avPlayer.seek(seekTime, media.SeekMode.SEEK_PREV_SYNC);
}
```

```TypeScript
async function  test(){
  // Use SEEK_CONTINUOUS with the onChange callback of the Slider. When slideMode is Moving, it triggers continuous seeking during the drag.
  let avPlayer = await media.createAVPlayer();
  let slideMovingTime: number = 2000;
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the prepared, playing, paused, or completed state before proceeding.
  avPlayer.seek(slideMovingTime, media.SeekMode.SEEK_CONTINUOUS);

  // To end the seek when slideMode is End, call seek(-1, media.SeekMode.SEEK_CONTINUOUS).
  avPlayer.seek(-1, media.SeekMode.SEEK_CONTINUOUS);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});

let seekTime: number = 5000;
videoPlayer.seek(seekTime, (err: BusinessError, result: number) => {
  if (err) {
    console.error('Failed to do seek!');
  } else {
    console.info('Succeeded in doing seek!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});
let seekTime: number = 5000;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).seek(seekTime, media.SeekMode.SEEK_NEXT_SYNC, (err: BusinessError, result: number) => {
    if (err) {
      console.error('Failed to do seek!');
    } else {
      console.info('Succeeded in doing seek!');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});
let seekTime: number = 5000;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).seek(seekTime).then((seekDoneTime: number) => { // seekDoneTime indicates the position after the seek operation is complete.
    console.info('Succeeded in doing seek');
  }).catch((error: BusinessError) => {
    console.error(`video catchCallback, error:${error}`);
  });

  (videoPlayer as media.VideoPlayer).seek(seekTime, media.SeekMode.SEEK_NEXT_SYNC).then((seekDoneTime: number) => {
    console.info('Succeeded in doing seek');
  }).catch((error: BusinessError) => {
    console.error(`video catchCallback, error:${error}`);
  });
}
```

## setVolume

```TypeScript
setVolume(vol: number): void
```

Sets the volume.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [setVolume](arkts-media-media-avplayer-i.md#setvolume)

<!--Device-AudioPlayer-setVolume(vol: number): void--><!--Device-AudioPlayer-setVolume(vol: number): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| vol | number | Yes | Relative volume. The value ranges from 0.00 to 1.00. The value **1.00** indicates the maximum volume (100%). |

**Examples**

```TypeScript
audioPlayer.on('volumeChange', () => {    // Set the 'volumeChange' event callback.
  console.info('audio volumeChange called');
});
audioPlayer.setVolume(1);    // Set the volume to 100%.
```

```TypeScript
async function test(){
  let avPlayer = await media.createAVPlayer();
  let volume: number = 1.0;
  avPlayer.setVolume(volume);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let vol: number = 0.5;
videoPlayer.setVolume(vol, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set Volume!');
  } else {
    console.info('Succeeded in setting Volume!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let vol: number = 0.5;
videoPlayer.setVolume(vol).then(() => {
  console.info('Succeeded in setting Volume');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## stop

```TypeScript
stop(): void
```

Stops audio playback.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [stop](arkts-media-media-avplayer-i.md#stop)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioPlayer-stop(): void--><!--Device-AudioPlayer-stop(): void-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// asyncallback.
videoRecorder.stop((err: BusinessError) => {
  if (err == null) {
    console.info('stop videorecorder success');
  } else {
    console.error('stop videorecorder failed and error is ' + err.message);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// promise.
videoRecorder.stop().then(() => {
  console.info('stop videorecorder success');
}).catch((err: BusinessError) => {
  console.error('stop videorecorder failed and catch error is ' + err.message);
});
```

```TypeScript
audioPlayer.on('stop', () => {    // Set the 'stop' event callback.
  console.info('audio stop called');
});
audioPlayer.stop();
```

```TypeScript
audioRecorder.on('stop', () => {    // Set the 'stop' event callback.
  console.info('audio recorder stop called');
});
audioRecorder.stop();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the prepared, playing, paused, or completed state before proceeding.
  avPlayer.stop((err: BusinessError) => {
    if (err) {
      console.error('Failed to stop,error message is :' + err.message);
    } else {
      console.info('Succeeded in stopping');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the prepared, playing, paused, or completed state before proceeding.
  avPlayer.stop().then(() => {
    console.info('Succeeded in stopping');
  }, (err: BusinessError) => {
    console.error('Failed to stop,error message is :' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.stop((err: BusinessError) => {
  if (err) {
    console.error(`Failed to stop AVRecorder and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in stopping AVRecorder');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.stop().then(() => {
  console.info('Succeeded in stopping AVRecorder');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to stop AVRecorder and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.stop((err: BusinessError) => {
  if (err) {
    console.error('Failed to stop!');
  } else {
    console.info('Succeeded in stopping!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.stop().then(() => {
  console.info('Succeeded in stopping');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## audioInterruptMode

```TypeScript
audioInterruptMode?: audio.InterruptMode
```

Audio interruption mode.

**Type:** audio.InterruptMode

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [audioInterruptMode](arkts-media-media-avplayer-i.md#audiointerruptmode)

<!--Device-AudioPlayer-audioInterruptMode?: audio.InterruptMode--><!--Device-AudioPlayer-audioInterruptMode?: audio.InterruptMode-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## currentTime

```TypeScript
readonly currentTime: number
```

Current audio playback position, in ms.

**Type:** number

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [currentTime](arkts-media-media-avplayer-i.md#currenttime)

<!--Device-AudioPlayer-readonly currentTime: number--><!--Device-AudioPlayer-readonly currentTime: number-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## duration

```TypeScript
readonly duration: number
```

Audio duration, in ms.

**Type:** number

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [duration](arkts-media-media-avplayer-i.md#duration)

<!--Device-AudioPlayer-readonly duration: number--><!--Device-AudioPlayer-readonly duration: number-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## fdSrc

```TypeScript
fdSrc: AVFileDescriptor
```

Description of the audio file. This property is required when audio assets of an application are continuously stored in a file.

Assume that a music file that stores continuous music assets consists of the following:

Music 1 (address offset: 0, byte length: 100)

Music 2 (address offset: 101; byte length: 50)

Music 3 (address offset: 151, byte length: 150)

1. To play music 1: AVFileDescriptor { fd = resource handle; offset = 0; length = 100; } 2. To play music 2: AVFileDescriptor { fd = resource handle; offset = 101; length = 50; } 3. To play music 3: AVFileDescriptor { fd = resource handle; offset = 151; length = 150; }

To play an independent music file, use **src=fd://xx**.

**Type:** [AVFileDescriptor](arkts-media-media-avfiledescriptor-i.md)

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [fdSrc](arkts-media-media-avplayer-i.md#fdsrc)

<!--Device-AudioPlayer-fdSrc: AVFileDescriptor--><!--Device-AudioPlayer-fdSrc: AVFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## loop

```TypeScript
loop: boolean
```

Whether to loop audio playback. **true** to loop, **false** otherwise.

**Type:** boolean

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [loop](arkts-media-media-avplayer-i.md#loop)

<!--Device-AudioPlayer-loop: boolean--><!--Device-AudioPlayer-loop: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## src

```TypeScript
src: string
```

Audio file URI. The mainstream audio formats (M4A, AAC, MP3, OGG, WAV, and AMR) are supported.

**Example of supported URLs**:

1. FD: fd://xx



2. HTTP: http://xx 3. HTTPS: https://xx 4. HLS: http://xx or https://xx

ohos.permission.READ_MEDIA or ohos.permission.INTERNET

**Type:** string

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [url](arkts-media-media-avplayer-i.md#url)

**Required permissions:** ohos.permission.READ_MEDIA or ohos.permission.INTERNET

<!--Device-AudioPlayer-src: string--><!--Device-AudioPlayer-src: string-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

## state

```TypeScript
readonly state: AudioState
```

Audio playback state. This state cannot be used as the condition for triggering the call of **play()**, **pause()**, or **stop()**.

**Type:** AudioState

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [state](arkts-media-media-avplayer-i.md#state)

<!--Device-AudioPlayer-readonly state: AudioState--><!--Device-AudioPlayer-readonly state: AudioState-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

