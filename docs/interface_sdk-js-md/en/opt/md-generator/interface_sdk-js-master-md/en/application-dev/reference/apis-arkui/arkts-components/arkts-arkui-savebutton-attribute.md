# SaveButton properties/events

Universal attributes are not supported. This component supports the attributes listed below, as well as universal attributes of security components. Only the following events are supported.

**Inheritance/Implementation:** SaveButtonAttribute extends SecurityComponentMethod<SaveButtonAttribute>

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare class SaveButtonAttribute--><!--Device-unnamed-declare class SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconBorderRadius

```TypeScript
iconBorderRadius(radius: Dimension | BorderRadiuses)
```

Sets the corner radius of the **SaveButton** component.

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SaveButtonAttribute-iconBorderRadius(radius: Dimension | BorderRadiuses): SaveButtonAttribute--><!--Device-SaveButtonAttribute-iconBorderRadius(radius: Dimension | BorderRadiuses): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [BorderRadiuses](../../apis-na/arkts-apis/arkts-na-units-borderradiuses-i.md) | Yes |

## iconSize

```TypeScript
iconSize(size: Dimension | SizeOptions)
```

Sets the icon size of the **SaveButton** component.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SaveButtonAttribute-iconSize(size: Dimension | SizeOptions): SaveButtonAttribute--><!--Device-SaveButtonAttribute-iconSize(size: Dimension | SizeOptions): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [SizeOptions](../arkts-apis/arkts-arkui-sizeoptions-i.md) | Yes |

## onClick

```TypeScript
onClick(event: SaveButtonCallback)
```

Triggered when the **SaveButton** component is clicked. When a user clicks the save button for the first time, an authorization dialog box is displayed. If the user allows authorization, the app obtains temporary access to media library APIs. For details about the authorization duration, see the description of the [SaveButton](../../../reference/apis-arkui/arkui-ts/ts-security-components-savebutton.md#savebutton-1) constructor. Authorization fails if the user declines authorization or closes the dialog box.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveButtonAttribute-onClick(event: SaveButtonCallback): SaveButtonAttribute--><!--Device-SaveButtonAttribute-onClick(event: SaveButtonCallback): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [SaveButtonCallback](arkts-arkui-savebuttoncallback-t.md) | Yes |

## setIcon

```TypeScript
setIcon(icon: Resource)
```

Sets the icon of the **SaveButton** component.

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SaveButtonAttribute-setIcon(icon: Resource): SaveButtonAttribute--><!--Device-SaveButtonAttribute-setIcon(icon: Resource): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| icon | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## setText

```TypeScript
setText(text: string | Resource)
```

Sets the text of the **SaveButton** component.

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SaveButtonAttribute-setText(text: string | Resource): SaveButtonAttribute--><!--Device-SaveButtonAttribute-setText(text: string | Resource): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## stateEffect

```TypeScript
stateEffect(enabled: boolean)
```

Sets the press effect of the **SaveButton** component.

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SaveButtonAttribute-stateEffect(enabled: boolean): SaveButtonAttribute--><!--Device-SaveButtonAttribute-stateEffect(enabled: boolean): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## symbolFontWeight

```TypeScript
symbolFontWeight(fontWeight: number | FontWeight | string | Resource)
```

Sets the font weight of the symbol icon for the save button. - Before calling this method, you need to call [setIcon](#setIcon) to configure a symbol- style icon resource (i.e., **\$r('sys.symbol.*xxx*')**). - If no symbol icon is configured, the font weight setting will not apply.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SaveButtonAttribute-symbolFontWeight(fontWeight: number | FontWeight | string | Resource): SaveButtonAttribute--><!--Device-SaveButtonAttribute-symbolFontWeight(fontWeight: number | FontWeight | string | Resource): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fontWeight | number \| FontWeight \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## symbolIconColor

```TypeScript
symbolIconColor(color: Array<ResourceColor>)
```

Sets the color of the symbol icon for the save button. - Before calling this method, you need to call [setIcon](#setIcon) to configure a symbol- style icon resource (i.e., **\$r('sys.symbol.xxx')**). - If no symbol icon is set, the color set via this method does not take effect. - It is recommended that you use this API together with [symbolRenderingStrategy](#symbolRenderingStrategy) to achieve different rendering effects.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SaveButtonAttribute-symbolIconColor(color: Array<ResourceColor>): SaveButtonAttribute--><!--Device-SaveButtonAttribute-symbolIconColor(color: Array<ResourceColor>): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | Array&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)&gt; | Yes |

## symbolRenderingStrategy

```TypeScript
symbolRenderingStrategy(strategy: SymbolRenderingStrategy)
```

Sets the rendering strategy for the symbol icon of the save button. - Before calling this method, you need to call [setIcon](#setIcon) to configure a symbol- style icon resource (i.e., **\$r('sys.symbol.*xxx*')**). - The configured rendering strategy will not apply if no symbol icon is set. - When this parameter is used together with [symbolIconColor](#symbolIconColor), the rendering strategy determines how the color array is applied.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SaveButtonAttribute-symbolRenderingStrategy(strategy: SymbolRenderingStrategy): SaveButtonAttribute--><!--Device-SaveButtonAttribute-symbolRenderingStrategy(strategy: SymbolRenderingStrategy): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strategy | [SymbolRenderingStrategy](arkts-arkui-symbolrenderingstrategy-e.md) | Yes |

## userCancelEvent

```TypeScript
userCancelEvent(enabled: boolean)
```

Sets the user authorization cancellation event for the **SaveButton** component. This API can be used to distinguish between user cancellation and authorization failures for differentiated service logic, such as logging user behaviors or prompting users to retry.

**Since:** 21

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-SaveButtonAttribute-userCancelEvent(enabled: boolean): SaveButtonAttribute--><!--Device-SaveButtonAttribute-userCancelEvent(enabled: boolean): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |
