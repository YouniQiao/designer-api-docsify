# DragSpringLoadingConfiguration

Defines parameters affecting spring loading detection. Typically, default system configurations suffice.Customization can be done by specifying the config when binding onDragSpringLoading or dynamically modifying it using the updateConfiguration method during the BEGIN state.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-dragController-export interface DragSpringLoadingConfiguration--><!--Device-dragController-export interface DragSpringLoadingConfiguration-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stillTimeLimit

```TypeScript
stillTimeLimit?: int
```

Time interval to maintain a stationary state before entering spring loading. Default: 500 ms.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragSpringLoadingConfiguration-stillTimeLimit?: int--><!--Device-DragSpringLoadingConfiguration-stillTimeLimit?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## updateInterval

```TypeScript
updateInterval?: int
```

Interval between update notifications after entering the spring loading state. Default: 100ms.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragSpringLoadingConfiguration-updateInterval?: int--><!--Device-DragSpringLoadingConfiguration-updateInterval?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## updateNotifyCount

```TypeScript
updateNotifyCount?: int
```

Maximum number of update notifications to report while in the spring loading state. Default: 3.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragSpringLoadingConfiguration-updateNotifyCount?: int--><!--Device-DragSpringLoadingConfiguration-updateNotifyCount?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## updateToFinishInterval

```TypeScript
updateToFinishInterval?: int
```

Maximum wait time from the last UPDATE state to the end of spring loading. Default: 100ms.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragSpringLoadingConfiguration-updateToFinishInterval?: int--><!--Device-DragSpringLoadingConfiguration-updateToFinishInterval?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

