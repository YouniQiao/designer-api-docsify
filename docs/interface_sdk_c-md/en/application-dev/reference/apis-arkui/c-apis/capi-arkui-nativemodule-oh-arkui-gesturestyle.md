# OH_ArkUI_GestureStyle

```c
typedef struct OH_ArkUI_GestureStyle OH_ArkUI_GestureStyle
```

## Overview

Defines a gesture style. It applies to scenarios where a gesture style needs to be configured and related event callbacks need to be received, making it easier for an application to manage gesture styles and event callbacks in a unified manner.<br> Call {@link OH_ArkUI_GestureStyle_Create} to create the corresponding gesture style object.<br><br>After the object is created, call the <b>OH_ArkUI_GestureStyle_RegisterOnXXXCallback</b> series APIs to<br>register specific event callbacks, for example, call {@link OH_ArkUI_GestureStyle_RegisterOnClickCallback}<br>to register the click event callback.<br><br>After use, call {@link OH_ArkUI_GestureStyle_Destroy} to destroy the gesture style object.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 24

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [styled_string.h](capi-styled-string-h.md)

