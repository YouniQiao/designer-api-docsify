# FontSettingOptions

字体配置项。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface FontSettingOptions--><!--Device-unnamed-declare interface FontSettingOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableVariableFontWeight

```TypeScript
enableVariableFontWeight?: boolean
```

是否启用可变字重调节。字体配置项作为  
[fontWeight](arkts-arkui-text-textattribute-i.md#fontweight)接口的入参，fontWeight接口中weight取值为[100, 900]内非整百数值时，enableVariableFontWeight用于设置weight的值是否生效。

默认值：false 

true：启用可变字重调节。此时如果weight取值为[100, 900]范围内任意整数，字重取值为weight，否则取默认值400。

false：禁用可变字重调节。此时如果weight取值为[100, 900]范围内的整百数值，字重取值为weight；weight是非整百数值时，字重取默认值400。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-FontSettingOptions-enableVariableFontWeight?: boolean--><!--Device-FontSettingOptions-enableVariableFontWeight?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

