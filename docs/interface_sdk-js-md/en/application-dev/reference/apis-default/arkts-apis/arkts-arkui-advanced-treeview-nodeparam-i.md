# NodeParam

Declare NodeParam

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NodeParam--><!--Device-unnamed-export interface NodeParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## container

```TypeScript
container?: () => void
```

Right-click child component bound to the node. The child component is decorated with @Builder.Default value: **() =&gt; void**.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeParam-container?: () => void--><!--Device-NodeParam-container?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## currentNodeId

```TypeScript
currentNodeId?: int
```

Current child node ID.The value must be greater than or equal to -1.The value cannot be the root node ID or null. Otherwise, an exception is thrown. In addition, duplicate **currentNodeId** values are not allowed.Default value: **-1**

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeParam-currentNodeId?: int--><!--Device-NodeParam-currentNodeId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## editIcon

```TypeScript
editIcon?: ResourceStr
```

Edit icon.The default value is an empty string.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeParam-editIcon?: ResourceStr--><!--Device-NodeParam-editIcon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: ResourceStr
```

Icon.The default value is an empty string.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeParam-icon?: ResourceStr--><!--Device-NodeParam-icon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isFolder

```TypeScript
isFolder?: boolean
```

Whether the node is a directory.Default value: **false**.  
**true**: The node is a directory. **false**: The node is not a directory.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeParam-isFolder?: boolean--><!--Device-NodeParam-isFolder?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## parentNodeId

```TypeScript
parentNodeId?: int
```

ID of the parent node.The value must be greater than or equal to -1.Default value: -1. The root node ID is -1. If the value is less than -1, the setting does not take effect.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeParam-parentNodeId?: int--><!--Device-NodeParam-parentNodeId?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryTitle

```TypeScript
primaryTitle?: ResourceStr
```

Primary title.The default value is an empty string.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeParam-primaryTitle?: ResourceStr--><!--Device-NodeParam-primaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitle

```TypeScript
secondaryTitle?: ResourceStr
```

Secondary title.The default value is an empty string.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeParam-secondaryTitle?: ResourceStr--><!--Device-NodeParam-secondaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIcon

```TypeScript
selectedIcon?: ResourceStr
```

Icon of the selected node.The default value is an empty string.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeParam-selectedIcon?: ResourceStr--><!--Device-NodeParam-selectedIcon?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolEditIconStyle

```TypeScript
symbolEditIconStyle?: SymbolGlyphModifier
```

Symbol edit icon, which has a higher priority than **editIcon**.Default value: **undefined**

**Type:** SymbolGlyphModifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeParam-symbolEditIconStyle?: SymbolGlyphModifier--><!--Device-NodeParam-symbolEditIconStyle?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolIconStyle

```TypeScript
symbolIconStyle?: SymbolGlyphModifier
```

Symbol icon, which has higher priority than **icon**.Default value: **undefined**

**Type:** SymbolGlyphModifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeParam-symbolIconStyle?: SymbolGlyphModifier--><!--Device-NodeParam-symbolIconStyle?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolSelectedIconStyle

```TypeScript
symbolSelectedIconStyle?: SymbolGlyphModifier
```

Symbol icon of the selected node., which has higher priority than **selectedIcon**.Default value: **undefined**

**Type:** SymbolGlyphModifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeParam-symbolSelectedIconStyle?: SymbolGlyphModifier--><!--Device-NodeParam-symbolSelectedIconStyle?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

