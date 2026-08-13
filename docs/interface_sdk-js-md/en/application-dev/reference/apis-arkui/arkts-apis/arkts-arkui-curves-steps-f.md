# steps

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## steps

```TypeScript
function steps(count: number, end: boolean): string
```

Creates a step curve.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [stepsCurve](../../apis-na/arkts-apis/arkts-na-curves-stepscurve-f.md#stepsCurve)

<!--Device-curves-function steps(count: number, end: boolean): string--><!--Device-curves-function steps(count: number, end: boolean): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | number | Yes | Number of steps. The value must be a positive integer. |
| end | boolean | Yes | Whether the step change occurs at the start or end of each interval.&lt;br&gt;- **true**: The step change occurs at the end of each interval.&lt;br&gt;- **false**: The step change occurs at the start of each interval. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Steps curve object. |

