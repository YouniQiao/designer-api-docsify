# init

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## init

```TypeScript
function init(curve?: Curve): string
```

Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the input parameter.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [initCurve](arkts-arkui-curves-initcurve-f.md)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| curve | Curve | No | Curve type.Default value: **Curve.Linear |

**Return value:**

| Type | Description |
| --- | --- |
| string | Interpolation curve object. |
