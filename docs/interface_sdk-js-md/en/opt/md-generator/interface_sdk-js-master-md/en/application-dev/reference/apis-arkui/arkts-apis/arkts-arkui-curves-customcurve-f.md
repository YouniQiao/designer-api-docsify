# customCurve

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## customCurve

```TypeScript
function customCurve(interpolate: (fraction: number) => number): ICurve
```

Creates a custom curve.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-curves-function customCurve(interpolate: (fraction: number) => number): ICurve--><!--Device-curves-function customCurve(interpolate: (fraction: number) => number): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| interpolate | (fraction: number) = & gt; number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |

## Examples

```TypeScript
import { curves } from '@kit.ArkUI';
let interpolate = (fraction: number): number => {
  return Math.sqrt(fraction);
};
let curve = curves.customCurve(interpolate); // Create a custom interpolation curve.
```
