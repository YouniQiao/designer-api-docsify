# ButtonOptions

按钮的样式。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare interface ButtonOptions--><!--Device-unnamed-declare interface ButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonStyle

```TypeScript
buttonStyle?: ButtonStyleMode
```

按钮的样式和重要程度。根据设置枚举值的不同，系统自动调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过  
[backgroundColor](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#backgroundcolor)、  
[fontColor](ButtonAttribute#fontColor)和[role](ButtonAttribute#role)接口设置，实际显示效果以最后一次设置为准。

默认值：ButtonStyleMode.EMPHASIZED 

**说明：**

按钮重要程度：强调按钮>普通按钮>文字按钮。

**Type:** [ButtonStyleMode](../arkts-apis/arkts-arkui-button-buttonstylemode-e.md)

**Default:** ButtonStyleMode.EMPHASIZED

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-ButtonOptions-buttonStyle?: ButtonStyleMode--><!--Device-ButtonOptions-buttonStyle?: ButtonStyleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controlSize

```TypeScript
controlSize?: ControlSize
```

按钮的尺寸。

默认值：ControlSize.NORMAL

**Type:** [ControlSize](../arkts-apis/arkts-arkui-button-controlsize-e.md)

**Default:** ControlSize.NORMAL

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-ButtonOptions-controlSize?: ControlSize--><!--Device-ButtonOptions-controlSize?: ControlSize-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## role

```TypeScript
role?: ButtonRole
```

按钮的角色。根据设置枚举值的不同，系统自动调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过  
[backgroundColor](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#backgroundcolor)、  
[fontColor](ButtonAttribute#fontColor)和[buttonStyle](ButtonAttribute#buttonStyle)接口设置，实际显示效果以最后一次设置为准。

默认值：ButtonRole.NORMAL

**Type:** [ButtonRole](arkts-arkui-buttonrole-e.md)

**Default:** ButtonRole.NORMAL

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

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

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonOptions-stateEffect?: boolean--><!--Device-ButtonOptions-stateEffect?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: ButtonType
```

按钮显示样式。

默认值：ButtonType.ROUNDED_RECTANGLE

API version 18及之后，ButtonType的默认值修改为ButtonType.ROUNDED_RECTANGLE。API version 18之前的版本，ButtonType的默认值为ButtonType.Capsule。

**Type:** [ButtonType](../arkts-apis/arkts-arkui-button-buttontype-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonOptions-type?: ButtonType--><!--Device-ButtonOptions-type?: ButtonType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

