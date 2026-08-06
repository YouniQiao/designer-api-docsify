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

Whether the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ event supports display-related attributes of the embed element.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Default value is false. If true, the changes of the display-related attributes of the embed element will be reported through the \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ event.

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

Whether the embed element support the default intrinsic size of 300 * 150, expressed in CSS pixels.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_When CSS size is set, the embed element size is CSS size, otherwise it is intrinsic size.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_If true, then the intrinsic size is 300 * 150.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_If false, the embed element will not be rendered when the CSS size is not set.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-EmbedOptions-supportDefaultIntrinsicSize?: boolean--><!--Device-EmbedOptions-supportDefaultIntrinsicSize?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

