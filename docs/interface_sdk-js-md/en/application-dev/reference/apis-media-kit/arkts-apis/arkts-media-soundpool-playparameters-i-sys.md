# PlayParameters

表示音频池播放参数设置。

通过设置播放相关参数，来控制播放的音量，循环次数，播放优先级等参数。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface PlayParameters--><!--Device-unnamed-export interface PlayParameters-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

## parallelPlayFlag

```TypeScript
parallelPlayFlag?: boolean
```

表示是否和其他正在播放的音频并行播放的标识。

true：不抢占音频焦点，和其他正在播放的音频一起并行播放；false：抢占焦点打断其他正在播放的音频。默认值：false。

此接口为系统接口。

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PlayParameters-parallelPlayFlag?: boolean--><!--Device-PlayParameters-parallelPlayFlag?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**System API:** This is a system API.

