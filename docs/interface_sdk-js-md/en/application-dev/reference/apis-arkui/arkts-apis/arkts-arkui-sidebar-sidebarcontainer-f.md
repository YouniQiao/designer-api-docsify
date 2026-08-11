# SideBarContainer

## SideBarContainer

```TypeScript
export declare function SideBarContainer(
  type?: SideBarContainerType,
  content_?: CustomBuilder
): SideBarContainerAttribute
```

Defines sidebar Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function SideBarContainer(  type?: SideBarContainerType,  content_?: CustomBuilder): SideBarContainerAttribute--><!--Device-unnamed-export declare function SideBarContainer(  type?: SideBarContainerType,  content_?: CustomBuilder): SideBarContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [SideBarContainerType](arkts-arkui-sidebar-sidebarcontainertype-e.md) | No | sidebar constructor options |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

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

Defines sidebar Component

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function SideBarContainer( 	style_: CustomBuilderT<SideBarContainerAttribute>, 	content_?: CustomBuilder,): SideBarContainerAttribute--><!--Device-unnamed-export declare function SideBarContainer( 	style_: CustomBuilderT<SideBarContainerAttribute>, 	content_?: CustomBuilder,): SideBarContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;SideBarContainerAttribute&gt; | Yes | sidebar attribute instance |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SideBarContainerAttribute](../arkts-components/arkts-arkui-sidebarcontainer-attribute.md) |  |

