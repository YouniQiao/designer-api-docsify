# NativeEmbedParamDataInfo

Provides details about the same-layer tag when the **param** element embedded in the **object** tag changes.

**Since:** 21

<!--Device-unnamed-declare interface NativeEmbedParamDataInfo--><!--Device-unnamed-declare interface NativeEmbedParamDataInfo-End-->

**System capability:** SystemCapability.Web.Webview.Core

## embedId

```TypeScript
embedId: string
```

Unique ID of the same-layer tag.

**Type:** string

**Since:** 21

<!--Device-NativeEmbedParamDataInfo-embedId: string--><!--Device-NativeEmbedParamDataInfo-embedId: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## objectAttributeId

```TypeScript
objectAttributeId?: string
```

ID of the same-layer tag.

**Type:** string

**Since:** 21

<!--Device-NativeEmbedParamDataInfo-objectAttributeId?: string--><!--Device-NativeEmbedParamDataInfo-objectAttributeId?: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## paramItems

```TypeScript
paramItems?: Array<NativeEmbedParamItem>
```

Details of the changed **param** element, including the status change type, ID, name, and value of each **param** element.

**Type:** Array&lt;NativeEmbedParamItem&gt;

**Since:** 21

<!--Device-NativeEmbedParamDataInfo-paramItems?: Array<NativeEmbedParamItem>--><!--Device-NativeEmbedParamDataInfo-paramItems?: Array<NativeEmbedParamItem>-End-->

**System capability:** SystemCapability.Web.Webview.Core

