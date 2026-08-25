# AVPlayer

播放管理类，用于管理和播放媒体资源。在调用AVPlayer的方法前，需要先通过 [createAVPlayer()](arkts-media-media-createavplayer-f.md)构建一个 AVPlayer实例。在使用AVPlayer实例的方法时，建议开发者注册相关回调，主动获取当前状态变化。 [on('stateChange')](arkts-media-media-avplayer-i.md#onstatechange)：监听播放状态机 AVPlayerState切换。[on('error')](arkts-media-media-avplayer-i.md#onerror)：监听错误事件。应用需要按照实际业务需求合理使用AVPlayer对象，按需创建并及时释放，避免持有过多AVPlayer实例导致内存消耗过大，否则在一定情况下可能导致系统终止应用。Audio/Video播放demo可参考：[音频播放开发指导](../../../media/media/using-avplayer-for-playback.md)、 [视频播放开发指导](../../../media/media/video-playback.md)。

> **说明：**&gt;
> - 本Interface首批接口从API version 9开始支持。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## forceLoadVideo

```TypeScript
forceLoadVideo(force: boolean): Promise<void>
```

指定是否强制加载视频。该接口仅在AVPlayer处于prepared、playing或paused状态时可调用。 使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [force](../../apis-arkui/arkts-components/arkts-arkui-historicalpoint-i.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getCurrentTrack

```TypeScript
getCurrentTrack(trackType: MediaType): Promise<number>
```

获取指定媒体类型所选择的轨道。该接口仅在AVPlayer处于prepared、playing或paused状态时可调用。 使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| trackType | [MediaType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-mediatype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## enableStartFrameRateOpt

```TypeScript
enableStartFrameRateOpt?: boolean
```

Whether a slower synchronization policy is used at the start of playback to reduce subjective image jitter caused by insufficient frame rate. Default value: false, means that the slower synchronization policy will not be used.

**类型：** boolean

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**系统接口：** 此接口为系统接口。

## privacyType

```TypeScript
privacyType?: audio.AudioPrivacyType
```

Audio privacy configuration. For more information, see [AudioPrivacyType](../../apis-audio-kit/arkts-apis/arkts-audio-audio-audioprivacytype-e.md). Default value: PRIVACY_TYPE_PUBLIC.

**类型：** audio.AudioPrivacyType

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**系统接口：** 此接口为系统接口。
