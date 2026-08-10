# WebBypassVsyncCondition

跳过渲染vsync条件。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-declare enum WebBypassVsyncCondition--><!--Device-unnamed-declare enum WebBypassVsyncCondition-End-->

**System capability:** SystemCapability.Web.Webview.Core

## NONE

```TypeScript
NONE = 0
```

默认值，按vsync调度流程绘制。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-WebBypassVsyncCondition-NONE = 0--><!--Device-WebBypassVsyncCondition-NONE = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## SCROLLBY_FROM_ZERO_OFFSET

```TypeScript
SCROLLBY_FROM_ZERO_OFFSET = 1
```

在使用scrollby（只支持带滚动偏移量）且Web页面滚动偏移量为0，渲染流程跳过vsync调度直接绘制。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-WebBypassVsyncCondition-SCROLLBY_FROM_ZERO_OFFSET = 1--><!--Device-WebBypassVsyncCondition-SCROLLBY_FROM_ZERO_OFFSET = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

