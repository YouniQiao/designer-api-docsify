# oh_swapfs.h

## Overview

Defines the native APIs for swapfs.

**Library**: libohswapfs.so

**System capability**: SystemCapability.FileManagement.File.Swapfs

**Since**: 26.0.0

**Related module**: [Swapfs](capi-swapfs.md)

## Summary

### Struct

| Name | typedef keyword | Description |
| -- | -- | -- |
| [OH_SwapfsConfig](capi-swapfs-oh-swapfsconfig.md) | OH_SwapfsConfig | Configuration for creating a swapfs manager. |
| [OH_SwapfsSwapOutRequest](capi-swapfs-oh-swapfsswapoutrequest.md) | OH_SwapfsSwapOutRequest | Request parameters for swap-out operation. |
| [OH_SwapfsSwapInRequest](capi-swapfs-oh-swapfsswapinrequest.md) | OH_SwapfsSwapInRequest | Request parameters for swap-in operation. |
| [OH_SwapfsDataInfo](capi-swapfs-oh-swapfsdatainfo.md) | OH_SwapfsDataInfo | Information about a single swap key. |
| [OH_SwapfsStats](capi-swapfs-oh-swapfsstats.md) | OH_SwapfsStats | Statistics of the current swapfs manager. |
| [OH_SwapfsManager](capi-swapfs-oh-swapfsmanager.md) | OH_SwapfsManager | The struct is used to perform operations related to swapfs manager. |

### Enum

