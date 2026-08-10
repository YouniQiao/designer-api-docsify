# SearchParams

AtomicServiceSearch中“搜索区”的可选属性。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-export interface SearchParams--><!--Device-unnamed-export interface SearchParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SearchParams, AtomicServiceSearch, SearchButtonParams, OperationParams, SelectParams, InputFilterParams, MenuAlignParams } from 'kits/@kit.ArkUI';
```

## onChange

```TypeScript
onChange?: EditableTextOnChangeCallback
```

输入内容发生变化时，触发该回调。默认值为`undefined`。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-onChange?: EditableTextOnChangeCallback--><!--Device-SearchParams-onChange?: EditableTextOnChangeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onContentScroll

```TypeScript
onContentScroll?: OnContentScrollCallback
```

文本内容滚动时，触发该回调。默认值为`undefined`。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-onContentScroll?: OnContentScrollCallback--><!--Device-SearchParams-onContentScroll?: OnContentScrollCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPaste

```TypeScript
onPaste?: OnPasteCallback
```

进行粘贴操作时，触发该回调。默认值为`undefined`。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-onPaste?: OnPasteCallback--><!--Device-SearchParams-onPaste?: OnPasteCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTextSelectionChange

```TypeScript
onTextSelectionChange?: OnTextSelectionChangeCallback
```

文本选择的位置发生变化或编辑状态下光标位置发生变化时，触发该回调。默认值为`undefined`。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-onTextSelectionChange?: OnTextSelectionChangeCallback--><!--Device-SearchParams-onTextSelectionChange?: OnTextSelectionChangeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancelIcon

```TypeScript
cancelIcon?: IconOptions
```

右侧清除按钮样式。默认值：`{style: CancelButtonStyle.INPUT, icon: {size: '16vp', color: '#99ffffff', src: ' '}}`。

当style为CancelButtonStyle.CONSTANT时，默认显示清除样式。

**Type:** [IconOptions](../arkts-components/arkts-arkui-iconoptions-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-cancelIcon?: IconOptions--><!--Device-SearchParams-cancelIcon?: IconOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## caretStyle

```TypeScript
caretStyle?: CaretStyle
```

光标样式。默认值：`{width: '1.5vp', color: '#007DFF'}`。

**Type:** [CaretStyle](arkts-arkui-caretstyle-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-caretStyle?: CaretStyle--><!--Device-SearchParams-caretStyle?: CaretStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## componentBackgroundColor

```TypeScript
componentBackgroundColor?: ResourceColor
```

设置组件的背景色。默认值：`\$r('sys.color.ohos_id_color_text_field_sub_bg')`。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-componentBackgroundColor?: ResourceColor--><!--Device-SearchParams-componentBackgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## copyOptions

```TypeScript
copyOptions?: CopyOptions
```

输入的文本是否可复制。默认值：`CopyOptions.LocalDevice`，支持设备内复制。

**Type:** [CopyOptions](arkts-arkui-copyoptions-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-copyOptions?: CopyOptions--><!--Device-SearchParams-copyOptions?: CopyOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## decoration

```TypeScript
decoration?: TextDecorationOptions
```

文本装饰线对象。默认值：`{type: TextDecorationType.None, color: Color.Black, style: TextDecorationStyle.SOLID}`。

**Type:** [TextDecorationOptions](arkts-arkui-common-textdecorationoptions-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-decoration?: TextDecorationOptions--><!--Device-SearchParams-decoration?: TextDecorationOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## editMenuOptions

```TypeScript
editMenuOptions?: EditMenuOptions
```

设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。默认值为`undefined`。

**Type:** [EditMenuOptions](arkts-arkui-editmenuoptions-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-editMenuOptions?: EditMenuOptions--><!--Device-SearchParams-editMenuOptions?: EditMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableHapticFeedback

```TypeScript
enableHapticFeedback?: boolean
```

是否开启触控反馈。true表示开启触控反馈。false表示不开启触控反馈。默认值：`true`。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-enableHapticFeedback?: boolean--><!--Device-SearchParams-enableHapticFeedback?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableKeyboardOnFocus

```TypeScript
enableKeyboardOnFocus?: boolean
```

Search获焦时，是否主动拉起软键盘。true表示Search获焦时主动拉起软键盘。false表示Search获焦时不主动拉起键盘。默认值：`true`。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-enableKeyboardOnFocus?: boolean--><!--Device-SearchParams-enableKeyboardOnFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enablePreviewText

```TypeScript
enablePreviewText?: boolean
```

是否开启输入预上屏。true表示开启输入预上屏。false表示不开启输入预上屏。默认值：`true`。 

需要配合开启输入法的预上屏功能。预上屏内容定义为文字暂存态，目前不支持文字拦截功能，因此该值为true时不触发onWillInsert、onDidInsert回调。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-enablePreviewText?: boolean--><!--Device-SearchParams-enablePreviewText?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enterKeyType

```TypeScript
enterKeyType?: EnterKeyType
```

输入法回车键类型。默认值：`EnterKeyType.Search`。

**Type:** [EnterKeyType](arkts-arkui-textinput-enterkeytype-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-enterKeyType?: EnterKeyType--><!--Device-SearchParams-enterKeyType?: EnterKeyType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

输入文本的字体颜色。默认值：`\$r('sys.color.ohos_id_color_text_secondary')`。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-fontColor?: ResourceColor--><!--Device-SearchParams-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontFeature

```TypeScript
fontFeature?: ResourceStr
```

设置文字特性效果，比如数字等宽的特性。

格式为：normal | &lt;feature-tag-value&gt;

&lt;feature-tag-value&gt;的格式为：&lt;string&gt; [ &lt;integer&gt; | on | off ]

&lt;feature-tag-value&gt;的个数可以有多个，中间用','隔开。

例如，使用等宽数字的输入格式为："ss01" on。默认值为`undefined`。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-fontFeature?: ResourceStr--><!--Device-SearchParams-fontFeature?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hideSelectionMenu

```TypeScript
hideSelectionMenu?: boolean
```

是否隐藏系统文本选择菜单。

设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，不弹出系统文本选择菜单。设置为false时，弹出系统文本选择菜单。默认值：`false`。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-hideSelectionMenu?: boolean--><!--Device-SearchParams-hideSelectionMenu?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## inputFilter

```TypeScript
inputFilter?: InputFilterParams
```

通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。仅支持单个字符匹配，不支持字符串匹配。默认值为`undefined`。

-value: 正则表达式。 

-error: 正则匹配失败时，返回被过滤的内容。

**Type:** [InputFilterParams](arkts-arkui-atomicservice-atomicservicesearch-inputfilterparams-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-inputFilter?: InputFilterParams--><!--Device-SearchParams-inputFilter?: InputFilterParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## letterSpacing

```TypeScript
letterSpacing?: number | string | Resource
```

设置文本字符间距。正数拉开字符距离，负数则拉近字符距离。浮点数默认值为0.0，单位为物理像素px。若输入类型非number且无法解析为数字，则使用默认值。

**Type:** number \| string \| Resource

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-letterSpacing?: number | string | Resource--><!--Device-SearchParams-letterSpacing?: number | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxFontSize

```TypeScript
maxFontSize?: number | string | Resource
```

设置文本最大显示字号。需要配合minFontSize以及布局大小限制使用，单独设置不生效。默认值为`undefined`。取值为number类型时，单位：fp。

**Type:** number \| string \| Resource

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-maxFontSize?: number | string | Resource--><!--Device-SearchParams-maxFontSize?: number | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxLength

```TypeScript
maxLength?: number
```

设置文本的最大输入字符数。默认不设置最大输入字符数限制。到达文本最大字符限制，将无法继续输入字符。默认值：`-1`。

**Type:** number

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-maxLength?: number--><!--Device-SearchParams-maxLength?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minFontSize

```TypeScript
minFontSize?: number | string | Resource
```

设置文本最小显示字号。需要配合maxFontSize以及布局大小限制使用，单独设置不生效。默认值为`undefined`。取值为number类型时，单位：fp。

**Type:** number \| string \| Resource

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-minFontSize?: number | string | Resource--><!--Device-SearchParams-minFontSize?: number | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCopy

```TypeScript
onCopy?: Callback<string>
```

进行复制操作时，触发该回调，string为被复制的文本内容。默认值为`undefined`。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-onCopy?: Callback<string>--><!--Device-SearchParams-onCopy?: Callback<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCut

```TypeScript
onCut?: Callback<string>
```

进行剪切操作时，触发该回调，string为被剪切的文本内容。默认值为`undefined`。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-onCut?: Callback<string>--><!--Device-SearchParams-onCut?: Callback<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidDelete

```TypeScript
onDidDelete?: Callback<DeleteValue>
```

在删除完成时触发该回调，在onWillDelete之后触发。当onWillDelete返回false拦截删除操作时，该回调不触发。默认值为`undefined`。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;DeleteValue&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-onDidDelete?: Callback<DeleteValue>--><!--Device-SearchParams-onDidDelete?: Callback<DeleteValue>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDidInsert

```TypeScript
onDidInsert?: Callback<InsertValue>
```

在输入完成时触发该回调，在onWillInsert之后触发。当onWillInsert返回false拦截插入操作时，该回调不触发。默认值为`undefined`。当enablePreviewText为true时，不触发本回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;InsertValue&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-onDidInsert?: Callback<InsertValue>--><!--Device-SearchParams-onDidInsert?: Callback<InsertValue>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onEditChange

```TypeScript
onEditChange?: Callback<boolean>
```

输入状态变化时，触发该回调。有光标时为编辑态，无光标时为非编辑态。isEditing为true表示正在输入。默认值为`undefined`。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-onEditChange?: Callback<boolean>--><!--Device-SearchParams-onEditChange?: Callback<boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onSubmit

```TypeScript
onSubmit?: Callback<string> | SearchSubmitCallback
```

点击搜索图标、搜索按钮或者按下软键盘搜索按钮时触发该回调。string为当前搜索框中输入的文本内容。默认值为`undefined`。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; \| SearchSubmitCallback

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-onSubmit?: Callback<string> | SearchSubmitCallback--><!--Device-SearchParams-onSubmit?: Callback<string> | SearchSubmitCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDelete

```TypeScript
onWillDelete?: Callback<DeleteValue, boolean>
```

在将要删除时，触发该回调。true表示正常删除，false表示不删除。默认值为`undefined`。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;DeleteValue, boolean&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-onWillDelete?: Callback<DeleteValue, boolean>--><!--Device-SearchParams-onWillDelete?: Callback<DeleteValue, boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillInsert

```TypeScript
onWillInsert?: Callback<InsertValue, boolean>
```

在将要输入时，触发该回调。true表示将输入内容正常插入结果字符串，false表示不插入。默认值为`undefined`。当enablePreviewText为true时，不触发本回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;InsertValue, boolean&gt;

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-onWillInsert?: Callback<InsertValue, boolean>--><!--Device-SearchParams-onWillInsert?: Callback<InsertValue, boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placeholderColor

```TypeScript
placeholderColor?: ResourceColor
```

placeholder文本颜色。默认值：`\$r('sys.color.ohos_id_color_text_secondary')`。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-placeholderColor?: ResourceColor--><!--Device-SearchParams-placeholderColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placeholderFont

```TypeScript
placeholderFont?: Font
```

设置placeholder文本样式，包括字体大小、字体粗细、字体族、字体风格。目前仅支持默认字体族。默认值：`{size: \$r('sys.float.ohos_id_text_size_body1')}`。

**Type:** [Font](arkts-arkui-arkui-uicontext-font-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-placeholderFont?: Font--><!--Device-SearchParams-placeholderFont?: Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pressedBackgroundColor

```TypeScript
pressedBackgroundColor?: ResourceColor
```

设置组件按压态的背景色。默认值：`\$r('sys.color.ohos_id_color_click_effect')`。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-pressedBackgroundColor?: ResourceColor--><!--Device-SearchParams-pressedBackgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## searchButton

```TypeScript
searchButton?: SearchButtonParams
```

设置搜索框末尾搜索按钮。点击搜索按钮，触发onSubmit回调。默认值为`undefined`

-searchButtonValue: 搜索框末尾搜索按钮文本内容。

-options: 配置搜索框文本样式。默认值：`{fontSize: '16fp', fontColor: '#ff3f97e9'}`。

**Type:** [SearchButtonParams](arkts-arkui-atomicservice-atomicservicesearch-searchbuttonparams-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-searchButton?: SearchButtonParams--><!--Device-SearchParams-searchButton?: SearchButtonParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## searchIcon

```TypeScript
searchIcon?: IconOptions | SymbolGlyphModifier
```

左侧搜索图标样式。

浅色模式默认值：`{size: '16vp', color: '#99182431', src: ' '}`。

深色模式默认值：`{size: '16vp', color: '#99ffffff', src: ' '}`。

**Type:** [IconOptions](../arkts-components/arkts-arkui-iconoptions-i.md) \| SymbolGlyphModifier

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-searchIcon?: IconOptions | SymbolGlyphModifier--><!--Device-SearchParams-searchIcon?: IconOptions | SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## searchKey

```TypeScript
searchKey?: ResourceStr
```

用作标识内部search组件的唯一键值，便于外部通过该键值引用或查找对应的Search组件。默认值：`undefined`。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-searchKey?: ResourceStr--><!--Device-SearchParams-searchKey?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor?: ResourceColor
```

文本选中底板颜色。默认值：系统默认底板颜色，20%不透明度。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-selectedBackgroundColor?: ResourceColor--><!--Device-SearchParams-selectedBackgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
textAlign?: TextAlign
```

文本在搜索框中的对齐方式。默认值：`TextAlign.Start`。

**Type:** [TextAlign](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-textalign-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-textAlign?: TextAlign--><!--Device-SearchParams-textAlign?: TextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textFont

```TypeScript
textFont?: Font
```

设置搜索框内输入文本样式，包括字体大小、字体粗细、字体族、字体风格。目前仅支持默认字体族。默认值：`{size: \$r('sys.float.ohos_id_text_size_body1')}`。

**Type:** [Font](arkts-arkui-arkui-uicontext-font-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-textFont?: Font--><!--Device-SearchParams-textFont?: Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textIndent

```TypeScript
textIndent?: Dimension
```

首行文本缩进。默认值：`0`。单位：vp。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-textIndent?: Dimension--><!--Device-SearchParams-textIndent?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: SearchType
```

输入框类型。默认值：`SearchType.Normal`。

**Type:** [SearchType](arkts-arkui-search-searchtype-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchParams-type?: SearchType--><!--Device-SearchParams-type?: SearchType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

