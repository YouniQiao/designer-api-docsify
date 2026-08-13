# AVPlayerState

```TypeScript
type AVPlayerState = 'idle' | 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' | 'released' | 'error'
```

[AVPlayer](arkts-media-media-n.md#media)的状态机，可通过state属性主动获取当前状态，也可通过监听 stateChange 事件上报当前状态，状态机之间的切换规则，可参考[音频播放开发指导](../../../media/media/using-avplayer-for-playback.md)。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-media-type AVPlayerState = 'idle' | 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' | 'released' | 'error'--><!--Device-media-type AVPlayerState = 'idle' | 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' | 'released' | 'error'-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

| 类型 |
| --- |
| 'idle' |
| 'initialized' |
| 'prepared' |
| 'playing' |
| 'paused' |
| 'completed' |
| 'stopped' |
| 'released' |
| 'error' |
