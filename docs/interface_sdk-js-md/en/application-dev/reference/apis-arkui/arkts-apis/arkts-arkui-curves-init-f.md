# init

## Modules to Import

```TypeScript
import { curves } from 'kits/@kit.ArkUI';
```

## init

```TypeScript
function init(curve?: Curve): string
```

Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the input parameter.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [initCurve](arkts-arkui-curves-initcurve-f.md#initcurve)

<!--Device-curves-function init(curve?: Curve): string--><!--Device-curves-function init(curve?: Curve): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| curve | [Curve](arkts-arkui-curve-e.md) | No | Curve type.&lt;br&gt;Default value: **Curve.Linear |

**Return value:**

| Type | Description |
| --- | --- |
| string | Interpolation curve object. |

