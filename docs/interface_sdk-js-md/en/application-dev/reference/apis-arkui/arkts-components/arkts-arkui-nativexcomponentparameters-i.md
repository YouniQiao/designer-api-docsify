# NativeXComponentParameters

Defines the options of the **XComponent**. An XComponent created with such constructor parameters can pass its corresponding FrameNode object to the Native side, enabling the use of NDK APIs for surface lifecycle–related settings and [component event listening](../../../ui/ndk-listen-to-component-events.md).

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Deprecated since:** -1

<!--Device-unnamed-declare interface NativeXComponentParameters--><!--Device-unnamed-declare interface NativeXComponentParameters-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageAIOptions

```TypeScript
imageAIOptions?: ImageAIOptions
```

AI analysis options. You can configure the analysis type or bind an analyzer controller through this parameter.

**Type:** ImageAIOptions

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-NativeXComponentParameters-imageAIOptions?: ImageAIOptions--><!--Device-NativeXComponentParameters-imageAIOptions?: ImageAIOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: XComponentType
```

Type of the component.

**Type:** XComponentType

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-NativeXComponentParameters-type: XComponentType--><!--Device-NativeXComponentParameters-type: XComponentType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

