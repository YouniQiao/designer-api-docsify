# DragSpringLoadingState

Defines the drag spring loading state. Under default system configuration, if no CANCEL occurs, the state reporting is as follows: Hover still--500ms-->BEGIN-->100ms-->UPDATE-->100ms-->UPDATE-->100ms-->UPDATE-->100ms-->END

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-dragController-export const enum DragSpringLoadingState--><!--Device-dragController-export const enum DragSpringLoadingState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BEGIN

```TypeScript
BEGIN = 0
```

The user has remained stationary for a period, initiating the spring loading process. This state allows for some preparatory operations during spring loading.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragSpringLoadingState-BEGIN = 0--><!--Device-DragSpringLoadingState-BEGIN = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## UPDATE

```TypeScript
UPDATE = 1
```

Already in the spring loading state. The system periodically checks the user's hover status. If the user remains stationary, it triggers an UPDATE state notification at regular intervals. This state allows for UI effect refreshes to emphasize the hover state.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragSpringLoadingState-UPDATE = 1--><!--Device-DragSpringLoadingState-UPDATE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## END

```TypeScript
END = 2
```

The entire spring loading state ends. The application can perform cleanup operations and execute navigation or view switching actions when this state occurs.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragSpringLoadingState-END = 2--><!--Device-DragSpringLoadingState-END = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CANCEL

```TypeScript
CANCEL = 3
```

After entering the BEGIN state, if the user moves out of the component range, exceeds the displacement threshold, lifts the finger, or switches windows (pull out), the CANCEL state is triggered. The application should restore the UI style and cancel any pending navigation or view switching actions.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragSpringLoadingState-CANCEL = 3--><!--Device-DragSpringLoadingState-CANCEL = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

