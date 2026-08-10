# ProgressMask

ProgressMask设置遮罩的进度、最大值和颜色。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare class ProgressMask--><!--Device-unnamed-declare class ProgressMask-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: number, total: number, color: ResourceColor)
```

构造ProgressMask对象。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProgressMask-constructor(value: number, total: number, color: ResourceColor)--><!--Device-ProgressMask-constructor(value: number, total: number, color: ResourceColor)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | 进度遮罩的当前值。&lt;br/&gt; 取值范围：[0.0, +∞) |
| total | number | Yes | 进度遮罩的最大值。&lt;br/&gt; 取值范围：[0.0, +∞) |
| color | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | 进度遮罩的颜色。 |

## enableBreathingAnimation

```TypeScript
enableBreathingAnimation(value: boolean): void
```

进度满时的呼吸光晕动画开关。不设置该接口时，默认关闭呼吸光晕动画。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ProgressMask-enableBreathingAnimation(value: boolean): void--><!--Device-ProgressMask-enableBreathingAnimation(value: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | 是否开启呼吸光晕动画。&lt;br/&gt;true：开启呼吸光晕动画。&lt;br/&gt;false：关闭呼吸光晕动画。 |

## updateColor

```TypeScript
updateColor(value: ResourceColor): void
```

更新进度遮罩的颜色。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProgressMask-updateColor(value: ResourceColor): void--><!--Device-ProgressMask-updateColor(value: ResourceColor): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | 进度遮罩的颜色。 |

## updateProgress

```TypeScript
updateProgress(value: number): void
```

更新进度遮罩的进度值。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProgressMask-updateProgress(value: number): void--><!--Device-ProgressMask-updateProgress(value: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | 进度遮罩的当前值。 |

