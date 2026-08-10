# ToggleConfiguration

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](arkts-arkui-common-commonconfiguration-i.md)。

**Inheritance/Implementation:** ToggleConfiguration extends [CommonConfiguration<ToggleConfiguration>](CommonConfiguration<ToggleConfiguration>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ToggleConfiguration extends CommonConfiguration<ToggleConfiguration>--><!--Device-unnamed-export declare interface ToggleConfiguration extends CommonConfiguration<ToggleConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isOn

```TypeScript
isOn: boolean
```

开关是否打开。

true：开关打开；false：开关关闭。

默认值：false 

**ArkTS-Sta起始版本：** 23

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleConfiguration-isOn: boolean--><!--Device-ToggleConfiguration-isOn: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## triggerChange

```TypeScript
triggerChange: Callback<boolean>
```

触发switch选中状态变化。

true：状态从关切换为开；false：状态从开切换为关。

**ArkTS-Sta起始版本：** 23

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;boolean&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleConfiguration-triggerChange: Callback<boolean>--><!--Device-ToggleConfiguration-triggerChange: Callback<boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

