# stepsCurve

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## stepsCurve

```TypeScript
function stepsCurve(count: number, end: boolean): ICurve
```

Creates a step curve.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-curves-function stepsCurve(count: number, end: boolean): ICurve--><!--Device-curves-function stepsCurve(count: number, end: boolean): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| count | number | Yes |
| end | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |

## Examples

```TypeScript
import { curves } from '@kit.ArkUI';
curves.stepsCurve(9, true);  // Create a step curve.
```
