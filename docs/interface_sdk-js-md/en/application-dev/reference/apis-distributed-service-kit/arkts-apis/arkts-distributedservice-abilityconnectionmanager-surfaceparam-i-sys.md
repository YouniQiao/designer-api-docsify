# SurfaceParam (System API)

Surface configuration parameters.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-abilityConnectionManager-interface SurfaceParam--><!--Device-abilityConnectionManager-interface SurfaceParam-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## flip

```TypeScript
flip?: FlipOptions
```

This value indicates whether the video is reversed.

**Type:** [FlipOptions](arkts-distributedservice-abilityconnectionmanager-flipoptions-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SurfaceParam-flip?: FlipOptions--><!--Device-SurfaceParam-flip?: FlipOptions-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

## format

```TypeScript
format?: VideoPixelFormat
```

Video PixelFormat, this option must be configured on the sender. Must be set before stream starts and cannot update once set.

**Type:** [VideoPixelFormat](arkts-distributedservice-abilityconnectionmanager-videopixelformat-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SurfaceParam-format?: VideoPixelFormat--><!--Device-SurfaceParam-format?: VideoPixelFormat-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

## height

```TypeScript
height: int
```

Encoding length. Must be set before stream starts and cannot update once set.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SurfaceParam-height: int--><!--Device-SurfaceParam-height: int-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

## rotation

```TypeScript
rotation?: int
```

This value identifies the rotation angle of the video. the range of rotation angle should be {0, 90, 180, 270}, default is 0

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SurfaceParam-rotation?: int--><!--Device-SurfaceParam-rotation?: int-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

## width

```TypeScript
width: int
```

Encoding width. Must be set before stream starts and cannot update once set.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SurfaceParam-width: int--><!--Device-SurfaceParam-width: int-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

