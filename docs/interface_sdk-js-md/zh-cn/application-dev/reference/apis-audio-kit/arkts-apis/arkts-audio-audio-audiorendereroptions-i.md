# AudioRendererOptions

```TypeScript
interface AudioRendererOptions
```

音频渲染器选项信息。

**起始版本：** 8

<!--Device-audio-interface AudioRendererOptions--><!--Device-audio-interface AudioRendererOptions-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

## 导入模块

```TypeScript
import { audio } from '@kit.AudioKit';
```

## keepActiveOnSilence

```TypeScript
keepActiveOnSilence?: boolean
```

是否在静音播放时保持音频通路运行，默认值为false。在默认情况下，播放静音数据，包括音量为0和输入静音数据，系统会在检测到后停止音频通路和硬件，以达到节省功耗的效果。当恢复有声数据时，系统会立即恢复。但恢复存在短暂耗时，如果应用需要在播放静音数据时保持通路运行，以确保数据输出时间固定，可通过此接口设置关闭。关闭效果仅在音频播放流运行阶段有效。默认值：false。

**类型：** boolean

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioRendererOptions-keepActiveOnSilence?: boolean--><!--Device-AudioRendererOptions-keepActiveOnSilence?: boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

## offloadAllowed

```TypeScript
offloadAllowed?: boolean
```

是否允许使用低功耗模式。当音频播放使用场景为音乐或听书时，系统会默认使用低功耗模式播放音频，可在后台播放时降低功耗。然而低功耗模式下，音频系统内缓存数据量很大，在实时生成音频数据的场景并不适用，此时开发者可设置不使用此模式。默认值：true。

**类型：** boolean

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AudioRendererOptions-offloadAllowed?: boolean--><!--Device-AudioRendererOptions-offloadAllowed?: boolean-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

## privacyType

```TypeScript
privacyType?: AudioPrivacyType
```

表示音频流是否可以被其他应用录制，默认值为0。

**类型：** [AudioPrivacyType](arkts-audio-audio-audioprivacytype-e.md)

**起始版本：** 10

<!--Device-AudioRendererOptions-privacyType?: AudioPrivacyType--><!--Device-AudioRendererOptions-privacyType?: AudioPrivacyType-End-->

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

## rendererInfo

```TypeScript
rendererInfo: AudioRendererInfo
```

音频渲染器信息。

**类型：** [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md)

**起始版本：** 8

<!--Device-AudioRendererOptions-rendererInfo: AudioRendererInfo--><!--Device-AudioRendererOptions-rendererInfo: AudioRendererInfo-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

## streamInfo

```TypeScript
streamInfo: AudioStreamInfo
```

音频流信息。

**类型：** [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)

**起始版本：** 8

<!--Device-AudioRendererOptions-streamInfo: AudioStreamInfo--><!--Device-AudioRendererOptions-streamInfo: AudioStreamInfo-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Renderer
