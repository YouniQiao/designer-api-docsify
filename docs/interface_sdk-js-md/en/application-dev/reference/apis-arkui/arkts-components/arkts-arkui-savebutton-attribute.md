# SaveButton properties/events

不支持通用属性，除了继承[安全控件通用属性](./security_component)，还支持以下属性。不支持通用事件，仅支持以下事件。

**Inheritance/Implementation:** SaveButtonAttribute extends [SecurityComponentMethod<SaveButtonAttribute>](SecurityComponentMethod<SaveButtonAttribute>)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare class SaveButtonAttribute extends SecurityComponentMethod<SaveButtonAttribute>--><!--Device-unnamed-declare class SaveButtonAttribute extends SecurityComponentMethod<SaveButtonAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconBorderRadius

```TypeScript
iconBorderRadius(radius: Dimension | BorderRadiuses)
```

设置保存控件图标的边框圆角半径。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SaveButtonAttribute-iconBorderRadius(radius: Dimension | BorderRadiuses): SaveButtonAttribute--><!--Device-SaveButtonAttribute-iconBorderRadius(radius: Dimension | BorderRadiuses): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| BorderRadiuses | Yes | 保存控件图标的圆角半径，支持设置四个圆角。 &lt;br&gt;默认值：四个圆角均为0vp。支持像素单位（vp、px等），取值范围≥0。传入负值时自动修正为0。&lt;br/&gt;若应用不具备ohos.permission.CUSTOMIZE_SAVE_BUTTON权限，则图标的圆角半径 设置不生效。 |

## iconSize

```TypeScript
iconSize(size: Dimension | SizeOptions)
```

设置保存控件的图标尺寸。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SaveButtonAttribute-iconSize(size: Dimension | SizeOptions): SaveButtonAttribute--><!--Device-SaveButtonAttribute-iconSize(size: Dimension | SizeOptions): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| SizeOptions | Yes | 图标尺寸，支持像素单位（vp、px等）。 &lt;br&gt;不支持设置百分比字符串。若设置Dimension类型入参的百分比字符串，则图标尺寸显示为默认值； 若设置SizeOptions类型入参的width或height属性为百分比字符串，则图标尺寸显示为0vp。&lt;br/&gt;对于保存控件提供的系统图标：&lt;br/&gt;- 使用Dimension类型入参时，宽 、高相等，均为设定值。&lt;br/&gt;- 使用SizeOptions类型入参时，若宽、高设定值不一致，则宽、高相等取两者较小值；若仅设定其中一个值，则取该值作为宽、高值。系统提供图标采用此规则是为保证图标的正方形显示和视觉一致 性。&lt;br/&gt;对于自定义图标：&lt;br/&gt;- 使用Dimension类型入参时，宽、高相等，均为设定值。&lt;br/&gt;- 使用SizeOptions类型入参时，建议同时设定宽和高，此时按照指定宽、高生效；若仅设定其中一个值，则宽 高均显示为该设定值。自定义图标允许灵活设定尺寸以适应不同图片比例。&lt;br/&gt;- 当设定的宽高与自定义图标的宽高比例不一致时，图片按[ImageFit.Cover](../arkts-apis/arkts-arkui-enums-imagefit-e.md/arkts-arkui-enums-imagefit-e.md)的方式填充显示区域。 |

## onClick

```TypeScript
onClick(event: SaveButtonCallback)
```

