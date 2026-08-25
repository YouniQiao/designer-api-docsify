# createAudioRenderer

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## createAudioRenderer

```TypeScript
function createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer>): void
```

获取音频渲染器。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AudioRendererOptions](arkts-audio-audio-audiorendereroptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRenderer](arkts-audio-audio-audiorenderer-i.md)&gt; | 是 |


## createAudioRenderer

```TypeScript
function createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer>
```

获取音频渲染器。使用Promise异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [AudioRendererOptions](arkts-audio-audio-audiorendereroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AudioRenderer](arkts-audio-audio-audiorenderer-i.md)&gt; |
