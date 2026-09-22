# OH_ArkUI_FontConfigs

```c
typedef struct OH_ArkUI_FontConfigs OH_ArkUI_FontConfigs
```

## Overview

Defines the font configurations of text. Currently, it supports setting and obtaining the font weight configuration through related APIs, and is applicable to scenarios that require custom font weight display effects. You can create a font configuration object through the {@link OH_ArkUI_FontConfigs_Create} API and destroy it<br>through the {@link OH_ArkUI_FontConfigs_Destroy} API. After the configurations are created, you can set and query<br>them through the following APIs: set the font weight configuration through the<br>{@link OH_ArkUI_FontConfigs_SetFontWeightConfigs} API, and obtain the font weight configuration through the<br>{@link OH_ArkUI_FontConfigs_GetFontWeightConfigs} API.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 24

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

**Header file**: [text.h](capi-text-h.md)

