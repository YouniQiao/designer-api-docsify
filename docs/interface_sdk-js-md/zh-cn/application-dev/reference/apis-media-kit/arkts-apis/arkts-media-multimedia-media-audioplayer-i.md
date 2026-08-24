# AudioPlayer


> **说明：**&gt;
> 从API version 6开始支持，从API version 9开始废弃，建议使用[AVPlayer](arkts-media-media-n.md)替代。
音频播放管理类，用于管理和播放音频媒体。在调用AudioPlayer的方法前，需要先通过 [createAudioPlayer()](arkts-media-media-createaudioplayer-f.md)构建一个AudioPlayer实例。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [media](arkts-media-media-n.md)

<!--Device-unnamed-interface AudioPlayer--><!--Device-unnamed-interface AudioPlayer-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

## 导入模块

```TypeScript
import { media } from '@kit.MediaKit';
```

## getTrackDescription

```TypeScript
getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void
```

获取音频轨道信息。需在'dataLoad'事件成功触发后，才能调用。通过回调函数获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)(callback: AsyncCallback&lt;Array&lt;MediaDescription&gt;&gt;)

<!--Device-AudioPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void--><!--Device-AudioPlayer-getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[MediaDescription](arkts-media-multimedia-media-mediadescription-i.md)&gt;&gt; | 是 | 回调函数。获取音频轨道信息成功时，err为undefined，data为获取到的 MediaDescription数组，否则为错误对象。 |

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

获取音频轨道信息。需在'dataLoad'事件成功触发后，才能调用。通过Promise获取返回值。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getTrackDescription](arkts-media-media-avplayer-i.md#gettrackdescription)()

<!--Device-AudioPlayer-getTrackDescription(): Promise<Array<MediaDescription>>--><!--Device-AudioPlayer-getTrackDescription(): Promise<Array<MediaDescription>>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;[MediaDescription](arkts-media-multimedia-media-mediadescription-i.md)&gt;&gt; | 音频轨道信息MediaDescription数组Promise返回值。 |

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

<!--Device-AudioPlayer-on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void--><!--Device-AudioPlayer-on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'audioInterrupt' | 是 | 音频焦点变化事件回调类型，支持的事件：'audioInterrupt'。 |
| callback | (info: audio.InterruptEvent) =&gt; void | 是 | 音频焦点变化事件回调方法。 |

## on('bufferingUpdate')

```TypeScript
on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void
```

开始订阅音频缓存更新事件。仅网络播放支持该订阅事件。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('bufferingUpdate')
> 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler)

<!--Device-AudioPlayer-on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void--><!--Device-AudioPlayer-on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'bufferingUpdate' | 是 | 音频缓存事件回调类型，支持的事件：'bufferingUpdate'。 |
| callback | (infoType: BufferingInfoType, value: number) =&gt; void | 是 | 音频缓存事件回调方法。<br> BufferingInfoTypevalue值固定为0。 |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

开始订阅音频播放事件。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('stateChange')
> 替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | 是 | 播放事件回调类型，支持的事件包括：'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange'。<br>- 'play'：完成 play()调用，音频开始播放，触发该事件。<br>- 'pause'：完成 pause()调用，音频暂停播放，触发该事件。<br>- 'stop'：完成stop() 调用，音频停止播放，触发该事件。<br>- 'reset'：完成reset()调用，播放器重置，触发该事件。<br>- 'dataLoad'：完成音频数 据加载后触发该事件，即src属性设置完成后触发该事件。<br>- 'finish'：完成音频播放后触发该事件。<br>- 'volumeChange'：完成 setVolume()调用，播放音量改变后触发该事件。 |
| callback | () =&gt; void | 是 | 播放事件回调方法。 |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

开始订阅音频播放错误事件，当上报error错误事件后，用户需处理error事件，退出播放操作。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('error')替
> 代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** on(type: 'error', callback: ErrorCallback)

