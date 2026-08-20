# ContextMenuEditStateFlags

Defines the context menu supported event bit flags, related to [onContextMenuShow](arkts-web-attribute.md#oncontextmenushow) method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum ContextMenuEditStateFlags--><!--Device-unnamed-export declare enum ContextMenuEditStateFlags-End-->

**System capability:** SystemCapability.Web.Webview.Core

## NONE

```TypeScript
NONE = 0
```

Editing is not allowed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ContextMenuEditStateFlags-NONE = 0--><!--Device-ContextMenuEditStateFlags-NONE = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## CAN_CUT

```TypeScript
CAN_CUT = 1 << 0
```

Cutting is supported.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ContextMenuEditStateFlags-CAN_CUT = 1 << 0--><!--Device-ContextMenuEditStateFlags-CAN_CUT = 1 << 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## CAN_COPY

```TypeScript
CAN_COPY = 1 << 1
```

Copying is supported.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ContextMenuEditStateFlags-CAN_COPY = 1 << 1--><!--Device-ContextMenuEditStateFlags-CAN_COPY = 1 << 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## CAN_PASTE

```TypeScript
CAN_PASTE = 1 << 2
```

Pasting is supported.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ContextMenuEditStateFlags-CAN_PASTE = 1 << 2--><!--Device-ContextMenuEditStateFlags-CAN_PASTE = 1 << 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

## CAN_SELECT_ALL

```TypeScript
CAN_SELECT_ALL = 1 << 3
```

Selecting all is supported.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ContextMenuEditStateFlags-CAN_SELECT_ALL = 1 << 3--><!--Device-ContextMenuEditStateFlags-CAN_SELECT_ALL = 1 << 3-End-->

**System capability:** SystemCapability.Web.Webview.Core

