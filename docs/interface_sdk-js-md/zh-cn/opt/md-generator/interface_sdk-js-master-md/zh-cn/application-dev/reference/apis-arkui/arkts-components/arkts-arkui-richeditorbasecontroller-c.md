# RichEditorBaseController

RichEditor组件控制器基类。

**继承/实现关系：** RichEditorBaseController implements [TextEditControllerEx](../arkts-apis/arkts-arkui-texteditcontrollerex-i.md#TextEditControllerEx)

**起始版本：** 12

**废弃版本：** -1

<!--Device-unnamed-declare class RichEditorBaseController--><!--Device-unnamed-declare class RichEditorBaseController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## closeSelectionMenu

```TypeScript
closeSelectionMenu(): void
```

关闭自定义选择菜单或系统默认选择菜单。 当controller未绑定组件或绑定controller的组件被释放时，该接口调用无效。

**起始版本：** 10

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-closeSelectionMenu(): void--><!--Device-RichEditorBaseController-closeSelectionMenu(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## deleteBackward

```TypeScript
deleteBackward(): void
```

删除光标前字符或选中内容。没有内容被选中时，删除当前光标位置前的1个字符；有内容被选中时，删除选中内容。 该接口不支持预上屏场景使用。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-deleteBackward(): void--><!--Device-RichEditorBaseController-deleteBackward(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getCaretOffset

```TypeScript
getCaretOffset(): number
```

返回当前光标所在位置。 当无法获取光标位置时（例如controller未与组件绑定时），该接口返回-1。

**起始版本：** 10

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-getCaretOffset(): number--><!--Device-RichEditorBaseController-getCaretOffset(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getCaretRect

```TypeScript
getCaretRect(): RectResult | undefined
```

返回当前光标与RichEditor组件的相对位置。如果光标不闪烁或controller未绑定组件，返回undefined。

**起始版本：** 18

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-getCaretRect(): RectResult | undefined--><!--Device-RichEditorBaseController-getCaretRect(): RectResult | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [RectResult](arkts-arkui-rectresult-i.md) |

## getLayoutManager

```TypeScript
getLayoutManager(): LayoutManager
```

获取布局管理器对象。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-getLayoutManager(): LayoutManager--><!--Device-RichEditorBaseController-getLayoutManager(): LayoutManager-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [LayoutManager](../arkts-apis/arkts-arkui-layoutmanager-i.md) |

## getPreviewText

```TypeScript
getPreviewText(): PreviewText
```

获取预上屏信息。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-getPreviewText(): PreviewText--><!--Device-RichEditorBaseController-getPreviewText(): PreviewText-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [PreviewText](../arkts-apis/arkts-arkui-previewtext-i.md) |

## getTypingStyle

```TypeScript
getTypingStyle(): RichEditorTextStyle
```

获取用户预设的文本样式。

**起始版本：** 11

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-getTypingStyle(): RichEditorTextStyle--><!--Device-RichEditorBaseController-getTypingStyle(): RichEditorTextStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [RichEditorTextStyle](arkts-arkui-richeditortextstyle-i.md) |

## isEditing

```TypeScript
isEditing(): boolean
```

获取当前富文本的编辑状态。当controller未绑定组件或绑定controller的组件被释放时，返回false。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-isEditing(): boolean--><!--Device-RichEditorBaseController-isEditing(): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## scrollToVisible

```TypeScript
scrollToVisible(range?: TextRange): void
```

将指定范围内的内容滚动到可视区域。

**起始版本：** 26.0.0

**废弃版本：** -1

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-scrollToVisible(range?: TextRange): void--><!--Device-RichEditorBaseController-scrollToVisible(range?: TextRange): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [TextRange](../arkts-apis/arkts-arkui-textrange-i.md) | 否 |

## setCaretOffset

```TypeScript
setCaretOffset(offset: number): boolean
```

设置光标位置。 当controller未绑定组件或绑定controller的组件被释放时，该接口返回false，设置不成功。

**起始版本：** 10

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-setCaretOffset(offset: number): boolean--><!--Device-RichEditorBaseController-setCaretOffset(offset: number): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setSelection

```TypeScript
setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

设置组件内的内容选中，选中部分背板高亮。 selectionStart和selectionEnd均为-1时表示全选，均为0时可以清空选中区。 未获焦时调用该接口不产生选中效果。 从API version 12开始，在PC/2in1设备（可通过deviceInfo.deviceType获取设备类型进行判断）中，无论options取何值，调用setSelection接口都不会弹出菜单；如果组件中已经存在菜单， 调用setSelection接口会关闭菜单。在非PC/2in1设备中，options取值为MenuPolicy.DEFAULT时，遵循以下规则： 1. 组件内有手柄菜单时，接口调用后不关闭菜单，并且调整菜单位置。 2. 组件内有不带手柄的菜单时，接口调用后不关闭菜单，并且菜单位置不变。 3. 组件内无菜单时，接口调用后也无菜单显示。

**起始版本：** 11

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void--><!--Device-RichEditorBaseController-setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| selectionStart | number | 是 |
| selectionEnd | number | 是 |
| options | [SelectionOptions](arkts-arkui-selectionoptions-i.md) | 否 |

## setStyledPlaceholder

```TypeScript
setStyledPlaceholder(styledString: StyledString): void
```

设置无输入时的属性字符串样式的提示文本。

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-setStyledPlaceholder(styledString: StyledString): void--><!--Device-RichEditorBaseController-setStyledPlaceholder(styledString: StyledString): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| styledString | [StyledString](../arkts-apis/arkts-arkui-styledstring-c.md) | 是 |

## setTypingParagraphStyle

```TypeScript
setTypingParagraphStyle(style: RichEditorParagraphStyle): void
```

设置用户预设的段落样式。仅在组件内容为空或组件末尾换行后，输入文本生效。当controller未绑定组件或绑定controller的组件被释放时，该接口调用无效。

**起始版本：** 20

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-setTypingParagraphStyle(style: RichEditorParagraphStyle): void--><!--Device-RichEditorBaseController-setTypingParagraphStyle(style: RichEditorParagraphStyle): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [RichEditorParagraphStyle](arkts-arkui-richeditorparagraphstyle-i.md) | 是 |

## setTypingStyle

```TypeScript
setTypingStyle(value: RichEditorTextStyle): void
```

设置用户预设的文本样式。 当controller未绑定组件或绑定controller的组件被释放时，该接口调用无效。

**起始版本：** 11

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-setTypingStyle(value: RichEditorTextStyle): void--><!--Device-RichEditorBaseController-setTypingStyle(value: RichEditorTextStyle): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RichEditorTextStyle](arkts-arkui-richeditortextstyle-i.md) | 是 |

## stopEditing

```TypeScript
stopEditing(): void
```

退出编辑态。 当controller未绑定组件或绑定controller的组件被释放时，该接口调用无效。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RichEditorBaseController-stopEditing(): void--><!--Device-RichEditorBaseController-stopEditing(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
