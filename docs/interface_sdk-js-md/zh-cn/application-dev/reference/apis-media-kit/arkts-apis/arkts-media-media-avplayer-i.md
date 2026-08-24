# AVPlayer

播放管理类，用于管理和播放媒体资源。在调用AVPlayer的方法前，需要先通过 [createAVPlayer()](arkts-media-media-createavplayer-f.md)构建一个 AVPlayer实例。在使用AVPlayer实例的方法时，建议开发者注册相关回调，主动获取当前状态变化。 on('stateChange')：监听播放状态机 AVPlayerState切换。on('error')：监听错误事件。应用需要按照实际业务需求合理使用AVPlayer对象，按需创建并及时释放，避免持有过多AVPlayer实例导致内存消耗过大，否则在一定情况下可能导致系统终止应用。Audio/Video播放demo可参考：[音频播放开发指导](../../../media/media/using-avplayer-for-playback.md)、 [视频播放开发指导](../../../media/media/video-playback.md)。

> **说明：**&gt;
> - 本Interface首批接口从API version 9开始支持。

**起始版本：** 23

<!--Device-media-interface AVPlayer--><!--Device-media-interface AVPlayer-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

## 导入模块

```TypeScript
import { media } from '@kit.MediaKit';
```

## addSubtitleFromFd

```TypeScript
addSubtitleFromFd(fd: int, offset?: long, length?: long): Promise<void>
```

