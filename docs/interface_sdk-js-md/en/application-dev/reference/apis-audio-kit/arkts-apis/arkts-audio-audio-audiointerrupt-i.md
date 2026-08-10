# AudioInterrupt

音频监听事件传入的参数。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃，无替代接口。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRendererOptions

<!--Device-audio-interface AudioInterrupt--><!--Device-audio-interface AudioInterrupt-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## contentType

```TypeScript
contentType: ContentType
```

音频打断媒体类型。

**Type:** [ContentType](../../apis-arkui/arkts-components/arkts-arkui-contenttype-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRendererOptions#rendererInfo

<!--Device-AudioInterrupt-contentType: ContentType--><!--Device-AudioInterrupt-contentType: ContentType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## pauseWhenDucked

```TypeScript
pauseWhenDucked: boolean
```

音频打断时是否可以暂停音频播放。true表示音频播放可以在音频打断期间暂停，false表示音频播放不可以在音频打断期间暂停。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.InterruptEvent#hintType

<!--Device-AudioInterrupt-pauseWhenDucked: boolean--><!--Device-AudioInterrupt-pauseWhenDucked: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

## streamUsage

```TypeScript
streamUsage: StreamUsage
```

音频流使用类型。

**Type:** [StreamUsage](arkts-audio-audio-streamusage-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.multimedia.audio.AudioRendererOptions#rendererInfo

<!--Device-AudioInterrupt-streamUsage: StreamUsage--><!--Device-AudioInterrupt-streamUsage: StreamUsage-End-->

**System capability:** SystemCapability.Multimedia.Audio.Renderer

