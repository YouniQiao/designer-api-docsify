# OH_ArkUI_NativeModule_LineSpacingOptions

```c
typedef struct OH_ArkUI_NativeModule_LineSpacingOptions OH_ArkUI_NativeModule_LineSpacingOptions
```

## Overview

Defines a text line spacing option object, which is used to set whether the text line spacing takes effect only between lines. You can create a line spacing option object by calling {@link OH_ArkUI_NativeModule_LineSpacingOptions_Create}. After the object is used, you must call<br>{@link OH_ArkUI_NativeModule_LineSpacingOptions_Destroy} to destroy it and release resources. The two APIs must be<br>used in pairs; otherwise, a memory leak occurs. After the object is created, you can call<br>{@link OH_ArkUI_NativeModule_LineSpacingOptions_SetOnlyBetweenLines} to set whether the line spacing takes effect<br>only between lines, and call {@link OH_ArkUI_NativeModule_LineSpacingOptions_GetOnlyBetweenLines} to obtain the line spacing configuration. This struct is applicable to scenarios that require precise control over the display effect of text line spacing, such as text display where no line spacing is added to the first and last lines.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 26.0.1

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [text.h](capi-text-h.md)

