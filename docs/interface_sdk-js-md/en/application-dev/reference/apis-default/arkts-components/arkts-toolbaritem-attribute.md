# ToolBarItemAttribute

Defines the ToolBarItem component attribute functions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface ToolBarItemAttribute--><!--Device-unnamed-export declare interface ToolBarItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyAttributesFinish

```TypeScript
applyAttributesFinish(): void
```

Notify ToolBarItem has finished setting up its attributes.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarItemAttribute-applyAttributesFinish(): void--><!--Device-ToolBarItemAttribute-applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## debugLine

```TypeScript
debugLine(sourceLine: string, moduleName?: string): this
```

Set the component's source code redirection information.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarItemAttribute-debugLine(sourceLine: string, moduleName?: string): this--><!--Device-ToolBarItemAttribute-debugLine(sourceLine: string, moduleName?: string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceLine | string | Yes | the source code line. |
| moduleName | string | No | module to which the component belongs. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setToolBarItemOptions

```TypeScript
setToolBarItemOptions(options?: ToolBarItemOptions): this
```

Sets toolbar item options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarItemAttribute-setToolBarItemOptions(options?: ToolBarItemOptions): this--><!--Device-ToolBarItemAttribute-setToolBarItemOptions(options?: ToolBarItemOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarItemOptions](arkts-toolbar-toolbaritemoptions-i.md) | No | column options |

**Return value:**

| Type | Description |
| --- | --- |
| this | ToolBarItemAttribute instance |

