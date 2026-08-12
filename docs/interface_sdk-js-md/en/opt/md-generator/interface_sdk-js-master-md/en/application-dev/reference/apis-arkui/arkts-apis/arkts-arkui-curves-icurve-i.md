# ICurve

Represents a curve object. Different types of curve objects can be created using APIs in this module, including   
[curves.cubicBezierCurve](arkts-arkui-curves-cubicbeziercurve-f.md#cubicBezierCurve) and   
[curves.interpolatingSpring](arkts-arkui-curves-interpolatingspring-f.md#interpolatingSpring). The curve object provides interpolation functionality through its member method [interpolate](#interpolate).

**Since:** 9

<!--Device-curves-interface ICurve--><!--Device-curves-interface ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## interpolate

```TypeScript
interpolate(fraction : number) : number
```

Calculates the interpolated value along the curve at the specified normalized time point.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ICurve-interpolate(fraction : number) : number--><!--Device-ICurve-interpolate(fraction : number) : number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fraction | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { curves } from '@kit.ArkUI'
let curveValue = curves.initCurve(Curve.EaseIn); // Create an ease-in curve.
let interpolatedValue: number = curveValue.interpolate(0.5); // Calculate the interpolation for half of the time.
```
