# ToolBarItem

## ToolBarItem

```TypeScript
export declare function ToolBarItem(
    options?: ToolBarItemOptions,
    content_?: CustomBuilder,
): ToolBarItemAttribute
```

定义ToolBarItem组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ToolBarItem(    options?: ToolBarItemOptions,    content_?: CustomBuilder,): ToolBarItemAttribute--><!--Device-unnamed-export declare function ToolBarItem(    options?: ToolBarItemOptions,    content_?: CustomBuilder,): ToolBarItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarItemOptions](../arkts-components/arkts-arkui-toolbaritemoptions-i.md) | No | 分栏选项 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 容器 |

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

定义ToolBarItem组件。需要在组件属性设置开始时调用setToolBarItemOptions，并在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ToolBarItem(    style: CustomBuilderT<ToolBarItemAttribute>,    content_?: CustomBuilder,): ToolBarItemAttribute--><!--Device-unnamed-export declare function ToolBarItem(    style: CustomBuilderT<ToolBarItemAttribute>,    content_?: CustomBuilder,): ToolBarItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ToolBarItemAttribute&gt; | Yes | 用于设置toolbaritem属性的回调。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 容器。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ToolBarItemAttribute](arkts-arkui-toolbar-toolbaritemattribute-i.md) | ToolBarItem的属性。 |

