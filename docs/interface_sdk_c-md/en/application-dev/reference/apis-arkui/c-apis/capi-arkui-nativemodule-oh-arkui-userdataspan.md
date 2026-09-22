# OH_ArkUI_UserDataSpan

```c
typedef struct OH_ArkUI_UserDataSpan OH_ArkUI_UserDataSpan
```

## Overview

Defines a user data span style, which is used to attach custom user data to a styled string in rich text for data identification and association during text interaction or custom rendering. For example, it can be used in scenarios such as attaching a message ID to a message text span in an instant messaging application, or attaching a custom-style tag to a text fragment in a rich text editor.<br> Call {@link OH_ArkUI_UserDataSpan_Create} to create a user data span style object.<br><br>After use, call {@link OH_ArkUI_UserDataSpan_Destroy} to destroy the user data span style object.<br><br>After successful creation, call {@link OH_ArkUI_UserDataSpan_SetUserData} to set the user data.<br><br>Call {@link OH_ArkUI_UserDataSpan_GetUserData} to obtain the user data.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 24

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [styled_string.h](capi-styled-string-h.md)