依据fd为视频添加外挂字幕，当前仅支持与视频资源同时设置（在avplayer设置fdSrc视频资源后设置外挂字幕）。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-addSubtitleFromFd(fd: int, offset?: long, length?: long): Promise<void>--><!--Device-AVPlayer-addSubtitleFromFd(fd: int, offset?: long, length?: long): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | int | 是 | 资源句柄，通过 [resourceManager.getRawFd](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-resourcemanager-i.md#getrawfd) 获取。 |
| offset | long | 否 | 资源偏移量，需要基于预置资源的信息输入，非法值会造成字幕频资源解析错误，默认值:0。 |
| length | long | 否 | 资源长度，默认值为文件中从偏移量开始的剩余字节，需要基于预置资源的信息输入，非法值会造成字幕频资源解析错误，默认值:0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The parameter check failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

```TypeScript
import { common } from '@kit.AbilityKit';

let avPlayer = await media.createAVPlayer();
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let fileDescriptor = await context.resourceManager.getRawFd('xxx.srt');

avPlayer.addSubtitleFromFd(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length);
```

## addSubtitleFromUrl

```TypeScript
addSubtitleFromUrl(url: string): Promise<void>
```

依据url为视频添加外挂字幕，当前仅支持与视频资源同时设置（在avplayer设置fdSrc视频资源后设置外挂字幕）。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-addSubtitleFromUrl(url: string): Promise<void>--><!--Device-AVPlayer-addSubtitleFromUrl(url: string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 外挂字幕文件地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The parameter check failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

```TypeScript
async function test(){
  let fdUrl:string = 'https://abc.bcd.example/cde/index.srt'; // 此处仅为示意，请替换为真实资源文件URL。
  let avPlayer: media.AVPlayer = await media.createAVPlayer();
  avPlayer.addSubtitleFromUrl(fdUrl);
}
```

## deselectTrack

```TypeScript
deselectTrack(index: int): Promise<void>
```

使用AVPlayer播放多音轨视频时取消指定音视频轨道播放，使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-deselectTrack(index: int): Promise<void>--><!--Device-AVPlayer-deselectTrack(index: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 多音视频资源的轨道索引，来自[getTrackDescription](#gettrackdescription)接口所获取的轨道信息 MediaDescription。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The parameter check failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avPlayer: media.AVPlayer = await media.createAVPlayer();
let audioTrackIndex: Object = 0;
avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
  if (arrList) {
    // 遍历轨道描述列表，提取非首个轨道的索引用于音频轨道选择
    for (let i = 0; i < arrList.length; i++) {
      if (i != 0) {
        // 获取音频轨道列表。
        audioTrackIndex = arrList[i][media.MediaDescriptionKey.MD_KEY_TRACK_INDEX];
      }
    }
  } else {
    console.error(`Failed to get TrackDescription.Code:${error.code},message:${error.message}`);
  }
});

// 选择其中一个音频轨道。
avPlayer.selectTrack(parseInt(audioTrackIndex.toString()));
// 取消选择上次选中的音频轨道，并恢复到默认音频轨道。
avPlayer.deselectTrack(parseInt(audioTrackIndex.toString()));
```

## getLoadedTimeRanges

```TypeScript
getLoadedTimeRanges(): Promise<Array<Range>>
```

获取已加载的时间区间段的列表。使用Promise异步回调。

> **说明：**&gt;
> - 对于本地媒体资源，返回的时间区间为0到整个媒体时长。&gt;
> - 对于网络媒体资源，返回本地已缓存的时间区间段的列表。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVPlayer-getLoadedTimeRanges(): Promise<Array<Range>>--><!--Device-AVPlayer-getLoadedTimeRanges(): Promise<Array<Range>>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;[Range](arkts-media-multimedia-media-range-i.md)&gt;&gt; | Promise对象，返回播放器当前已加载的时间区间段的列表。 <br>时间区间段以播放时间轴上的[start, end]位置表示，单位为毫秒。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.getLoadedTimeRanges().then((range: Array<media.Range>) => {
    console.info(`Succeeded in calling getLoadedTimeRanges: ${range}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to getLoadedTimeRanges.Code:${err.code},message:${err.message}`);
  });
}
```

## getPlaybackInfo

```TypeScript
getPlaybackInfo(): Promise<PlaybackInfo>
```

获取播放过程信息，可以在prepared/playing/paused状态调用。使用Promise异步回调。

**起始版本：** 23

<!--Device-AVPlayer-getPlaybackInfo(): Promise<PlaybackInfo>--><!--Device-AVPlayer-getPlaybackInfo(): Promise<PlaybackInfo>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[PlaybackInfo](arkts-media-multimedia-media-playbackinfo-i.md)&gt; | Promise对象，返回播放器信息PlaybackInfo。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avPlayer: media.AVPlayer | undefined;
let playbackInfo: media.PlaybackInfo | undefined;
media.createAVPlayer(async (err: BusinessError, player: media.AVPlayer) => {
  if (player) {
    avPlayer = player;
    console.info(`Succeeded in creating AVPlayer`);
    if (avPlayer) {
      try {
        playbackInfo = await avPlayer.getPlaybackInfo();
        console.info(`AVPlayer getPlaybackInfo = ${JSON.stringify(playbackInfo)}`); // 打印整个PlaybackInfo的值。
      } catch (error) {
        console.error(`error = ${error}`);
      }
    }
  } else {
    console.error(`Failed to create AVPlayer, error message:${err.message}`);
  }
});
```

## getPlaybackRate

```TypeScript
getPlaybackRate(): Promise<double>
```

获取当前播放器的播放速率。使用Promise异步回调。

**起始版本：** 23

<!--Device-AVPlayer-getPlaybackRate(): Promise<double>--><!--Device-AVPlayer-getPlaybackRate(): Promise<double>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;double&gt; | Promise对象，返回播放倍速速率。 |

**示例**

```TypeScript
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.getPlaybackRate().then((rate: number) => {
    console.info('Succeeded getPlaybackRate' + rate);
  });
}
```

## getPlaybackStatisticMetrics

```TypeScript
getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>
```

获取当前播放器的统计指标信息，可以在准备（prepared）/播放（playing）/暂停（paused）/完成（completed）/停止（stopped）状态调用。使用Promise异步回调。

**起始版本：** 23

<!--Device-AVPlayer-getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>--><!--Device-AVPlayer-getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[PlaybackMetrics](arkts-media-playbackmetrics-t.md)&gt; | Promise对象，返回当前播放器的指标信息PlaybackMetrics。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let avPlayer: media.AVPlayer | undefined;
let playbackMetrics: media.PlaybackMetrics | undefined;
media.createAVPlayer(async (err: BusinessError, player: media.AVPlayer) => {
  if (player) {
    avPlayer = player;
    console.info(`Succeeded in creating AVPlayer`);
    if (avPlayer) {
      try {
        playbackMetrics = await avPlayer.getPlaybackStatisticMetrics();
        console.info(`AVPlayer getPlaybackStatisticMetrics = ${JSON.stringify(playbackMetrics)}`); // 打印整个playbackMetrics的值。
      } catch (error) {
        console.error(`error = ${error}`);
      }
    }
  } else {
    console.error(`Failed to create AVPlayer, error message:${err.message}`);
  }
});
```

## getSeekableTimeRanges

```TypeScript
getSeekableTimeRanges(): Promise<Array<Range>>
```

获取可跳转的时间区间段的列表。使用Promise异步回调。

> **说明：**&gt;
> - 对于本地媒体资源及支持分段请求的媒体资源，返回的时间区间为0到整个媒体时长。&gt;
> - 对于仅支持分块传输的媒体资源，没有可跳转的时间范围。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVPlayer-getSeekableTimeRanges(): Promise<Array<Range>>--><!--Device-AVPlayer-getSeekableTimeRanges(): Promise<Array<Range>>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;[Range](arkts-media-multimedia-media-range-i.md)&gt;&gt; | Promise对象，返回播放器当前可跳转的时间区间段的列表。 <br>时间区间段以播放时间轴上的[start, end]位置表示，单位为毫秒。 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.getSeekableTimeRanges().then((range: Array<media.Range>) => {
    console.info(`Succeeded in calling getSeekableTimeRanges: ${range}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to getSeekableTimeRanges.Code:${err.code},message:${err.message}`);
  });
}
```

## getSelectedTracks

```TypeScript
getSelectedTracks(): Promise<Array<int>>
```

获取已选择的音视频轨道索引，可以在prepared/playing/paused状态调用。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-getSelectedTracks(): Promise<Array<int>>--><!--Device-AVPlayer-getSelectedTracks(): Promise<Array<int>>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;int&gt;&gt; | Promise对象，返回已选择音视频轨道索引数组。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared、playing或paused状态后才能调用。
  avPlayer.getSelectedTracks().then((arrList: Array<number>) => {
    console.info('Succeeded in getting SelectedTracks');
  }).catch((error: BusinessError) => {
    console.error(`Failed to get SelectedTracks.Code:${error.code},message:${error.message}`);
  });
}
```

