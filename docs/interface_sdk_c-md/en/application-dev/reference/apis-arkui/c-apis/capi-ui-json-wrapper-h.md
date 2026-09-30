# ui_json_wrapper.h

## Overview

Declares the shared JSON data object for the UI perception and control APIs.

**Include**: <arkui/ui_json_wrapper.h>

**Library**: libace_ndk.z.so

**Since**: 26.2.0

**Related module**: [ArkUI_NativeModule](capi-arkui-nativemodule.md)

## Summary

### Struct

| Name | typedef keyword | Description |
| -- | -- | -- |
| [OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) | OH_ArkUI_NativeModule_UIJsonWrapper | Defines an opaque, immutable JSON data object.<br> The object holds a JSON string. It is used both to carry data delivered by the framework (UI sensing) and to carry commands submitted by the application (UI control). |

### Enum

| Name | typedef keyword | Description |
| -- | -- | -- |
| [OH_ArkUI_NativeModule_UIJsonFormat](#oh_arkui_nativemodule_uijsonformat) | OH_ArkUI_NativeModule_UIJsonFormat | Enumerated type of the JSON output format. |

### Function

| Name | Description |
| -- | -- |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIJsonWrapperCreate(const char *data, uint32_t size, OH_ArkUI_NativeModule_UIJsonWrapper **outOwned)](#oh_arkui_nativemodule_uijsonwrappercreate) | Creates a JSON data object from a caller-provided JSON string.<br> The provided string is copied into the object. The caller owns the created object and must release it with [OH_ArkUI_NativeModule_UIJsonWrapperDestroy](capi-ui-json-wrapper-h.md#oh_arkui_nativemodule_uijsonwrapperdestroy) when it is no longer needed.<br> The provided string should contain a schemaVersion field. If it is absent, or the specified version value is outside the supported range, it is treated as 1, as follows: { "schemaVersion": 1, ... }<br> Note: the data string passed to this function remains owned by the caller. Destroying the JSON wrapper object returned by this API does not release the memory pointed to by data on the caller's behalf. |
| [const char *OH_ArkUI_NativeModule_UIJsonWrapperGetData(const OH_ArkUI_NativeModule_UIJsonWrapper *json)](#oh_arkui_nativemodule_uijsonwrappergetdata) | Obtains the JSON string held by the object.<br> The returned string is read-only and null-terminated. It points to memory owned by the JSON object and remains valid until the object is destroyed. The caller must not modify or free the returned string. |
| [uint32_t OH_ArkUI_NativeModule_UIJsonWrapperGetSize(const OH_ArkUI_NativeModule_UIJsonWrapper *json)](#oh_arkui_nativemodule_uijsonwrappergetsize) | Obtains the byte length of the JSON string.<br> The returned length excludes the terminating null character. For an empty JSON string, zero is returned. |
| [void OH_ArkUI_NativeModule_UIJsonWrapperDestroy(OH_ArkUI_NativeModule_UIJsonWrapper *json)](#oh_arkui_nativemodule_uijsonwrapperdestroy) | Destroys a JSON data object and releases its resources.<br> Passing null has no effect. Any pointer returned by OH_ArkUI_NativeModule_UIJsonWrapper_GetData becomes invalid after this call.<br> Note: call this function only on a JSON wrapper object whose ownership you explicitly hold, for example, a wrapper created with OH_ArkUI_NativeModule_UIJsonWrapper_Create, or a wrapper whose ownership you have explicitly obtained through an ownership transfer function. Do not use this function to release JSON wrapper objects that are constructed and handed out by the system, for example, the object delivered through [OH_ArkUI_NativeModule_UIInfoCollectionInteractionJsonCallback](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiinfocollectioninteractionjsoncallback). |

## Enum type description

### OH_ArkUI_NativeModule_UIJsonFormat

```c
enum OH_ArkUI_NativeModule_UIJsonFormat
```

**Description**

Enumerated type of the JSON output format.

**Since**: 26.2.0

| Enum item | Description |
| -- | -- |
| OH_ARKUI_NATIVE_MODULE_UI_JSON_COMPACT = 0 | Produces canonical JSON without unnecessary whitespace.<br>**Since**: 26.2.0 |
| OH_ARKUI_NATIVE_MODULE_UI_JSON_PRETTY = 1 | Generates JSON with double-space indentation and line breaks.<br>**Since**: 26.2.0 |


## Function description

### OH_ArkUI_NativeModule_UIJsonWrapperCreate()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIJsonWrapperCreate(const char *data, uint32_t size, OH_ArkUI_NativeModule_UIJsonWrapper **outOwned)
```

**Description**

Creates a JSON data object from a caller-provided JSON string.<br> The provided string is copied into the object. The caller owns the created object and must release it with [OH_ArkUI_NativeModule_UIJsonWrapperDestroy](capi-ui-json-wrapper-h.md#oh_arkui_nativemodule_uijsonwrapperdestroy) when it is no longer needed.<br> The provided string should contain a schemaVersion field. If it is absent, or the specified version value is outside the supported range, it is treated as 1, as follows: { "schemaVersion": 1, ... }<br> Note: the data string passed to this function remains owned by the caller. Destroying the JSON wrapper object returned by this API does not release the memory pointed to by data on the caller's behalf.

**Since**: 26.2.0

**Resource release**: ui_json_wrapper/OH_ArkUI_NativeModule_UIJsonWrapperDestroy {outOwned}

**Parameters**:

| Parameter | Description |
| -- | -- |
| const char *data | [in] Pointer to the JSON string. It must not be null and must remain valid for the duration of the call. The callee does not retain it. An empty string is valid and corresponds to a size of 0. |
| uint32_t size | [in] Byte length (in bytes) of the JSON string, excluding the terminating null character. It must equal the actual length of data. If size is inconsistent with the actual string length, ARKUI_ERROR_CODE_PARAM_INVALID is returned. |
| [OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) **outOwned | [out] Receives the created object on success. The caller owns the returned object and must release it with [OH_ArkUI_NativeModule_UIJsonWrapperDestroy](capi-ui-json-wrapper-h.md#oh_arkui_nativemodule_uijsonwrapperdestroy). It must not be null, requires no initialization, and on failure is set to null. |

**Returns**:

| Type | Description |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR if the operation is successful.</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID if a parameter is invalid.</li> </ul> |

### OH_ArkUI_NativeModule_UIJsonWrapperGetData()

```c
const char *OH_ArkUI_NativeModule_UIJsonWrapperGetData(const OH_ArkUI_NativeModule_UIJsonWrapper *json)
```

**Description**

Obtains the JSON string held by the object.<br> The returned string is read-only and null-terminated. It points to memory owned by the JSON object and remains valid until the object is destroyed. The caller must not modify or free the returned string.

**Since**: 26.2.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [const OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) *json | [in] The JSON data object. It must not be null. |

**Returns**:

| Type | Description |
| -- | -- |
| const char * | The borrowed JSON string, or null if json is null. |

### OH_ArkUI_NativeModule_UIJsonWrapperGetSize()

```c
uint32_t OH_ArkUI_NativeModule_UIJsonWrapperGetSize(const OH_ArkUI_NativeModule_UIJsonWrapper *json)
```

**Description**

Obtains the byte length of the JSON string.<br> The returned length excludes the terminating null character. For an empty JSON string, zero is returned.

**Since**: 26.2.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [const OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) *json | [in] The JSON data object. It must not be null. |

**Returns**:

| Type | Description |
| -- | -- |
| uint32_t | <ul> <li>The byte length of the JSON string, excluding the terminating null character.</li> <li>Returns 0 for an empty JSON string.</li> </ul> |

### OH_ArkUI_NativeModule_UIJsonWrapperDestroy()

```c
void OH_ArkUI_NativeModule_UIJsonWrapperDestroy(OH_ArkUI_NativeModule_UIJsonWrapper *json)
```

**Description**

Destroys a JSON data object and releases its resources.<br> Passing null has no effect. Any pointer returned by OH_ArkUI_NativeModule_UIJsonWrapper_GetData becomes invalid after this call.<br> Note: call this function only on a JSON wrapper object whose ownership you explicitly hold, for example, a wrapper created with OH_ArkUI_NativeModule_UIJsonWrapper_Create, or a wrapper whose ownership you have explicitly obtained through an ownership transfer function. Do not use this function to release JSON wrapper objects that are constructed and handed out by the system, for example, the object delivered through [OH_ArkUI_NativeModule_UIInfoCollectionInteractionJsonCallback](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiinfocollectioninteractionjsoncallback).

**Since**: 26.2.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) *json | [in] The JSON data object to destroy. |


