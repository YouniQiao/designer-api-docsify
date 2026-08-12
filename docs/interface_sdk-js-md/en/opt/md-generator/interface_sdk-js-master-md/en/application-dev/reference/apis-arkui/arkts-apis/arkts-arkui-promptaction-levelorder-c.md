# LevelOrder

Defines the display order of a dialog box.

**Since:** 18

<!--Device-unnamed-export class LevelOrder--><!--Device-unnamed-export class LevelOrder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## clamp

```TypeScript
static clamp(order: number): LevelOrder
```

Creates a dialog box level with the specified order.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LevelOrder-static clamp(order: number): LevelOrder--><!--Device-LevelOrder-static clamp(order: number): LevelOrder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| order | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LevelOrder](arkts-arkui-promptaction-levelorder-c.md) |

## getOrder

```TypeScript
getOrder(): number
```

Obtains the display order of this dialog box.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LevelOrder-getOrder(): number--><!--Device-LevelOrder-getOrder(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
