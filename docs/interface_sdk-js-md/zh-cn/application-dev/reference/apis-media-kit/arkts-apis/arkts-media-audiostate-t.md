# AudioState

```TypeScript
type AudioState = 'idle' | 'playing' | 'paused' | 'stopped' | 'error'
```

音频播放的状态机。可通过state属性获取当前状态。

> **说明：**
> 
> 从API version 6开始支持，从API version 9开始废弃，建议使用[AVPlayerState](arkts-media-media-avplayerstate-t.md)替代。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 9

**替代接口：** [AVPlayerState](arkts-media-media-avplayerstate-t.md)

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

| 类型 |
| --- |
| 'idle' |
| 'playing' |
| 'paused' |
| 'stopped' |
| 'error' |
