# AlertDialogButtonBaseOptions

警告弹窗中按钮的样式。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface AlertDialogButtonBaseOptions--><!--Device-unnamed-declare interface AlertDialogButtonBaseOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action: VoidCallback
```

Button选中时的回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogButtonBaseOptions-action: VoidCallback--><!--Device-AlertDialogButtonBaseOptions-action: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Button背景颜色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogButtonBaseOptions-backgroundColor?: ResourceColor--><!--Device-AlertDialogButtonBaseOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
defaultFocus?: boolean
```

设置Button是否是默认焦点，默认值false。值为true表示Button为默认焦点，值为false表示Button不为默认焦点。

**Type:** boolean

**Default:** false

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogButtonBaseOptions-defaultFocus?: boolean--><!--Device-AlertDialogButtonBaseOptions-defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enabled

```TypeScript
enabled?: boolean
```

点击Button是否响应，默认值true。

值为true时，Button可以响应。值为false时，Button不可以响应。

**Type:** boolean

**Default:** true

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogButtonBaseOptions-enabled?: boolean--><!--Device-AlertDialogButtonBaseOptions-enabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

Button的文本颜色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogButtonBaseOptions-fontColor?: ResourceColor--><!--Device-AlertDialogButtonBaseOptions-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: DialogButtonStyle
```

设置Button的风格样式，默认值DialogButtonStyle.DEFAULT。

**Type:** [DialogButtonStyle](arkts-arkui-dialogbuttonstyle-e.md)

**Default:** -

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogButtonBaseOptions-style?: DialogButtonStyle--><!--Device-AlertDialogButtonBaseOptions-style?: DialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: ResourceStr
```

Button的文本内容，若值为null，则该按钮不显示。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AlertDialogButtonBaseOptions-value: ResourceStr--><!--Device-AlertDialogButtonBaseOptions-value: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

