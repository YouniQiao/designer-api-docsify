# WebBypassVsyncCondition

Enumerates whether to allow the rendering process to bypass the vsync scheduling.

**Since:** 20

<!--Device-unnamed-declare enum WebBypassVsyncCondition--><!--Device-unnamed-declare enum WebBypassVsyncCondition-End-->

**System capability:** SystemCapability.Web.Webview.Core

## NONE

```TypeScript
NONE = 0
```

The rendering process does not bypass the vsync scheduling. Default value.

**Since:** 20

<!--Device-WebBypassVsyncCondition-NONE = 0--><!--Device-WebBypassVsyncCondition-NONE = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## SCROLLBY_FROM_ZERO_OFFSET

```TypeScript
SCROLLBY_FROM_ZERO_OFFSET = 1
```

When **scrollBy** is used (only the scrolling offset is supported) and the scrolling offset of the web page is **0**, the rendering process bypasses the vsync scheduling.

**Since:** 20

<!--Device-WebBypassVsyncCondition-SCROLLBY_FROM_ZERO_OFFSET = 1--><!--Device-WebBypassVsyncCondition-SCROLLBY_FROM_ZERO_OFFSET = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

