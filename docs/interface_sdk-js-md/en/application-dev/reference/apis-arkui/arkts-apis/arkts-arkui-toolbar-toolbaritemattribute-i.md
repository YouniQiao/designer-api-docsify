# ToolBarItemAttribute

定义ToolBarItem组件的属性方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ToolBarItemAttribute--><!--Device-unnamed-export declare interface ToolBarItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

通知ToolBarItem已完成属性设置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarItemAttribute-applyAttributesFinish(): void--><!--Device-ToolBarItemAttribute-applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

设置组件的源代码重定向信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarItemAttribute-debugLine(sourceLine: string, moduleName?: string): this--><!--Device-ToolBarItemAttribute-debugLine(sourceLine: string, moduleName?: string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceLine | string | Yes | 源代码行。 |
| moduleName | string | No | 组件所属的模块。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setToolBarItemOptions

```TypeScript
setToolBarItemOptions(options?: ToolBarItemOptions): this
```

设置toolbar item选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarItemAttribute-setToolBarItemOptions(options?: ToolBarItemOptions): this--><!--Device-ToolBarItemAttribute-setToolBarItemOptions(options?: ToolBarItemOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarItemOptions](../arkts-components/arkts-arkui-toolbaritemoptions-i.md) | No | 列选项 |

**Return value:**

| Type | Description |
| --- | --- |
| this | ToolBarItemAttribute实例 |

