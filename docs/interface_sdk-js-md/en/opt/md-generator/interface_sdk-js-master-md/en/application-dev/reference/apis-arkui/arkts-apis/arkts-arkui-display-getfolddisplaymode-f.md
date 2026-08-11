# getFoldDisplayMode

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getFoldDisplayMode

```TypeScript
function getFoldDisplayMode(): FoldDisplayMode
```

Obtains the display mode of this foldable device.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-display-function getFoldDisplayMode(): FoldDisplayMode--><!--Device-display-function getFoldDisplayMode(): FoldDisplayMode-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## Examples

```TypeScript
let data: display.FoldDisplayMode = display.getFoldDisplayMode();
console.info(`Succeeded in obtaining fold display mode. Data: ${data}`);
```
