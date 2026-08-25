# TextEditControllerEx

文本扩展编辑控制器。继承自[TextBaseController](arkts-arkui-textcommon-textbasecontroller-i.md)。

**继承/实现关系：** TextEditControllerEx extends [TextBaseController](arkts-arkui-textcommon-textbasecontroller-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getCaretOffset

```TypeScript
getCaretOffset(): int | undefined
```

返回当前光标所在位置。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 |
| --- |
| int \| undefined |

## getPreviewText

```TypeScript
getPreviewText(): PreviewText | undefined
```

获取预上屏信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [PreviewText](arkts-arkui-textcommon-previewtext-i.md) \| undefined |

## isEditing

```TypeScript
isEditing(): boolean | undefined
```

获取当前富文本的编辑状态。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean \| undefined |

## setCaretOffset

```TypeScript
setCaretOffset(offset: int): boolean | undefined
```

设置光标偏移位置。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | int | 是 |

**返回值：**

| 类型 |
| --- |
| boolean \| undefined |

## stopEditing

```TypeScript
stopEditing(): void
```

退出编辑态。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
