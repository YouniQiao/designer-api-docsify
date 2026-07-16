# ProvideOptions

Defines the options of Provide PropertyDecorator.

**Since:** 11

<!--Device-unnamed-declare interface ProvideOptions--><!--Device-unnamed-declare interface ProvideOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowOverride

```TypeScript
allowOverride?: string
```

Override the @Provide of any parent or parent of parent @Component.@Provide({allowOverride: "name"}) is also allowed to be used even when there is no ancestor @Component whose @Provide would be overridden.

**Type:** string

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-ProvideOptions-allowOverride?: string--><!--Device-ProvideOptions-allowOverride?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

