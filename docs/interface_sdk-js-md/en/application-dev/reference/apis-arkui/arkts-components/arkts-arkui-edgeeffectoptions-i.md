# EdgeEffectOptions

[edgeEffect](../../../reference/apis-arkui/arkui-ts/ts-container-scrollable-common.md#edgeeffect11)属性参数对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface EdgeEffectOptions--><!--Device-unnamed-declare interface EdgeEffectOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alwaysEnabled

```TypeScript
alwaysEnabled: boolean
```

组件内容大小小于组件自身时，设置是否开启滑动效果。设置为true开启滑动效果，设置为false关闭滑动效果。[List](../../apis-arkts/arkts-apis/arkts-arkts-util-list-list-c.md/arkts-arkts-util-list-list-c.md)、[Grid](../arkts-apis/arkts-arkui-grid-grid-f.md/arkts-arkui-grid-grid-f.md#grid)和  
[WaterFlow](./water_flow)组件默认值是false，[Scroll](../arkts-apis/arkts-arkui-scroll-scroll-f.md/arkts-arkui-scroll-scroll-f.md#scroll)组件默认值是true。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EdgeEffectOptions-alwaysEnabled: boolean--><!--Device-EdgeEffectOptions-alwaysEnabled: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## effectEdge

```TypeScript
effectEdge?: number
```

设置边缘效果生效的边缘。

如果设置[EffectEdge](arkts-arkui-effectedge-e.md).START表示只有起始边生效。如果设置[EffectEdge](arkts-arkui-effectedge-e.md).END表示只有末尾边生效。

默认值为[EffectEdge](arkts-arkui-effectedge-e.md).START | [EffectEdge](arkts-arkui-effectedge-e.md).END表示双边同时生效。当设置为其它异常值时，则默认双边同时生效。

如果需要双边都不生效，可将edgeEffect设置为EdgeEffect.None。

**Type:** number

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-EdgeEffectOptions-effectEdge?: number--><!--Device-EdgeEffectOptions-effectEdge?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

