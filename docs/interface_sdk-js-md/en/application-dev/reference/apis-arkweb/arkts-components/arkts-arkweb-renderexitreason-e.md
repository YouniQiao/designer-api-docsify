# RenderExitReason

Enum type supplied to {@link renderExitReason} when onRenderExited being called.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare enum RenderExitReason--><!--Device-unnamed-declare enum RenderExitReason-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ProcessAbnormalTermination

```TypeScript
ProcessAbnormalTermination = 0
```

Render process non-zero exit status.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RenderExitReason-ProcessAbnormalTermination = 0--><!--Device-RenderExitReason-ProcessAbnormalTermination = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ProcessWasKilled

```TypeScript
ProcessWasKilled = 1
```

SIGKILL or task manager kill.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RenderExitReason-ProcessWasKilled = 1--><!--Device-RenderExitReason-ProcessWasKilled = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ProcessCrashed

```TypeScript
ProcessCrashed = 2
```

Segmentation fault.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RenderExitReason-ProcessCrashed = 2--><!--Device-RenderExitReason-ProcessCrashed = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ProcessOom

```TypeScript
ProcessOom = 3
```

Out of memory.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RenderExitReason-ProcessOom = 3--><!--Device-RenderExitReason-ProcessOom = 3-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ProcessExitUnknown

```TypeScript
ProcessExitUnknown = 4
```

Unknown reason.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RenderExitReason-ProcessExitUnknown = 4--><!--Device-RenderExitReason-ProcessExitUnknown = 4-End-->

**System capability:** SystemCapability.Web.Webview.Core

