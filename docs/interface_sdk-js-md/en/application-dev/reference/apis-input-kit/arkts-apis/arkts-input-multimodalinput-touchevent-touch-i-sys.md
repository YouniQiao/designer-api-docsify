# Touch

Defines the touch point information.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface Touch--><!--Device-unnamed-export declare interface Touch-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { SourceType, ToolType, TouchEvent, FixedMode, KeyAction, Touch } from '@kit.InputKit';
```

## blobId

```TypeScript
blobId?: int
```

Touch point attribute ID. Currently, only single-finger touch is supported. The value **1** indicates left-hand touch, and the value **2** indicates right-hand touch.

**Type:** int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Touch-blobId?: int--><!--Device-Touch-blobId?: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## fixedDisplayX

```TypeScript
fixedDisplayX?: int
```

Corrected value of the screenX coordinate in one-hand mode, in px.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Touch-fixedDisplayX?: int--><!--Device-Touch-fixedDisplayX?: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## fixedDisplayY

```TypeScript
fixedDisplayY?: int
```

Corrected value of the screenY coordinate in one-hand mode, in px.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Touch-fixedDisplayY?: int--><!--Device-Touch-fixedDisplayY?: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