## getTrackDescription

```TypeScript
getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void
```

获取音视频轨道信息，可以在prepared/playing/paused状态调用。获取所有音视轨道信息，应在数据加载回调后调用。使用callback方式异步获取返回值。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void--><!--Device-AVPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MediaDescription](arkts-media-multimedia-media-mediadescription-i.md)&gt;&gt; | 是 | 回调函数，当获取音视频轨道信息成功，err为undefined，data为获取到的 MediaDescription数组；否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by callback. |

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

获取音视频轨道信息，可以在prepared/playing/paused状态调用。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-getTrackDescription(): Promise<Array<MediaDescription>>--><!--Device-AVPlayer-getTrackDescription(): Promise<Array<MediaDescription>>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;[MediaDescription](arkts-media-multimedia-media-mediadescription-i.md)&gt;&gt; | Promise对象，返回音视频轨道信息MediaDescription数组。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

参见 [getTrackDescription](#gettrackdescription)

## getTrackSelectionFilter

```TypeScript
getTrackSelectionFilter(): Promise<TrackSelectionFilter>
```

获取播放器当前配置的轨道选择过滤器。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVPlayer-getTrackSelectionFilter(): Promise<TrackSelectionFilter>--><!--Device-AVPlayer-getTrackSelectionFilter(): Promise<TrackSelectionFilter>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[TrackSelectionFilter](arkts-media-media-trackselectionfilter-i.md)&gt; | Promise对象，返回当前配置的轨道选择过滤器。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function test() {
  let player = await media.createAVPlayer();
  player.getTrackSelectionFilter().then((selectionFilter: media.TrackSelectionFilter) => {
    console.info(`Succeeded in getting TrackSelectionFilter: ${selectionFilter}`);
  }).catch((err: BusinessError) => {
    console.error('Failed to getTrackSelectionFilter, error message is:' + err.message);
  });
}
```

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

暂停播放音视频资源，只能在playing状态调用。使用callback方式异步获取返回值。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-pause(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-pause(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 暂停播放的回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by callback. |

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

暂停播放音视频资源，只能在playing状态调用。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-pause(): Promise<void>--><!--Device-AVPlayer-pause(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

参见 [pause](#pause)

## play

```TypeScript
play(callback: AsyncCallback<void>): void
```

开始播放音视频资源，只能在prepared/paused/completed状态调用。使用callback方式异步获取返回值。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-play(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-play(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 开始播放的回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by callback. |

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

开始播放音视频资源，只能在prepared/paused/completed状态调用。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-play(): Promise<void>--><!--Device-AVPlayer-play(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

参见 [play](#play)

## prepare

```TypeScript
prepare(callback: AsyncCallback<void>): void
```

准备播放音频/视频，需在stateChange事件成 功触发至initialized状态后，才能调用。使用callback方式异步获取返回值。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-prepare(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-prepare(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 准备播放的回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by callback. |
| [5400106](../errorcode-media.md#5400106-不支持的规格) | Unsupported format. Return by callback. |

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

准备播放音频/视频，需在stateChange事件成 功触发至initialized状态后，才能调用。使用Promise异步回调。如果应用使用到多个短视频频繁切换的场景，为了提升切换性能，可以考虑创建多个AVPlayer对象，提前准备下一个视频，详情参见 [在线短视频流畅切换](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-smooth-switching)。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-prepare(): Promise<void>--><!--Device-AVPlayer-prepare(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |
| [5400106](../errorcode-media.md#5400106-不支持的规格) | Unsupported format. Return by promise. |

**示例**

参见 [prepare](#prepare)

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

销毁播放资源，除released状态外，均可以调用。使用callback方式异步获取返回值。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-release(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 销毁播放的回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by callback. |

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

销毁播放资源，除released状态，都可以调用。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-release(): Promise<void>--><!--Device-AVPlayer-release(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

参见 [release](#release)

## reset

```TypeScript
reset(callback: AsyncCallback<void>): void
```

重置播放，只能在initialized/prepared/playing/paused/completed/stopped/error状态调用。使用callback方式异步获取返回值。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-reset(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-reset(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 重置播放的回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by callback. |

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

重置播放，只能在initialized/prepared/playing/paused/completed/stopped/error状态调用。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-reset(): Promise<void>--><!--Device-AVPlayer-reset(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

参见 [reset](#reset)

## seek

```TypeScript
seek(timeMs: int, mode?: SeekMode): void
```

跳转到指定播放位置，只能在prepared/playing/paused/completed状态调用，可以通过 on('seekDone')事件确认是否生效。

> **注意：**&gt;
> 从API版本26.0.0开始，直播场景支持seek。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-seek(timeMs: int, mode?: SeekMode): void--><!--Device-AVPlayer-seek(timeMs: int, mode?: SeekMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | int | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为 [0, [duration](../../../reference/apis-media-kit/arkts-apis-media-AVPlayer.md)]。<br>当模式为 SEEK_CONTINUOUS时，可以取值-1，表示SEEK_CONTINUOUS模式结束。该值必须为整数。 |
| mode | [SeekMode](arkts-media-multimedia-media-seekmode-e.md) | 否 | 基于视频I帧的跳转模式，默认为SEEK_PREV_SYNC模式，**仅在视频资源播放时设置**。 |

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

## seekToDefaultPosition

```TypeScript
seekToDefaultPosition(): void
```

跳转到播放源的默认接入点。直播流为当前推荐的最新接入点；点播视频通常为视频起始位置（等同于seek(0)）。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVPlayer-seekToDefaultPosition(): void--><!--Device-AVPlayer-seekToDefaultPosition(): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by callback. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function test(){
  let avPlayer = await media.createAVPlayer();
  try {
    avPlayer.seekToDefaultPosition()
    console.info('Succeeded in calling seekToDefaultPosition.');
  } catch (err) {
    console.error(`Failed to seekToDefaultPosition. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## selectTrack

```TypeScript
selectTrack(index: int, mode?: SwitchMode): Promise<void>
```

使用AVPlayer播放多音视频轨资源时，允许用户以指定模式切换到指定轨道以继续播放。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-selectTrack(index: int, mode?: SwitchMode): Promise<void>--><!--Device-AVPlayer-selectTrack(index: int, mode?: SwitchMode): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 多音视频资源的轨道索引。该值必须为整数。<br>取值约束：可通过 [getTrackDescription](#gettrackdescription)接口返回的音视频轨道信息 MediaDescription中读取的key为MD_KEY_TRACK_INDEX所对应的值。<br>每个 key值的Object类型和范围，请参考MediaDescriptionKey对应Key值的说明。 |
| mode | [SwitchMode](arkts-media-multimedia-media-switchmode-e.md) | 否 | 切换轨道的模式。<br>取值约束：该模式仅适用于视频轨道的切换。<br>默认值：SMOOTH模式，在片段末尾进行切换，以确保视频播放的连续性。 **仅在DASH/HLS协议网络流视频轨切换时生效。**<br>从API版本26.0.0开始支持HLS协议网络流视频。<br>**起始版本：** 26.0.0 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The parameter check failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer: media.AVPlayer = await media.createAVPlayer();
  let audioTrackIndex: Object = 0;
  avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
    if (arrList) {
      // 遍历轨道描述列表，提取非首个轨道的索引用于音频轨道选择
      for (let i = 0; i < arrList.length; i++) {
        if (i != 0) {
          // 获取当前轨道的索引。
          audioTrackIndex = arrList[i][media.MediaDescriptionKey.MD_KEY_TRACK_INDEX];
        }
      }
    } else {
      console.error(`Failed to get TrackDescription.Code:${error.code},message:${error.message}`);
    }
  });

  // 选择其中一个音频轨道。
  avPlayer.selectTrack(parseInt(audioTrackIndex.toString()));
}
```

## setMediaMuted

```TypeScript
setMediaMuted(mediaType: MediaType, muted: boolean): Promise<void>
```

设置音频静音/取消音频静音，从API version 20开始，增加支持设置画面显示/不显示。使用Promise异步回调。只能在prepared/playing/paused/completed状态下调用。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-setMediaMuted(mediaType: MediaType, muted: boolean): Promise<void>--><!--Device-AVPlayer-setMediaMuted(mediaType: MediaType, muted: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaType | [MediaType](arkts-media-multimedia-media-mediatype-e.md) | 是 | 媒体类型枚举。<br>**API version 12-19**：仅支持设置MEDIA_TYPE_AUD。<br>**API version 20及以后**：增 加支持设置MEDIA_TYPE_VID。 |
| muted | boolean | 是 | API version 12-19**：仅支持设置音频播放策略，表示音频是否静音播放。true为静音播放，false为取消静音播放。<br> **API version 20及以后**：增加支持设置视频播放策略，表示视频画面是否关闭。true为关闭画面，false为恢复画面。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | The parameter check failed. Return by promise. |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

```TypeScript
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
  avPlayer.prepare().then(() => {
    console.info('Succeeded in preparing');
    avPlayer.setMediaMuted(media.MediaType.MEDIA_TYPE_AUD, true);
  }, (err: BusinessError) => {
    console.error(`Failed to prepare.Code:${err.code},message:${err.message}`);
  });
}
```

## setMediaSource

```TypeScript
setMediaSource(src: MediaSource, strategy?: PlaybackStrategy): Promise<void>
```

流媒体预下载资源设置，下载url对应的流媒体数据，并暂存在内存中。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-setMediaSource(src: MediaSource, strategy?: PlaybackStrategy): Promise<void>--><!--Device-AVPlayer-setMediaSource(src: MediaSource, strategy?: PlaybackStrategy): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [MediaSource](arkts-media-multimedia-media-mediasource-i.md) | 是 | 流媒体预下载媒体来源。 |
| strategy | [PlaybackStrategy](arkts-media-multimedia-media-playbackstrategy-i.md) | 否 | 流媒体预下载播放策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

```TypeScript
async function test(){
  let player = await media.createAVPlayer();
  let headers: Record<string, string> = {'User-Agent' : 'User-Agent-Value'};
  let mediaSource : media.MediaSource = media.createMediaSourceWithUrl('http://xxx',  headers);
  let playStrategy : media.PlaybackStrategy = {
    preferredWidth: 1,
    preferredHeight: 2,
    preferredBufferDuration: 3,
    preferredHdr: false,
    preferredBufferDurationForPlaying: 1,
    thresholdForAutoQuickPlay: 5
  };
  player.setMediaSource(mediaSource, playStrategy);
}
```

## setPlaybackStrategy

```TypeScript
setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>
```

设置播放策略，只能在initialized状态下调用。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>--><!--Device-AVPlayer-setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | [PlaybackStrategy](arkts-media-multimedia-media-playbackstrategy-i.md) | 是 | 播放策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

```TypeScript
import { common } from '@kit.AbilityKit';

