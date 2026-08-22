# VideoPlayer

视频播放管理类，用于管理和播放视频媒体。在调用VideoPlayer的方法前，需要先通过 [createVideoPlayer()](arkts-media-media-createvideoplayer-f.md)构建 一个VideoPlayer实例。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer](arkts-media-media-n.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [media](arkts-media-media-n.md)

<!--Device-unnamed-interface VideoPlayer--><!--Device-unnamed-interface VideoPlayer-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## 导入模块

```TypeScript
import { media } from '@kit.MediaKit';
```

## getTrackDescription

```TypeScript
getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void
```

获取视频轨道信息。通过回调函数获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)(callback: AsyncCallback&lt;Array&lt;MediaDescription&gt;&gt;)

<!--Device-VideoPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void--><!--Device-VideoPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MediaDescription](arkts-media-multimedia-media-mediadescription-i.md)&gt;&gt; | 是 | 回调函数。获取视频轨道信息成功时，err为undefined，data为获取到的视频轨道信息 MediaDescription数组，否则为错误对象。 |

**示例**

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
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared、playing或paused状态后才能调用。
  avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
    if (error) {
      console.error(`Failed to do getTrackDescription, error:${error}`);
    } else {
      console.info('Succeeded in doing getTrackDescription');
    }
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared、playing或paused状态后才能调用。
  avPlayer.getTrackDescription().then((arrList: Array<media.MediaDescription>) => {
    console.info('Succeeded in getting TrackDescription');
  }).catch((error: BusinessError) => {
    console.error(`Failed to get TrackDescription.Code:${error.code},message:${error.message}`);
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

获取视频轨道信息。通过Promise获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)()

<!--Device-VideoPlayer-getTrackDescription(): Promise<Array<MediaDescription>>--><!--Device-VideoPlayer-getTrackDescription(): Promise<Array<MediaDescription>>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;[MediaDescription](arkts-media-multimedia-media-mediadescription-i.md)&gt;&gt; | Promise对象，返回获取的视频轨道信息MediaDescription数组。 |

**示例**

参见 [getTrackDescription](#gettrackdescription)

## on('audioInterrupt')

```TypeScript
on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void
```

监听音频焦点变化事件，参考[audio.InterruptEvent](../../apis-audio-kit/arkts-apis/arkts-audio-audio-interruptevent-i.md)。

> **说明：**
> 
> 从API version 9开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('audioInterrupt')
> 替代。

**起始版本：** 9

**废弃版本：** 9

**替代接口：** on(type: 'audioInterrupt', callback: Callback&lt;audio.InterruptEvent&gt;)

<!--Device-VideoPlayer-on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void--><!--Device-VideoPlayer-on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | 是 | 音频焦点变化事件回调类型，支持的事件：'audioInterrupt'。 |
| callback | (info: audio.InterruptEvent) =&gt; void | 是 | 音频焦点变化事件回调方法。 |

## on('bufferingUpdate')

```TypeScript
on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void
```

开始监听视频缓存更新事件。仅网络播放支持该订阅事件。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('bufferingUpdate')
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler)

<!--Device-VideoPlayer-on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void--><!--Device-VideoPlayer-on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'bufferingUpdate' | 是 | 视频缓存事件回调类型，支持的事件：'bufferingUpdate'。 |
| callback | (infoType: BufferingInfoType, value: number) =&gt; void | 是 | 视频缓存事件回调方法。<br> BufferingInfoTypevalue值固定为0。 |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

开始监听视频播放错误事件，当上报error错误事件后，用户需处理error事件，退出播放操作。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('error')替
> 代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on(type: 'error', callback: ErrorCallback)

<!--Device-VideoPlayer-on(type: 'error', callback: ErrorCallback): void--><!--Device-VideoPlayer-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'error' | 是 | 播放错误事件回调类型，支持的事件包括：'error'。<br>- 'error'：视频播放中发生错误，触发该事件。 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 | 播放错误事件回调方法。 |

## on('playbackCompleted')

```TypeScript
on(type: 'playbackCompleted', callback: Callback<void>): void
```

开始监听视频播放完成事件。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('stateChange')
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-VideoPlayer-on(type: 'playbackCompleted', callback: Callback<void>): void--><!--Device-VideoPlayer-on(type: 'playbackCompleted', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'playbackCompleted' | 是 | 视频播放完成事件回调类型，支持的事件：'playbackCompleted'。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | 视频播放完成事件回调方法。 |

## on('startRenderFrame')

```TypeScript
on(type: 'startRenderFrame', callback: Callback<void>): void
```

开始监听视频播放首帧送显上报事件。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('startRenderFrame')
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on(type: 'startRenderFrame', callback: Callback&lt;void&gt;)

<!--Device-VideoPlayer-on(type: 'startRenderFrame', callback: Callback<void>): void--><!--Device-VideoPlayer-on(type: 'startRenderFrame', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'startRenderFrame' | 是 | 视频播放首帧送显上报事件回调类型，支持的事件：'startRenderFrame'。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | 视频播放首帧送显上报事件回调方法。 |

## on('videoSizeChanged')

```TypeScript
on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void
```

开始监听视频播放宽高变化事件。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('videoSizeChange')
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler)

<!--Device-VideoPlayer-on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void--><!--Device-VideoPlayer-on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'videoSizeChanged' | 是 | 视频播放宽高变化事件回调类型，支持的事件：'videoSizeChanged'。 |
| callback | (width: number, height: number) =&gt; void | 是 | 视频播放宽高变化事件回调方法，width表示宽，height表示高。 |

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

通过回调方式暂停播放视频。通过回调函数获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.pause](arkts-media-media-avplayer-i.md#pause)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [pause](arkts-media-media-avplayer-i.md#pause)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-pause(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-pause(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当暂停播放视频成功，err为undefined，否则为错误对象。 |

**示例**

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
audioPlayer.on('pause', () => {    // 设置'pause'事件回调。
  console.info('audio pause called');
});
audioPlayer.pause();
```

```TypeScript
audioRecorder.on('pause', () => {    // 设置'pause'事件回调。
  console.info('audio recorder pause called');
});
audioRecorder.pause();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至playing状态后才能调用。
  avPlayer.pause((err: BusinessError) => {
    if (err) {
      console.error(`Failed to pause.Code:${err.code},message:${err.message}`);
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
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至playing状态后才能调用。
  avPlayer.pause().then(() => {
    console.info('Succeeded in pausing');
  }, (err: BusinessError) => {
    console.error(`Failed to pause.Code:${err.code},message:${err.message}`);
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
  // 创建转码实例。
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

暂停播放视频。通过Promise获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.pause](arkts-media-media-avplayer-i.md#pause)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [pause](arkts-media-media-avplayer-i.md#pause)()

<!--Device-VideoPlayer-pause(): Promise<void>--><!--Device-VideoPlayer-pause(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 暂停播放视频的Promise返回值。 |

**示例**

参见 [pause](#pause)

## play

```TypeScript
play(callback: AsyncCallback<void>): void
```

开始播放视频。通过回调函数获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.play](arkts-media-media-avplayer-i.md#play)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [play](arkts-media-media-avplayer-i.md#play)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-play(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-play(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当开始播放视频成功，err为undefined，否则为错误对象。 |

**示例**

```TypeScript
audioPlayer.on('play', () => {    // 设置'play'事件回调。
  console.info('audio play called');
});
audioPlayer.play();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared、paused或completed状态后才能调用。
  avPlayer.play((err: BusinessError) => {
    if (err) {
      console.error(`Failed to play.Code:${err.code},message:${err.message}`);
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
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared、paused或completed状态后才能调用。
  avPlayer.play().then(() => {
    console.info('Succeeded in playing');
  }, (err: BusinessError) => {
    console.error(`Failed to play.Code:${err.code},message:${err.message}`);
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

开始播放视频。通过Promise获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.play](arkts-media-media-avplayer-i.md#play)替代
> 。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [play](arkts-media-media-avplayer-i.md#play)()

<!--Device-VideoPlayer-play(): Promise<void>--><!--Device-VideoPlayer-play(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 开始播放视频的Promise返回值。 |

**示例**

参见 [play](#play)

## prepare

```TypeScript
prepare(callback: AsyncCallback<void>): void
```

准备播放视频。通过回调函数获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.prepare](arkts-media-media-avplayer-i.md#prepare)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [prepare](arkts-media-media-avplayer-i.md#prepare)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-prepare(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-prepare(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当准备播放视频成功，err为undefined，否则为错误对象。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 配置参数以实际硬件设备支持的范围为准。
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
  url : 'fd://xx', // 文件需先由调用者创建，并给予适当的权限。
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

// 配置参数以实际硬件设备支持的范围为准。
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
  url : 'fd://xx', // 文件需先由调用者创建，并给予适当的权限。
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
  uri : 'fd://1',       // fd通过fs.open()获取。文件需先由调用者创建，并给予适当的权限。
  location : { latitude : 30, longitude : 130},
};
audioRecorder.on('prepare', () => {    // 设置'prepare'事件回调。
  console.info('prepare called');
});
audioRecorder.prepare(audioRecorderConfig);
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
  avPlayer.prepare((err: BusinessError) => {
    if (err) {
      console.error(`Failed to prepare.Code:${err.code},message:${err.message}`);
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
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
  avPlayer.prepare().then(() => {
    console.info('Succeeded in preparing');
  }, (err: BusinessError) => {
    console.error(`Failed to prepare.Code:${err.code},message:${err.message}`);
  });
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 配置参数以实际硬件设备支持的范围为准。
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
  videoOrientation: '0' // 合理值0、90、180、270，非合理值prepare接口报错。
};
let avRecorderConfig: media.AVRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : avRecorderProfile,
  url : 'fd://', // 文件需先通过fs.open接口（@kit.FileKit）打开获取文件描述符fd，赋予读写权限，将fd传给此参数，详见文件管理开发指导。
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

// 配置参数以实际硬件设备支持的范围为准。
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
  videoOrientation: '0' // 合理值0、90、180、270，非合理值prepare接口报错。
};
let avRecorderConfig: media.AVRecorderConfig = {
  audioSourceType : media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
  videoSourceType : media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
  profile : avRecorderProfile,
  url : 'fd://',  // 文件需先通过fileIo.open接口（@kit.CoreFileKit）打开获取文件描述符fd，赋予读写权限，将fd传给此参数。
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
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  // 配置参数以实际硬件设备支持的范围为准。
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

准备播放视频。通过Promise获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.prepare](arkts-media-media-avplayer-i.md#prepare)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [prepare](arkts-media-media-avplayer-i.md#prepare)()

<!--Device-VideoPlayer-prepare(): Promise<void>--><!--Device-VideoPlayer-prepare(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 准备播放视频的Promise返回值。 |

**示例**

参见 [prepare](#prepare)

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放视频资源。通过回调函数获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.release](arkts-media-media-avplayer-i.md#release)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [release](arkts-media-media-avplayer-i.md#release)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-release(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当释放视频资源成功，err为undefined，否则为错误对象。 |

**示例**

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
audioRecorder.on('release', () => {    // 设置'release'事件回调。
  console.info('audio recorder release called');
});
audioRecorder.release();
audioRecorder = undefined;
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;

// 释放资源。
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.release((error: BusinessError) => {
      if (error) {
        console.error(`Failed to release, code: ${error.code}, message: ${error.message}`);
        return;
      }
      console.info(`Succeeded in releasing`);
    });
  } else {
    console.error(`Failed to create AVImageGenerator, code: ${err.code}, message: ${err.message}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let avImageGenerator: media.AVImageGenerator | undefined = undefined;

// 释放资源。
media.createAVImageGenerator((err: BusinessError, generator: media.AVImageGenerator) => {
  if (generator) {
    avImageGenerator = generator;
    console.info(`Succeeded in creating AVImageGenerator`);
    avImageGenerator.release().then(() => {
      console.info(`Succeeded in releasing.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to release, code: ${error.code}, message: ${error.message}`);
    });
  } else {
    console.error(`Failed to create AVImageGenerator, code: ${err.code}, message: ${err.message}`);
  }
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建AVMetadataExtractor对象。
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.release((error: BusinessError) => {
    if (error) {
      console.error(`Failed to release, code: ${error.code} message: ${error.message}`);
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
  // 创建AVMetadataExtractor对象。
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  if (avMetadataExtractor) {
    avMetadataExtractor.release().then(() => {
      console.info(`Succeeded in releasing.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to release, code: ${error.code} message: ${error.message}`);
    });
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发除released以外的状态才能调用。
  avPlayer.release((err: BusinessError) => {
    if (err) {
      console.error(`Failed to release.Code:${err.code},message:${err.message}`);
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
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发除released以外的状态才能调用。
  avPlayer.release().then(() => {
    console.info('Succeeded in releasing');
  }, (err: BusinessError) => {
    console.error(`Failed to release.Code:${err.code},message:${err.message}`);
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
import { media } from '@kit.MediaKit';

async function testRelease() {
  // 创建录屏实例。
  let avScreenCaptureRecorder = await media.createAVScreenCaptureRecorder();

  // 其余流程。

  // 调用release方法。
  if (avScreenCaptureRecorder) {
    avScreenCaptureRecorder.release().then(() => {
      console.info('Succeeded in releasing avScreenCaptureRecorder');
    }).catch((err: BusinessError) => {
      console.error(`Failed to release avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
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

释放视频资源。通过Promise获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.release](arkts-media-media-avplayer-i.md#release)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [release](arkts-media-media-avplayer-i.md#release)()

<!--Device-VideoPlayer-release(): Promise<void>--><!--Device-VideoPlayer-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 释放视频资源的Promise返回值。 |

**示例**

参见 [release](#release)

## reset

```TypeScript
reset(callback: AsyncCallback<void>): void
```

重置播放视频。通过回调函数获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.reset](arkts-media-media-avplayer-i.md#reset)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [reset](arkts-media-media-avplayer-i.md#reset)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-reset(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-reset(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当重置播放视频成功，err为undefined，否则为错误对象。 |

**示例**

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
audioPlayer.on('reset', () => {    // 设置'reset'事件回调。
  console.info('audio reset called');
});
audioPlayer.reset();
```

```TypeScript
audioRecorder.on('reset', () => {    // 设置'reset'事件回调。
  console.info('audio recorder reset called');
});
audioRecorder.reset();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized、prepared、playing、paused、completed或stopped状态后才能调用。
  avPlayer.reset((err: BusinessError) => {
    if (err) {
      console.error(`Failed to reset.Code:${err.code},message:${err.message}`);
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
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized、prepared、playing、paused、completed或stopped状态后才能调用。
  avPlayer.reset().then(() => {
    console.info('Succeeded in resetting');
  }, (err: BusinessError) => {
    console.error(`Failed to reset.Code:${err.code},message:${err.message}`);
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

重置播放视频。通过Promise获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.reset](arkts-media-media-avplayer-i.md#reset)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [reset](arkts-media-media-avplayer-i.md#reset)()

<!--Device-VideoPlayer-reset(): Promise<void>--><!--Device-VideoPlayer-reset(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**示例**

参见 [reset](#reset)

## seek

```TypeScript
seek(timeMs: number, callback: AsyncCallback<number>): void
```

跳转到指定播放位置，默认跳转到指定时间点的上一个关键帧。通过回调函数获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](arkts-media-media-avplayer-i.md#seek)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [seek](arkts-media-media-avplayer-i.md#seek)

<!--Device-VideoPlayer-seek(timeMs: number, callback: AsyncCallback<number>): void--><!--Device-VideoPlayer-seek(timeMs: number, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为[0, duration]。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 | 回调函数。跳转到指定播放位置成功时，err为undefined，data为获取到的跳转到的播放位置，否则为错误对象。 |

**示例**

```TypeScript
audioPlayer.on('timeUpdate', (seekDoneTime: number) => {    // 设置'timeUpdate'事件回调。
  if (seekDoneTime == null) {
    console.error('Failed to seek');
    return;
  }
  console.info('Succeeded in seek. seekDoneTime: ' + seekDoneTime);
});
audioPlayer.seek(30000);    // seek到30000ms的位置。
```

```TypeScript
async function  test(){
  let avPlayer = await media.createAVPlayer();
  let seekTime: number = 1000;
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared、playing、paused或completed状态后才能调用。
  avPlayer.seek(seekTime, media.SeekMode.SEEK_PREV_SYNC);
}
```

```TypeScript
async function  test(){
  // SEEK_CONTINUOUS 可以结合Slider的onChange回调方法进行对应处理，当slideMode为Moving时，触发拖动过程的SeekContinuous。
  let avPlayer = await media.createAVPlayer();
  let slideMovingTime: number = 2000;
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared、playing、paused或completed状态后才能调用。
  avPlayer.seek(slideMovingTime, media.SeekMode.SEEK_CONTINUOUS);

  // 当slideMode为End时，调用seek(-1, media.SeekMode.SEEK_CONTINUOUS)结束seek。
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
  (videoPlayer as media.VideoPlayer).seek(seekTime).then((seekDoneTime: number) => { // seekDoneTime表示seek完成后的时间点。
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

跳转到指定播放位置。通过回调函数获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](arkts-media-media-avplayer-i.md#seek)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [seek](arkts-media-media-avplayer-i.md#seek)

<!--Device-VideoPlayer-seek(timeMs: number, mode: SeekMode, callback: AsyncCallback<number>): void--><!--Device-VideoPlayer-seek(timeMs: number, mode: SeekMode, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为[0, duration]。 |
| mode | [SeekMode](arkts-media-multimedia-media-seekmode-e.md) | 是 | 跳转模式。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 | 回调函数。跳转到指定播放位置成功时，err为undefined，data为获取到的跳转到的播放位置，否则为错误对象。 |

**示例**

参见 [seek](#seek)

## seek

```TypeScript
seek(timeMs: number, mode?: SeekMode): Promise<number>
```

跳转到指定播放位置，如果没有设置mode则跳转到指定时间点的上一个关键帧。通过Promise获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](arkts-media-media-avplayer-i.md#seek)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [seek](arkts-media-media-avplayer-i.md#seek)

<!--Device-VideoPlayer-seek(timeMs: number, mode?: SeekMode): Promise<number>--><!--Device-VideoPlayer-seek(timeMs: number, mode?: SeekMode): Promise<number>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为[0, duration]。 |
| mode | [SeekMode](arkts-media-multimedia-media-seekmode-e.md) | 否 | 基于视频I帧的跳转模式，默认为SEEK_PREV_SYNC模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | 跳转到指定播放位置的Promise返回值，单位ms。 |

**示例**

参见 [seek](#seek)

## setDisplaySurface

```TypeScript
setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void
```

设置SurfaceId。通过回调函数获取返回值。

> **说明：**
> 
> - SetDisplaySurface需要在设置url和Prepare之间，无音频的视频流必须设置Surface否则Prepare失败。
> 
> - 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.surfaceId](../../../reference/apis-media-kit/arkts-apis-media-AVPlayer.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** null

<!--Device-VideoPlayer-setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 指定SurfaceId，应从XComponent组件获取，获取方式请参考 XComponent。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当设置SurfaceId成功，err为undefined，否则为错误对象。 |

**示例**

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

设置SurfaceId。通过Promise获取返回值。

> **说明：**
> 
> - SetDisplaySurface需要在设置url和Prepare之间，无音频的视频流必须设置Surface否则Prepare失败。
> 
> - 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.surfaceId](../../../reference/apis-media-kit/arkts-apis-media-AVPlayer.md)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** null

<!--Device-VideoPlayer-setDisplaySurface(surfaceId: string): Promise<void>--><!--Device-VideoPlayer-setDisplaySurface(surfaceId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 指定SurfaceId，应从XComponent组件获取，获取方式请参考 XComponent。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 设置SurfaceId的Promise返回值。 |

**示例**

参见 [setDisplaySurface](#setdisplaysurface)

## setSpeed

```TypeScript
setSpeed(speed: number, callback: AsyncCallback<number>): void
```

设置播放速度。通过回调函数获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> AVPlayer.setSpeed替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** setSpeed

<!--Device-VideoPlayer-setSpeed(speed: number, callback: AsyncCallback<number>): void--><!--Device-VideoPlayer-setSpeed(speed: number, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | number | 是 | 指定播放视频速度，具体见PlaybackSpeed。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 | 回调函数。设置播放速度成功时，err为undefined，data为设置的播放速度，否则为错误对象。 |

**示例**

```TypeScript
async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared、playing、paused或completed状态后才能调用。
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

设置播放速度。通过Promise获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> AVPlayer.setSpeed替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** setSpeed

<!--Device-VideoPlayer-setSpeed(speed: number): Promise<number>--><!--Device-VideoPlayer-setSpeed(speed: number): Promise<number>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | number | 是 | 指定播放视频速度，具体见PlaybackSpeed。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，返回设置的播放速度，具体见 [PlaybackSpeed]{ |

**示例**

参见 [setSpeed](#setspeed)

## setVolume

```TypeScript
setVolume(vol: number, callback: AsyncCallback<void>): void
```

设置音量。通过回调函数获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.setVolume](arkts-media-media-avplayer-i.md#setvolume)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setVolume](arkts-media-media-avplayer-i.md#setvolume)

<!--Device-VideoPlayer-setVolume(vol: number, callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-setVolume(vol: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vol | number | 是 | 指定的相对音量大小，取值范围为[0.00-1.00]，1表示最大音量，即100%。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当设置音量成功，err为undefined，否则为错误对象。 |

**示例**

```TypeScript
audioPlayer.on('volumeChange', () => {    // 设置'volumeChange'事件回调。
  console.info('audio volumeChange called');
});
audioPlayer.setVolume(1);    // 设置音量到100%。
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

设置音量。通过Promise获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.setVolume](arkts-media-media-avplayer-i.md#setvolume)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setVolume](arkts-media-media-avplayer-i.md#setvolume)

<!--Device-VideoPlayer-setVolume(vol: number): Promise<void>--><!--Device-VideoPlayer-setVolume(vol: number): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vol | number | 是 | 指定的相对音量大小，取值范围为[0.00-1.00]，1表示最大音量，即100%。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 设置音量的Promise返回值。 |

**示例**

参见 [setVolume](#setvolume)

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

通过回调方式停止播放视频。通过回调函数获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.stop](arkts-media-media-avplayer-i.md#stop)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [stop](arkts-media-media-avplayer-i.md#stop)(callback: AsyncCallback&lt;void&gt;)

<!--Device-VideoPlayer-stop(callback: AsyncCallback<void>): void--><!--Device-VideoPlayer-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当停止播放视频成功，err为undefined，否则为错误对象。 |

**示例**

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
audioPlayer.on('stop', () => {    // 设置'stop'事件回调。
  console.info('audio stop called');
});
audioPlayer.stop();
```

```TypeScript
audioRecorder.on('stop', () => {    // 设置'stop'事件回调。
  console.info('audio recorder stop called');
});
audioRecorder.stop();
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared、playing、paused或completed状态后才能调用。
  avPlayer.stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop.Code:${err.code},message:${err.message}`);
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
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared、playing、paused或completed状态后才能调用。
  avPlayer.stop().then(() => {
    console.info('Succeeded in stopping');
  }, (err: BusinessError) => {
    console.error(`Failed to stop.Code:${err.code},message:${err.message}`);
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

停止播放视频。通过Promise获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.stop](arkts-media-media-avplayer-i.md#stop)替代
> 。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [stop](arkts-media-media-avplayer-i.md#stop)()

<!--Device-VideoPlayer-stop(): Promise<void>--><!--Device-VideoPlayer-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 停止播放视频的Promise返回值。 |

**示例**

参见 [stop](#stop)

## audioInterruptMode

```TypeScript
audioInterruptMode?: audio.InterruptMode
```

音频焦点模式。

**类型：** audio.InterruptMode

**起始版本：** 9

**废弃版本：** 9

**替代接口：** audioInterruptMode

<!--Device-VideoPlayer-audioInterruptMode?: audio.InterruptMode--><!--Device-VideoPlayer-audioInterruptMode?: audio.InterruptMode-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## currentTime

```TypeScript
readonly currentTime: number
```

视频的当前播放位置，单位为毫秒（ms）。

**类型：** number

**起始版本：** 8

**废弃版本：** 9

**替代接口：** currentTime

<!--Device-VideoPlayer-readonly currentTime: number--><!--Device-VideoPlayer-readonly currentTime: number-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## duration

```TypeScript
readonly duration: number
```

视频时长，单位为毫秒（ms），返回-1表示直播模式。

**类型：** number

**起始版本：** 8

**废弃版本：** 9

**替代接口：** duration

<!--Device-VideoPlayer-readonly duration: number--><!--Device-VideoPlayer-readonly duration: number-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## fdSrc

```TypeScript
fdSrc: AVFileDescriptor
```

视频媒体文件描述，使用场景：应用中的视频资源被连续存储在同一个文件中。

**使用示例**：

假设一个连续存储的音乐文件:

视频1(地址偏移:0，字节长度:100)

视频2(地址偏移:101，字节长度:50)

视频3(地址偏移:151，字节长度:150)

1. 播放视频1：AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; } 2. 播放视频2：AVFileDescriptor { fd = 资源句柄; offset = 101; length = 50; } 3. 播放视频3：AVFileDescriptor { fd = 资源句柄; offset = 151; length = 150; }

假设是一个独立的视频文件: 请使用src=fd://xx

**类型：** [AVFileDescriptor](arkts-media-multimedia-media-avfiledescriptor-i.md)

**起始版本：** 9

**废弃版本：** 9

**替代接口：** fdSrc

<!--Device-VideoPlayer-fdSrc: AVFileDescriptor--><!--Device-VideoPlayer-fdSrc: AVFileDescriptor-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## height

```TypeScript
readonly height: number
```

视频高，单位为像素（px）。

**类型：** number

**起始版本：** 8

**废弃版本：** 9

**替代接口：** height

<!--Device-VideoPlayer-readonly height: number--><!--Device-VideoPlayer-readonly height: number-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## loop

```TypeScript
loop: boolean
```

视频循环播放属性，设置为'true'表示循环播放。

**类型：** boolean

**起始版本：** 8

**废弃版本：** 9

**替代接口：** loop

<!--Device-VideoPlayer-loop: boolean--><!--Device-VideoPlayer-loop: boolean-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## state

```TypeScript
readonly state: VideoPlayState
```

视频播放的状态。

**类型：** [VideoPlayState](arkts-media-videoplaystate-t.md)

**起始版本：** 8

**废弃版本：** 9

**替代接口：** state

<!--Device-VideoPlayer-readonly state: VideoPlayState--><!--Device-VideoPlayer-readonly state: VideoPlayState-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## url

```TypeScript
url: string
```

视频媒体URL，支持当前主流的视频格式(mp4、mpeg-ts、mkv)。

**支持路径示例**：

1. fd类型播放：fd://xx



2. http网络播放: http://xx 3. https网络播放: https://xx 4. hls网络播放路径：http://xx或者https://xx 5. file类型: file://xx

**说明：**

从API version 11开始不支持webm。

**类型：** string

**起始版本：** 8

**废弃版本：** 9

**替代接口：** url

<!--Device-VideoPlayer-url: string--><!--Device-VideoPlayer-url: string-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## videoScaleType

```TypeScript
videoScaleType?: VideoScaleType
```

视频缩放模式。默认值为VIDEO_SCALE_TYPE_FIT。

**类型：** [VideoScaleType](arkts-media-multimedia-media-videoscaletype-e.md)

**起始版本：** 9

**废弃版本：** 9

**替代接口：** videoScaleType

<!--Device-VideoPlayer-videoScaleType?: VideoScaleType--><!--Device-VideoPlayer-videoScaleType?: VideoScaleType-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

## width

```TypeScript
readonly width: number
```

视频宽，单位为像素（px）。

**类型：** number

**起始版本：** 8

**废弃版本：** 9

**替代接口：** width

<!--Device-VideoPlayer-readonly width: number--><!--Device-VideoPlayer-readonly width: number-End-->

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

