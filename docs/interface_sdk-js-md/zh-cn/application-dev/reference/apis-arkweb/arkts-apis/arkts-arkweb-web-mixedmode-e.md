# MixedMode

The Web's behavior to load from HTTP or HTTPS. Defaults to MixedMode.None.@enum { number }

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## ALL

```TypeScript
ALL = 0
```

Loose Mode: HTTP and HTTPS hybrid content can be loaded. This means that all insecure content can be loaded.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## COMPATIBLE

```TypeScript
COMPATIBLE = 1
```

Compatibility Modes: HTTP and HTTPS hybrid content can be loaded in compatibility mode. This means that some insecure content may be loaded.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## NONE

```TypeScript
NONE = 2
```

Strict Mode: HTTP and HTTPS hybrid content cannot be loaded.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core
