# OH_ArkUI_ParagraphStyle

```c
typedef struct OH_ArkUI_ParagraphStyle OH_ArkUI_ParagraphStyle
```

## Overview

Defines a paragraph style for uniformly setting the text alignment, line break, truncation, and other layout behaviors when building rich text paragraphs. It applies to scenarios that require fine-grained layout control over paragraphs, for example, setting the paragraph alignment in a rich text editor, and controlling the line break and truncation of long text in a news reader.<br> Call {@link OH_ArkUI_ParagraphStyle_Create} to create the corresponding paragraph style object.<br><br>Call {@link OH_ArkUI_ParagraphStyle_Destroy} to destroy the paragraph style object.<br><br>After the object is created, call the <b>OH_ArkUI_ParagraphStyle_SetXXX</b> series APIs to set specific<br>styles, for example, call {@link OH_ArkUI_ParagraphStyle_SetTextAlign} to set the text alignment. If the object fails to be created (a null pointer is returned) or the object has been destroyed, calling the <b>SetXXX</b> series APIs will not take effect.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 24

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [styled_string.h](capi-styled-string-h.md)

