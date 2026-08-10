# WaterFlow

## WaterFlow

```TypeScript
export declare function WaterFlow(
    options?: WaterFlowOptions, 
    content_?: CustomBuilder,
): WaterFlowAttribute
```

定义瀑布流组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function WaterFlow(    options?: WaterFlowOptions,     content_?: CustomBuilder,): WaterFlowAttribute--><!--Device-unnamed-export declare function WaterFlow(    options?: WaterFlowOptions,     content_?: CustomBuilder,): WaterFlowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [WaterFlowOptions](../arkts-components/arkts-arkui-waterflowoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 子组件 |

**Return value:**

| Type | Description |
| --- | --- |
| [WaterFlowAttribute](arkts-arkui-waterflow-waterflowattribute-i.md) |  |


## WaterFlow

```TypeScript
export declare function WaterFlow(
    style_: CustomBuilderT<WaterFlowAttribute>, 
    content_?: CustomBuilder
): WaterFlowAttribute
```

定义WaterFlow组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function WaterFlow(    style_: CustomBuilderT<WaterFlowAttribute>,     content_?: CustomBuilder): WaterFlowAttribute--><!--Device-unnamed-export declare function WaterFlow(    style_: CustomBuilderT<WaterFlowAttribute>,     content_?: CustomBuilder): WaterFlowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;WaterFlowAttribute&gt; | Yes | 创建WaterFlow的样式 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [WaterFlowAttribute](arkts-arkui-waterflow-waterflowattribute-i.md) | WaterFlow的属性。 |

