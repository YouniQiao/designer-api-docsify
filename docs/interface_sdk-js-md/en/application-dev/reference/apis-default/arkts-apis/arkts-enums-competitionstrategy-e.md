# CompetitionStrategy

Defines whether a competition for gesture recognition results should occur between the event injector and the gesture recognizers of the target component. This strategy determines how the injected input event interacts with the target component's own gesture handling logic.

@enum { number }

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

<!--Device-unnamed-export enum CompetitionStrategy--><!--Device-unnamed-export enum CompetitionStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 0
```

No competition strategy. The injected event does not compete with any existing gestures. Both the injected event and existing gestures can be processed independently and in parallel.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompetitionStrategy-DEFAULT = 0--><!--Device-CompetitionStrategy-DEFAULT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## COMPETITION

```TypeScript
COMPETITION = 1
```

Competition strategy. The gesture recognition result from the event injector will compete with those from the target component's own recognizers.

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CompetitionStrategy-COMPETITION = 1--><!--Device-CompetitionStrategy-COMPETITION = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

