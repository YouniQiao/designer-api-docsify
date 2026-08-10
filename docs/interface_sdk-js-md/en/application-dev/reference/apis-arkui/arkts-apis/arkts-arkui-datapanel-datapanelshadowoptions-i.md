# DataPanelShadowOptions

DataPanelShadowOptions继承自[MultiShadowOptions](arkts-arkui-common-multishadowoptions-i.md)，具有MultiShadowOptions的全部属性。

**Inheritance/Implementation:** DataPanelShadowOptions extends [MultiShadowOptions](arkts-arkui-common-multishadowoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface DataPanelShadowOptions extends MultiShadowOptions--><!--Device-unnamed-export declare interface DataPanelShadowOptions extends MultiShadowOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colors

```TypeScript
colors?: Array<ResourceColor | LinearGradient>
```

各数据段投影的颜色。默认值：与valueColors值相同  
**说明：**若设置的投影颜色的个数少于数据段个数时，则显示的投影颜色的个数和设置的投影颜色个数一致。

**Type:** Array&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md) \| LinearGradient&gt;

**Default:** Consistent with valueColors

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataPanelShadowOptions-colors?: Array<ResourceColor | LinearGradient>--><!--Device-DataPanelShadowOptions-colors?: Array<ResourceColor | LinearGradient>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

