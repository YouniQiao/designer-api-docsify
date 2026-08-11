# Touch

Defines the touch point information.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface Touch--><!--Device-unnamed-export declare interface Touch-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { SourceType, ToolType, TouchEvent, FixedMode, KeyAction, Touch } from 'kits/@kit.InputKit';
```

## blobId

```TypeScript
blobId?: int
```

Touch point attribute ID. Currently, only single-finger touch is supported. The value **1** indicates left-hand touch, and the value **2** indicates right-hand touch.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Touch-blobId?: int--><!--Device-Touch-blobId?: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## fixedDisplayX

```TypeScript
fixedDisplayX?: int
```

Corrected value of the screenX coordinate in one-hand mode, in px.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-Touch-fixedDisplayX?: int--><!--Device-Touch-fixedDisplayX?: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## fixedDisplayY

```TypeScript
fixedDisplayY?: int
```

Corrected value of the screenY coordinate in one-hand mode, in px.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-Touch-fixedDisplayY?: int--><!--Device-Touch-fixedDisplayY?: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

