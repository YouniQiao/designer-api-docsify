# OH_ArkUI_BackgroundColorStyle

```c
typedef struct OH_ArkUI_BackgroundColorStyle OH_ArkUI_BackgroundColorStyle
```

## Overview

Defines a background color style, which supports customizing the background color and corner radius. It is used to set a background highlight effect for a styled string, for example, search result highlighting, key text marking, and label-style text display, to improve the visual hierarchy and recognizability of text.<br> Call {@link OH_ArkUI_BackgroundColorStyle_Create} to create a background color style object.<br><br>After the object is created, call {@link OH_ArkUI_BackgroundColorStyle_SetColor} and<br>{@link OH_ArkUI_BackgroundColorStyle_SetRadius} to set the background color and corner radius.<br><br>Call {@link OH_ArkUI_BackgroundColorStyle_GetColor} and {@link OH_ArkUI_BackgroundColorStyle_GetRadius}<br>to obtain the background color and corner radius.<br><br>After the object is used, call {@link OH_ArkUI_BackgroundColorStyle_Destroy} to destroy it.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 24

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [styled_string.h](capi-styled-string-h.md)

