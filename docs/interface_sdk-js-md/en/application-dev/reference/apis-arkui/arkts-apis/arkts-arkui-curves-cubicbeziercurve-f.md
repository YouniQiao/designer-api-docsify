# cubicBezierCurve

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## cubicBezierCurve

```TypeScript
function cubicBezierCurve(x1: number, y1: number, x2: number, y2: number): ICurve
```

Creates a cubic Bezier curve, with x-coordinates automatically normalized between 0 and 1.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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
| [ICurve](../arkts-components/arkts-arkui-icurve-i.md) |
