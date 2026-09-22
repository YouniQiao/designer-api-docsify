# OH_ArkUI_TextStyle

```c
typedef struct OH_ArkUI_TextStyle OH_ArkUI_TextStyle
```

## Overview

Defines a text font style, which is used to set attributes such as the font color, size, and style of text. It is applicable to scenarios where text display effects need to be customized.<br> Call {@link OH_ArkUI_TextStyle_Create} to create a text font style object.<br><br>Call {@link OH_ArkUI_TextStyle_Destroy} to destroy the text font style object. After destruction, do not call<br>the <b>OH_ArkUI_TextStyle_SetXXX</b> series APIs.<br><br>After the object is created successfully, call the <b>OH_ArkUI_TextStyle_SetXXX</b> series APIs to set specific<br>styles. If creation fails, do not call the <b>SetXXX</b> series APIs. For example, call<br>{@link OH_ArkUI_TextStyle_SetFontColor} to set the font color.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 24

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [styled_string.h](capi-styled-string-h.md)

