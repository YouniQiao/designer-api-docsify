# RenderExitReason

Enum type supplied to [renderExitReason](arkts-arkweb-web-onrenderexitedevent-i.md#renderexitreason) when onRenderExited being called.@enum { number }

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## PROCESS_ABNORMAL_TERMINATION

```TypeScript
PROCESS_ABNORMAL_TERMINATION = 0
```

Render process non-zero exit status.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## PROCESS_WAS_KILLED

```TypeScript
PROCESS_WAS_KILLED = 1
```

SIGKILL or task manager kill.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## PROCESS_CRASHED

```TypeScript
PROCESS_CRASHED = 2
```

The rendering process crashes and exits, such as a segment error.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## PROCESS_OOM

```TypeScript
PROCESS_OOM = 3
```

Out of memory.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## PROCESS_EXIT_UNKNOWN

```TypeScript
PROCESS_EXIT_UNKNOWN = 4
```

Unknown reason.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core
