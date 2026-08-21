# SegmentButtonIconItem

图标按钮信息。

> **说明：**
> 
> 未选中态的图标`icon`和选中态的图标`selectedIcon`都需设置，单独设置无效。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-interface SegmentButtonIconItem--><!--Device-unnamed-interface SegmentButtonIconItem-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## accessibilityDescription

```TypeScript
accessibilityDescription?: ResourceStr
```

无障碍说明，为用户解释组件操作，设置详细解释文本，帮助用户理解操作后果。若组件有文本和无障碍说明，选中时先播报文本，再播报无障碍说明。

默认值：空字符串。

值为undefined时，按默认值处理。

**类型：** ResourceStr

**默认值：** ""

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonIconItem-accessibilityDescription?: ResourceStr--><!--Device-SegmentButtonIconItem-accessibilityDescription?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
accessibilityLevel?: string
```

无障碍重要性，用于控制当前组件是否可被无障碍辅助服务所识别。

支持的值为:

"auto"：当前组件可被无障碍辅助服务所识别。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

值为undefined时，按默认值处理。

**类型：** string

**默认值：** "auto"

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonIconItem-accessibilityLevel?: string--><!--Device-SegmentButtonIconItem-accessibilityLevel?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon: ResourceStr
```

未选中态的按钮图标。

值为undefined时，不显示图标。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonIconItem-icon: ResourceStr--><!--Device-SegmentButtonIconItem-icon: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## iconAccessibilityText

```TypeScript
iconAccessibilityText?: ResourceStr
```

未选中态按钮图标的无障碍文本。默认值为空字符串。

值为undefined时，按默认值处理。

**类型：** ResourceStr

**默认值：** ""

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonIconItem-iconAccessibilityText?: ResourceStr--><!--Device-SegmentButtonIconItem-iconAccessibilityText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## selectedIcon

```TypeScript
selectedIcon: ResourceStr
```

选中态的按钮图标。

值为undefined时，不显示图标。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonIconItem-selectedIcon: ResourceStr--><!--Device-SegmentButtonIconItem-selectedIcon: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## selectedIconAccessibilityText

```TypeScript
selectedIconAccessibilityText?: ResourceStr
```

选中态按钮图标的无障碍文本。默认值为空字符串。

值为undefined时，按默认值处理。

**类型：** ResourceStr

**默认值：** ""

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButtonIconItem-selectedIconAccessibilityText?: ResourceStr--><!--Device-SegmentButtonIconItem-selectedIconAccessibilityText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

