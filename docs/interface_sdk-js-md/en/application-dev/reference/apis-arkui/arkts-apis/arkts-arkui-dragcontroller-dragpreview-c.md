# DragPreview

Provides the functions of setting color or updating animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-dragController-export class DragPreview--><!--Device-dragController-export class DragPreview-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { dragController } from 'dragController';
```

## animate

```TypeScript
animate(options: AnimationOptions, handler: () => void): void
```

update preview style with animation

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragPreview-animate(options: AnimationOptions, handler: () => void): void--><!--Device-DragPreview-animate(options: AnimationOptions, handler: () => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | AnimationOptions | Yes | animation options |
| handler | () =&gt; void | Yes | change style functions |

## setForegroundColor

```TypeScript
setForegroundColor(color: ResourceColor): void
```

change foreground color of preview

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragPreview-setForegroundColor(color: ResourceColor): void--><!--Device-DragPreview-setForegroundColor(color: ResourceColor): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | ResourceColor | Yes | color value |

