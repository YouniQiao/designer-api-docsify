# CommonTransition

页面转场通用动效。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare class CommonTransition<T>--><!--Device-unnamed-declare class CommonTransition<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

转场通用动效的构造函数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonTransition-constructor()--><!--Device-CommonTransition-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## opacity

```TypeScript
opacity(value: number): T
```

设置入场的起点透明度值或者退场的终点透明度值。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonTransition-opacity(value: number): T--><!--Device-CommonTransition-opacity(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | 设置入场的起点透明度值或者退场的终点透明度值。&lt;br/&gt;取值范围：[0, 1] |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回当前组件。 |

## scale

```TypeScript
scale(value: ScaleOptions): T
```

设置页面转场时的缩放效果。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonTransition-scale(value: ScaleOptions): T--><!--Device-CommonTransition-scale(value: ScaleOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScaleOptions](arkts-arkui-scaleoptions-i.md) | Yes | 设置页面转场时的缩放效果，为入场时起点和退场时终点的值。&lt;br/&gt;- x：横向放大倍数（或缩小比例）。&lt;br/&gt;- y：纵向放大倍数（或缩小比例）。&lt;br/&gt;- z： 竖向放大倍数（或缩小比例）。&lt;br/&gt;- centerX、centerY缩放中心点。centerX和centerY默认值是"50%"，即默认以页面的中心点为旋转中心点。&lt;br/&gt;- 中心点为(0, 0)代表页面的左上 角。<br>**Since:** 18 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回当前组件。 |

## slide

```TypeScript
slide(value: SlideEffect): T
```

设置页面转场时的滑入滑出效果。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonTransition-slide(value: SlideEffect): T--><!--Device-CommonTransition-slide(value: SlideEffect): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SlideEffect](arkts-arkui-slideeffect-e.md) | Yes | 页面转场时的滑入滑出效果。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回当前组件。 |

## translate

```TypeScript
translate(value: TranslateOptions): T
```

设置页面转场时的平移效果。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonTransition-translate(value: TranslateOptions): T--><!--Device-CommonTransition-translate(value: TranslateOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TranslateOptions](../arkts-apis/arkts-arkui-common-translateoptions-i.md) | Yes | 设置页面转场时的平移效果，为入场时起点和退场时终点的值，和slide同时设置时默认生效slide。&lt;br/&gt;- x：横向的平移距离。&lt;br/&gt;- y：纵向的平 移距离。&lt;br/&gt;- z：竖向的平移距离。<br>**Since:** 18 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回当前组件。 |