<!--Device-AudioPlayer-on(type: 'error', callback: ErrorCallback): void--><!--Device-AudioPlayer-on(type: 'error', callback: ErrorCallback): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'error' | 是 | 播放错误事件回调类型，支持的事件包括：'error'。<br>- 'error'：音频播放中发生错误，触发该事件。 |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 | 播放错误事件回调方法。 |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

开始订阅音频播放事件。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('stateChange')
> 替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | 是 | 播放事件回调类型，支持的事件包括：'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange'。<br>- 'play'：完成 play()调用，音频开始播放，触发该事件。<br>- 'pause'：完成 pause()调用，音频暂停播放，触发该事件。<br>- 'stop'：完成stop() 调用，音频停止播放，触发该事件。<br>- 'reset'：完成reset()调用，播放器重置，触发该事件。<br>- 'dataLoad'：完成音频数 据加载后触发该事件，即src属性设置完成后触发该事件。<br>- 'finish'：完成音频播放后触发该事件。<br>- 'volumeChange'：完成 setVolume()调用，播放音量改变后触发该事件。 |
| callback | () =&gt; void | 是 | 播放事件回调方法。 |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

开始订阅音频播放事件。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('stateChange')
> 替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | 是 | 播放事件回调类型，支持的事件包括：'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange'。<br>- 'play'：完成 play()调用，音频开始播放，触发该事件。<br>- 'pause'：完成 pause()调用，音频暂停播放，触发该事件。<br>- 'stop'：完成stop() 调用，音频停止播放，触发该事件。<br>- 'reset'：完成reset()调用，播放器重置，触发该事件。<br>- 'dataLoad'：完成音频数 据加载后触发该事件，即src属性设置完成后触发该事件。<br>- 'finish'：完成音频播放后触发该事件。<br>- 'volumeChange'：完成 setVolume()调用，播放音量改变后触发该事件。 |
| callback | () =&gt; void | 是 | 播放事件回调方法。 |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

开始订阅音频播放事件。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('stateChange')
> 替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | 是 | 播放事件回调类型，支持的事件包括：'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange'。<br>- 'play'：完成 play()调用，音频开始播放，触发该事件。<br>- 'pause'：完成 pause()调用，音频暂停播放，触发该事件。<br>- 'stop'：完成stop() 调用，音频停止播放，触发该事件。<br>- 'reset'：完成reset()调用，播放器重置，触发该事件。<br>- 'dataLoad'：完成音频数 据加载后触发该事件，即src属性设置完成后触发该事件。<br>- 'finish'：完成音频播放后触发该事件。<br>- 'volumeChange'：完成 setVolume()调用，播放音量改变后触发该事件。 |
| callback | () =&gt; void | 是 | 播放事件回调方法。 |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

开始订阅音频播放事件。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('stateChange')
> 替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | 是 | 播放事件回调类型，支持的事件包括：'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange'。<br>- 'play'：完成 play()调用，音频开始播放，触发该事件。<br>- 'pause'：完成 pause()调用，音频暂停播放，触发该事件。<br>- 'stop'：完成stop() 调用，音频停止播放，触发该事件。<br>- 'reset'：完成reset()调用，播放器重置，触发该事件。<br>- 'dataLoad'：完成音频数 据加载后触发该事件，即src属性设置完成后触发该事件。<br>- 'finish'：完成音频播放后触发该事件。<br>- 'volumeChange'：完成 setVolume()调用，播放音量改变后触发该事件。 |
| callback | () =&gt; void | 是 | 播放事件回调方法。 |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

开始订阅音频播放事件。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('stateChange')
> 替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | 是 | 播放事件回调类型，支持的事件包括：'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange'。<br>- 'play'：完成 play()调用，音频开始播放，触发该事件。<br>- 'pause'：完成 pause()调用，音频暂停播放，触发该事件。<br>- 'stop'：完成stop() 调用，音频停止播放，触发该事件。<br>- 'reset'：完成reset()调用，播放器重置，触发该事件。<br>- 'dataLoad'：完成音频数 据加载后触发该事件，即src属性设置完成后触发该事件。<br>- 'finish'：完成音频播放后触发该事件。<br>- 'volumeChange'：完成 setVolume()调用，播放音量改变后触发该事件。 |
| callback | () =&gt; void | 是 | 播放事件回调方法。 |

