# SideBarContainer

## SideBarContainer

```TypeScript
@ComponentBuilder
export declare function SideBarContainer(
  type?: SideBarContainerType,
  content_?: CustomBuilder
): SideBarContainerAttribute
```

Defines sidebar Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function SideBarContainer(  type?: SideBarContainerType,  content_?: CustomBuilder): SideBarContainerAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function SideBarContainer(  type?: SideBarContainerType,  content_?: CustomBuilder): SideBarContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [SideBarContainerType](arkts-sidebar-sidebarcontainertype-e.md) | No | sidebar constructor options |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SideBarContainerAttribute](arkts-sidebarcontainer-attribute.md) |  |


## SideBarContainer

```TypeScript
@Builder
export declare function SideBarContainer(
 	style_: CustomBuilderT<SideBarContainerAttribute>,
 	content_?: CustomBuilder,
): SideBarContainerAttribute
```

Defines sidebar Component

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function SideBarContainer( 	style_: CustomBuilderT<SideBarContainerAttribute>, 	content_?: CustomBuilder,): SideBarContainerAttribute--><!--Device-unnamed-@Builderexport declare function SideBarContainer( 	style_: CustomBuilderT<SideBarContainerAttribute>, 	content_?: CustomBuilder,): SideBarContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[SideBarContainerAttribute](arkts-sidebarcontainer-attribute.md)&gt; | Yes | sidebar attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SideBarContainerAttribute](arkts-sidebarcontainer-attribute.md) |  |

