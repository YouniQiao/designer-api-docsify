# NavDestination

## NavDestination

```TypeScript
export declare function NavDestination(

  content_?: CustomBuilder
): NavDestinationAttribute
```

创建[Navigation](../../apis-arkui/arkts-components/arkts-arkui-navigation-i)子页面的根容器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function NavDestination(  content_?: CustomBuilder): NavDestinationAttribute--><!--Device-unnamed-export declare function NavDestination(  content_?: CustomBuilder): NavDestinationAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 否 | 支持多个子组件。&lt;br/&gt;**说明：** &lt;br/&gt;子组件类型：系统组件和自定义组件，支持渲染控制类型（ [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)、 [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md)和 [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)）。 |

**返回值：**

| 类型 | 说明 |
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

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function NavDestination( style_: CustomBuilderT<NavDestinationAttribute>, content_?: CustomBuilder,): NavDestinationAttribute--><!--Device-unnamed-export declare function NavDestination( style_: CustomBuilderT<NavDestinationAttribute>, content_?: CustomBuilder,): NavDestinationAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;NavDestinationAttribute&gt; | 是 | navDestination属性实例 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 否 | 内容区 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NavDestinationAttribute](arkts-arkui-navdestination-navdestinationattribute-i.md) |  |

