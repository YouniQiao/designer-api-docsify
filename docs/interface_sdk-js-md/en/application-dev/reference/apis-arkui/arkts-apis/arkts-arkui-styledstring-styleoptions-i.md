# StyleOptions

属性字符串初始化选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface StyleOptions--><!--Device-unnamed-export declare interface StyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## length

```TypeScript
length?: int
```

设置属性字符串样式的长度。

当length的值小于0或超出字符串长度与start的差值时，按字符串长度与start的差值处理。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyleOptions-length?: int--><!--Device-StyleOptions-length?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start?: int
```

设置属性字符串样式的开始位置。

当start的值小于0或超出字符串长度时，按0处理。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyleOptions-start?: int--><!--Device-StyleOptions-start?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## styledKey

```TypeScript
styledKey: StyledStringKey
```

样式类型的枚举值。

**Type:** [StyledStringKey](arkts-arkui-styledstring-styledstringkey-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyleOptions-styledKey: StyledStringKey--><!--Device-StyleOptions-styledKey: StyledStringKey-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## styledValue

```TypeScript
styledValue: StyledStringValue
```

样式对象。

**Type:** [StyledStringValue](arkts-arkui-styledstringvalue-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StyleOptions-styledValue: StyledStringValue--><!--Device-StyleOptions-styledValue: StyledStringValue-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

