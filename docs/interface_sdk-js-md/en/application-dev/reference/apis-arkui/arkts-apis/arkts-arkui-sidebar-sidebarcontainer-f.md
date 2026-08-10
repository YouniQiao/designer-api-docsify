# SideBarContainer

## SideBarContainer

```TypeScript
export declare function SideBarContainer(
  type?: SideBarContainerType,
  content_?: CustomBuilder
): SideBarContainerAttribute
```

创建侧边栏容器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function SideBarContainer(  type?: SideBarContainerType,  content_?: CustomBuilder): SideBarContainerAttribute--><!--Device-unnamed-export declare function SideBarContainer(  type?: SideBarContainerType,  content_?: CustomBuilder): SideBarContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [SideBarContainerType](arkts-arkui-sidebar-sidebarcontainertype-e.md) | No | 设置侧边栏的显示类型。&lt;br/&gt;默认值：SideBarContainerType.Embed |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 可以包含子组件。&lt;br/&gt;**说明：** &lt;br/&gt;1. 子组件类型：系统组件和自定义组件，不支持渲染控制类型（ [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)、 [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md)和 [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)）。&lt;br/&gt;2. 子组件个数：必须且仅包含2个子组件。&lt; br/&gt;3. 子组件个数异常时：3个或以上子组件，显示第一个和第二个。1个子组件，显示侧边栏，内容区为空白。&lt;br/&gt;4. SideBarContainer走焦时，先在内容区走焦，再在侧边栏走焦。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SideBarContainerAttribute](../arkts-components/arkts-arkui-sidebarcontainer-attribute.md) |  |


## SideBarContainer

```TypeScript
export declare function SideBarContainer(
 	style_: CustomBuilderT<SideBarContainerAttribute>,
 	content_?: CustomBuilder,
): SideBarContainerAttribute
```

定义侧边栏组件

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function SideBarContainer( 	style_: CustomBuilderT<SideBarContainerAttribute>, 	content_?: CustomBuilder,): SideBarContainerAttribute--><!--Device-unnamed-export declare function SideBarContainer( 	style_: CustomBuilderT<SideBarContainerAttribute>, 	content_?: CustomBuilder,): SideBarContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;SideBarContainerAttribute&gt; | Yes | 侧边栏属性实例 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 内容区 |

**Return value:**

| Type | Description |
| --- | --- |
| [SideBarContainerAttribute](../arkts-components/arkts-arkui-sidebarcontainer-attribute.md) |  |

