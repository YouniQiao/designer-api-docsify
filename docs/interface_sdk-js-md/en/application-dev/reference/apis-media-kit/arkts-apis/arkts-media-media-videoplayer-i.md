# VideoPlayer

VideoPlayer is a class for video playback management. It provides APIs to manage and play videos. Before calling any API in VideoPlayer, you must use [createVideoPlayer()](arkts-media-media-createvideoplayer-f.md) to create a VideoPlayer instance.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [media](arkts-multimedia-media.md)

<!--Device-media-interface VideoPlayer--><!--Device-media-interface VideoPlayer-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## getTrackDescription

```TypeScript
getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void
```

Obtains the video track information. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)(callback: AsyncCallback&lt;Array&lt;MediaDescription&gt;&gt;)

<!--Device-VideoPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void--><!--Device-VideoPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

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

Obtains the video track information. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)()

<!--Device-VideoPlayer-getTrackDescription(): Promise<Array<MediaDescription>>--><!--Device-VideoPlayer-getTrackDescription(): Promise<Array<MediaDescription>>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[MediaDescription](arkts-media-media-mediadescription-i.md)&gt;&gt; | Promise used to return the MediaDescription array that holds the video track information. |

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

<!--Device-VideoPlayer-on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void--><!--Device-VideoPlayer-on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | Yes | Event type, which is **'audioInterrupt'** in this case. |
| callback | (info: audio.InterruptEvent) =&gt; void | Yes | Callback invoked when the event is triggered. |

## on('bufferingUpdate')

```TypeScript
on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void
```

Subscribes to the video buffering update event. This API works only under online playback.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler)

<!--Device-VideoPlayer-on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void--><!--Device-VideoPlayer-on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'bufferingUpdate' | Yes | Event type, which is **'bufferingUpdate'** in this case. |
| callback | (infoType: BufferingInfoType, value: number) =&gt; void | Yes | Callback invoked when the event is triggered.<br>The value of [BufferingInfoType](arkts-media-media-bufferinginfotype-e.md) is fixed at **0**. |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to video playback error events. After an error event is reported, you must handle the event and exit the playback.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'error', callback: ErrorCallback)

<!--Device-VideoPlayer-on(type: 'error', callback: ErrorCallback): void--><!--Device-VideoPlayer-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type, which is **'error'** in this case.<br>This event is triggered when an error occurs during video playback. |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Callback invoked when the event is triggered. |

## on('playbackCompleted')

```TypeScript
on(type: 'playbackCompleted', callback: Callback<void>): void
```

Subscribes to the video playback completion event.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-VideoPlayer-on(type: 'playbackCompleted', callback: Callback<void>): void--><!--Device-VideoPlayer-on(type: 'playbackCompleted', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'playbackCompleted' | Yes | Event type, which is **'playbackCompleted'** in this case. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback invoked when the event is triggered. |

## on('startRenderFrame')

```TypeScript
on(type: 'startRenderFrame', callback: Callback<void>): void
```

Subscribes to the frame rendering start event.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'startRenderFrame', callback: Callback&lt;void&gt;)

