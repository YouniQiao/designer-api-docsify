# AudioRenderer

音频渲染。在使用AudioRenderer的接口之前，需先通过 [audio.createAudioRenderer](arkts-audio-audio-createaudiorenderer-f.md) 获取AudioRenderer实例。

**起始版本：** 8

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## getTarget

```TypeScript
getTarget(): RenderTarget
```

获取当前音频渲染器的渲染目标。

> **说明：**&gt;
> - 若未更改过渲染目标，将返回默认值[PLAYBACK](arkts-audio-audio-rendertarget-e-sys.md)。&gt;
> - 若调用此接口前，已经调用过[SetTarget](#settarget)，请确保
> [SetTarget](#settarget)的Promise对象已成功解析，否则获取到的数值可能不准确。

**起始版本：** 22

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [RenderTarget](arkts-audio-audio-rendertarget-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setTarget

```TypeScript
setTarget(target: RenderTarget): Promise<void>
```

设置音频渲染器的渲染目标。使用Promise异步回调。

> **说明：**&gt;
> - 此方法仅可在音频渲染器未处于运行或释放状态时调用，否则将返回错误。&gt;
> - 将渲染目标更改为非[PLAYBACK](arkts-audio-audio-rendertarget-e-sys.md)的模式后：
> 
> - 该音频渲染器的音频路由与中断策略将无法使用[AudioSessionManager](arkts-multimedia-audio.md)相关接口。
> 
> - 该音频渲染器的device type为[SYSTEM_PRIVATE](arkts-audio-audio-devicetype-e.md)。
> 
> - 调用[Start](arkts-audio-audio-audiorenderer-i.md#start)且audio
> scene不为[AUDIO_SCENE_VOICE_CHAT](arkts-audio-audio-audioscene-e.md)时，将返回错误码6800301。
> 
> - 调用
> [getAudioTime](arkts-audio-audio-audiorenderer-i.md#getaudiotime)或
> [getAudioTimeSync](arkts-audio-audio-audiorenderer-i.md#getaudiotimesync)时，将返回错误码6800301。
> 
> - 调用[getAudioTimestampInfo](arkts-audio-audio-audiorenderer-i.md#getaudiotimestampinfo)或
> [getAudioTimestampInfoSync](arkts-audio-audio-audiorenderer-i.md#getaudiotimestampinfosync)时，将返回错误码6800301。
> 
> - 调用[setDefaultOutputDevice](arkts-audio-audio-audiorenderer-i.md#setdefaultoutputdevice)时，将返回错
> 误码6800301。

**起始版本：** 22

**需要权限：** ohos.permission.INJECT_PLAYBACK_TO_AUDIO_CAPTURE

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | [RenderTarget](arkts-audio-audio-rendertarget-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800103](../errorcode-audio.md#6800103-状态不支持) |
| [6800104](../errorcode-audio.md#6800104-参数选项不支持) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |
