# OH_ArkUI_CustomSpan

```c
typedef struct OH_ArkUI_CustomSpan OH_ArkUI_CustomSpan
```

## Overview

Defines a custom span, which is used to implement custom measurement and drawing capabilities in a styled string. A custom span determines its placeholder size through the measurement callback and draws custom content in the corresponding area through the drawing callback, thereby embedding custom graphic elements into rich text.<br> Call {@link OH_ArkUI_CustomSpan_Create} to create a custom span object.<br><br>After the object is created, call {@link OH_ArkUI_CustomSpan_RegisterOnMeasureCallback} to register the<br>measurement callback.<br><br>Call {@link OH_ArkUI_CustomSpan_RegisterOnDrawCallback} to register the drawing callback.<br><br>Call {@link OH_ArkUI_CustomSpan_Destroy} to destroy the custom span object.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 24

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [styled_string.h](capi-styled-string-h.md)

