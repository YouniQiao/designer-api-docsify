# ToolBarItem

## ToolBarItem

```TypeScript
@ComponentBuilder
export declare function ToolBarItem(
    options?: ToolBarItemOptions,
    content_?: CustomBuilder,
): ToolBarItemAttribute
```

Defines ToolBarItem Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function ToolBarItem(    options?: ToolBarItemOptions,    content_?: CustomBuilder,): ToolBarItemAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ToolBarItem(    options?: ToolBarItemOptions,    content_?: CustomBuilder,): ToolBarItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarItemOptions](arkts-na-toolbar-toolbaritemoptions-i.md) | No | column options |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarItemAttribute](arkts-na-toolbar-toolbaritemattribute-i.md) |  |


## ToolBarItem

```TypeScript
@Builder
export declare function ToolBarItem(
    style: CustomBuilderT<ToolBarItemAttribute>,
    content_?: CustomBuilder,
): ToolBarItemAttribute
```

Defines ToolBarItem Component.It requires call setToolBarItemOptions at start of the component attribute set-up, and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ToolBarItem(    style: CustomBuilderT<ToolBarItemAttribute>,    content_?: CustomBuilder,): ToolBarItemAttribute--><!--Device-unnamed-@Builderexport declare function ToolBarItem(    style: CustomBuilderT<ToolBarItemAttribute>,    content_?: CustomBuilder,): ToolBarItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;[ToolBarItemAttribute](arkts-na-toolbar-toolbaritemattribute-i.md)&gt; | Yes | the callback to set up toolbaritem's attributes. |
| content_ | CustomBuilder | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarItemAttribute](arkts-na-toolbar-toolbaritemattribute-i.md) | The attribute of the ToolBarItem. |

