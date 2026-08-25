# SaveButton properties/events

Universal attributes are not supported. This component supports the attributes listed below, as well as universal attributes of security components. Only the following events are supported.

**Inheritance/Implementation:** SaveButtonAttribute extends SecurityComponentMethod<SaveButtonAttribute>

**Since:** 10

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## iconBorderRadius

```TypeScript
iconBorderRadius(radius: Dimension | BorderRadiuses)
```

Sets the corner radius of the **SaveButton** component.

**Since:** 20

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [BorderRadiuses](../arkts-apis/arkts-arkui-borderradiuses-t.md) | Yes |

## iconSize

```TypeScript
iconSize(size: Dimension | SizeOptions)
```

Sets the icon size of the **SaveButton** component.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [SizeOptions](../arkts-apis/arkts-arkui-sizeoptions-i.md) | Yes |

## onClick

```TypeScript
onClick(event: SaveButtonCallback)
```

Triggered when the **SaveButton** component is clicked. When a user clicks the save button for the first time, an authorization dialog box is displayed. If the user allows authorization, the app obtains temporary access to media library APIs. For details about the authorization duration, see the description of the SaveButton constructor. Authorization fails if the user declines authorization or closes the dialog box.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

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

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

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

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

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

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

## symbolFontWeight

```TypeScript
symbolFontWeight(fontWeight: number | FontWeight | string | Resource)
```

Sets the font weight of the symbol icon for the save button.  
- Before calling this method, you need to call [setIcon](#seticon) to configure a symbol-  
style icon resource (i.e., **\$r('sys.symbol.*xxx*')**).  
- If no symbol icon is configured, the font weight setting will not apply.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fontWeight | number \| FontWeight \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## symbolIconColor

```TypeScript
symbolIconColor(color: Array<ResourceColor>)
```

Sets the color of the symbol icon for the save button.  
- Before calling this method, you need to call [setIcon](#seticon) to configure a symbol-  
style icon resource (i.e., **\$r('sys.symbol.xxx')**).  
- If no symbol icon is set, the color set via this method does not take effect.  
- It is recommended that you use this API together with  
[symbolRenderingStrategy](#symbolrenderingstrategy) to achieve different rendering effects.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | Array&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)&gt; | Yes |

## symbolRenderingStrategy

```TypeScript
symbolRenderingStrategy(strategy: SymbolRenderingStrategy)
```

Sets the rendering strategy for the symbol icon of the save button.  
- Before calling this method, you need to call [setIcon](#seticon) to configure a symbol-  
style icon resource (i.e., **\$r('sys.symbol.*xxx*')**).  
- The configured rendering strategy will not apply if no symbol icon is set.  
- When this parameter is used together with [symbolIconColor](#symboliconcolor), the  
rendering strategy determines how the color array is applied.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

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

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |
