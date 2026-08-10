# Tabs

## Tabs

```TypeScript
export declare function Tabs(
    options?: TabsOptions, 
    content_?: CustomBuilder,
): TabsAttribute
```

创建Tabs容器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Tabs(    options?: TabsOptions,     content_?: CustomBuilder,): TabsAttribute--><!--Device-unnamed-export declare function Tabs(    options?: TabsOptions,     content_?: CustomBuilder,): TabsAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TabsOptions](arkts-arkui-tabs-tabsoptions-i.md) | No | Tabs组件参数。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 仅支持子组件[TabContent](../../apis-arkui/arkts-components/arkts-arkui-tab_content-i)，以及渲染控制类型 [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)和 [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md)，不建议自定义组件作为子组件。并且if/else和ForEach下也仅支持 TabContent作为子组件，不建议自定义组件作为子组件。&lt;br/&gt;**说明：** &lt;br/&gt;1. Tabs子组件设置了通用属性 [visibility](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-visibility.md#visibility)的值为None，或者设 置值为Hidden时，对应子组件不显示，但依然会在视窗内占位。&lt;br/&gt;2. 已经显示的Tabs子组件TabContent后续隐藏时不会被销毁，若需要页面懒加载和释放，可以参考 [示例13](../../../reference/apis-arkui/arkui-ts/ts-container-tabs copy.md#示例13页面懒加载和释放)。&lt;br/&gt;3. Tabs设置 [height](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-size.md#height)为auto时，可根据子组件高度自适应高度大小。设置 [width](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-size.md#width)为auto时，可根据子组件宽度自适应宽度大小。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TabsAttribute](../arkts-components/arkts-arkui-tabs-attribute.md) |  |


## Tabs

```TypeScript
export declare function Tabs(
 style_: CustomBuilderT<TabsAttribute>,
 content_?: CustomBuilder,
): TabsAttribute
```

定义Tabs组件

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Tabs( style_: CustomBuilderT<TabsAttribute>, content_?: CustomBuilder,): TabsAttribute--><!--Device-unnamed-export declare function Tabs( style_: CustomBuilderT<TabsAttribute>, content_?: CustomBuilder,): TabsAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;TabsAttribute&gt; | Yes | tabs属性实例 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 内容区 |

**Return value:**

| Type | Description |
| --- | --- |
| [TabsAttribute](../arkts-components/arkts-arkui-tabs-attribute.md) |  |

