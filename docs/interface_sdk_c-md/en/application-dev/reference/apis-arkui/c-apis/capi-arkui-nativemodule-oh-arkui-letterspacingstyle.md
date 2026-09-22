# OH_ArkUI_LetterSpacingStyle

```c
typedef struct OH_ArkUI_LetterSpacingStyle OH_ArkUI_LetterSpacingStyle
```

## Overview

Defines a letter spacing style, which is used to set the letter spacing of text to optimize the layout effect. It applies to scenarios where text is too densely arranged and difficult to read and the letter spacing needs to be adjusted, improving text readability and layout aesthetics.<br> Call {@link OH_ArkUI_LetterSpacingStyle_Create} to create a letter spacing style object.<br><br>After the object is created, call {@link OH_ArkUI_LetterSpacingStyle_SetLetterSpacing} to set the specific<br>letter spacing value. For details about the value selection principle, see the description of this API.<br><br>Call {@link OH_ArkUI_LetterSpacingStyle_GetLetterSpacing} to obtain the letter spacing value.<br><br>When the object is no longer used, call {@link OH_ArkUI_LetterSpacingStyle_Destroy} to destroy it. If creation fails, do not call the preceding APIs.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 24

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [styled_string.h](capi-styled-string-h.md)

