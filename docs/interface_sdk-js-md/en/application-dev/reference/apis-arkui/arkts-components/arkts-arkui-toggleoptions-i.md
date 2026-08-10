# ToggleOptions

Toggle组件的配置信息。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface ToggleOptions--><!--Device-unnamed-declare interface ToggleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isOn

```TypeScript
isOn?: boolean
```

开关是否打开。

true：打开；false：关闭。

默认值：false

该属性支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。

该属性支持[!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ToggleOptions-isOn?: boolean--><!--Device-ToggleOptions-isOn?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: ToggleType
```

开关的样式。

默认值：ToggleType.Switch

**Type:** [ToggleType](../arkts-apis/arkts-arkui-toggle-toggletype-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ToggleOptions-type: ToggleType--><!--Device-ToggleOptions-type: ToggleType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

