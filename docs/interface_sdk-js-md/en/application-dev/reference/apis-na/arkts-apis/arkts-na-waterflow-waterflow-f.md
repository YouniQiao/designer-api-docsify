# WaterFlow

## WaterFlow

```TypeScript
@ComponentBuilder
export declare function WaterFlow(
    options?: WaterFlowOptions,
    content_?: CustomBuilder,
): WaterFlowAttribute
```

Defines WaterFlow Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function WaterFlow(    options?: WaterFlowOptions,    content_?: CustomBuilder,): WaterFlowAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function WaterFlow(    options?: WaterFlowOptions,    content_?: CustomBuilder,): WaterFlowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [WaterFlowOptions](arkts-na-waterflow-waterflowoptions-i.md) | No | options |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| WaterFlowAttribute |  |


## WaterFlow

```TypeScript
@Builder
export declare function WaterFlow(
    style_: CustomBuilderT<WaterFlowAttribute>,
    content_?: CustomBuilder
): WaterFlowAttribute
```

Defines WaterFlow Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function WaterFlow(    style_: CustomBuilderT<WaterFlowAttribute>,    content_?: CustomBuilder): WaterFlowAttribute--><!--Device-unnamed-@Builderexport declare function WaterFlow(    style_: CustomBuilderT<WaterFlowAttribute>,    content_?: CustomBuilder): WaterFlowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;WaterFlowAttribute&gt; | Yes | The style to create a WaterFlow. |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| WaterFlowAttribute | The attribute of the WaterFlow. |

