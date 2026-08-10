# HiPlayDeviceInfo (System API)

HiPlay 设备类型定义

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-avSession-interface HiPlayDeviceInfo--><!--Device-avSession-interface HiPlayDeviceInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## castMode

```TypeScript
castMode?: int
```

HiPlay 投播模式，设备级和应用级

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-HiPlayDeviceInfo-castMode?: int--><!--Device-HiPlayDeviceInfo-castMode?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## castUid

```TypeScript
castUid?: int
```

HiPlay 当前投播uid

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-HiPlayDeviceInfo-castUid?: int--><!--Device-HiPlayDeviceInfo-castUid?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## supportCastMode

```TypeScript
supportCastMode?: int
```

支持的Cast Mode，包含设备级和应用级投播

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-HiPlayDeviceInfo-supportCastMode?: int--><!--Device-HiPlayDeviceInfo-supportCastMode?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

## supportMultiDeviceMode

```TypeScript
supportMultiDeviceMode?: int
```

是否支持多设备连接能力。取值限定为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-HiPlayDeviceInfo-supportMultiDeviceMode?: int--><!--Device-HiPlayDeviceInfo-supportMultiDeviceMode?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

