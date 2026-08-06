# FocusAxisEvent

Describes the focus axis event object. Inherits from [BaseEvent]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Inheritance/Implementation:** FocusAxisEvent extends [BaseEvent](../arkts-apis/arkts-arkui-component/common-baseevent-i.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-unnamed-declare interface FocusAxisEvent extends BaseEvent--><!--Device-unnamed-declare interface FocusAxisEvent extends BaseEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## axisMap

```TypeScript
axisMap: Map<AxisModel, number>
```

Axis value table of the focus axis event.

**Type:** Map&lt;AxisModel, number&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FocusAxisEvent-axisMap: Map<AxisModel, number>--><!--Device-FocusAxisEvent-axisMap: Map<AxisModel, number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stopPropagation

```TypeScript
stopPropagation: Callback<void>
```

Blocks \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ propagation.

**Type:** Callback&lt;void&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FocusAxisEvent-stopPropagation: Callback<void>--><!--Device-FocusAxisEvent-stopPropagation: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

