# AudioCapturerFilter（系统接口）

过滤条件类。在调用selectOutputDeviceByFilter接口前，需要先创建AudioCapturerFilter实例。

**起始版本：** 23

<!--Device-audio-interface AudioCapturerFilter--><!--Device-audio-interface AudioCapturerFilter-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { audio } from '@kit.AudioKit';
```

## capturerInfo

```TypeScript
capturerInfo?: AudioCapturerInfo
```

表示采集器信息。SystemCapability.Multimedia.Audio.Capturer

**类型：** [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md)

**起始版本：** 23

<!--Device-AudioCapturerFilter-capturerInfo?: AudioCapturerInfo--><!--Device-AudioCapturerFilter-capturerInfo?: AudioCapturerInfo-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**系统接口：** 此接口为系统接口。

## uid

```TypeScript
uid?: int
```

表示应用ID。SystemCapability.Multimedia.Audio.Core

**类型：** int

**起始版本：** 23

<!--Device-AudioCapturerFilter-uid?: int--><!--Device-AudioCapturerFilter-uid?: int-End-->

**系统能力：** SystemCapability.Multimedia.Audio.Core

**系统接口：** 此接口为系统接口。

**示例**

```TypeScript
import { audio } from '@kit.AudioKit';

let inputAudioCapturerFilter: audio.AudioCapturerFilter = {
    uid : 20010041,
    capturerInfo : {
        source: audio.SourceType.SOURCE_TYPE_MIC,
        capturerFlags: 0
    }
};
```

