# VideoProfile

视频配置信息项，继承[Profile](arkts-camera-camera-profile-i.md)。

**继承/实现关系：** VideoProfile extends [Profile](arkts-camera-camera-profile-i.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Camera.Core

## 导入模块

```TypeScript
import { camera } from '@kit.CameraKit';
```

## frameRateRange

```TypeScript
readonly frameRateRange: FrameRateRange
```

帧率范围。单位：fps(frames per second)。

**类型：** [FrameRateRange](arkts-camera-camera-frameraterange-i.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core
