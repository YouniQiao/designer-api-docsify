# SettingParam (System API)

Defines the effect parameters used to preheat an image.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## faceSlender

```TypeScript
faceSlender: int
```

Face slimming level, which is obtained through [Beauty.getSupportedBeautyRange](arkts-camera-camera-beautyquery-i-sys.md#getsupportedbeautyrange). For example, the value **1** indicates level-1 slimming.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## skinSmoothLevel

```TypeScript
skinSmoothLevel: int
```

Skin smoothing level, which is obtained through [Beauty.getSupportedBeautyRange](arkts-camera-camera-beautyquery-i-sys.md#getsupportedbeautyrange). For example, the value **1** indicates level-1 smoothing.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## skinTone

```TypeScript
skinTone: int
```

Skin tone perfection level, which is obtained through [Beauty.getSupportedBeautyRange](arkts-camera-camera-beautyquery-i-sys.md#getsupportedbeautyrange). For example, the value **0xBF986C** indicates a specific color.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.
