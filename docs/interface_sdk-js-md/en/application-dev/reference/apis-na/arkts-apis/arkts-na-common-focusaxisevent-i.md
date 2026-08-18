# FocusAxisEvent

Focus axis event object description.

**Inheritance/Implementation:** FocusAxisEvent extends [BaseEvent](arkts-na-common-baseevent-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface FocusAxisEvent--><!--Device-unnamed-export declare interface FocusAxisEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stopPropagation

```TypeScript
stopPropagation(): void
```

The blocking event pops up.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FocusAxisEvent-stopPropagation(): void--><!--Device-FocusAxisEvent-stopPropagation(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## axisMap

```TypeScript
axisMap: Map<AxisModel, double>
```

The axis values of axis event.

**Type:** Map&lt;[AxisModel](../../apis-arkui/arkts-apis/arkts-arkui-axismodel-e.md), double&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FocusAxisEvent-axisMap: Map<AxisModel, double>--><!--Device-FocusAxisEvent-axisMap: Map<AxisModel, double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

