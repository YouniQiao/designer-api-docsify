# createAudioRenderer

## 导入模块

```TypeScript
import { audio } from '@kit.AudioKit';
```

## createAudioRenderer

```TypeScript
function createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer>): void
```

获取音频渲染器。使用callback异步回调。

**起始版本：** 8

<!--Device-audio-function createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer>): void--><!--Device-audio-function createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioRendererOptions](arkts-audio-audio-audiorendereroptions-i.md) | 是 | 配置渲染器。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRenderer](arkts-audio-audio-audiorenderer-i.md)&gt; | 是 | 回调函数。当获取音频渲染器成功，err为undefined，data为获取到的音频渲染器对象；否则为错误对象。 |

**示例**

```TypeScript
import { audio } from '@kit.AudioKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};

let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};

let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

let audioRenderer: audio.AudioRenderer;

audio.createAudioRenderer(audioRendererOptions,(err, data) => {
  if (err) {
    console.error(`AudioRenderer Created: Error: ${err}`);
  } else {
    console.info('AudioRenderer Created: SUCCESS');
    audioRenderer = data;
  }
});
```

```TypeScript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};

let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};

let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

let audioRenderer: audio.AudioRenderer;

audio.createAudioRenderer(audioRendererOptions).then((data) => {
  audioRenderer = data;
  console.info('AudioFrameworkRenderLog: AudioRenderer Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`AudioFrameworkRenderLog: AudioRenderer Created : ERROR : ${err}`);
});
```


## createAudioRenderer

```TypeScript
function createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer | null>): void
```

获取一个 [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) 实例。 此方法使用 Promise 方式返回渲染器实例。AudioRenderer 实例用于播放流式音频数据。 使用 AudioRenderer API 时，为达到更好的性能和更低的功耗，应用需遵循以下指导： 在音乐或有声书后台播放场景下，可参考最佳实践文档《音乐播放场景低功耗规则》，实现低功耗。 在导航场景下，可参考《导航定位场景低功耗规则》，实现低功耗。应用开发者还需注意应用进入后台时的处理，检查音频播放是否仍需继续，参见《音频资源使用规范》。 避免持续发送静音音频数据造成系统资源浪费，否则系统检测到该行为后会采取管控措施，参见《音频播放规范》。如果您想使用 AudioRenderer API 实现音乐播放应用，还需考虑多种交互场景，参见《音频应用开发实践》。

**起始版本：** 23

<!--Device-audio-function createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer | null>): void--><!--Device-audio-function createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer | null>): void-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioRendererOptions](arkts-audio-audio-audiorendereroptions-i.md) | 是 | 配置渲染器。 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRenderer](arkts-audio-audio-audiorenderer-i.md) \| null&gt; | 是 | 回调函数用于返回音频渲染器实例，或在发生错误时返回 null。 |

**示例**

参见 [createAudioRenderer](#createaudiorenderer)


## createAudioRenderer

```TypeScript
function createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer>
```

获取音频渲染器。使用Promise异步回调。

**起始版本：** 8

<!--Device-audio-function createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer>--><!--Device-audio-function createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioRendererOptions](arkts-audio-audio-audiorendereroptions-i.md) | 是 | 配置渲染器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AudioRenderer](arkts-audio-audio-audiorenderer-i.md)&gt; | Promise对象，返回音频渲染器对象。 |

**示例**

参见 [createAudioRenderer](#createaudiorenderer)


## createAudioRenderer

```TypeScript
function createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer | null>
```

获取一个 [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) 实例。 此方法使用 Promise 方式返回渲染器实例。AudioRenderer 实例用于播放流式音频数据。 使用 AudioRenderer API 时，为达到更好的性能和更低的功耗，应用需遵循以下指导： 在音乐或有声书后台播放场景下，可参考最佳实践文档《音乐播放场景低功耗规则》，实现低功耗。 在导航场景下，可参考《导航定位场景低功耗规则》，实现低功耗。应用开发者还需注意应用进入后台时的处理，检查音频播放是否仍需继续，参见《音频资源使用规范》。 避免持续发送静音音频数据造成系统资源浪费，否则系统检测到该行为后会采取管控措施，参见《音频播放规范》。如果您想使用 AudioRenderer API 实现音乐播放应用，还需考虑多种交互场景，参见《音频应用开发实践》。

**起始版本：** 23

<!--Device-audio-function createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer | null>--><!--Device-audio-function createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer | null>-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AudioRendererOptions](arkts-audio-audio-audiorendereroptions-i.md) | 是 | 配置渲染器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AudioRenderer](arkts-audio-audio-audiorenderer-i.md) \| null&gt; | Promise对象，返回音频渲染器对象，或在发生错误时返回 null。 |

**示例**

参见 [createAudioRenderer](#createaudiorenderer)

