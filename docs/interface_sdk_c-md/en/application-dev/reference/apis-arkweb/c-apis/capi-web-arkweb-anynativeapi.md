# ArkWeb_AnyNativeAPI

```c
typedef struct ArkWeb_AnyNativeAPI {...} ArkWeb_AnyNativeAPI
```

## Overview

ArkWeb_AnyNativeAPI is the basic struct type of ArkWeb Native API, used to uniformly represent pointers tovarious Native API structs obtained through the [OH_ArkWeb_GetNativeAPI](capi-arkweb-interface-h.md#oh_arkweb_getnativeapi) API. This struct contains a sizemember of the size_t type, which records the size of the current struct.

**Since**: 12

**Related module**: [Web](capi-web.md)

**Header file**: [arkweb_interface.h](capi-arkweb-interface-h.md)

## Summary

### Member variables

| Name | Description |
| -- | -- |
| size_t size | Size of the struct. |


