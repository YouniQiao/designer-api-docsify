# IconItemOptions

定义了尾部builder接口，针对背板大小及颜色设置限制。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface IconItemOptions--><!--Device-unnamed-export interface IconItemOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## accessibilityDescription

```TypeScript
accessibilityDescription?: ResourceStr
```

后缀图标的无障碍描述。此描述用于向用户详细解释后缀图标，开发人员应为后缀图标的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从后缀图标的属性和无障碍文本中直接获知时。如果后缀 图标同时具备文本属性和无障碍说明属性，当后缀图标被选中时，系统将首先播报后缀图标的文本属性，随后播报无障碍说明属性的内容。

默认值：空字符串。

值为undefined时，按默认值处理。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IconItemOptions-accessibilityDescription?: ResourceStr--><!--Device-IconItemOptions-accessibilityDescription?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
accessibilityLevel?: string
```

尾部图标无障碍重要性。用于控制尾部图标是否可被无障碍辅助服务所识别。

支持的值为:

"auto"：尾部图标转化为“yes”。

"yes"：尾部图标可被无障碍辅助服务所识别。

"no"：尾部图标不可被无障碍辅助服务所识别。

"no-hide-descendants"：尾部图标及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"

值为undefined时，按默认值处理。

**类型：** string

**默认值：** "auto"

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IconItemOptions-accessibilityLevel?: string--><!--Device-IconItemOptions-accessibilityLevel?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
accessibilityText?: ResourceStr
```

后缀图标的无障碍文本属性。用于为用户进一步说明后缀图标，开发人员可为后缀图标的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从后缀图标本身属性与无障碍 文本中了解到时。若后缀图标既拥有文本属性又拥有无障碍说明属性，则后缀图标被选中时，先播报后缀图标的文本属性，再播报无障碍说明属性的内容。

默认值：空字符串。

值为undefined时，按默认值处理。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IconItemOptions-accessibilityText?: ResourceStr--><!--Device-IconItemOptions-accessibilityText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action: VoidCallback
```

自定义Builder items的回调，尾部图标被点击时触发。

为undefined时，表示解绑事件。

**类型：** VoidCallback

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IconItemOptions-action: VoidCallback--><!--Device-IconItemOptions-action: VoidCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon: IconOptions
```

自定义Builder icon。

Chip大小是ChipSize.SMALL时，suffix默认值：{width: 16,height: 16}。

Chip大小是ChipSize.NORMAL时，suffix默认值：{width: 24,height: 24}。&lt;/br&gt; 如果想动态修改size，那么必须在引入 [IconGroupSuffix](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipgroup-icongroupsuffix-s.md)时，使用 SymbolGlyphModifier 类型。

值为undefined时，按默认值处理。

**类型：** [IconOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-chipgroup-iconoptions-i.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IconItemOptions-icon: IconOptions--><!--Device-IconItemOptions-icon: IconOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

