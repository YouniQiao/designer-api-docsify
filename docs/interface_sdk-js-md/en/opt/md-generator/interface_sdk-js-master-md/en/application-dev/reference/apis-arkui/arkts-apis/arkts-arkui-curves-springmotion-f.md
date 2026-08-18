# springMotion

## Modules to Import

```TypeScript
```

## springMotion

```TypeScript
function springMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve
```

Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object, each animation replaces their predecessor and inherits the velocity.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-curves-function springMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve--><!--Device-curves-function springMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| response | number | No |
| dampingFraction | number | No |
| overlapDuration | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ICurve](arkts-arkui-curves-icurve-i.md) |

**Examples**

```TypeScript
import { curves } from '@kit.ArkUI';
curves.springMotion(); // Create a spring animation curve with default settings.
curves.springMotion(0.5); // Create a spring animation curve with the specified response value.
curves.springMotion(0.5, 0.6); // Create a spring animation curve with the specified response and dampingFraction values.
curves.springMotion(0.5, 0.6, 0); // Create a spring animation curve with the specified parameter values.
```
