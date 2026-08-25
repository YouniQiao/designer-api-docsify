# RichEditor

## RichEditor

```TypeScript
export declare function RichEditor(
    options: RichEditorOptions | RichEditorStyledStringOptions, 
): RichEditorAttribute
```

创建富文本组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RichEditorOptions](arkts-arkui-richeditor-richeditoroptions-i.md) \| [RichEditorStyledStringOptions](arkts-arkui-richeditor-richeditorstyledstringoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |


## RichEditor

```TypeScript
export declare function RichEditor(
    style: CustomBuilderT<RichEditorAttribute>,
): RichEditorAttribute
```

创建富文本组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RichEditorAttribute](arkts-arkui-richeditor-richeditorattribute-i.md) |
