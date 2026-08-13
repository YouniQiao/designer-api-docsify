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

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function SideBarContainer(  type?: SideBarContainerType,  content_?: CustomBuilder): SideBarContainerAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function SideBarContainer(  type?: SideBarContainerType,  content_?: CustomBuilder): SideBarContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [SideBarContainerType](arkts-na-sidebar-sidebarcontainertype-e.md) | No | sidebar constructor options |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SideBarContainerAttribute](arkts-na-sidebar-sidebarcontainerattribute-i.md) |  |


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

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function SideBarContainer( 	style_: CustomBuilderT<SideBarContainerAttribute>, 	content_?: CustomBuilder,): SideBarContainerAttribute--><!--Device-unnamed-@Builderexport declare function SideBarContainer( 	style_: CustomBuilderT<SideBarContainerAttribute>, 	content_?: CustomBuilder,): SideBarContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[SideBarContainerAttribute](arkts-na-sidebar-sidebarcontainerattribute-i.md)&gt; | Yes | sidebar attribute instance |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SideBarContainerAttribute](arkts-na-sidebar-sidebarcontainerattribute-i.md) |  |

