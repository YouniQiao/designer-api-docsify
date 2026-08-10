# AVSessionType

```TypeScript
type AVSessionType = 'audio' | 'video' | 'voice_call' | 'video_call' | 'photo'
```

当前会话支持的会话类型。

该类型可取的值为下表字符串。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-avSession-type AVSessionType = 'audio' | 'video' | 'voice_call' | 'video_call' | 'photo'--><!--Device-avSession-type AVSessionType = 'audio' | 'video' | 'voice_call' | 'video_call' | 'photo'-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

| Type | Description |
| --- | --- |
| 'audio' | 音频 |
| 'video' | 视频 |
| 'voice_call' | 音频通话。 [since 11] |
| 'video_call' | 视频通话。 [since 12] |
| 'photo' | 图片。 [since 22] |

