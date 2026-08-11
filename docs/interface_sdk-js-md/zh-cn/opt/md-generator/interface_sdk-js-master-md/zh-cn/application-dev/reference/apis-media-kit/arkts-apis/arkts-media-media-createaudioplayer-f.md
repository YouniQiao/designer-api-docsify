# createAudioPlayer

## createAudioPlayer

```TypeScript
function createAudioPlayer(): AudioPlayer
```

同步方式创建音频播放实例。

> **说明：**
> > 从API version 6开始支持，从API version 9开始废弃，建议使用
> [createAVPlayer](arkts-media-media-createavplayer-f.md#createavplayer)替代。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [media.createAVPlayer](arkts-media-media-createavplayer-f.md#createavplayer)(callback:

<!--Device-media-function createAudioPlayer(): AudioPlayer--><!--Device-media-function createAudioPlayer(): AudioPlayer-End-->

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**返回值：**

| 类型 |
| --- |
| [AudioPlayer](arkts-media-multimedia-media-audioplayer-i.md) |

## 示例

```TypeScript
let audioPlayer: media.AudioPlayer = media.createAudioPlayer();
```