## on('timeUpdate')

```TypeScript
on(type: 'timeUpdate', callback: Callback<number>): void
```

开始订阅音频播放时间更新事件。处于播放状态时，每隔1s上报一次该事件。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('timeUpdate')
> 替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** on(type: 'timeUpdate', callback: Callback&lt;int&gt;)

<!--Device-AudioPlayer-on(type: 'timeUpdate', callback: Callback<number>): void--><!--Device-AudioPlayer-on(type: 'timeUpdate', callback: Callback<number>): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'timeUpdate' | 是 | 播放事件回调类型，支持的事件包括：'timeUpdate'。<br>- 'timeUpdate'：音频播放时间戳更新，开始播放后自动触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 | 播放事件回调方法。回调方法入参为更新后的时间戳。 |

## on('play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange')

```TypeScript
on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void
```

开始订阅音频播放事件。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> AVPlayer.on('stateChange')
> 替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)

<!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void--><!--Device-AudioPlayer-on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange' | 是 | 播放事件回调类型，支持的事件包括：'play' \| 'pause' \| 'stop' \| 'reset' \| 'dataLoad' \| 'finish' \| 'volumeChange'。<br>- 'play'：完成 play()调用，音频开始播放，触发该事件。<br>- 'pause'：完成 pause()调用，音频暂停播放，触发该事件。<br>- 'stop'：完成stop() 调用，音频停止播放，触发该事件。<br>- 'reset'：完成reset()调用，播放器重置，触发该事件。<br>- 'dataLoad'：完成音频数 据加载后触发该事件，即src属性设置完成后触发该事件。<br>- 'finish'：完成音频播放后触发该事件。<br>- 'volumeChange'：完成 setVolume()调用，播放音量改变后触发该事件。 |
| callback | () =&gt; void | 是 | 播放事件回调方法。 |

## pause

```TypeScript
pause(): void
```