| Name | typedef keyword | Description |
| -- | -- | -- |
| [OH_SwapfsKeyStatus](#oh_swapfskeystatus) | OH_SwapfsKeyStatus | Defines the status of a swap key. |
| [OH_SwapfsDisableReason](#oh_swapfsdisablereason) | OH_SwapfsDisableReason | Defines the reason why the swap-out feature is disabled. |

### Macro

| Name | Description |
| -- | -- |
| SWAPFS_DIO_ALIGNMENT 4096U | Minimum alignment requirement for Direct IO buffers.<br>**Since**: 26.0.0 |

### Function

| Name | Description |
| -- | -- |
| [OH_Swapfs_ErrCode OH_Swapfs_CreateManager(const OH_SwapfsConfig *config, OH_SwapfsManager **manager)](#oh_swapfs_createmanager) | Creates a swapfs manager. |
| [OH_Swapfs_ErrCode OH_Swapfs_DestroyManager(OH_SwapfsManager *manager)](#oh_swapfs_destroymanager) | Destroys a swapfs manager and releases all resources.This function enters the shutting-down state and rejects new swap-out, swap-in, remove,and remove-all operations. It waits up to 5 seconds for active operations to complete.If all operations complete within the timeout, all swap data owned by the manager isautomatically removed and the manager is destroyed. If the wait times out, this functioncancels the shutting-down state and returns SWAPFS_E_BUSY; the caller can retry later. |
| [OH_Swapfs_ErrCode OH_Swapfs_SwapOut(OH_SwapfsManager *manager, const OH_SwapfsSwapOutRequest *request, uint64_t *keyId)](#oh_swapfs_swapout) | Swaps out data from memory to disk.When config.useDirectIo is false, buffered IO is used. When true, Direct IO is requiredand misaligned buffers cause an error. In DIO mode, the swap file size is padded toSWAPFS_DIO_ALIGNMENT (occupiedSize is greater than or equal to dataSize). |
| [OH_Swapfs_ErrCode OH_Swapfs_SwapIn(OH_SwapfsManager *manager, const OH_SwapfsSwapInRequest *request, uint64_t *readSize)](#oh_swapfs_swapin) | Swaps in data from disk back to memory.In DIO mode, the buffer address and size must be aligned to SWAPFS_DIO_ALIGNMENT, andbufferSize must be greater than or equal to occupiedSize. In buffered mode, bufferSizemust be greater than or equal to dataSize. On success, readSize receives the originaldataSize (not occupiedSize). |
| [OH_Swapfs_ErrCode OH_Swapfs_QueryData(OH_SwapfsManager *manager, uint64_t keyId, OH_SwapfsDataInfo *info)](#oh_swapfs_querydata) | Queries information about a specific swap key. |
| [OH_Swapfs_ErrCode OH_Swapfs_GetStats(OH_SwapfsManager *manager, OH_SwapfsStats *stats)](#oh_swapfs_getstats) | Obtains statistics of the current swapfs manager. |
| [OH_Swapfs_ErrCode OH_Swapfs_RemoveData(OH_SwapfsManager *manager, uint64_t keyId)](#oh_swapfs_removedata) | Logically deletes a specific swap key.The key is marked as REMOVING state immediately. Existing swap-in operations can still complete.New swap-in or query operations on this key will return SWAPFS_E_KEY_STATE_INVALID.This function does not return SWAPFS_E_BUSY for concurrent swap-in operations. |
| [OH_Swapfs_ErrCode OH_Swapfs_RemoveAllData(OH_SwapfsManager *manager)](#oh_swapfs_removealldata) | Removes all swap keys in the manager.If there are active operations in progress (swap-out or swap-in), or any key is in REMOVINGstate, this function returns SWAPFS_E_BUSY without starting any removal. |

## Enum type description

### OH_SwapfsKeyStatus

```c
enum OH_SwapfsKeyStatus
```

**Description**

Defines the status of a swap key.

**Since**: 26.0.0

| Enum item | Description |
| -- | -- |
| OH_SWAPFS_KEY_STATUS_ACTIVE = 0 | The key is active and available for swap-in, query, or removal.<br>**Since**: 26.0.0 |
| OH_SWAPFS_KEY_STATUS_REMOVING = 1 | The key is logically deleted. New swap-in or query operations will be rejected.<br>**Since**: 26.0.0 |

### OH_SwapfsDisableReason

```c
enum OH_SwapfsDisableReason
```

**Description**

Defines the reason why the swap-out feature is disabled.

**Since**: 26.0.0

| Enum item | Description |
| -- | -- |
| OH_SWAPFS_DISABLE_REASON_NONE = 0 | The feature is enabled (no disable reason).<br>**Since**: 26.0.0 |
| OH_SWAPFS_DISABLE_REASON_NOSPC = 1 | Device storage space is insufficient.<br>**Since**: 26.0.0 |


## Function description

### OH_Swapfs_CreateManager()

```c
OH_Swapfs_ErrCode OH_Swapfs_CreateManager(const OH_SwapfsConfig *config, OH_SwapfsManager **manager)
```

**Description**

Creates a swapfs manager.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [const OH_SwapfsConfig](capi-swapfs-oh-swapfsconfig.md) *config | [in] Pointer to the configuration, or NULL to use the default configuration(default temporary directory, 1GB limit, useDirectIo=false). |
| [OH_SwapfsManager](capi-swapfs-oh-swapfsmanager.md) **manager | [out] Double pointer to receive the created OH_SwapfsManager handle.Must not be NULL. On failure, the pointed value is set to NULL. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_Swapfs_ErrCode](capi-swapfs-errcode-h.md#oh_swapfs_errcode) | Returns the error code of the execution.<br>         <ul><br>         <li>[SWAPFS_E_OK](capi-swapfs-errcode-h.md#oh_swapfs_errcode) if the execution is successful.</li><br>         <li>[SWAPFS_E_INVAL](capi-swapfs-errcode-h.md#oh_swapfs_errcode) manager is nullptr.</li><br>         <li>[SWAPFS_E_NOMEM](capi-swapfs-errcode-h.md#oh_swapfs_errcode) memory allocation failed.</li><br>         <li>[SWAPFS_E_ACCES](capi-swapfs-errcode-h.md#oh_swapfs_errcode) permission denied for the swap root path.</li><br>         <li>[SWAPFS_E_PATH_UNAVAILABLE](capi-swapfs-errcode-h.md#oh_swapfs_errcode) swap root path cannot be created.</li><br>         <li>202 if a non-system application calls this system API.</li><br>         </ul> |

### OH_Swapfs_DestroyManager()

```c
OH_Swapfs_ErrCode OH_Swapfs_DestroyManager(OH_SwapfsManager *manager)
```

**Description**

Destroys a swapfs manager and releases all resources.This function enters the shutting-down state and rejects new swap-out, swap-in, remove,and remove-all operations. It waits up to 5 seconds for active operations to complete.If all operations complete within the timeout, all swap data owned by the manager isautomatically removed and the manager is destroyed. If the wait times out, this functioncancels the shutting-down state and returns SWAPFS_E_BUSY; the caller can retry later.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_SwapfsManager](capi-swapfs-oh-swapfsmanager.md) *manager | [in] Pointer to the OH_SwapfsManager object to destroy. Must not be NULL. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_Swapfs_ErrCode](capi-swapfs-errcode-h.md#oh_swapfs_errcode) | Returns the error code of the execution.<br>         <ul><br>         <li>[SWAPFS_E_OK](capi-swapfs-errcode-h.md#oh_swapfs_errcode) if the execution is successful.</li><br>         <li>[SWAPFS_E_INVAL](capi-swapfs-errcode-h.md#oh_swapfs_errcode) manager is nullptr.</li><br>         <li>[SWAPFS_E_BUSY](capi-swapfs-errcode-h.md#oh_swapfs_errcode) there are active operations in progress.</li><br>         <li>202 if a non-system application calls this system API.</li><br>         </ul> |

### OH_Swapfs_SwapOut()

```c
OH_Swapfs_ErrCode OH_Swapfs_SwapOut(OH_SwapfsManager *manager, const OH_SwapfsSwapOutRequest *request, uint64_t *keyId)
```

**Description**

Swaps out data from memory to disk.When config.useDirectIo is false, buffered IO is used. When true, Direct IO is requiredand misaligned buffers cause an error. In DIO mode, the swap file size is padded toSWAPFS_DIO_ALIGNMENT (occupiedSize is greater than or equal to dataSize).

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_SwapfsManager](capi-swapfs-oh-swapfsmanager.md) *manager | [in] Pointer to the OH_SwapfsManager object. Must not be NULL. |
| [const OH_SwapfsSwapOutRequest](capi-swapfs-oh-swapfsswapoutrequest.md) *request | [in] Pointer to the swap-out request containing the data buffer and its size.Must not be NULL. |
| uint64_t *keyId | [out] Pointer to receive the generated keyId for this swap data. Must not be NULL.On failure, the pointed value is unchanged. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_Swapfs_ErrCode](capi-swapfs-errcode-h.md#oh_swapfs_errcode) | Returns the error code of the execution.<br>         <ul><br>         <li>[SWAPFS_E_OK](capi-swapfs-errcode-h.md#oh_swapfs_errcode) if the execution is successful.</li><br>         <li>[SWAPFS_E_INVAL](capi-swapfs-errcode-h.md#oh_swapfs_errcode) manager is nullptr, request is nullptr, keyId is nullptr,<br>             buffer is nullptr, or bufferSize is 0.</li><br>         <li>[SWAPFS_E_DIO_ALIGN](capi-swapfs-errcode-h.md#oh_swapfs_errcode) useDirectIo is true and buffer is not aligned.</li><br>         <li>[SWAPFS_E_NOSPC](capi-swapfs-errcode-h.md#oh_swapfs_errcode) insufficient device storage space.</li><br>         <li>[SWAPFS_E_QUOTA_EXCEEDED](capi-swapfs-errcode-h.md#oh_swapfs_errcode) swap space quota exceeded.</li><br>         <li>[SWAPFS_E_FEATURE_DISABLED](capi-swapfs-errcode-h.md#oh_swapfs_errcode) swap-out is disabled due to low space or policy.</li><br>         <li>[SWAPFS_E_IO_ERROR](capi-swapfs-errcode-h.md#oh_swapfs_errcode) IO write failure.</li><br>         <li>[SWAPFS_E_NOMEM](capi-swapfs-errcode-h.md#oh_swapfs_errcode) memory allocation failed.</li><br>         <li>[SWAPFS_E_ACCES](capi-swapfs-errcode-h.md#oh_swapfs_errcode) permission denied.</li><br>         <li>[SWAPFS_E_BUSY](capi-swapfs-errcode-h.md#oh_swapfs_errcode) RemoveAllData is in progress or too many concurrent operations.</li><br>         <li>[SWAPFS_E_SHUTTING_DOWN](capi-swapfs-errcode-h.md#oh_swapfs_errcode) manager is shutting down.</li><br>         <li>202 if a non-system application calls this system API.</li><br>         </ul> |

### OH_Swapfs_SwapIn()

```c
OH_Swapfs_ErrCode OH_Swapfs_SwapIn(OH_SwapfsManager *manager, const OH_SwapfsSwapInRequest *request, uint64_t *readSize)
```

**Description**

Swaps in data from disk back to memory.In DIO mode, the buffer address and size must be aligned to SWAPFS_DIO_ALIGNMENT, andbufferSize must be greater than or equal to occupiedSize. In buffered mode, bufferSizemust be greater than or equal to dataSize. On success, readSize receives the originaldataSize (not occupiedSize).

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_SwapfsManager](capi-swapfs-oh-swapfsmanager.md) *manager | [in] Pointer to the OH_SwapfsManager object. Must not be NULL. |
| [const OH_SwapfsSwapInRequest](capi-swapfs-oh-swapfsswapinrequest.md) *request | [in] Pointer to the swap-in request containing keyId, buffer, and bufferSize.Must not be NULL. |
| uint64_t *readSize | [out] Pointer to receive the original data size in bytes, or NULL if thecaller does not need it. On success, receives the original dataSize. On failure, the pointedvalue is unchanged. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_Swapfs_ErrCode](capi-swapfs-errcode-h.md#oh_swapfs_errcode) | Returns the error code of the execution.<br>         <ul><br>         <li>[SWAPFS_E_OK](capi-swapfs-errcode-h.md#oh_swapfs_errcode) if the execution is successful.</li><br>         <li>[SWAPFS_E_INVAL](capi-swapfs-errcode-h.md#oh_swapfs_errcode) manager is nullptr, request is nullptr, keyId is 0,<br>             buffer is nullptr, or bufferSize is 0.</li><br>         <li>[SWAPFS_E_DIO_ALIGN](capi-swapfs-errcode-h.md#oh_swapfs_errcode) buffer address or size is not aligned to SWAPFS_DIO_ALIGNMENT.</li><br>         <li>[SWAPFS_E_BUFFER_TOO_SMALL](capi-swapfs-errcode-h.md#oh_swapfs_errcode) bufferSize is smaller than the required size.</li><br>         <li>[SWAPFS_E_KEY_NOT_FOUND](capi-swapfs-errcode-h.md#oh_swapfs_errcode) keyId does not exist.</li><br>         <li>[SWAPFS_E_KEY_STATE_INVALID](capi-swapfs-errcode-h.md#oh_swapfs_errcode) key is in REMOVING state.</li><br>         <li>[SWAPFS_E_IO_ERROR](capi-swapfs-errcode-h.md#oh_swapfs_errcode) IO read failure.</li><br>         <li>[SWAPFS_E_NOMEM](capi-swapfs-errcode-h.md#oh_swapfs_errcode) memory allocation failed.</li><br>         <li>[SWAPFS_E_ACCES](capi-swapfs-errcode-h.md#oh_swapfs_errcode) permission denied.</li><br>         <li>[SWAPFS_E_BUSY](capi-swapfs-errcode-h.md#oh_swapfs_errcode) too many concurrent operations.</li><br>         <li>[SWAPFS_E_SHUTTING_DOWN](capi-swapfs-errcode-h.md#oh_swapfs_errcode) manager is shutting down.</li><br>         <li>202 if a non-system application calls this system API.</li><br>         </ul> |

### OH_Swapfs_QueryData()

```c
OH_Swapfs_ErrCode OH_Swapfs_QueryData(OH_SwapfsManager *manager, uint64_t keyId, OH_SwapfsDataInfo *info)
```

**Description**

Queries information about a specific swap key.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_SwapfsManager](capi-swapfs-oh-swapfsmanager.md) *manager | [in] Pointer to the OH_SwapfsManager object. Must not be NULL. |
| uint64_t keyId | [in] The keyId to query. |
| [OH_SwapfsDataInfo](capi-swapfs-oh-swapfsdatainfo.md) *info | [out] Pointer to the OH_SwapfsDataInfo structure to receive the key information.Must not be NULL. On failure, the content is unchanged. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_Swapfs_ErrCode](capi-swapfs-errcode-h.md#oh_swapfs_errcode) | Returns the error code of the execution.<br>         <ul><br>         <li>[SWAPFS_E_OK](capi-swapfs-errcode-h.md#oh_swapfs_errcode) if the execution is successful.</li><br>         <li>[SWAPFS_E_INVAL](capi-swapfs-errcode-h.md#oh_swapfs_errcode) manager is nullptr, keyId is 0, or info is nullptr.</li><br>         <li>[SWAPFS_E_KEY_NOT_FOUND](capi-swapfs-errcode-h.md#oh_swapfs_errcode) keyId does not exist.</li><br>         <li>[SWAPFS_E_KEY_STATE_INVALID](capi-swapfs-errcode-h.md#oh_swapfs_errcode) key is in REMOVING state.</li><br>         <li>202 if a non-system application calls this system API.</li><br>         </ul> |

### OH_Swapfs_GetStats()

```c
OH_Swapfs_ErrCode OH_Swapfs_GetStats(OH_SwapfsManager *manager, OH_SwapfsStats *stats)
```

**Description**

Obtains statistics of the current swapfs manager.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_SwapfsManager](capi-swapfs-oh-swapfsmanager.md) *manager | [in] Pointer to the OH_SwapfsManager object. Must not be NULL. |
| [OH_SwapfsStats](capi-swapfs-oh-swapfsstats.md) *stats | [out] Pointer to the OH_SwapfsStats structure to receive the statistics.Must not be NULL. On failure, the content is unchanged. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_Swapfs_ErrCode](capi-swapfs-errcode-h.md#oh_swapfs_errcode) | Returns the error code of the execution.<br>         <ul><br>         <li>[SWAPFS_E_OK](capi-swapfs-errcode-h.md#oh_swapfs_errcode) if the execution is successful.</li><br>         <li>[SWAPFS_E_INVAL](capi-swapfs-errcode-h.md#oh_swapfs_errcode) manager is nullptr, or stats is nullptr.</li><br>         <li>202 if a non-system application calls this system API.</li><br>         </ul> |

### OH_Swapfs_RemoveData()

```c
OH_Swapfs_ErrCode OH_Swapfs_RemoveData(OH_SwapfsManager *manager, uint64_t keyId)
```

**Description**

Logically deletes a specific swap key.The key is marked as REMOVING state immediately. Existing swap-in operations can still complete.New swap-in or query operations on this key will return SWAPFS_E_KEY_STATE_INVALID.This function does not return SWAPFS_E_BUSY for concurrent swap-in operations.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_SwapfsManager](capi-swapfs-oh-swapfsmanager.md) *manager | [in] Pointer to the OH_SwapfsManager object. Must not be NULL. |
| uint64_t keyId | [in] The keyId to remove. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_Swapfs_ErrCode](capi-swapfs-errcode-h.md#oh_swapfs_errcode) | Returns the error code of the execution.<br>         <ul><br>         <li>[SWAPFS_E_OK](capi-swapfs-errcode-h.md#oh_swapfs_errcode) if the execution is successful.</li><br>         <li>[SWAPFS_E_INVAL](capi-swapfs-errcode-h.md#oh_swapfs_errcode) manager is nullptr or keyId is 0.</li><br>         <li>[SWAPFS_E_KEY_NOT_FOUND](capi-swapfs-errcode-h.md#oh_swapfs_errcode) keyId does not exist.</li><br>         <li>[SWAPFS_E_KEY_STATE_INVALID](capi-swapfs-errcode-h.md#oh_swapfs_errcode) key is already in REMOVING state.</li><br>         <li>[SWAPFS_E_NOMEM](capi-swapfs-errcode-h.md#oh_swapfs_errcode) memory allocation failed.</li><br>         <li>[SWAPFS_E_BUSY](capi-swapfs-errcode-h.md#oh_swapfs_errcode) too many concurrent operations.</li><br>         <li>[SWAPFS_E_SHUTTING_DOWN](capi-swapfs-errcode-h.md#oh_swapfs_errcode) manager is shutting down.</li><br>         <li>202 if a non-system application calls this system API.</li><br>         </ul> |

### OH_Swapfs_RemoveAllData()

```c
OH_Swapfs_ErrCode OH_Swapfs_RemoveAllData(OH_SwapfsManager *manager)
```

**Description**

Removes all swap keys in the manager.If there are active operations in progress (swap-out or swap-in), or any key is in REMOVINGstate, this function returns SWAPFS_E_BUSY without starting any removal.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_SwapfsManager](capi-swapfs-oh-swapfsmanager.md) *manager | [in] Pointer to the OH_SwapfsManager object. Must not be NULL. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_Swapfs_ErrCode](capi-swapfs-errcode-h.md#oh_swapfs_errcode) | Returns the error code of the execution.<br>         <ul><br>         <li>[SWAPFS_E_OK](capi-swapfs-errcode-h.md#oh_swapfs_errcode) if the execution is successful.</li><br>         <li>[SWAPFS_E_INVAL](capi-swapfs-errcode-h.md#oh_swapfs_errcode) manager is nullptr.</li><br>         <li>[SWAPFS_E_NOMEM](capi-swapfs-errcode-h.md#oh_swapfs_errcode) memory allocation failed.</li><br>         <li>[SWAPFS_E_BUSY](capi-swapfs-errcode-h.md#oh_swapfs_errcode) there are active operations in progress or pending keys in REMOVING state.</li><br>         <li>[SWAPFS_E_SHUTTING_DOWN](capi-swapfs-errcode-h.md#oh_swapfs_errcode) manager is shutting down.</li><br>         <li>202 if a non-system application calls this system API.</li><br>         </ul> |


