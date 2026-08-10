# CheckboxOptions

多选框的信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface CheckboxOptions--><!--Device-unnamed-declare interface CheckboxOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## group

```TypeScript
group?: string
```

用于指定多选框所属群组的名称（即所属CheckboxGroup的名称）。

默认值：undefined，默认状态下配合[CheckboxGroupOptions](../arkts-apis/arkts-arkui-checkboxgroup-checkboxgroupoptions-i.md/arkts-arkui-checkboxgroup-checkboxgroupoptions-i.md)属性group信息为undefined的节点使用。 

**说明：**

未配合使用[CheckboxGroup](../arkts-apis/arkts-arkui-checkboxgroup-checkboxgroup-f.md/arkts-arkui-checkboxgroup-checkboxgroup-f.md#checkboxgroup)组件时，此值无用。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CheckboxOptions-group?: string--><!--Device-CheckboxOptions-group?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## indicatorBuilder

```TypeScript
indicatorBuilder?: CustomBuilder
```

配置多选框的选中样式为自定义组件。当需要实现非默认勾选图标的选中样式（如文字、数字、自定义图标等）时使用此参数。自定义组件与Checkbox组件为中心点对齐显示。indicatorBuilder设置为undefined/null时，默认为indicatorBuilder未设置状态，使用默认的勾选图标样式。

**Type:** [CustomBuilder](arkts-arkui-custombuilder-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CheckboxOptions-indicatorBuilder?: CustomBuilder--><!--Device-CheckboxOptions-indicatorBuilder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name?: string
```

指定多选框名称，用于标识不同的多选框实例。

默认值：undefined，取值为undefined无效果。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CheckboxOptions-name?: string--><!--Device-CheckboxOptions-name?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

