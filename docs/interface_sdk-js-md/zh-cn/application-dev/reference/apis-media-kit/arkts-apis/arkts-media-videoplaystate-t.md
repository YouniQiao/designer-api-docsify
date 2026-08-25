# VideoPlayState

```TypeScript
type VideoPlayState = 'idle' | 'prepared' | 'playing' | 'paused' | 'stopped' | 'error'
```

视频播放的状态机，可通过state属性获取当前状态。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayerState](arkts-media-media-avplayerstate-t.md)替代。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [AVPlayerState](arkts-media-media-avplayerstate-t.md)

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

| 类型 |
| --- |
| 'idle' |
| 'prepared' |
| 'playing' |
| 'paused' |
| 'stopped' |
| 'error' |
