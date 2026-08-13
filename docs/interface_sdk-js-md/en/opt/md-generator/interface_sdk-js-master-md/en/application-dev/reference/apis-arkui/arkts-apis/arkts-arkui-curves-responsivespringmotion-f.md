# responsiveSpringMotion

## Modules to Import

```TypeScript
import { curves } from '@kit.ArkUI';
```

## responsiveSpringMotion

```TypeScript
function responsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve
```

Creates a responsive spring animation curve. It is a special case of [springMotion](arkts-arkui-curves-springmotion-f.md#springMotion), with the only difference in the default values. It can be used together with **springMotion**.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-curves-function responsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve--><!--Device-curves-function responsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve-End-->

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

## Examples

```TypeScript
import { curves } from '@kit.ArkUI';
curves.responsiveSpringMotion(); // Create a responsive spring animation curve with default settings.
```
