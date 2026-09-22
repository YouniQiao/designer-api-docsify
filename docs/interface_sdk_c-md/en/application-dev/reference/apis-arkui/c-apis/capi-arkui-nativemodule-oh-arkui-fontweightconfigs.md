# OH_ArkUI_FontWeightConfigs

```c
typedef struct OH_ArkUI_FontWeightConfigs OH_ArkUI_FontWeightConfigs
```

## Overview

Defines the font weight configurations of text. It is suitable for scenarios that require precise control over text font weight or where the text font weight needs to follow device font setting changes. You can create a text font weight configuration object through {@link OH_ArkUI_FontWeightConfigs_Create}, and must call<br>{@link OH_ArkUI_FontWeightConfigs_Destroy} to destroy the object and release resources after use to avoid memory<br>leaks. After the configuration object is created, you can set and query the information through the following APIs:<br>use {@link OH_ArkUI_FontWeightConfigs_SetEnableVariableFontWeight} to set whether to enable variable font weight<br>adjustment, use {@link OH_ArkUI_FontWeightConfigs_GetEnableVariableFontWeight} to check whether variable font weight<br>adjustment is enabled, use {@link OH_ArkUI_FontWeightConfigs_SetEnableDeviceFontWeightCategory} to set whether the<br>text font weight is updated with the font weight level of the device, and use<br>{@link OH_ArkUI_FontWeightConfigs_GetEnableDeviceFontWeightCategory} to check whether the text font weight is updated with the font weight level of the device. When this configuration object is used and is not a null pointer, if the user does not explicitly make the configuration through the APIs, each configuration item uses its default value (variable font weight adjustment is disabled by default, and text font weight is updated with the font weight level of the device by default). When this configuration object is a null pointer, the default values are not used, and the text font weight behavior is the same as that of the parent component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 24

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [text.h](capi-text-h.md)

