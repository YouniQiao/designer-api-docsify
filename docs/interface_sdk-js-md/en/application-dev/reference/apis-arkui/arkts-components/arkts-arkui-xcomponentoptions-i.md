# XComponentOptions

定义XComponent的选项。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface XComponentOptions--><!--Device-unnamed-declare interface XComponentOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller: XComponentController
```

绑定到组件的控制器，可用于调用组件的方法。该参数仅在type为SURFACE或TEXTURE时有效。

**Type:** [XComponentController](../arkts-apis/arkts-arkui-xcomponent-xcomponentcontroller-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentOptions-controller: XComponentController--><!--Device-XComponentOptions-controller: XComponentController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageAIOptions

```TypeScript
imageAIOptions?: ImageAIOptions
```

给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器，仅类型为SURFACE或TEXTURE时有效。未设置时不配置AI分析选项，可通过[enableAnalyzer](XComponentAttribute#enableAnalyzer)属性单独启用AI分析。

**Type:** [ImageAIOptions](../arkts-apis/arkts-arkui-imageaioptions-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentOptions-imageAIOptions?: ImageAIOptions--><!--Device-XComponentOptions-imageAIOptions?: ImageAIOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: XComponentType
```

组件的类型。

**Type:** [XComponentType](../arkts-apis/arkts-arkui-xcomponenttype-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentOptions-type: XComponentType--><!--Device-XComponentOptions-type: XComponentType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

