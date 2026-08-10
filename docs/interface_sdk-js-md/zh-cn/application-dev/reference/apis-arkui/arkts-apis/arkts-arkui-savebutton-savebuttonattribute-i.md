# SaveButtonAttribute

Declares interface for the attributes of the save button.

**继承/实现关系：** SaveButtonAttribute extends [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface SaveButtonAttribute extends SecurityComponentMethod--><!--Device-unnamed-export declare interface SaveButtonAttribute extends SecurityComponentMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## iconBorderRadius

```TypeScript
iconBorderRadius(radius: Dimension | BorderRadiuses | undefined): this
```

Sets the border radius of the icon.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SaveButtonAttribute-iconBorderRadius(radius: Dimension | BorderRadiuses | undefined): this--><!--Device-SaveButtonAttribute-iconBorderRadius(radius: Dimension | BorderRadiuses | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | [Dimension](arkts-arkui-dimension-t.md) \| BorderRadiuses \| undefined | 是 | Border radius of the icon to set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the save button. |

## iconSize

```TypeScript
iconSize(size: Dimension | SizeOptions | undefined): this
```

Sets the size of the icon.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SaveButtonAttribute-iconSize(size: Dimension | SizeOptions | undefined): this--><!--Device-SaveButtonAttribute-iconSize(size: Dimension | SizeOptions | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Dimension](arkts-arkui-dimension-t.md) \| SizeOptions \| undefined | 是 | Dimensions of the icon to set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the save button. |

## onClick

```TypeScript
onClick(event: SaveButtonCallback | undefined): this
```

Called when the save button is clicked.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SaveButtonAttribute-onClick(event: SaveButtonCallback | undefined): this--><!--Device-SaveButtonAttribute-onClick(event: SaveButtonCallback | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [SaveButtonCallback](arkts-arkui-savebuttoncallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the save button. |

## setIcon

```TypeScript
setIcon(icon: Resource | undefined): this
```

Sets the icon of the save button.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SaveButtonAttribute-setIcon(icon: Resource | undefined): this--><!--Device-SaveButtonAttribute-setIcon(icon: Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| icon | [Resource](arkts-arkui-resource-t.md) \| undefined | 是 | Source of the icon. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the save button. |

## setText

```TypeScript
setText(text: string | Resource | undefined): this
```

Sets the text of the save button.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SaveButtonAttribute-setText(text: string | Resource | undefined): this--><!--Device-SaveButtonAttribute-setText(text: string | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string \| Resource \| undefined | 是 | Content of text. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the save button. |

## stateEffect

```TypeScript
stateEffect(enabled: boolean | undefined): this
```

Enables the press effect of the button.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SaveButtonAttribute-stateEffect(enabled: boolean | undefined): this--><!--Device-SaveButtonAttribute-stateEffect(enabled: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 | Whether to enable the press effect. The value true means to enable the press effect; the value false means the opposite. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the save button. |

## symbolFontWeight

```TypeScript
symbolFontWeight(fontWeight: int | FontWeight | string | Resource | undefined): this
```

Sets the font weight of the symbol icon.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SaveButtonAttribute-symbolFontWeight(fontWeight: int | FontWeight | string | Resource | undefined): this--><!--Device-SaveButtonAttribute-symbolFontWeight(fontWeight: int | FontWeight | string | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fontWeight | int \| FontWeight \| string \| Resource \| undefined | 是 | Font weight of the symbol icon. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the save button. |

## symbolIconColor

```TypeScript
symbolIconColor(color: Array<ResourceColor> | undefined): this
```

Sets the color of the symbol icon.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SaveButtonAttribute-symbolIconColor(color: Array<ResourceColor> | undefined): this--><!--Device-SaveButtonAttribute-symbolIconColor(color: Array<ResourceColor> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Array&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md)&gt; \| undefined | 是 | Color of the symbol icon. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the save button. |

## symbolRenderingStrategy

```TypeScript
symbolRenderingStrategy(strategy: SymbolRenderingStrategy | undefined): this
```

Sets the rendering policy of the symbol icon.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SaveButtonAttribute-symbolRenderingStrategy(strategy: SymbolRenderingStrategy | undefined): this--><!--Device-SaveButtonAttribute-symbolRenderingStrategy(strategy: SymbolRenderingStrategy | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | [SymbolRenderingStrategy](../arkts-components/arkts-arkui-symbolrenderingstrategy-e.md) \| undefined | 是 | Rendering policy of the symbol icon. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the save button. |

## userCancelEvent

```TypeScript
userCancelEvent(enabled: boolean | undefined): this
```

Receives the event when the user clicks cancel.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SaveButtonAttribute-userCancelEvent(enabled: boolean | undefined): this--><!--Device-SaveButtonAttribute-userCancelEvent(enabled: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 | Whether to receive the event when the user clicks cancel. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attributes of the save button. |

