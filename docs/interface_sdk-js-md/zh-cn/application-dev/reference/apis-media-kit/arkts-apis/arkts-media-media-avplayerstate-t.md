# AVPlayerState

```TypeScript
type AVPlayerState = 'idle' | 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' | 'released' | 'error'
```

[AVPlayer](arkts-multimedia-media.md)的状态机，可通过state属性主动获取当前状态，也可通过监听 [stateChange](arkts-media-media-avplayer-i.md#onstatechange) 事件上报当前状态，状态机之间的切换规则，可参考[音频播放开发指导](../../../media/media/using-avplayer-for-playback.md)。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
