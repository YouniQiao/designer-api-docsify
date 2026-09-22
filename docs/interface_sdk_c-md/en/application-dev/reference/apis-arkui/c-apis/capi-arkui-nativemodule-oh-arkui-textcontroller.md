# OH_ArkUI_TextController

```c
typedef struct OH_ArkUI_TextController OH_ArkUI_TextController
```

## Overview

Defines a text component controller, which is used to control and interact with the text component on the native side. You can create a controller object through {@link OH_ArkUI_TextController_Create}. When the object is<br>created, you must call {@link OH_ArkUI_TextController_Destroy} to destroy it and release resources after use. The<br>two must be used in pairs; otherwise, memory leaks will occur. After the controller is created, you can use APIs<br>such as {@link OH_ArkUI_TextController_SetStyledString} to set the styled string of the text component, implementing dynamic management and style control of the text content. This is applicable to scenarios where the text component needs to be operated at the native layer.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 26.0.0

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [text.h](capi-text-h.md)

