# ButtonOptions

按钮的样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ButtonOptions--><!--Device-unnamed-export declare interface ButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonStyle

```TypeScript
buttonStyle?: ButtonStyleMode
```

按钮的样式和重要程度，根据设置枚举值的不同，系统自动会调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过  
[backgroundColor](arkts-arkui-common-commonmethod-i.md#backgroundcolor)、[fontColor](fontColor)和  
[role](arkts-arkui-button-buttonoptions-i.md#role)接口设置，实际显示效果以最后一次设置为准。

默认值：ButtonStyleMode.EMPHASIZED 

**说明：**

按钮重要程度：强调按钮>普通按钮>文字按钮。

**卡片能力（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 12开始，该接口支持在原子化服务中使用。

**Type:** [ButtonStyleMode](arkts-arkui-button-buttonstylemode-e.md)

**Default:** ButtonStyleMode.EMPHASIZED

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonOptions-buttonStyle?: ButtonStyleMode--><!--Device-ButtonOptions-buttonStyle?: ButtonStyleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controlSize

```TypeScript
controlSize?: ControlSize
```

按钮的尺寸。

默认值：ControlSize.NORMAL

**卡片能力（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 12开始，该接口支持在原子化服务中使用。

**Type:** [ControlSize](arkts-arkui-button-controlsize-e.md)

**Default:** ControlSize.NORMAL

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonOptions-controlSize?: ControlSize--><!--Device-ButtonOptions-controlSize?: ControlSize-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## role

```TypeScript
role?: ButtonRole
```

按钮的角色，根据设置枚举值的不同，系统自动会调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过  
[backgroundColor](arkts-arkui-common-commonmethod-i.md#backgroundcolor)、[fontColor](fontColor)和  
[buttonStyle](arkts-arkui-button-buttonoptions-i.md#buttonstyle)接口设置，实际显示效果以最后一次设置为准。

默认值：ButtonRole.NORMAL 

**卡片能力（仅ArkTS-Dyn）：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 12开始，该接口支持在原子化服务中使用。

**Type:** [ButtonRole](../arkts-components/arkts-arkui-buttonrole-e.md)

**Default:** ButtonRole.NORMAL

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonOptions-role?: ButtonRole--><!--Device-ButtonOptions-role?: ButtonRole-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stateEffect

```TypeScript
stateEffect?: boolean
```

按钮按下时是否开启按压态显示效果。

true：开启按压效果；false：关闭按压效果。

默认值：true

**说明：**

当开启按压态显示效果，且开发者设置状态样式时，会基于状态样式设置完成后的背景色再进行颜色叠加。

**卡片能力（仅ArkTS-Dyn）：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonOptions-stateEffect?: boolean--><!--Device-ButtonOptions-stateEffect?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: ButtonType
```

按钮显示样式。

默认值：ButtonType.ROUNDED_RECTANGLE

从API version 18及之后，ButtonType的默认值修改为ButtonType.ROUNDED_RECTANGLE。API version 18之前的版本，ButtonType的默认值为ButtonType.Capsule。

**卡片能力（仅ArkTS-Dyn）：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**Type:** [ButtonType](arkts-arkui-button-buttontype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonOptions-type?: ButtonType--><!--Device-ButtonOptions-type?: ButtonType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

