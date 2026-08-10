# ToggleConfiguration

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](../arkts-apis/arkts-arkui-common-commonconfiguration-i.md/arkts-arkui-common-commonconfiguration-i.md)。

**Inheritance/Implementation:** ToggleConfiguration extends [CommonConfiguration<ToggleConfiguration>](CommonConfiguration<ToggleConfiguration>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface ToggleConfiguration extends CommonConfiguration<ToggleConfiguration>--><!--Device-unnamed-declare interface ToggleConfiguration extends CommonConfiguration<ToggleConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enabled

```TypeScript
enabled: boolean
```

是否可以切换状态。

true：可以切换状态；false：不可以切换状态。

默认值：true

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ToggleConfiguration-enabled: boolean--><!--Device-ToggleConfiguration-enabled: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isOn

```TypeScript
isOn: boolean
```

开关是否打开。

true：开关打开；false：开关关闭。

默认值：false

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ToggleConfiguration-isOn: boolean--><!--Device-ToggleConfiguration-isOn: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## triggerChange

```TypeScript
triggerChange: Callback<boolean>
```

用于触发Toggle开关状态变化的回调函数，通常在自定义ContentModifier中通过编程方式改变开关状态。调用此回调并传入true可将开关状态设置为打开，传入false可将开关状态设置为关闭。

**Type:** [Callback](arkts-arkui-callback-i.md)&lt;boolean&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ToggleConfiguration-triggerChange: Callback<boolean>--><!--Device-ToggleConfiguration-triggerChange: Callback<boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

