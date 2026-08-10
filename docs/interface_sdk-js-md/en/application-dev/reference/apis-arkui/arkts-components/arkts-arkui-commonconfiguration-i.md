# CommonConfiguration

开发者需要自定义class实现ContentModifier接口。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface CommonConfiguration<T>--><!--Device-unnamed-declare interface CommonConfiguration<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentModifier

```TypeScript
contentModifier: ContentModifier<T>
```

用于将用户需要的组件信息发送到自定义内容区。

**Type:** [ContentModifier](arkts-arkui-contentmodifier-i.md)&lt;T&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonConfiguration-contentModifier: ContentModifier<T>--><!--Device-CommonConfiguration-contentModifier: ContentModifier<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enabled

```TypeScript
enabled: boolean
```

如果该值为true，则contentModifier可用，并且可以响应triggerChange等操作，如果设置为false，则不会响应triggerChange等操作。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonConfiguration-enabled: boolean--><!--Device-CommonConfiguration-enabled: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

