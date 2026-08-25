# springCurve

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## springCurve

```TypeScript
function springCurve(velocity: number, mass: number, stiffness: number, damping: number): ICurve
```

Creates a spring curve. The curve shape is subject to the spring parameters, and the animation duration is subject to the **duration** parameter in **animation** and **animateTo**.

**Since:** 9

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
