# ToolBarItem

## ToolBarItem

```TypeScript
export declare function ToolBarItem(
    options?: ToolBarItemOptions,
    content_?: CustomBuilder,
): ToolBarItemAttribute
```

Defines ToolBarItem Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ToolBarItem(    options?: ToolBarItemOptions,    content_?: CustomBuilder,): ToolBarItemAttribute--><!--Device-unnamed-export declare function ToolBarItem(    options?: ToolBarItemOptions,    content_?: CustomBuilder,): ToolBarItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarItemOptions](../arkts-components/arkts-arkui-toolbaritemoptions-i.md) | No | column options |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarItemAttribute](arkts-arkui-toolbar-toolbaritemattribute-i.md) |  |


## ToolBarItem

```TypeScript
export declare function ToolBarItem(
    style: CustomBuilderT<ToolBarItemAttribute>,
    content_?: CustomBuilder,
): ToolBarItemAttribute
```

Defines ToolBarItem Component.It requires call setToolBarItemOptions at start of the component attribute set-up,and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ToolBarItem(    style: CustomBuilderT<ToolBarItemAttribute>,    content_?: CustomBuilder,): ToolBarItemAttribute--><!--Device-unnamed-export declare function ToolBarItem(    style: CustomBuilderT<ToolBarItemAttribute>,    content_?: CustomBuilder,): ToolBarItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ToolBarItemAttribute&gt; | Yes | the callback to set up toolbaritem's attributes. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarItemAttribute](arkts-arkui-toolbar-toolbaritemattribute-i.md) | The attribute of the ToolBarItem. |

