# ScrollDirectionalLockType

Enum defining the scope of directional lock behavior in the WebView, used with [enableScrollDirectionalLock](arkts-arkweb-web-webattribute-i.md#enablescrolldirectionallock).

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Web.Webview.Core

## ALL

```TypeScript
ALL = 0
```

Applies directional lock across all scroll contexts. This includes both nested and flat scroll scenarios.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

## NESTED_SCROLL

```TypeScript
NESTED_SCROLL = 1
```

Applies directional lock only within nested scroll scenarios. This is the default behavior in ArkWeb to improve UX in complex scroll hierarchies.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core
