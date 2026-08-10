# CheckboxOptions

多选框的信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CheckboxOptions--><!--Device-unnamed-export declare interface CheckboxOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## group

```TypeScript
group?: string
```

用于指定多选框所属群组的名称（即所属CheckboxGroup的名称）。

默认值：undefined，默认状态下配合[CheckboxGroupOptions](arkts-arkui-checkboxgroup-checkboxgroupoptions-i.md)属性group信息为undefined的节点使用。 

**说明：**

未配合使用[CheckboxGroup](arkts-arkui-checkboxgroup-checkboxgroup-f.md#checkboxgroup)组件时，此值无用。 

**卡片能力（仅ArkTS-Dyn）：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxOptions-group?: string--><!--Device-CheckboxOptions-group?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## indicatorBuilder

```TypeScript
indicatorBuilder?: CustomBuilder
```

配置多选框的选中样式为自定义组件。自定义组件与Checkbox组件为中心点对齐显示。indicatorBuilder设置为undefined/null时，默认为indicatorBuilder未设置状态。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 12开始，该接口支持在原子化服务中使用。

**Type:** [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxOptions-indicatorBuilder?: CustomBuilder--><!--Device-CheckboxOptions-indicatorBuilder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name?: string
```

指定多选框名称。

默认值：undefined，取值为undefined无效果。 

**卡片能力（仅ArkTS-Dyn）：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxOptions-name?: string--><!--Device-CheckboxOptions-name?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

