# NavDestination

## NavDestination

```TypeScript
export declare function NavDestination(

  content_?: CustomBuilder
): NavDestinationAttribute
```

创建[Navigation](../../apis-arkui/arkts-components/arkts-arkui-navigation-i)子页面的根容器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function NavDestination(  content_?: CustomBuilder): NavDestinationAttribute--><!--Device-unnamed-export declare function NavDestination(  content_?: CustomBuilder): NavDestinationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 支持多个子组件。&lt;br/&gt;**说明：** &lt;br/&gt;子组件类型：系统组件和自定义组件，支持渲染控制类型（ [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)、 [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md)和 [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)）。 |

**Return value:**

| Type | Description |
| --- | --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |  |


## NavDestination

```TypeScript
export declare function NavDestination(
 style_: CustomBuilderT<NavDestinationAttribute>,
 content_?: CustomBuilder,
): NavDestinationAttribute
```

定义NavDestination组件

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function NavDestination( style_: CustomBuilderT<NavDestinationAttribute>, content_?: CustomBuilder,): NavDestinationAttribute--><!--Device-unnamed-export declare function NavDestination( style_: CustomBuilderT<NavDestinationAttribute>, content_?: CustomBuilder,): NavDestinationAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;NavDestinationAttribute&gt; | Yes | navDestination属性实例 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 内容区 |

**Return value:**

| Type | Description |
| --- | --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |  |

