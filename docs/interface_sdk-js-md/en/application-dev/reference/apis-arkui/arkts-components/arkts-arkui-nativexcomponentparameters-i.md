# NativeXComponentParameters

定义native xcomponent参数。使用此类构造参数创建的XComponent可以将其对应的[FrameNode](../arkts-apis/arkts-arkui-framenode-c.md/arkts-arkui-framenode-c.md)对象传递到Native侧，从而能够使用NDK接口进行surface生命周期相关设置和[组件事件监听](../../../ui/ndk-listen-to-component-events.md)。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

<!--Device-unnamed-declare interface NativeXComponentParameters--><!--Device-unnamed-declare interface NativeXComponentParameters-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageAIOptions

```TypeScript
imageAIOptions?: ImageAIOptions
```

给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。未设置时不配置AI分析选项，仅类型为SURFACE或TEXTURE时有效。

**Type:** [ImageAIOptions](../arkts-apis/arkts-arkui-imageaioptions-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-NativeXComponentParameters-imageAIOptions?: ImageAIOptions--><!--Device-NativeXComponentParameters-imageAIOptions?: ImageAIOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: XComponentType
```

XComponent的类型。

**Type:** [XComponentType](../arkts-apis/arkts-arkui-xcomponenttype-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-NativeXComponentParameters-type: XComponentType--><!--Device-NativeXComponentParameters-type: XComponentType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

