# GesturePoint

GesturePoint表示手势触摸点。

本模块用于创建辅助功能注入手势所需的手势路径的触摸点信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-export declare class GesturePoint--><!--Device-unnamed-export declare class GesturePoint-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## Modules to Import

```TypeScript
import { GesturePoint } from 'kits/@kit.AccessibilityKit';
```

## constructor

```TypeScript
constructor(positionX: double, positionY: double)
```

构造函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

<!--Device-GesturePoint-constructor(positionX: double, positionY: double)--><!--Device-GesturePoint-constructor(positionX: double, positionY: double)-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| positionX | double | Yes | 触摸点X坐标，单位为像素（px）。 |
| positionY | double | Yes | 触摸点Y坐标，单位为像素（px）。 |

## Examples

```TypeScript
import { GesturePoint } from '@kit.AccessibilityKit';

let gesturePoint = new GesturePoint(1, 2);
```

## positionX

```TypeScript
positionX: double
```

触摸点X坐标，单位为像素（px）。

**Type:** double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-GesturePoint-positionX: double--><!--Device-GesturePoint-positionX: double-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

## positionY

```TypeScript
positionY: double
```

触摸点Y坐标，单位为像素（px）。

**Type:** double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-GesturePoint-positionY: double--><!--Device-GesturePoint-positionY: double-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

