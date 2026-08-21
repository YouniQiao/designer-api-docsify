# ButtonOptions

按钮的样式参数，用于设置弹出框按钮属性。

> **说明：**
> 
> buttonStyle和role优先级高于fontColor和background。当buttonStyle和role设置的是默认值时，fontColor和background生效。
> 
> 若同时给多个按钮设置defaultFocus，则默认焦点为设置defaultFocus按钮中显示顺序的第一个按钮。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare class ButtonOptions--><!--Device-unnamed-export declare class ButtonOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## action

```TypeScript
public action?: () => void
```

按钮的点击事件。

**类型：** () =&gt; void

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonOptions-public action?: () => void--><!--Device-ButtonOptions-public action?: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## background

```TypeScript
public background?: ResourceColor
```

按钮的背景色。

默认值跟随buttonStyle。

**类型：** ResourceColor

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonOptions-public background?: ResourceColor--><!--Device-ButtonOptions-public background?: ResourceColor-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## buttonStyle

```TypeScript
public buttonStyle?: ButtonStyleMode
```

按钮的样式。

默认值：2in1设备为ButtonStyleMode.NORMAL，其他设备为ButtonStyleMode.TEXTUAL。

**类型：** ButtonStyleMode

**默认值：** ButtonStyleMode.TEXTUAL

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonOptions-public buttonStyle?: ButtonStyleMode--><!--Device-ButtonOptions-public buttonStyle?: ButtonStyleMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
public defaultFocus?: boolean
```

按钮是否设置默认焦点。

true：按钮是默认焦点

false：按钮不是默认焦点

默认值：false

**类型：** boolean

**默认值：** { false }

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonOptions-public defaultFocus?: boolean--><!--Device-ButtonOptions-public defaultFocus?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
public fontColor?: ResourceColor
```

按钮的字体颜色。

默认值跟随buttonStyle。

**类型：** ResourceColor

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonOptions-public fontColor?: ResourceColor--><!--Device-ButtonOptions-public fontColor?: ResourceColor-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## role

```TypeScript
public role?: ButtonRole
```

按钮的角色。

默认值：ButtonRole.NORMAL

**类型：** ButtonRole

**默认值：** ButtonRole.NORMAL

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonOptions-public role?: ButtonRole--><!--Device-ButtonOptions-public role?: ButtonRole-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
public textAlign?: TextAlign
```

按钮文本的对齐方式。

默认值：TextAlign.Start

**类型：** TextAlign

**默认值：** { TextAlign.Start }

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonOptions-public textAlign?: TextAlign--><!--Device-ButtonOptions-public textAlign?: TextAlign-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
public value: ResourceStr
```

按钮的内容。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonOptions-public value: ResourceStr--><!--Device-ButtonOptions-public value: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

