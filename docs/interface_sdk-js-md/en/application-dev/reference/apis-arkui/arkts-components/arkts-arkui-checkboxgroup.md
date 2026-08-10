# CheckboxGroup

多选框群组，用于控制多选框全选或取消全选状态。适用于需要批量管理多个Checkbox选择状态的场景，如列表项批量选择、表单全选等，可简化用户操作，提升交互体验。

> **说明：**

## 子组件

无

## CheckboxGroup

```TypeScript
CheckboxGroup(options?: CheckboxGroupOptions)
```

创建多选框群组，用于控制群组内Checkbox的全选或取消全选状态，具有相同group值的Checkbox和CheckboxGroup属于同一群组。

在结合带缓存功能的组件使用时（如[List]{@link list}），未被创建的Checkbox选中状态需要应用手动控制。详细示例请参考  
[示例4](docroot://reference/apis-arkui/arkui-ts/ts-basic-components-checkboxgroup.md#示例4设置全选)。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CheckboxGroupInterface-(options?: CheckboxGroupOptions): CheckboxGroupAttribute--><!--Device-CheckboxGroupInterface-(options?: CheckboxGroupOptions): CheckboxGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CheckboxGroupOptions](../arkts-apis/arkts-arkui-checkboxgroup-checkboxgroupoptions-i.md) | No | 配置多选框群组参数。 <br/> 未设置时，按照CheckboxGroupOptions中各参数的默认值配置。 |

## Summary

- [CheckBoxGroupConfiguration](arkts-arkui-checkboxgroup-checkboxgroupconfiguration-i.md)
- [CheckboxGroupOptions](arkts-arkui-checkboxgroup-checkboxgroupoptions-i.md)
- [CheckboxGroupResult](arkts-arkui-checkboxgroup-checkboxgroupresult-i.md)
- [OnCheckboxGroupChangeCallback](arkts-arkui-checkboxgroup-oncheckboxgroupchangecallback-t.md)
- [SelectStatus](arkts-arkui-checkboxgroup-selectstatus-e.md)
