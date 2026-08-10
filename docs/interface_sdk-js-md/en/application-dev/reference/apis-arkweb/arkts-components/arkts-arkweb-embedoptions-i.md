# EmbedOptions

Web同层渲染的配置。

**Since:** 16

**ArkTS mode:** ArkTS-Dyn only, since version 16.

<!--Device-unnamed-declare interface EmbedOptions--><!--Device-unnamed-declare interface EmbedOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## supportCssDisplayChange

```TypeScript
supportCssDisplayChange?: boolean
```

设置同层渲染可见性接口是否支持显示属性。

同层渲染可见性接口默认支持同层标签相对于视口的可见状态。

设置为true时，支持显示CSS属性，包括visibility、display和宽高。

设置为false时，不支持显示CSS属性，仅支持同层标签相对于视口的可见性。

**Type:** boolean

**Default:** false

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-EmbedOptions-supportCssDisplayChange?: boolean--><!--Device-EmbedOptions-supportCssDisplayChange?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## supportDefaultIntrinsicSize

```TypeScript
supportDefaultIntrinsicSize?: boolean
```

设置同层渲染元素是否支持固定大小 300 * 150。

当H5侧CSS设置了大小时，同层渲染元素大小为CSS大小，否则为固定大小。

为true时，固定大小为 300 * 150。

为false时，若H5侧CSS未设置大小，则同层渲染元素不渲染。

默认值：false

单位：像素。

**Type:** boolean

**Default:** false

**Since:** 16

**ArkTS mode:** ArkTS-Dyn only, since version 16.

<!--Device-EmbedOptions-supportDefaultIntrinsicSize?: boolean--><!--Device-EmbedOptions-supportDefaultIntrinsicSize?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

