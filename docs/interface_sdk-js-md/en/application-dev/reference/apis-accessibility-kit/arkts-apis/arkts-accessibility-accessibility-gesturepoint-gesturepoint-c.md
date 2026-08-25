# GesturePoint

Represents a gesture touch point, which is the basic unit that constitutes a GesturePath node and is used to define the touch position in the gesture trajectory for accessibility gesture injection. For details about how to use it, see [GesturePath](arkts-accessibility-accessibility-gesturepath-gesturepath-c.md).

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
import { GesturePoint } from '@kit.AccessibilityKit';
```

## constructor

```TypeScript
constructor(positionX: double, positionY: double)
```

Creates a **GesturePoint** instance based on the given X and Y coordinates.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Deprecated since:** 12

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [positionX](#positionx) | number | Yes |
| [positionY](#positiony) | number | Yes |

**Examples**

```TypeScript
import { GesturePoint } from '@kit.AccessibilityKit';

let gesturePoint = new GesturePoint(1, 2);
```

## positionX

```TypeScript
positionX: number
```

X coordinate of the touch point, in pixels (px).

**Type:** number

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## positionY

```TypeScript
positionY: number
```

Y coordinate of the touch point, in pixels (px).

**Type:** number

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core
