# SketchStatusData（系统接口）

Defines the PiP status data.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-camera-interface SketchStatusData--><!--Device-camera-interface SketchStatusData-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## centerPointOffset

```TypeScript
centerPointOffset: Point
```

Offset of PiP.

**类型：** [Point](arkts-camera-camera-point-i.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-SketchStatusData-centerPointOffset: Point--><!--Device-SketchStatusData-centerPointOffset: Point-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## sketchRatio

```TypeScript
sketchRatio: double
```

Zoom ratio of PiP.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-SketchStatusData-sketchRatio: double--><!--Device-SketchStatusData-sketchRatio: double-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## status

```TypeScript
status: int
```

Status of PiP. The options are 0 (stopped), 1 (started), 2 (stopping), and 3 (starting).

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-SketchStatusData-status: int--><!--Device-SketchStatusData-status: int-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

