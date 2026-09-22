# OH_ArkUI_LeadingMarginSpanDrawInfo

```c
typedef struct OH_ArkUI_LeadingMarginSpanDrawInfo OH_ArkUI_LeadingMarginSpanDrawInfo
```

## Overview

Defines the custom drawing information for leading margin indentation, including the drawing context information of the current line (such as the drawing area and offset). You can implement custom leading margin indentation drawing logic in the callback function based on this information. It is applicable to scenarios such as adding custom icons or decorative elements to the first line of a paragraph, or implementing special indentation styles, making paragraph layout more flexible and rich. For example, draw a bookmark icon for the first line of a paragraph in a reader application, or draw a custom indentation marker for a specific paragraph in a document editor.<br> Call {@link OH_ArkUI_LeadingMarginSpanDrawInfo_Create} to create the corresponding custom drawing information<br>object for leading margin indentation.<br><br>Call {@link OH_ArkUI_LeadingMarginSpanDrawInfo_Destroy} to destroy the object.<br><br>This object is used in the callback function registered by<br>{@link OH_ArkUI_ParagraphStyle_RegisterOnDrawLeadingMarginCallback} to provide the drawing context of the current line and the custom drawing information object.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 24

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [styled_string.h](capi-styled-string-h.md)

