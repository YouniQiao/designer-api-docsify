# TabContent

## TabContent

```TypeScript
export declare function TabContent(
    
    content_?: CustomBuilder,
): TabContentAttribute
```

创建支持单个子组件。&lt;br/&gt;**说明：**&lt;br/&gt;可内置系统组件和自定义组件，支持渲染控制类型（
 [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)、  
 [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md)和  
 [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)）。页签和内容。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function TabContent(        content_?: CustomBuilder,): TabContentAttribute--><!--Device-unnamed-export declare function TabContent(        content_?: CustomBuilder,): TabContentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 支持单个子组件。&lt;br/&gt;**说明：**&lt;br/&gt;可内置系统组件和自定义组件，支持渲染控制类型（ [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)、 [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md)和 [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)）。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TabContentAttribute](../arkts-components/arkts-arkui-tabcontent-attribute.md) |  |


## TabContent

```TypeScript
export declare function TabContent(
 style_: CustomBuilderT<TabContentAttribute>,
 content_?: CustomBuilder,
): TabContentAttribute
```

定义选项卡内容组件

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function TabContent( style_: CustomBuilderT<TabContentAttribute>, content_?: CustomBuilder,): TabContentAttribute--><!--Device-unnamed-export declare function TabContent( style_: CustomBuilderT<TabContentAttribute>, content_?: CustomBuilder,): TabContentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;TabContentAttribute&gt; | Yes | tabContent属性实例 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 选项卡内容 |

**Return value:**

| Type | Description |
| --- | --- |
| [TabContentAttribute](../arkts-components/arkts-arkui-tabcontent-attribute.md) |  |

