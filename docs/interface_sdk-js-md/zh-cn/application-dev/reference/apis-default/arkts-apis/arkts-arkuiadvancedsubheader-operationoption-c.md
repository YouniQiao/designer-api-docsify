# OperationOption

Declare type OperationOption

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class OperationOption--><!--Device-unnamed-export declare class OperationOption-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## accessibilityDescription

```TypeScript
public accessibilityDescription?: ResourceStr
```

子标题右侧按钮的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组 件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。

默认值：类型为LOADING时，默认值为“正在加载”，其他类型默认值为“单指双击即可执行”。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OperationOption-public accessibilityDescription?: ResourceStr--><!--Device-OperationOption-public accessibilityDescription?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
public accessibilityLevel?: string
```

子标题右侧按钮无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。

支持的值为：

"auto"：当前组件会转换"yes"。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"

**类型：** string

**默认值：** "auto"

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OperationOption-public accessibilityLevel?: string--><!--Device-OperationOption-public accessibilityLevel?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
public accessibilityText?: ResourceStr
```

子标题右侧按钮的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的 内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。

默认值：类型为TEXT_ARROW和BUTTON时默认值为当前项value属性内容，其他类型默认值为“ ”。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OperationOption-public accessibilityText?: ResourceStr--><!--Device-OperationOption-public accessibilityText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
public action?: () => void
```

子标题右侧按钮点击事件。

**类型：** () =&gt; void

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OperationOption-public action?: () => void--><!--Device-OperationOption-public action?: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
public defaultFocus?: boolean
```

子标题右侧按钮是否为默认焦点。

true：子标题右侧按钮是默认焦点。

false：子标题右侧按钮不是默认焦点。

默认值：false

**类型：** boolean

**默认值：** { false }

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OperationOption-public defaultFocus?: boolean--><!--Device-OperationOption-public defaultFocus?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
public id?: string
```

子标题右侧按钮id。需要为子标题右侧按钮设置id的时候设置此参数，缺省时不设置此参数。

默认值：undefined，表示不设置子标题右侧按钮id。

**类型：** string

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OperationOption-public id?: string--><!--Device-OperationOption-public id?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
public value: ResourceStr
```

操作区元素内容。当operationType为TEXT_ARROW或BUTTON时，value为文本内容；当operationType为ICON_GROUP时，value为图标资源。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OperationOption-public value: ResourceStr--><!--Device-OperationOption-public value: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

