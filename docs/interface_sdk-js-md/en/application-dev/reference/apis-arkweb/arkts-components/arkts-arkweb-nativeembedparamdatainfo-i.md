# NativeEmbedParamDataInfo

提供同层渲染object标签内嵌param元素变化时同层标签的详细信息。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-unnamed-declare interface NativeEmbedParamDataInfo--><!--Device-unnamed-declare interface NativeEmbedParamDataInfo-End-->

**System capability:** SystemCapability.Web.Webview.Core

## embedId

```TypeScript
embedId: string
```

同层标签的唯一id。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-NativeEmbedParamDataInfo-embedId: string--><!--Device-NativeEmbedParamDataInfo-embedId: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## objectAttributeId

```TypeScript
objectAttributeId?: string
```

同层标签的id信息。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-NativeEmbedParamDataInfo-objectAttributeId?: string--><!--Device-NativeEmbedParamDataInfo-objectAttributeId?: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## paramItems

```TypeScript
paramItems?: Array<NativeEmbedParamItem>
```

发生变化的param元素的详细信息，包括每一个param元素的状态变化类型、id、参数名称和参数值。

**Type:** Array&lt;NativeEmbedParamItem&gt;

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-NativeEmbedParamDataInfo-paramItems?: Array<NativeEmbedParamItem>--><!--Device-NativeEmbedParamDataInfo-paramItems?: Array<NativeEmbedParamItem>-End-->

**System capability:** SystemCapability.Web.Webview.Core

