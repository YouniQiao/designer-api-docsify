# OH_ArkUI_BaselineOffsetStyle

```c
typedef struct OH_ArkUI_BaselineOffsetStyle OH_ArkUI_BaselineOffsetStyle
```

## Overview

Defines a baseline offset style, which is used to set the baseline offset of text in a styled string so that the text moves up or down relative to the baseline in the vertical direction, thereby achieving special typesetting effects such as superscripts and subscripts. The baseline offset style takes effect for the styled string only after a style object is created and the offset value is set.<br> Call {@link OH_ArkUI_BaselineOffsetStyle_Create} to create a baseline offset style object.<br><br>After the object is created, call {@link OH_ArkUI_BaselineOffsetStyle_SetBaselineOffset} to set the baseline<br>offset value.<br><br>Call {@link OH_ArkUI_BaselineOffsetStyle_GetBaselineOffset} to obtain the baseline offset value.<br><br>After the object is used, call {@link OH_ArkUI_BaselineOffsetStyle_Destroy} to destroy it.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 24

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [styled_string.h](capi-styled-string-h.md)

