# ToggleOptions

Toggle的信息。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ToggleOptions--><!--Device-unnamed-export declare interface ToggleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isOn

```TypeScript
isOn?: boolean | undefined | Bindable<boolean>
```

开关是否打开。

true：打开；false：关闭。

默认值：false

该属性支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。

该属性支持[!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**卡片能力（仅ArkTS-Dyn）：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**ArkTS-Dyn起始版本：** 8 

**ArkTS-Sta起始版本：** 23

**Type:** boolean \| undefined \| Bindable&lt;boolean&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleOptions-isOn?: boolean | undefined | Bindable<boolean>--><!--Device-ToggleOptions-isOn?: boolean | undefined | Bindable<boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: ToggleType
```

开关的样式。

默认值：ToggleType.Switch

**卡片能力（仅ArkTS-Dyn）：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**ArkTS-Dyn起始版本：** 8 

**ArkTS-Sta起始版本：** 23

**Type:** [ToggleType](arkts-arkui-toggle-toggletype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleOptions-type: ToggleType--><!--Device-ToggleOptions-type: ToggleType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

