# TextEditControllerEx

文本扩展编辑控制器。 继承自[TextBaseController](arkts-arkui-textbasecontroller-i.md#TextBaseController)。

**继承/实现关系：** TextEditControllerEx extends [TextBaseController](arkts-arkui-textbasecontroller-i.md#TextBaseController)

**起始版本：** 12

**废弃版本：** -1

<!--Device-unnamed-declare interface TextEditControllerEx--><!--Device-unnamed-declare interface TextEditControllerEx-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getCaretOffset

```TypeScript
getCaretOffset(): number
```

返回当前光标所在位置。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TextEditControllerEx-getCaretOffset(): number--><!--Device-TextEditControllerEx-getCaretOffset(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getPreviewText

```TypeScript
getPreviewText?(): PreviewText
```

获取预上屏信息。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TextEditControllerEx-getPreviewText?(): PreviewText--><!--Device-TextEditControllerEx-getPreviewText?(): PreviewText-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [PreviewText](arkts-arkui-previewtext-i.md) |

## isEditing

```TypeScript
isEditing(): boolean
```

获取当前富文本的编辑状态。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TextEditControllerEx-isEditing(): boolean--><!--Device-TextEditControllerEx-isEditing(): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## setCaretOffset

```TypeScript
setCaretOffset(offset: number): boolean
```

设置光标偏移位置。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TextEditControllerEx-setCaretOffset(offset: number): boolean--><!--Device-TextEditControllerEx-setCaretOffset(offset: number): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## stopEditing

```TypeScript
stopEditing(): void
```

退出编辑态。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TextEditControllerEx-stopEditing(): void--><!--Device-TextEditControllerEx-stopEditing(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