暂停播放音频资源。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.pause](arkts-media-media-avplayer-i.md#pause)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [pause](arkts-media-media-avplayer-i.md#pause)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioPlayer-pause(): void--><!--Device-AudioPlayer-pause(): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

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

## play

```TypeScript
play(): void
```

开始播放音频资源，需在'dataLoad'事件成功触发后，才能调用。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.play](arkts-media-media-avplayer-i.md#play)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [play](arkts-media-media-avplayer-i.md#play)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioPlayer-play(): void--><!--Device-AudioPlayer-play(): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

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

## release

```TypeScript
release(): void
```

释放音频资源。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.release](arkts-media-media-avplayer-i.md#release)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [release](arkts-media-media-avplayer-i.md#release)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioPlayer-release(): void--><!--Device-AudioPlayer-release(): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

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

## reset

```TypeScript
reset(): void
```

重置播放音频资源。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.reset](arkts-media-media-avplayer-i.md#reset)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [reset](arkts-media-media-avplayer-i.md#reset)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioPlayer-reset(): void--><!--Device-AudioPlayer-reset(): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

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

## seek

```TypeScript
seek(timeMs: number): void
```

跳转到指定播放位置。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](arkts-media-media-avplayer-i.md#seek)替代
> 。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [seek](arkts-media-media-avplayer-i.md#seek)

<!--Device-AudioPlayer-seek(timeMs: number): void--><!--Device-AudioPlayer-seek(timeMs: number): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围[0, duration]。 |

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

## setVolume

```TypeScript
setVolume(vol: number): void
```

设置音量。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.setVolume](arkts-media-media-avplayer-i.md#setvolume)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [setVolume](arkts-media-media-avplayer-i.md#setvolume)

<!--Device-AudioPlayer-setVolume(vol: number): void--><!--Device-AudioPlayer-setVolume(vol: number): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vol | number | 是 | 指定的相对音量大小，取值范围为[0.00-1.00]，1表示最大音量，即100%。 |

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
stop(): void
```

停止播放音频资源。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用
> [AVPlayer.stop](arkts-media-media-avplayer-i.md#stop)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [stop](arkts-media-media-avplayer-i.md#stop)(callback: AsyncCallback&lt;void&gt;)

<!--Device-AudioPlayer-stop(): void--><!--Device-AudioPlayer-stop(): void-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

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

## audioInterruptMode

```TypeScript
audioInterruptMode?: audio.InterruptMode
```

音频焦点模型。

**类型：** audio.InterruptMode

**起始版本：** 9

**废弃版本：** 9

**替代接口：** audioInterruptMode

<!--Device-AudioPlayer-audioInterruptMode?: audio.InterruptMode--><!--Device-AudioPlayer-audioInterruptMode?: audio.InterruptMode-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

## currentTime

```TypeScript
readonly currentTime: number
```

音频的当前播放位置，单位为毫秒（ms）。

**类型：** number

**起始版本：** 6

**废弃版本：** 9

**替代接口：** currentTime

<!--Device-AudioPlayer-readonly currentTime: number--><!--Device-AudioPlayer-readonly currentTime: number-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

## duration

```TypeScript
readonly duration: number
```

音频时长，单位为毫秒（ms）。

**类型：** number

**起始版本：** 6

**废弃版本：** 9

**替代接口：** duration

<!--Device-AudioPlayer-readonly duration: number--><!--Device-AudioPlayer-readonly duration: number-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

## fdSrc

```TypeScript
fdSrc: AVFileDescriptor
```

音频媒体文件描述，使用场景：应用中的音频资源被连续存储在同一个文件中。  
**使用示例**：假设一个连续存储的音乐文件:音乐1(地址偏移:0，字节长度:100)音乐2(地址偏移:101，字节长度:50)音乐3(地址偏移:151，字节长度:150)
1. 播放音乐1：AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; }
2. 播放音乐2：AVFileDescriptor { fd = 资源句柄; offset = 101; length = 50; }
3. 播放音乐3：AVFileDescriptor { fd = 资源句柄; offset = 151; length = 150; }
假设是一个独立的音乐文件: 请使用src=fd://xx

**类型：** [AVFileDescriptor](arkts-media-multimedia-media-avfiledescriptor-i.md)

**起始版本：** 9

**废弃版本：** 9

**替代接口：** fdSrc

<!--Device-AudioPlayer-fdSrc: AVFileDescriptor--><!--Device-AudioPlayer-fdSrc: AVFileDescriptor-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

## loop

```TypeScript
loop: boolean
```

音频循环播放属性，设置为'true'表示循环播放。

**类型：** boolean

**起始版本：** 6

**废弃版本：** 9

**替代接口：** loop

<!--Device-AudioPlayer-loop: boolean--><!--Device-AudioPlayer-loop: boolean-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

## src

```TypeScript
src: string
```

音频媒体URI，支持当前主流的音频格式(m4a、aac、mp3、ogg、wav、amr)。  
**支持路径示例**：
1. fd类型播放：fd://xx

2. http网络播放: http://xx
3. https网络播放: https://xx
4. hls网络播放路径：http://xx或者https://xx
ohos.permission.READ_MEDIA 或 ohos.permission.INTERNET。

**类型：** string

**起始版本：** 6

**废弃版本：** 9

**替代接口：** url

**需要权限：** ohos.permission.READ_MEDIA or ohos.permission.INTERNET

<!--Device-AudioPlayer-src: string--><!--Device-AudioPlayer-src: string-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

## state

```TypeScript
readonly state: AudioState
```

可以查询音频播放的状态，该状态不可作为调用play/pause/stop等状态切换的触发条件。

**类型：** [AudioState](arkts-media-audiostate-t.md)

**起始版本：** 6

**废弃版本：** 9

**替代接口：** state

<!--Device-AudioPlayer-readonly state: AudioState--><!--Device-AudioPlayer-readonly state: AudioState-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