<!--Device-VideoPlayer-on(type: 'startRenderFrame', callback: Callback<void>): void--><!--Device-VideoPlayer-on(type: 'startRenderFrame', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'startRenderFrame' | Yes | Event type, which is **'startRenderFrame'** in this case. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback invoked when the event is triggered. |

## on('videoSizeChanged')

```TypeScript
on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void
```

Subscribes to the video width and height change event.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-media-media-avplayer-i.md#onmediakeysysteminfoupdate)(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler)

<!--Device-VideoPlayer-on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void--><!--Device-VideoPlayer-on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'videoSizeChanged' | Yes | Event type, which is **'videoSizeChanged'** in this case. |
| callback | (width: number, height: number) =&gt; void | Yes | Callback invoked when the event is triggered. **width** indicates the video width, and **height** indicates the video height. |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

Pauses video playback. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [pause](arkts-media-media-avplayer-i.md#pause)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-pause(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-pause(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

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

## pause

```TypeScript
pause(): Promise<void>
```

Pauses video playback. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [pause](arkts-media-media-avplayer-i.md#pause)()

<!--Device-VideoPlayer-pause(): Promise<void>--><!--Device-VideoPlayer-pause(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [pause](#pause)

## play

```TypeScript
play(callback: AsyncCallback<void>): void
```

Starts video playback. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [play](arkts-media-media-avplayer-i.md#play)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-play(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-play(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

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

## play

```TypeScript
play(): Promise<void>
```

Starts video playback. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [play](arkts-media-media-avplayer-i.md#play)()

<!--Device-VideoPlayer-play(): Promise<void>--><!--Device-VideoPlayer-play(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [play](#play)

## prepare

```TypeScript
prepare(callback: AsyncCallback<void>): void
```

Prepares for video playback. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [prepare](arkts-media-media-avplayer-i.md#prepare)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-prepare(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-prepare(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Configure the parameters based on those supported by the hardware device.
let videoProfile: media.VideoRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT_MPEG_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
}

let videoConfig: media.VideoRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : videoProfile,
  url : 'fd://xx', // The file must be created by the caller and granted with proper permissions.
  rotation : 0,
  location : { latitude : 30, longitude : 130 }
}

// asyncallback.
videoRecorder.prepare(videoConfig, (err: BusinessError) => {
  if (err == null) {
    console.info('prepare success');
  } else {
    console.error('prepare failed and error is ' + err.message);
  }
})
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Configure the parameters based on those supported by the hardware device.
let videoProfile: media.VideoRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT_MPEG_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
}

let videoConfig: media.VideoRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : videoProfile,
  url : 'fd://xx', // The file must be created by the caller and granted with proper permissions.
  rotation : 0,
  location : { latitude : 30, longitude : 130 }
}

// promise.
videoRecorder.prepare(videoConfig).then(() => {
  console.info('prepare success');
}).catch((err: BusinessError) => {
  console.error('prepare failed and catch error is ' + err.message);
});
```

```TypeScript
let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC_LC,
  audioEncodeBitRate : 64000,
  audioSampleRate : 44100,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC_ADTS,
  uri : 'fd://1',       // The file must be created by the caller and granted with proper permissions.
  location : { latitude : 30, longitude : 130},
};
audioRecorder.on('prepare', () => {    // Set the 'prepare' event callback.
  console.info('prepare called');
});
audioRecorder.prepare(audioRecorderConfig);
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the initialized state before proceeding.
  avPlayer.prepare((err: BusinessError) => {
    if (err) {
      console.error('Failed to prepare,error message is :' + err.message);
    } else {
      console.info('Succeeded in preparing');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the initialized state before proceeding.
  avPlayer.prepare().then(() => {
    console.info('Succeeded in preparing');
  }, (err: BusinessError) => {
    console.error('Failed to prepare,error message is :' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Configure the parameters based on those supported by the hardware device.
let avRecorderProfile: media.AVRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT_MPEG_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
};
let videoMetaData: media.AVMetadata = {
  videoOrientation: '0' // The value can be 0, 90, 180, or 270. If any other value is used, prepare() reports an error.
};
let avRecorderConfig: media.AVRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : avRecorderProfile,
  url : 'fd://', // Before passing an FD to this parameter, the file must be created by the caller and granted with the read and write permissions. Example value: fd://45.
  metadata: videoMetaData,
  location : { latitude : 30, longitude : 130 }
};

avRecorder.prepare(avRecorderConfig, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to prepare and error is: Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in preparing');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Configure the parameters based on those supported by the hardware device.
let avRecorderProfile: media.AVRecorderProfile = {
  audioBitrate : 48000,
  audioChannels : 2,
  audioCodec : media.CodecMimeType.AUDIO_AAC,
  audioSampleRate : 48000,
  fileFormat : media.ContainerFormatType.CFT_MPEG_4,
  videoBitrate : 2000000,
  videoCodec : media.CodecMimeType.VIDEO_AVC,
  videoFrameWidth : 640,
  videoFrameHeight : 480,
  videoFrameRate : 30
};
let videoMetaData: media.AVMetadata = {
  videoOrientation: '0' // The value can be 0, 90, 180, or 270. If any other value is used, prepare() reports an error.
};
let avRecorderConfig: media.AVRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : avRecorderProfile,
  url : 'fd://',  // Before passing an FD to this parameter, the file must be created by the caller and granted with the read and write permissions. Example value: fd://45.
  metadata : videoMetaData,
  location : { latitude : 30, longitude : 130 }
};

avRecorder.prepare(avRecorderConfig).then(() => {
  console.info('Succeeded in preparing');
}).catch((err: Error) => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to prepare and error is: Code: ${error.code}, message: ${error.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVTranscoder instance.
  let avTranscoder = await media.createAVTranscoder();
  // Configure the parameters based on those supported by the hardware device.
  let avTranscoderConfig: media.AVTranscoderConfig = {
    audioBitrate : 200000,
    audioCodec : media.CodecMimeType.AUDIO_AAC,
    fileFormat : media.ContainerFormatType.CFT_MPEG_4,
    videoBitrate : 3000000,
    videoCodec : media.CodecMimeType.VIDEO_AVC,
  };

  avTranscoder.prepare(avTranscoderConfig).then(() => {
    console.info('prepare success');
  }).catch((err: BusinessError) => {
    console.error('prepare failed and catch error is ' + err.message);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.prepare((err: BusinessError) => {
  if (err) {
    console.error('Failed to prepare!');
  } else {
    console.info('Succeeded in preparing!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.prepare().then(() => {
  console.info('Succeeded in preparing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## prepare

```TypeScript
prepare(): Promise<void>
```

Prepares for video playback. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [prepare](arkts-media-media-avplayer-i.md#prepare)()

<!--Device-VideoPlayer-prepare(): Promise<void>--><!--Device-VideoPlayer-prepare(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [prepare](#prepare)

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases the video playback resources. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [release](arkts-media-media-avplayer-i.md#release)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-release(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

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

## release

```TypeScript
release(): Promise<void>
```

Releases the video playback resources. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [release](arkts-media-media-avplayer-i.md#release)()

<!--Device-VideoPlayer-release(): Promise<void>--><!--Device-VideoPlayer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [release](#release)

## reset

```TypeScript
reset(callback: AsyncCallback<void>): void
```

Resets video playback. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [reset](arkts-media-media-avplayer-i.md#reset)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-reset(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-reset(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

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

## reset

```TypeScript
reset(): Promise<void>
```

Resets video playback. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [reset](arkts-media-media-avplayer-i.md#reset)()

<!--Device-VideoPlayer-reset(): Promise<void>--><!--Device-VideoPlayer-reset(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [reset](#reset)

## seek

```TypeScript
seek(timeMs: number, callback: AsyncCallback<number>): void
```

Seeks to the specified playback position. The previous key frame at the specified position is played. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [seek](arkts-media-media-avplayer-i.md#seek)

<!--Device-VideoPlayer-seek(timeMs: number, callback: AsyncCallback<number>): void--><!--Device-VideoPlayer-seek(timeMs: number, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeMs | number | Yes | Position to seek to, in ms. The value range is [0, duration]. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the new playback position; otherwise, **err** is an error object. |

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

## seek

```TypeScript
seek(timeMs: number, mode: SeekMode, callback: AsyncCallback<number>): void
```

Seeks to the specified playback position. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [seek](arkts-media-media-avplayer-i.md#seek)

<!--Device-VideoPlayer-seek(timeMs: number, mode: SeekMode, callback: AsyncCallback<number>): void--><!--Device-VideoPlayer-seek(timeMs: number, mode: SeekMode, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeMs | number | Yes | Position to seek to, in ms. The value range is [0, duration]. |
| mode | SeekMode | Yes | Seek mode. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the new playback position; otherwise, **err** is an error object. |

**Examples**

See [seek](#seek)

## seek

```TypeScript
seek(timeMs: number, mode?: SeekMode): Promise<number>
```

Seeks to the specified playback position. If **mode** is not specified, the previous key frame at the specified position is played. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [seek](arkts-media-media-avplayer-i.md#seek)

<!--Device-VideoPlayer-seek(timeMs: number, mode?: SeekMode): Promise<number>--><!--Device-VideoPlayer-seek(timeMs: number, mode?: SeekMode): Promise<number>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timeMs | number | Yes | Position to seek to, in ms. The value range is [0, duration]. |
| mode | SeekMode | No | Seek mode based on the video I frame. The default value is **SEEK_PREV_SYNC**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the playback position, in ms. |

**Examples**

See [seek](#seek)

## setDisplaySurface

```TypeScript
setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void
```

Sets a surface ID. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - **SetDisplaySurface** must be called between the URL setting and the calling of **prepare**. A surface must
> be set for video streams without audio. Otherwise, the calling of **prepare** fails.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

<!--Device-VideoPlayer-setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | Surface ID, which is obtained from the **XComponent**. For details about how to obtain it, see XComponent. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let surfaceId: string = '';
videoPlayer.setDisplaySurface(surfaceId, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set DisplaySurface!');
  } else {
    console.info('Succeeded in setting DisplaySurface!');
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let surfaceId: string = '';
videoPlayer.setDisplaySurface(surfaceId).then(() => {
  console.info('Succeeded in setting DisplaySurface');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

## setDisplaySurface

```TypeScript
setDisplaySurface(surfaceId: string): Promise<void>
```

Sets a surface ID. This API uses a promise to return the result.

> **NOTE：**&gt;
> - **SetDisplaySurface** must be called between the URL setting and the calling of **prepare**. A surface must
> be set for video streams without audio. Otherwise, the calling of **prepare** fails.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

<!--Device-VideoPlayer-setDisplaySurface(surfaceId: string): Promise<void>--><!--Device-VideoPlayer-setDisplaySurface(surfaceId: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | Surface ID, which is obtained from the **XComponent**. For details about how to obtain it, see XComponent. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [setDisplaySurface](#setdisplaysurface)

## setSpeed

```TypeScript
setSpeed(speed: number, callback: AsyncCallback<number>): void
```

Sets the playback speed. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setSpeed](arkts-media-media-avplayer-i.md#setspeed)

<!--Device-VideoPlayer-setSpeed(speed: number, callback: AsyncCallback<number>): void--><!--Device-VideoPlayer-setSpeed(speed: number, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speed | number | Yes | Video playback speed. For details, see [PlaybackSpeed](arkts-media-media-playbackspeed-e.md). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the playback speed; otherwise, **err** is an error object. |

**Examples**

```TypeScript
async function  test(){
  let avPlayer = await media.createAVPlayer();
  // Here is only an example. In real development, you must wait for the stateChange event to successfully trigger and reach the prepared, playing, paused, or completed state before proceeding.
  avPlayer.setSpeed(media.PlaybackSpeed.SPEED_FORWARD_2_00_X);
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
let speed = media.PlaybackSpeed.SPEED_FORWARD_2_00_X;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).setSpeed(speed, (err: BusinessError, result: number) => {
    if (err) {
      console.error('Failed to set Speed!');
    } else {
      console.info('Succeeded in setting Speed!');
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
let speed = media.PlaybackSpeed.SPEED_FORWARD_2_00_X;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).setSpeed(speed).then((result: number) => {
    console.info('Succeeded in setting Speed');
  }).catch((error: BusinessError) => {
    console.error(`Failed to set Speed, error:${error}`);// todo:: error.
  });
}
```

## setSpeed

```TypeScript
setSpeed(speed: number): Promise<number>
```

Sets the playback speed. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setSpeed](arkts-media-media-avplayer-i.md#setspeed)

<!--Device-VideoPlayer-setSpeed(speed: number): Promise<number>--><!--Device-VideoPlayer-setSpeed(speed: number): Promise<number>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speed | number | Yes | Video playback speed. For details, see [PlaybackSpeed](arkts-media-media-playbackspeed-e.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the playback speed. For details, see [PlaybackSpeed]{ |

**Examples**

See [setSpeed](#setspeed)

## setVolume

```TypeScript
setVolume(vol: number, callback: AsyncCallback<void>): void
```

Sets the volume. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setVolume](arkts-media-media-avplayer-i.md#setvolume)

<!--Device-VideoPlayer-setVolume(vol: number, callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-setVolume(vol: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| vol | number | Yes | Relative volume. The value ranges from 0.00 to 1.00. The value **1.00** indicates the maximum volume (100%). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the setting is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

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

## setVolume

```TypeScript
setVolume(vol: number): Promise<void>
```

Sets the volume. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setVolume](arkts-media-media-avplayer-i.md#setvolume)

<!--Device-VideoPlayer-setVolume(vol: number): Promise<void>--><!--Device-VideoPlayer-setVolume(vol: number): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| vol | number | Yes | Relative volume. The value ranges from 0.00 to 1.00. The value **1.00** indicates the maximum volume (100%). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [setVolume](#setvolume)

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

Stops video playback. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [stop](arkts-media-media-avplayer-i.md#stop)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-stop(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-stop(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

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

## stop

```TypeScript
stop(): Promise<void>
```

Stops video playback. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [stop](arkts-media-media-avplayer-i.md#stop)()

<!--Device-VideoPlayer-stop(): Promise<void>--><!--Device-VideoPlayer-stop(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

See [stop](#stop)

## audioInterruptMode

```TypeScript
audioInterruptMode?: audio.InterruptMode
```

Audio interruption mode.

**Type:** audio.InterruptMode

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [audioInterruptMode](arkts-media-media-avplayer-i.md#audiointerruptmode)

<!--Device-VideoPlayer-audioInterruptMode?: audio.InterruptMode--><!--Device-VideoPlayer-audioInterruptMode?: audio.InterruptMode-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## currentTime

```TypeScript
readonly currentTime: number
```

Current video playback position, in ms.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [currentTime](arkts-media-media-avplayer-i.md#currenttime)

<!--Device-VideoPlayer-readonly currentTime: number--><!--Device-VideoPlayer-readonly currentTime: number-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## duration

```TypeScript
readonly duration: number
```

Video duration, in ms. The value **-1** indicates the live mode.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [duration](arkts-media-media-avplayer-i.md#duration)

<!--Device-VideoPlayer-readonly duration: number--><!--Device-VideoPlayer-readonly duration: number-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## fdSrc

```TypeScript
fdSrc: AVFileDescriptor
```

Description of a video file. This property is required when video assets of an application are continuously stored in a file.Assume that a music file that stores continuous music assets consists of the following:Video 1 (address offset: 0, byte length: 100)Video 2 (address offset: 101; byte length: 50)Video 3 (address offset: 151, byte length: 150)
1. To play video 1: AVFileDescriptor { fd = resource handle; offset = 0; length = 100; }
2. To play video 2: AVFileDescriptor { fd = resource handle; offset = 101; length = 50; }
3. To play video 3: AVFileDescriptor { fd = resource handle; offset = 151; length = 150; }
To play an independent video file, use **src=fd://xx**.

**Type:** [AVFileDescriptor](arkts-media-media-avfiledescriptor-i.md)

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [fdSrc](arkts-media-media-avplayer-i.md#fdsrc)

<!--Device-VideoPlayer-fdSrc: AVFileDescriptor--><!--Device-VideoPlayer-fdSrc: AVFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## height

```TypeScript
readonly height: number
```

Video height, in px.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [height](arkts-media-media-avplayer-i.md#height)

<!--Device-VideoPlayer-readonly height: number--><!--Device-VideoPlayer-readonly height: number-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## loop

```TypeScript
loop: boolean
```

Whether to loop video playback. **true** to loop, **false** otherwise.

**Type:** boolean

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [loop](arkts-media-media-avplayer-i.md#loop)

<!--Device-VideoPlayer-loop: boolean--><!--Device-VideoPlayer-loop: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## state

```TypeScript
readonly state: VideoPlayState
```

Video playback state.

**Type:** [VideoPlayState](arkts-media-media-videoplaystate-t.md)

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [state](arkts-media-media-avplayer-i.md#state)

<!--Device-VideoPlayer-readonly state: VideoPlayState--><!--Device-VideoPlayer-readonly state: VideoPlayState-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## url

```TypeScript
url: string
```

Video URL. The video formats MP4, MPEG-TS, and MKV are supported.  
**Example of supported URLs**:
1. FD: fd://xx

2. HTTP: http://xx
3. HTTPS: https://xx
4. HLS: http://xx or https://xx
5. File type: file://xx  
**NOTE：**WebM is no longer supported since API version 11.

**Type:** string

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [url](arkts-media-media-avplayer-i.md#url)

<!--Device-VideoPlayer-url: string--><!--Device-VideoPlayer-url: string-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## videoScaleType

```TypeScript
videoScaleType?: VideoScaleType
```

Video scale type. The default value is **VIDEO_SCALE_TYPE_FIT**.

**Type:** [VideoScaleType](arkts-media-media-videoscaletype-e.md)

**Since:** 9

**Deprecated since:** 9

**Substitutes:** [videoScaleType](arkts-media-media-avplayer-i.md#videoscaletype)

<!--Device-VideoPlayer-videoScaleType?: VideoScaleType--><!--Device-VideoPlayer-videoScaleType?: VideoScaleType-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

## width

```TypeScript
readonly width: number
```

Video width, in px.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [width](arkts-media-media-avplayer-i.md#width)

<!--Device-VideoPlayer-readonly width: number--><!--Device-VideoPlayer-readonly width: number-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoPlayer

