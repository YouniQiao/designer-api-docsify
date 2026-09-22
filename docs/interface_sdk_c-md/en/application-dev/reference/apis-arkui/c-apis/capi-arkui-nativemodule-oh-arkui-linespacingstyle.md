# OH_ArkUI_LineSpacingStyle

```c
typedef struct OH_ArkUI_LineSpacingStyle OH_ArkUI_LineSpacingStyle
```

## Overview

Defines a line spacing style, which is used to set the spacing between text lines to improve text readability and visual effect. It applies to scenarios that require fine-grained control over the line spacing of multi-line text layout, such as e-book readers, news and information applications, and editors for long documents.<br> Call {@link OH_ArkUI_LineSpacingStyle_Create} to create a line spacing style object. The default line<br>spacing value is <b>0</b>, and whether the line spacing takes effect only between lines defaults to<br><b>false</b>.<br><br>Call {@link OH_ArkUI_LineSpacingStyle_Destroy} to destroy the line spacing style object.<br><br>After the object is created, call {@link OH_ArkUI_LineSpacingStyle_SetLineSpacing} to set the line spacing<br>value. For details about the value range and constraints, see the description of this API.<br><br>Call {@link OH_ArkUI_LineSpacingStyle_SetOnlyBetweenLines} to set whether the line spacing takes effect only between lines. For details about the value principle, see the description of this API.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 26.0.0

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [styled_string.h](capi-styled-string-h.md)

