# GesturePath

Represents gesture path information, used to simulate user touch gestures (such as tap, swipe, etc.) in accessibility services.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
import { GesturePath } from '@kit.AccessibilityKit';
```

## constructor

```TypeScript
constructor(durationTime: long)
```

Creates a gesture path object by passing in the total gesture duration. After creating a GesturePath instance, you must also set the required property points.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Deprecated since:** 12

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [durationTime](arkts-accessibility-accessibility-gesturepath-gesturepath-c.md) | number | Yes |

**Examples**

```TypeScript
import { GesturePath } from '@kit.AccessibilityKit';

let gesturePath = new GesturePath(20);
```

## durationTime

```TypeScript
durationTime: number
```

Total gesture duration, in ms. The value must be greater than 0.

**Type:** number

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## points

```TypeScript
points: Array<GesturePoint>
```

Sequence of touch points on the gesture path, used to form the movement trajectory of the gesture. Each touch point represents a coordinate position on the path. The array length must be greater than 0.

**Type:** Array&lt;[GesturePoint](arkts-accessibility-accessibility-gesturepoint-gesturepoint-c.md)&gt;

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.BarrierFree.Accessibility.Core