let player = await media.createAVPlayer();
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let fileDescriptor = await context.resourceManager.getRawFd('xxx.mp4');
player.fdSrc = fileDescriptor;
let playStrategy : media.PlaybackStrategy = {
  preferredWidth: 1,
  preferredHeight: 2,
  preferredBufferDuration: 3,
  preferredHdr: false,
  mutedMediaType: media.MediaType.MEDIA_TYPE_AUD,
  preferredBufferDurationForPlaying: 1,
  thresholdForAutoQuickPlay: 5
};
player.setPlaybackStrategy(playStrategy);
```

## setTrackSelectionFilter

```TypeScript
setTrackSelectionFilter(filter : TrackSelectionFilter): Promise<void>
```

为播放器设置轨道选择过滤器，播放器将使用该过滤器来选择可用的轨道用于播放。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AVPlayer-setTrackSelectionFilter(filter : TrackSelectionFilter): Promise<void>--><!--Device-AVPlayer-setTrackSelectionFilter(filter : TrackSelectionFilter): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [TrackSelectionFilter](arkts-media-media-trackselectionfilter-i.md) | 是 | 轨道选择过滤器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

async function test() {
  let player = await media.createAVPlayer();
  let selectionFilter: media.TrackSelectionFilter = {
    maxVideoBitrate: 80000,
    minVideoBitrate: 0,
    maxVideoFrameRate: 60,
    minVideoFrameRate: 0,
    maxVideoResolution: { width: 1080, height: 720 },
    minVideoResolution: { width: 0, height: 0 },
    preferredVideoMimeTypes: [media.CodecMimeType.VIDEO_AVC],
    maxAudioBitrate: 8000,
    minAudioBitrate: 0,
    maxAudioChannels: 3,
    preferredAudioMimeTypes: [media.CodecMimeType.AUDIO_AAC, media.CodecMimeType.AUDIO_MP3],
    preferredAudioLanguages: [],
    preferredSubtitleLanguages: []
  };
  player.setTrackSelectionFilter(selectionFilter).then(() => {
    console.info('Succeeded in setting TrackSelectionFilter');
  }).catch((err: BusinessError) => {
    console.error('Failed to setTrackSelectionFilter, error message is:' + err.message);
  });
}
```

## setVolume

```TypeScript
setVolume(volume: double): void
```

设置媒体播放音量，只能在prepared/playing/paused/completed状态调用，可以通过 on('volumeChange')事件确认是否生效。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-setVolume(volume: double): void--><!--Device-AVPlayer-setVolume(volume: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | double | 是 | 指定的相对音量大小，取值范围为[0.00-1.00]，1表示最大音量，即100%。 |

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

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止播放音视频资源，只能在prepared/playing/paused/completed状态调用。使用callback方式异步获取返回值。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-stop(callback: AsyncCallback<void>): void--><!--Device-AVPlayer-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 停止播放的回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by callback. |

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

停止播放音视频资源，只能在prepared/playing/paused/completed状态调用。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AVPlayer-stop(): Promise<void>--><!--Device-AVPlayer-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) | Operation not allowed. Return by promise. |

**示例**

参见 [stop](#stop)

