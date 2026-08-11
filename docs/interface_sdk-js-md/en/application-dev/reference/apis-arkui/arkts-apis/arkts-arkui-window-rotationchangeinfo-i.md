# RotationChangeInfo

Describes the window information obtained during window rotation changes.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-window-interface RotationChangeInfo--><!--Device-window-interface RotationChangeInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## displayId

```TypeScript
displayId: long
```

ID of the screen where the window is located.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RotationChangeInfo-displayId: long--><!--Device-RotationChangeInfo-displayId: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## displayRect

```TypeScript
displayRect: Rect
```

Size of the rectangle after the screen where the window is located is rotated.

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RotationChangeInfo-displayRect: Rect--><!--Device-RotationChangeInfo-displayRect: Rect-End-->

**System capability:** SystemCapability.Window.SessionManager

## orientation

```TypeScript
orientation: int
```

Display orientation of the window.

- **0**: portrait.  
- **1**: reverse landscape.  
- **2**: reverse portrait.  
- **3**: landscape.

Note that the orientation here is different from the orientation property of the display object.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RotationChangeInfo-orientation: int--><!--Device-RotationChangeInfo-orientation: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## type

```TypeScript
type: RotationChangeType
```

Type of window rotation event.

**Type:** [RotationChangeType](arkts-arkui-window-rotationchangetype-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RotationChangeInfo-type: RotationChangeType--><!--Device-RotationChangeInfo-type: RotationChangeType-End-->

**System capability:** SystemCapability.Window.SessionManager

