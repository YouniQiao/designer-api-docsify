# interpolatingSpring

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## interpolatingSpring

```TypeScript
function interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve
```

Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-curves-function interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve--><!--Device-curves-function interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| velocity | number | Yes |
| mass | number | Yes |
| stiffness | number | Yes |
| damping | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |

## Examples

```TypeScript
import { curves } from '@kit.ArkUI';
curves.interpolatingSpring(10, 1, 228, 30); // Create an interpolating spring curve whose duration is subject to spring parameters.
```
