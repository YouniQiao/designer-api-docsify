# StyleOptions

属性字符串样式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface StyleOptions--><!--Device-unnamed-declare interface StyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## length

```TypeScript
length?: number
```

设置属性字符串样式的长度。

当length的值小于0或超出字符串长度与start的差值时，按字符串长度与start的差值处理。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyleOptions-length?: number--><!--Device-StyleOptions-length?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start?: number
```

设置属性字符串样式的开始位置。

当start的值小于0或超出字符串长度时，按0处理。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyleOptions-start?: number--><!--Device-StyleOptions-start?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## styledKey

```TypeScript
styledKey: StyledStringKey
```

样式类型的枚举值。

**Type:** [StyledStringKey](arkts-arkui-styledstring-styledstringkey-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyleOptions-styledKey: StyledStringKey--><!--Device-StyleOptions-styledKey: StyledStringKey-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## styledValue

```TypeScript
styledValue: StyledStringValue
```

用于设置属性字符串样式的样式对象。

**Type:** [StyledStringValue](arkts-arkui-styledstringvalue-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-StyleOptions-styledValue: StyledStringValue--><!--Device-StyleOptions-styledValue: StyledStringValue-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

