# ActionSheetButtonOptions

弹窗中按钮的样式。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ActionSheetButtonOptions--><!--Device-unnamed-export interface ActionSheetButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action: VoidCallback
```

Button选中时的回调。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**ArkTS-Dyn起始版本：** 8

**ArkTS-Sta起始版本：** 23

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetButtonOptions-action: VoidCallback--><!--Device-ActionSheetButtonOptions-action: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
defaultFocus?: boolean
```

设置Button是否是默认焦点，true表示Button是默认焦点，false表示Button不是默认焦点。

默认值：false

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**ArkTS-Dyn起始版本：** 10 

**ArkTS-Sta起始版本：** 23

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetButtonOptions-defaultFocus?: boolean--><!--Device-ActionSheetButtonOptions-defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enabled

```TypeScript
enabled?: boolean
```

点击Button是否响应，true表示Button可以响应，false表示Button不可以响应。

默认值：true

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**ArkTS-Dyn起始版本：** 10 

**ArkTS-Sta起始版本：** 23

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetButtonOptions-enabled?: boolean--><!--Device-ActionSheetButtonOptions-enabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: DialogButtonStyle
```

设置Button的风格样式。

默认值：DialogButtonStyle.DEFAULT

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**ArkTS-Dyn起始版本：** 10 

**ArkTS-Sta起始版本：** 23

**Type:** [DialogButtonStyle](arkts-arkui-dialogbuttonstyle-e.md)

**Default:** DialogButtonStyle.DEFAULT

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetButtonOptions-style?: DialogButtonStyle--><!--Device-ActionSheetButtonOptions-style?: DialogButtonStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: string | Resource
```

Button文本内容。

当文本内容过长无法显示时，用省略号代替未显示的部分。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**ArkTS-Dyn起始版本：** 8 

**ArkTS-Sta起始版本：** 23

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActionSheetButtonOptions-value: string | Resource--><!--Device-ActionSheetButtonOptions-value: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

