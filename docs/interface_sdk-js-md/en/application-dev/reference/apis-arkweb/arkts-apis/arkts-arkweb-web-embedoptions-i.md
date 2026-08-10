# EmbedOptions

Defines the Embed Options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface EmbedOptions--><!--Device-unnamed-export declare interface EmbedOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## supportCssDisplayChange

```TypeScript
supportCssDisplayChange?: boolean
```

Whether the {@link onNativeEmbedVisibilityChange} event supports display-related attributes of the embed element.&lt;br&gt;Default value is false. If true, the changes of the display-related attributes of the embed element will be reported through the {@link onNativeEmbedVisibilityChange} event.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-EmbedOptions-supportCssDisplayChange?: boolean--><!--Device-EmbedOptions-supportCssDisplayChange?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## supportDefaultIntrinsicSize

```TypeScript
supportDefaultIntrinsicSize?: boolean
```

Whether the embed element support the default intrinsic size of 300 * 150, expressed in CSS pixels.&lt;br&gt;When CSS size is set, the embed element size is CSS size, otherwise it is intrinsic size.&lt;br&gt;If true, then the intrinsic size is 300 * 150.&lt;br&gt;If false, the embed element will not be rendered when the CSS size is not set.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-EmbedOptions-supportDefaultIntrinsicSize?: boolean--><!--Device-EmbedOptions-supportDefaultIntrinsicSize?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