点击保存控件触发该回调。用户首次点击保存控件时会展示授权弹窗，点击允许后授权成功，应用会获取访问媒体库接口的临时授权（授权持续时间见[SaveButton](../../../reference/apis-arkui/arkui-ts/ts-security-components-savebutton.md#savebutton-1)构造函数说明）；点击拒绝或关闭弹窗则授权失败。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveButtonAttribute-onClick(event: SaveButtonCallback): SaveButtonAttribute--><!--Device-SaveButtonAttribute-onClick(event: SaveButtonCallback): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [SaveButtonCallback](../arkts-apis/arkts-arkui-savebuttoncallback-t.md) | Yes | 点击事件的回调对象，包含点击事件信息、授权结果和错误信息。 &lt;br&gt;从APIversion 18开始，统一使用SaveButtonCallback，可额外获取error信息。<br>**Since:** 18 |

## setIcon

```TypeScript
setIcon(icon: Resource)
```

设置保存控件的图标。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SaveButtonAttribute-setIcon(icon: Resource): SaveButtonAttribute--><!--Device-SaveButtonAttribute-setIcon(icon: Resource): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes | 自定义图标资源信息，仅支持Resource类型的数据源。 &lt;br&gt;可支持的图片格式：png、jpg、jpeg、bmp、svg、webp、gif和heif等，支持的图片格式范围见[Image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md/arkts-multimedia-image.md)。当资源为非图片资源或不支持的格式时，图标显示为空白。&lt;br/&gt;从API版本26.0.0开始，支持Symbol格式的Resource类型的数据源。&lt;br/&gt;若应用不具备ohos.permission.CUS TOMIZE_SAVE_BUTTON权限，则自定义图标设置不生效，保存控件保持默认样式。 |

## setText

```TypeScript
setText(text: string | Resource)
```

设置保存控件的文本。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SaveButtonAttribute-setText(text: string | Resource): SaveButtonAttribute--><!--Device-SaveButtonAttribute-setText(text: string | Resource): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string \| Resource | Yes | 自定义文本信息。适用于需要使用与业务强相关的文本替代系统预置描述的场景。传入字符串时直接使用文本内容；传入Resource时，可配合资源管理实现多语言文本。 &lt;br&gt;若应用不具备ohos.permission.CUSTOMIZE_SAVE_BUTTON权限，则该设置不生效，保存控件保持默认样式。 |

## stateEffect

```TypeScript
stateEffect(enabled: boolean)
```

设置保存控件的按压效果。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SaveButtonAttribute-stateEffect(enabled: boolean): SaveButtonAttribute--><!--Device-SaveButtonAttribute-stateEffect(enabled: boolean): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | true表示保存控件按压时显示按压效果，false表示保存控件按压时不显示按压效果。 &lt;br&gt;默认值：true。&lt;br/&gt;若应用不具备ohos.permission.CUSTOMIZE_SAVE_BUTTON权限，按压效果设置不生效。 |

## symbolFontWeight

```TypeScript
symbolFontWeight(fontWeight: number | FontWeight | string | Resource)
```

设置保存控件Symbol图标粗细。

- 调用本方法前，需先调用[setIcon](SaveButtonAttribute#setIcon)设置Symbol格式的图标资源（如\$r('sys.symbol.xxx')），本方法才会生效。  
- 若未设置Symbol图标，该方法设置的粗细不会生效。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SaveButtonAttribute-symbolFontWeight(fontWeight: number | FontWeight | string | Resource): SaveButtonAttribute--><!--Device-SaveButtonAttribute-symbolFontWeight(fontWeight: number | FontWeight | string | Resource): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fontWeight | number \| FontWeight \| string \| Resource | Yes | 设置保存控件Symbol图标粗细。 &lt;br&gt;支持number类型：取值范围为[100, 900]，取值间隔为100，数值越大字体越粗。&lt;br/&gt;支持string类型：可传入number类型的数字字符串（如"400"），或[FontWeight](../arkts-apis/arkts-arkui-enums-fontweight-e.md/arkts-arkui-enums-fontweight-e.md)的枚举值的小写字符串（如"normal"）。&lt;br/&gt;默认值：FontWeight.Normal（对应数值400）。&lt;br/&gt;若应用不具备ohos.permission.CUSTOMIZE_SAVE_ BUTTON权限，则该设置不生效。 |

## symbolIconColor

```TypeScript
symbolIconColor(color: Array<ResourceColor>)
```

设置保存控件Symbol图标颜色。

- 调用本方法前，需先调用[setIcon](SaveButtonAttribute#setIcon)设置Symbol格式的图标资源（如\$r('sys.symbol.xxx')），本方法才会生效。  
- 若未设置Symbol图标，该方法设置的颜色不会生效。  
- 建议与[symbolRenderingStrategy](SaveButtonAttribute#symbolRenderingStrategy)配合使用，以实现不同的渲染效果。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SaveButtonAttribute-symbolIconColor(color: Array<ResourceColor>): SaveButtonAttribute--><!--Device-SaveButtonAttribute-symbolIconColor(color: Array<ResourceColor>): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Array&lt;ResourceColor&gt; | Yes | 设置保存控件Symbol图标颜色。适用于Symbol图标需要与业务视觉风格保持一致的场景。 &lt;br&gt;默认值：随[symbolRenderingStrategy](SaveButtonAttribute#symbolRenderingStrategy)不同而变化。 &lt;br&gt;若应用不具备ohos.permission.CUSTOMIZE_SAVE_BUTTON权限，则该设置不生效。 |

## symbolRenderingStrategy

```TypeScript
symbolRenderingStrategy(strategy: SymbolRenderingStrategy)
```

设置保存控件Symbol图标渲染策略。

- 调用本方法前，需先调用[setIcon](SaveButtonAttribute#setIcon)设置Symbol格式的图标资源（如\$r('sys.symbol.xxx')），本方法才会生效。  
- 若未设置Symbol图标，该方法设置的渲染策略不会生效。  
- 与[symbolIconColor](SaveButtonAttribute#symbolIconColor)配合使用时，渲染策略会影响颜色数组的作用方式。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SaveButtonAttribute-symbolRenderingStrategy(strategy: SymbolRenderingStrategy): SaveButtonAttribute--><!--Device-SaveButtonAttribute-symbolRenderingStrategy(strategy: SymbolRenderingStrategy): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| strategy | [SymbolRenderingStrategy](arkts-arkui-symbolrenderingstrategy-e.md) | Yes | 保存控件Symbol图标渲染策略，用于控制Symbol图标的渲染方式。 &lt;br&gt;默认值：SymbolRenderingStrategy.SINGLE。 &lt;br&gt;若应用不具备ohos.permission.CUSTOMIZE_SAVE_BUTTON权限，则该设置不生效。 |

## userCancelEvent

```TypeScript
userCancelEvent(enabled: boolean)
```

设置接收保存控件的用户取消授权事件。适用于需要区分用户主动取消授权和授权失败的场景，以便进行不同的业务处理，例如记录用户行为、提供重试提示等。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-SaveButtonAttribute-userCancelEvent(enabled: boolean): SaveButtonAttribute--><!--Device-SaveButtonAttribute-userCancelEvent(enabled: boolean): SaveButtonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | 表示是否接收保存控件的用户取消授权事件。 &lt;br&gt;true表示当用户在授权弹窗中主动取消时，会通过回调将结果区分为CANCELED_BY_USER；false表示不单独区分此类场景。&lt;br/&gt;当业务需要区分“用户取消”和“系统错误/授 权失败”时，建议开启该参数。 |

