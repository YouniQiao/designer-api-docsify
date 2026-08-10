# SaveButtonOptions

用于设置保存控件的图标、文本、按钮类型等属性。

> **说明：**
> 
> - 建议icon或text至少传入一个。
> 
> - 如果icon、text都不传入，SaveButton将使用默认样式创建，默认样式：SaveIconStyle默认样式为FULL_FILLED；
> SaveDescription默认样式为DOWNLOAD；ButtonType默认样式为Capsule。
> 
> - icon、text和buttonType不支持动态修改。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface SaveButtonOptions--><!--Device-unnamed-declare interface SaveButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonType

```TypeScript
buttonType?: ButtonType
```

设置保存控件的背景样式。默认值：ButtonType.Capsule。

**Type:** [ButtonType](../arkts-apis/arkts-arkui-button-buttontype-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveButtonOptions-buttonType?: ButtonType--><!--Device-SaveButtonOptions-buttonType?: ButtonType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon?: SaveIconStyle
```

设置保存控件的图标风格。&lt;br&gt;不传入该参数表示不显示图标；若同时也不传text，整体配置将显示为默认样式。

**Type:** [SaveIconStyle](arkts-arkui-saveiconstyle-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveButtonOptions-icon?: SaveIconStyle--><!--Device-SaveButtonOptions-icon?: SaveIconStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: SaveDescription
```

设置保存控件的文本描述。&lt;br&gt;不传入该参数表示不显示文本描述；若同时也不传icon，整体配置将显示为默认样式。

**Type:** [SaveDescription](arkts-arkui-savedescription-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveButtonOptions-text?: SaveDescription--><!--Device-SaveButtonOptions-text?: SaveDescription-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

