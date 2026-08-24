# createTonePlayer（系统接口）

## 导入模块

```TypeScript
import { audio } from '@kit.AudioKit';
```

## createTonePlayer

```TypeScript
function createTonePlayer(options: AudioRendererInfo, callback: AsyncCallback<TonePlayer>): void
```

创建DTMF播放器。使用callback异步回调。

**起始版本：** 9

<!--Device-audio-function createTonePlayer(options: AudioRendererInfo, callback: AsyncCallback<TonePlayer>): void--><!--Device-audio-function createTonePlayer(options: AudioRendererInfo, callback: AsyncCallback<TonePlayer>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Tone

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) | 是 | 配置音频渲染器信息。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[TonePlayer](arkts-audio-audio-toneplayer-i-sys.md)&gt; | 是 | 回调函数。当获取DTMF播放器成功，err为undefined，data为获取到的DTMF播放器对象；否则为错误对象。 |

**示例**

```TypeScript
import { audio } from '@kit.AudioKit';

let audioRendererInfo: audio.AudioRendererInfo = {
  usage : audio.StreamUsage.STREAM_USAGE_DTMF,
  rendererFlags : 0
};
let tonePlayer: audio.TonePlayer;

audio.createTonePlayer(audioRendererInfo, (err, data) => {
  console.info(`callback call createTonePlayer: audioRendererInfo: ${audioRendererInfo}`);
  if (err) {
    console.error(`callback call createTonePlayer return error: ${err.message}`);
  } else {
    console.info(`callback call createTonePlayer return data: ${data}`);
    tonePlayer = data;
  }
});
```

```TypeScript
import { audio } from '@kit.AudioKit';

let audioRendererInfo: audio.AudioRendererInfo = {
  usage : audio.StreamUsage.STREAM_USAGE_DTMF,
  rendererFlags : 0
};
let tonePlayer: audio.TonePlayer;

audio.createTonePlayer(audioRendererInfo, (err, data) => {
  console.info(`callback call createTonePlayer: audioRendererInfo: ${audioRendererInfo}`);
  if (err) {
    console.error(`callback call createTonePlayer return error: ${err.message}`);
  } else {
    console.info(`callback call createTonePlayer return data: ${data}`);
    tonePlayer = data;
  }
});
```

```TypeScript
import { audio } from '@kit.AudioKit';

let tonePlayer: audio.TonePlayer;
async function createTonePlayerBefore(){
  let audioRendererInfo: audio.AudioRendererInfo = {
    usage : audio.StreamUsage.STREAM_USAGE_DTMF,
    rendererFlags : 0
  };
  tonePlayer = await audio.createTonePlayer(audioRendererInfo);
}
```

```TypeScript
import { audio } from '@kit.AudioKit';

let tonePlayer: audio.TonePlayer;
async function createTonePlayerBefore(){
  let audioRendererInfo: audio.AudioRendererInfo = {
    usage : audio.StreamUsage.STREAM_USAGE_DTMF,
    rendererFlags : 0
  };
  tonePlayer = await audio.createTonePlayer(audioRendererInfo);
}
```


## createTonePlayer

```TypeScript
function createTonePlayer(options: AudioRendererInfo, callback: AsyncCallback<TonePlayer | null>): void
```

获取一个 [TonePlayer](arkts-audio-audio-toneplayer-i-sys.md) 实例，此方法采用异步回调方式返回渲染器实例。

**起始版本：** 23

<!--Device-audio-function createTonePlayer(options: AudioRendererInfo, callback: AsyncCallback<TonePlayer | null>): void--><!--Device-audio-function createTonePlayer(options: AudioRendererInfo, callback: AsyncCallback<TonePlayer | null>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Tone

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) | 是 | 配置音频渲染器信息。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[TonePlayer](arkts-audio-audio-toneplayer-i-sys.md) \| null&gt; | 是 | 回调函数用于返回 tonePlayer 实例，或在发生错误时返回 null。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |

**示例**

参见 [createTonePlayer](#createtoneplayer)


## createTonePlayer

```TypeScript
function createTonePlayer(options: AudioRendererInfo): Promise<TonePlayer>
```

创建DTMF播放器。使用Promise异步回调。

**起始版本：** 9

<!--Device-audio-function createTonePlayer(options: AudioRendererInfo): Promise<TonePlayer>--><!--Device-audio-function createTonePlayer(options: AudioRendererInfo): Promise<TonePlayer>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Tone

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) | 是 | 配置音频渲染器信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[TonePlayer](arkts-audio-audio-toneplayer-i-sys.md)&gt; | Promise对象，返回DTMF播放器对象。 |

**示例**

参见 [createTonePlayer](#createtoneplayer)


## createTonePlayer

```TypeScript
function createTonePlayer(options: AudioRendererInfo): Promise<TonePlayer | null>
```

获取一个 [TonePlayer](arkts-audio-audio-toneplayer-i-sys.md) 实例，此方法使用 Promise 返回渲染器实例。

**起始版本：** 23

<!--Device-audio-function createTonePlayer(options: AudioRendererInfo): Promise<TonePlayer | null>--><!--Device-audio-function createTonePlayer(options: AudioRendererInfo): Promise<TonePlayer | null>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Tone

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) | 是 | 配置音频渲染器信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[TonePlayer](arkts-audio-audio-toneplayer-i-sys.md) \| null&gt; | Promise 过去用于返回 tonePlayer 实例，或者在发生错误时返回 null。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not system App. |

**示例**

参见 [createTonePlayer](#createtoneplayer)

