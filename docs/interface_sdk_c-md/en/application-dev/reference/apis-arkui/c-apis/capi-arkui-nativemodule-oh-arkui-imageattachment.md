# OH_ArkUI_ImageAttachment

```c
typedef struct OH_ArkUI_ImageAttachment OH_ArkUI_ImageAttachment
```

## Overview

Defines an image object used to embed image content in a styled string. As a component of the styled string, the image can be attached to the styled string to implement mixed text and image layout after the image source and style attributes are set.<br> Call {@link OH_ArkUI_ImageAttachment_Create} to create an image style object.<br><br>Call {@link OH_ArkUI_ImageAttachment_Destroy} to destroy the image style object.<br><br>After the object is created, call the <b>OH_ArkUI_ImageAttachment_SetXXX</b> series APIs to set style<br>attributes, for example, call {@link OH_ArkUI_ImageAttachment_SetPixelMap} to set the image source.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 24

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [styled_string.h](capi-styled-string-h.md)

