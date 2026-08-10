# SelectionContainerAttribute

支持[通用属性](../../../reference/apis-arkui/arkui-ts/ts-component-general-attributes.md)。

> **说明：**
> 
> - 不支持[隐私遮罩](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-obscured.md)。
> 
> - 不支持[图形变换](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-transformation.md)，跨节点场景中Text子组件不支持图形变
> 换。

**Inheritance/Implementation:** SelectionContainerAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface SelectionContainerAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SelectionContainerAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SelectionContainerInstance, SelectionContainer, OnMenuItemClickWithTextCallback, SelectionContainerOptions, SelectionContainerAttribute, SelectionContainerEditMenuOptions, SelectionContainerTextJoinStyle, SelectionContainerController, SelectionContainerMenuOptions } from 'kits/@kit.ArkUI';
```

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SelectionContainerAttribute> | AttributeModifier<CommonMethod>
    | undefined): this
```

设置组件的动态属性。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default attributeModifier(modifier: AttributeModifier<SelectionContainerAttribute> | AttributeModifier<CommonMethod>    | undefined): this--><!--Device-SelectionContainerAttribute-default attributeModifier(modifier: AttributeModifier<SelectionContainerAttribute> | AttributeModifier<CommonMethod>    | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;SelectionContainerAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## bindSelectionMenu

```TypeScript
default bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined,
    responseType: TextResponseType | undefined, options?: SelectionContainerMenuOptions | undefined): this
```

设置自定义选择菜单。未通过该接口设置时，默认spanType为TextSpanType.TEXT，responseType为TextResponseType.LONG_PRESS。

> **说明：**
> 
> - bindSelectionMenu的长按响应时长为600ms，
> [bindContextMenu](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-menu.md#bindcontextmenu8)的长按响应时
> 长为800ms，当两者同时绑定且触发方式均为长按时，优先响应bindSelectionMenu。
> 
> - 自定义菜单过长时，建议内部嵌套使用[Scroll](../../../reference/apis-arkui/arkui-ts/ts-container-scroll.md)组件，避免键盘被遮挡。
> 
> - 选区跨越不可复制Text时，菜单仅基于实际选中的可复制文本进行显示和处理。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined,    responseType: TextResponseType | undefined, options?: SelectionContainerMenuOptions | undefined): this--><!--Device-SelectionContainerAttribute-default bindSelectionMenu(spanType: TextSpanType | undefined, content: CustomBuilder | undefined,    responseType: TextResponseType | undefined, options?: SelectionContainerMenuOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| spanType | [TextSpanType](../arkts-components/arkts-arkui-textspantype-e.md) \| undefined | Yes | 选择菜单类型。用于指定选择菜单作用的文本类型范围，不同类型对应不同的菜单行为。各枚举值的含义及适用场景详见 [TextSpanType](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#textspantype11枚举说明)。 |
| content | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| undefined | Yes | 选择菜单内容。 |
| responseType | [TextResponseType](../arkts-components/arkts-arkui-textresponsetype-e.md) \| undefined | Yes | 选择菜单响应类型。 |
| options | [SelectionContainerMenuOptions](arkts-arkui-arkui-components-selectioncontainer-selectioncontainermenuoptions-i.md) \| undefined | No | 选择菜单选项，用于配置菜单出现、消失、显示、隐藏等事件的回调。当需要监听这些菜单事件时传入此参数，不 传入时默认不监听菜单事件。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## caretColor

```TypeScript
default caretColor(color: ResourceColor | undefined): this
```

设置选中文本手柄颜色。未通过该接口设置时，默认手柄颜色为'#007DFF'（蓝色）。

> **说明：**
> 
> - 该属性在跨节点场景中用于各Text子组件选中文本手柄颜色。
> 
> - 在跨节点场景中Text子组件[caretColor](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#caretcolor14)设置无
> 效，始终使用SelectionContainer的配置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default caretColor(color: ResourceColor | undefined): this--><!--Device-SelectionContainerAttribute-default caretColor(color: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 手柄颜色。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## copyOption

```TypeScript
default copyOption(value: CopyOptions | undefined): this
```

设置组件的复制粘贴配置项。未通过该接口设置时，默认为CopyOptions.InApp。

> **说明：**
> 
> Text子组件已显式设置[copyOption](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#copyoption9)时，优先使用
> Text子组件的配置；未设置时，使用SelectionContainer的配置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default copyOption(value: CopyOptions | undefined): this--><!--Device-SelectionContainerAttribute-default copyOption(value: CopyOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CopyOptions](arkts-arkui-copyoptions-e.md) \| undefined | Yes | 复制粘贴配置项，用于设置文本的可复制范围。具体说明请参考CopyOptions枚举。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## editMenuOptions

```TypeScript
default editMenuOptions(editMenu: SelectionContainerEditMenuOptions | undefined): this
```

设置选中文本后的编辑菜单选项，包括菜单文本、图标和回调等。

> **说明：**
> 
> 当同时为当前场景设置了[bindSelectionMenu](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-i.md#bindselectionmenu)和editMenuOptions时，优先使用bindSelectionMenu，editMenuOptions不生
> 效。bindSelectionMenu用于完全自定义菜单风格和触发条件，由开发者定义所有菜单项；editMenuOptions用于在系统默认菜单基础上添加扩展项，触发条件不变。建议根据自定义程度需求选择。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default editMenuOptions(editMenu: SelectionContainerEditMenuOptions | undefined): this--><!--Device-SelectionContainerAttribute-default editMenuOptions(editMenu: SelectionContainerEditMenuOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| editMenu | [SelectionContainerEditMenuOptions](arkts-arkui-arkui-components-selectioncontainer-selectioncontainereditmenuoptions-i.md) \| undefined | Yes | 自定义编辑菜单配置。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(isEnabled: boolean | undefined): this
```

设置是否开启触控反馈。未通过该接口设置时，默认开启。

开启触控反馈时，需要在工程的[module.json5配置文件](../../../quick-start/module-configuration-file.md)中配置requestPermissions字段开启振动权限，配置如下：

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default enableHapticFeedback(isEnabled: boolean | undefined): this--><!--Device-SelectionContainerAttribute-default enableHapticFeedback(isEnabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes | 是否开启触控反馈。 &lt;br&gt;true表示开启触控反馈，false表示不开启触控反馈。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## onCopy

```TypeScript
default onCopy(callback: Callback<string> | undefined): this
```

长按文本内部区域弹出选择菜单后，点击选择菜单的复制按钮，触发该回调。仅支持复制文本。使用callback异步回调。

> **说明：**
> 
> - 回调参数为按Text组件视觉顺序拼接后的选中文本，拼接方式由[textJoinStyle](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-i.md#textjoinstyle)配置决定。
> 
> - 仅当容器级[onWillCopy](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-i.md#onwillcopy)返回true时，该回调才会触发。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default onCopy(callback: Callback<string> | undefined): this--><!--Device-SelectionContainerAttribute-default onCopy(callback: Callback<string> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string&gt; \| undefined | Yes | 复制回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## onTextSelectionChange

```TypeScript
default onTextSelectionChange(callback: Callback<Array<string>> | undefined): this
```

SelectionContainer中选中文本发生变化时触发该回调。使用callback异步回调。

> **说明：**
> 
> - 回调参数数组中各项顺序与Text组件视觉顺序一致。
> 
> - 数组中的每一项对应一个Text子组件的选中文本。
> 
> - 仅包含有选中文本的Text子组件，不包含未选中Text子组件，也不包含不可复制Text的空字符串占位。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default onTextSelectionChange(callback: Callback<Array<string>> | undefined): this--><!--Device-SelectionContainerAttribute-default onTextSelectionChange(callback: Callback<Array<string>> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;Array&lt;string&gt;&gt; \| undefined | Yes | 选中文本变化回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## onWillCopy

```TypeScript
default onWillCopy(callback: Callback<string, boolean> | undefined): this
```

在进行复制操作前，触发该回调。使用callback异步回调。

> **说明：**
> 
> - 回调参数为按Text组件视觉顺序拼接后的选中文本，拼接方式由[textJoinStyle](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-i.md#textjoinstyle)配置决定。
> 
> - 返回false时，会阻止本次跨节点复制及容器级[onCopy](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-i.md#oncopy)回调触发，但不会影响各Text子组件已独立处理完成的复制事件逻辑。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default onWillCopy(callback: Callback<string, boolean> | undefined): this--><!--Device-SelectionContainerAttribute-default onWillCopy(callback: Callback<string, boolean> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string, boolean&gt; \| undefined | Yes | 复制前检查回调，返回true表示允许复制，返回false表示不允许复制。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## selectedBackgroundColor

```TypeScript
default selectedBackgroundColor(color: ResourceColor | undefined): this
```

设置选中文本底板颜色。未通过该接口设置时，默认选中文本底板颜色为'#007DFF'（蓝色），如果未设置不透明度，默认为20%不透明度。

> **说明：**
> 
> - 该属性在跨节点场景中用于各Text子组件选中区域的高亮颜色。
> 
> - Text子组件已显式设置
> [selectedBackgroundColor](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#selectedbackgroundcolor14)
> 时，优先使用Text子组件的配置；未设置时，使用SelectionContainer的配置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default selectedBackgroundColor(color: ResourceColor | undefined): this--><!--Device-SelectionContainerAttribute-default selectedBackgroundColor(color: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 选中文本底板颜色。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## setSelectionContainerOptions

```TypeScript
default setSelectionContainerOptions(): this
```

设置SelectionContainer选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default setSelectionContainerOptions(): this--><!--Device-SelectionContainerAttribute-default setSelectionContainerOptions(): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

## textJoinStyle

```TypeScript
default textJoinStyle(style: SelectionContainerTextJoinStyle | undefined): this
```

设置SelectionContainer内聚合文本的拼接方式。未通过该接口设置时，默认为SelectionContainerTextJoinStyle.NEWLINE，表示不同文本节点之间使用换行符\n拼接。

> **说明：**
> 
> - 该配置会影响[onWillCopy](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-i.md#onwillcopy)、[onCopy](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-i.md#oncopy)、[bindSelectionMenu](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-i.md#bindselectionmenu)相关回调中返回
> 的文本内容。
> 
> - 该配置也会影响系统内置菜单项中依赖文本拼接结果的逻辑。例如，选择两个Text节点中的文本时，若配置为SelectionContainerTextJoinStyle.NEWLINE，执行复制后两段文本之间会插入换行符；若配置
> 为SelectionContainerTextJoinStyle.DIRECT，执行复制后两段文本会直接拼接。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionContainerAttribute-default textJoinStyle(style: SelectionContainerTextJoinStyle | undefined): this--><!--Device-SelectionContainerAttribute-default textJoinStyle(style: SelectionContainerTextJoinStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [SelectionContainerTextJoinStyle](arkts-arkui-arkui-components-selectioncontainer-selectioncontainertextjoinstyle-e.md) \| undefined | Yes | 聚合文本拼接方式。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | returns the instance of the SelectionContainerAttribute. |

