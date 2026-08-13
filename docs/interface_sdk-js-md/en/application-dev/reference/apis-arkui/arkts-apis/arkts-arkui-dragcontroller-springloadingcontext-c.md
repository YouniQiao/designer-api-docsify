# SpringLoadingContext

Context information for the current spring loading trigger. This object is passed to the application in the spring loading callback, allowing it to obtain the current state, dynamically refresh UI effects, and access drag data to determine whether to handle the drag operation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-dragController-export class SpringLoadingContext--><!--Device-dragController-export class SpringLoadingContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { dragController } from '@kit.ArkUI';
```

## abort

```TypeScript
abort(): void
```

Aborts subsequent spring loading triggers. Note: Aborting does not trigger a CANCEL notification, the application must handle state cleanup when aborting.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SpringLoadingContext-abort(): void--><!--Device-SpringLoadingContext-abort(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## updateConfiguration

```TypeScript
updateConfiguration(config: DragSpringLoadingConfiguration): void
```

Updates the spring loading configuration for the current trigger. Only effective during the BEGIN state. This method does not modify the original configuration set during onDragSpringLoading binding. It provides an opportunity for dynamic configuration updates during the current trigger. Typically, applications should use default configurations or set them once during binding. Use this method sparingly, e.g., for different drag data types requiring varied UX timing.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SpringLoadingContext-updateConfiguration(config: DragSpringLoadingConfiguration): void--><!--Device-SpringLoadingContext-updateConfiguration(config: DragSpringLoadingConfiguration): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | DragSpringLoadingConfiguration | Yes |  |

## currentConfig

```TypeScript
currentConfig?: DragSpringLoadingConfiguration
```

Current spring loading configuration. Absent when the state is CANCEL.

**Type:** DragSpringLoadingConfiguration

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SpringLoadingContext-currentConfig?: DragSpringLoadingConfiguration--><!--Device-SpringLoadingContext-currentConfig?: DragSpringLoadingConfiguration-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## currentNotifySequence

```TypeScript
currentNotifySequence: int
```

Sequence number of the current spring loading state notification. Begins at 0 for BEGIN and increments with each callback.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SpringLoadingContext-currentNotifySequence: int--><!--Device-SpringLoadingContext-currentNotifySequence: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dragInfos

```TypeScript
dragInfos?: SpringLoadingDragInfos
```

Drag-related information. Absent when the state is CANCEL.

**Type:** [SpringLoadingDragInfos](arkts-arkui-dragcontroller-springloadingdraginfos-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SpringLoadingContext-dragInfos?: SpringLoadingDragInfos--><!--Device-SpringLoadingContext-dragInfos?: SpringLoadingDragInfos-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## state

```TypeScript
state: DragSpringLoadingState
```

Current spring loading state. Refer to the DragSpringLoadingState enum for details.

**Type:** [DragSpringLoadingState](arkts-arkui-dragcontroller-dragspringloadingstate-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SpringLoadingContext-state: DragSpringLoadingState--><!--Device-SpringLoadingContext-state: DragSpringLoadingState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

