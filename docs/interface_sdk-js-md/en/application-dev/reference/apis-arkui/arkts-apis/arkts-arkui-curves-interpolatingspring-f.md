# interpolatingSpring

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## interpolatingSpring

```TypeScript
function interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve
```

Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in **animation** or **animateTo**.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| velocity | number | Yes |
| mass | number | Yes |
| [stiffness](../arkts-components/arkts-arkui-chainanimationoptions-i-sys.md) | number | Yes |
| [damping](../arkts-components/arkts-arkui-chainanimationoptions-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ICurve](../arkts-components/arkts-arkui-icurve-i.md) |
