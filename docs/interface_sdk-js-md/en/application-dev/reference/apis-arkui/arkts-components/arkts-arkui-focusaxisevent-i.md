# FocusAxisEvent

焦点轴事件的对象说明，继承于[BaseEvent](arkts-arkui-baseevent-i.md)。

**Inheritance/Implementation:** FocusAxisEvent extends [BaseEvent](arkts-arkui-baseevent-i.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-unnamed-declare interface FocusAxisEvent extends BaseEvent--><!--Device-unnamed-declare interface FocusAxisEvent extends BaseEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## axisMap

```TypeScript
axisMap: Map<AxisModel, number>
```

焦点轴事件的轴值表。

**Type:** Map&lt;[AxisModel](../arkts-apis/arkts-arkui-axismodel-e.md), number&gt;

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

阻塞[事件冒泡](../../../ui/arkts-interaction-basic-principles.md#事件冒泡)传递。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FocusAxisEvent-stopPropagation: Callback<void>--><!--Device-FocusAxisEvent-stopPropagation: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

