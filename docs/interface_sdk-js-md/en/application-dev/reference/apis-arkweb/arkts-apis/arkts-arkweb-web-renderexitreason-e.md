# RenderExitReason

Enum type supplied to [renderExitReason](arkts-arkweb-web-onrenderexitedevent-i.md#renderExitReason) when onRenderExited being called.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum RenderExitReason--><!--Device-unnamed-export declare enum RenderExitReason-End-->

**System capability:** SystemCapability.Web.Webview.Core

## PROCESS_ABNORMAL_TERMINATION

```TypeScript
PROCESS_ABNORMAL_TERMINATION = 0
```

Render process non-zero exit status.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RenderExitReason-PROCESS_ABNORMAL_TERMINATION = 0--><!--Device-RenderExitReason-PROCESS_ABNORMAL_TERMINATION = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## PROCESS_WAS_KILLED

```TypeScript
PROCESS_WAS_KILLED = 1
```

SIGKILL or task manager kill.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RenderExitReason-PROCESS_WAS_KILLED = 1--><!--Device-RenderExitReason-PROCESS_WAS_KILLED = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## PROCESS_CRASHED

```TypeScript
PROCESS_CRASHED = 2
```

The rendering process crashes and exits, such as a segment error.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RenderExitReason-PROCESS_CRASHED = 2--><!--Device-RenderExitReason-PROCESS_CRASHED = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

## PROCESS_OOM

```TypeScript
PROCESS_OOM = 3
```

Out of memory.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RenderExitReason-PROCESS_OOM = 3--><!--Device-RenderExitReason-PROCESS_OOM = 3-End-->

**System capability:** SystemCapability.Web.Webview.Core

## PROCESS_EXIT_UNKNOWN

```TypeScript
PROCESS_EXIT_UNKNOWN = 4
```

Unknown reason.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RenderExitReason-PROCESS_EXIT_UNKNOWN = 4--><!--Device-RenderExitReason-PROCESS_EXIT_UNKNOWN = 4-End-->

**System capability:** SystemCapability.Web.Webview.Core

