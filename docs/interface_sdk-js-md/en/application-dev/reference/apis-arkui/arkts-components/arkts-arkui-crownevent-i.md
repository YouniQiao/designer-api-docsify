# CrownEvent

组件接收表冠事件的数据结构。内容包括时间戳、旋转角速度、旋转角度、表冠动作和阻止事件冒泡。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface CrownEvent--><!--Device-unnamed-declare interface CrownEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action: CrownAction
```

表冠动作。

**Type:** [CrownAction](../arkts-apis/arkts-arkui-crownaction-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CrownEvent-action: CrownAction--><!--Device-CrownEvent-action: CrownAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## angularVelocity

```TypeScript
angularVelocity: number
```

旋转角速度。

单位：deg/s

**Type:** number

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CrownEvent-angularVelocity: number--><!--Device-CrownEvent-angularVelocity: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## degree

```TypeScript
degree: number
```

相对旋转角度。

单位：deg 

取值范围:[-360, 360]。

**Type:** number

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CrownEvent-degree: number--><!--Device-CrownEvent-degree: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stopPropagation

```TypeScript
stopPropagation: Callback<void>
```

阻止[事件冒泡](../../../ui/arkts-interaction-basic-principles.md#事件冒泡)。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CrownEvent-stopPropagation: Callback<void>--><!--Device-CrownEvent-stopPropagation: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timestamp

```TypeScript
timestamp: number
```

时间戳。触发事件时距离系统启动的时间间隔。

单位：ns

**Type:** number

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CrownEvent-timestamp: number--><!--Device-CrownEvent-timestamp: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

