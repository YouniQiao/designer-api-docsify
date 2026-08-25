# RenderExitReason

Enum type supplied to [renderExitReason](arkts-arkweb-web-onrenderexitedevent-i.md#renderexitreason) when onRenderExited being called.@enum { number }

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## PROCESS_ABNORMAL_TERMINATION

```TypeScript
PROCESS_ABNORMAL_TERMINATION = 0
```

Render process non-zero exit status.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## PROCESS_WAS_KILLED

```TypeScript
PROCESS_WAS_KILLED = 1
```

SIGKILL or task manager kill.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## PROCESS_CRASHED

```TypeScript
PROCESS_CRASHED = 2
```

The rendering process crashes and exits, such as a segment error.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## PROCESS_OOM

```TypeScript
PROCESS_OOM = 3
```

Out of memory.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## PROCESS_EXIT_UNKNOWN

```TypeScript
PROCESS_EXIT_UNKNOWN = 4
```

Unknown reason.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core
