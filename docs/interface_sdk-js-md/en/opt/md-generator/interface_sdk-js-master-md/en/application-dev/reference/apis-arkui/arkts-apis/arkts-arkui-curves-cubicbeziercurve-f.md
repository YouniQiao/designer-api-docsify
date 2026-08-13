# cubicBezierCurve

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## cubicBezierCurve

```TypeScript
function cubicBezierCurve(x1: number, y1: number, x2: number, y2: number): ICurve
```

Creates a cubic Bezier curve, with x-coordinates automatically normalized between 0 and 1.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-curves-function cubicBezierCurve(x1: number, y1: number, x2: number, y2: number): ICurve--><!--Device-curves-function cubicBezierCurve(x1: number, y1: number, x2: number, y2: number): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x1 | number | Yes |
| y1 | number | Yes |
| x2 | number | Yes |
| y2 | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |

## Examples

```TypeScript
import { curves } from '@kit.ArkUI';
curves.cubicBezierCurve(0.1, 0.0, 0.1, 1.0); // Create a cubic Bézier curve.
```
