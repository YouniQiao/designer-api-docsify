# AVMetricsEvent

Describes the information of an Metrics Event.

**起始版本：** 23

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## details

```TypeScript
details: Record<string, Object>
```

The detailed information of the event.

**类型：** Record&lt;string, Object&gt;

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

## event

```TypeScript
event: AVMetricsEventType
```

Type of the metrics event.

**类型：** [AVMetricsEventType](arkts-media-media-avmetricseventtype-e.md)

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

## playbackPosition

```TypeScript
playbackPosition: number
```

The playback progress position when the event occurs.

**类型：** number

**起始版本：** 23

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

## timeStamp

```TypeScript
timeStamp: number
```

Absolute timestamp when the event occurred.

**类型：** number

**起始版本：** 23

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
