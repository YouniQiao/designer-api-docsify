# SaveButtonAttribute

Declares interface for the attributes of the save button.

**Inheritance/Implementation:** SaveButtonAttribute extends [SecurityComponentMethod](securitycomponent-securitycomponentmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SaveButtonAttribute extends SecurityComponentMethod--><!--Device-unnamed-export declare interface SaveButtonAttribute extends SecurityComponentMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconBorderRadius

```TypeScript
iconBorderRadius(radius: Dimension | BorderRadiuses | undefined): this
```

Sets the border radius of the icon.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

<!--Device-SaveButtonAttribute-iconBorderRadius(radius: Dimension | BorderRadiuses | undefined): this--><!--Device-SaveButtonAttribute-iconBorderRadius(radius: Dimension | BorderRadiuses | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| BorderRadiuses \| undefined | Yes | Border radius of the icon to set. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the attributes of the save button. |

## iconSize

```TypeScript
iconSize(size: Dimension | SizeOptions | undefined): this
```

Sets the size of the icon.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SaveButtonAttribute-iconSize(size: Dimension | SizeOptions | undefined): this--><!--Device-SaveButtonAttribute-iconSize(size: Dimension | SizeOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| SizeOptions \| undefined | Yes | Dimensions of the icon to set. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the attributes of the save button. |

## onClick

```TypeScript
onClick(event: SaveButtonCallback | undefined): this
```

Called when the save button is clicked.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SaveButtonAttribute-onClick(event: SaveButtonCallback | undefined): this--><!--Device-SaveButtonAttribute-onClick(event: SaveButtonCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the attribute of the save button. |

## setIcon

```TypeScript
setIcon(icon: Resource | undefined): this
```

Sets the icon of the save button.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

<!--Device-SaveButtonAttribute-setIcon(icon: Resource | undefined): this--><!--Device-SaveButtonAttribute-setIcon(icon: Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Source of the icon. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the attributes of the save button. |

## setText

```TypeScript
setText(text: string | Resource | undefined): this
```

Sets the text of the save button.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

<!--Device-SaveButtonAttribute-setText(text: string | Resource | undefined): this--><!--Device-SaveButtonAttribute-setText(text: string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string \| Resource \| undefined | Yes | Content of text. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the attributes of the save button. |

## stateEffect

```TypeScript
stateEffect(enabled: boolean | undefined): this
```

Enables the press effect of the button.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

<!--Device-SaveButtonAttribute-stateEffect(enabled: boolean | undefined): this--><!--Device-SaveButtonAttribute-stateEffect(enabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | Whether to enable the press effect. The value true means to enable the press effect; the value false means the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the attributes of the save button. |

## symbolFontWeight

```TypeScript
symbolFontWeight(fontWeight: int | FontWeight | string | Resource | undefined): this
```

Sets the font weight of the symbol icon.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

<!--Device-SaveButtonAttribute-symbolFontWeight(fontWeight: int | FontWeight | string | Resource | undefined): this--><!--Device-SaveButtonAttribute-symbolFontWeight(fontWeight: int | FontWeight | string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fontWeight | int \| FontWeight \| string \| Resource \| undefined | Yes | Font weight of the symbol icon. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the attributes of the save button. |

## symbolIconColor

```TypeScript
symbolIconColor(color: Array<ResourceColor> | undefined): this
```

Sets the color of the symbol icon.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

<!--Device-SaveButtonAttribute-symbolIconColor(color: Array<ResourceColor> | undefined): this--><!--Device-SaveButtonAttribute-symbolIconColor(color: Array<ResourceColor> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; \| undefined | Yes | Color of the symbol icon. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the attributes of the save button. |

## symbolRenderingStrategy

```TypeScript
symbolRenderingStrategy(strategy: SymbolRenderingStrategy | undefined): this
```

Sets the rendering policy of the symbol icon.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

<!--Device-SaveButtonAttribute-symbolRenderingStrategy(strategy: SymbolRenderingStrategy | undefined): this--><!--Device-SaveButtonAttribute-symbolRenderingStrategy(strategy: SymbolRenderingStrategy | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| strategy | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | Rendering policy of the symbol icon. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the attributes of the save button. |

## userCancelEvent

```TypeScript
userCancelEvent(enabled: boolean | undefined): this
```

Receives the event when the user clicks cancel.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SaveButtonAttribute-userCancelEvent(enabled: boolean | undefined): this--><!--Device-SaveButtonAttribute-userCancelEvent(enabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | Whether to receive the event when the user clicks cancel. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the attributes of the save button. |

