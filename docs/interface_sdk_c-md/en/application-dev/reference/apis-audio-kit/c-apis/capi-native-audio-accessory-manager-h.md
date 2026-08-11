# native_audio_accessory_manager.h

## Overview

Declare audio accessory manager related interfaces.

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 26.0.0

**Related module**: [OHAudio](capi-ohaudio.md)

## Summary

### Function

| Name | typedef keyword | Description |
| -- | -- | -- |
| [typedef bool (\*OH_AudioAccessory_SetNoiseReductionCallback)(OH_AudioAccessory *accessory, OH_AudioNoiseReductionMode mode)](#oh_audioaccessory_setnoisereductioncallback) | OH_AudioAccessory_SetNoiseReductionCallback | Callback for noise reduction mode change on an accessory.<b>When Called:</b> When the system requests a change to the noisereduction mode on the accessory. This callback may be called at any timeafter the accessory is connected. |
| [OH_AudioCommon_Result OH_AudioManager_GetAccessoryManager(OH_AudioAccessoryManager **outManager)](#oh_audiomanager_getaccessorymanager) | - | Obtains the audio accessory manager instance. |
| [OH_AudioCommon_Result OH_AudioAccessoryManager_CreateInput(OH_AudioAccessoryManager *manager, const OH_AudioAccessoryInfo *info, const OH_AudioAccessoryCapabilities *capabilities, OH_AudioAccessory_OpenInputStreamCallback openInputStream, OH_AudioAccessory **outOwnedAccessory)](#oh_audioaccessorymanager_createinput) | - | Creates an input audio accessory instance and registers its capabilities.This function creates only the audio accessory instance. It does not createany input stream immediately.The framework performs a deep copy of the accessoryName, manufacturer,modelNumber, and macAddress fields. The caller may free these buffersafter this function returns.The framework also performs a deep copy of the streamProperties arrayin capabilities. The caller may free this array after this function returns.On success, the framework allocates an [OH_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) handle andreturns it through accessory pointer.Input streams are created lazily by the framework when an applicationactually starts recording from this accessory. At that time, the frameworkcreates a new [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) handle and invokesopen stream. The callback receives the newly created stream handleand the requested stream information, and is where the caller must registerthe required stream callbacks.The stream handle is managed by the framework and must not be released bythe caller. A stream remains valid until the framework invokes[OH_AudioAccessoryInputStream_ReleaseCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstream_releasecallback) for that stream. Afterthe release callback returns, the stream handle becomes invalid and must notbe used again. During the lifetime of one accessory handle, input streamsmay be created and released multiple times. |
| [OH_AudioCommon_Result OH_AudioAccessoryManager_SetAssociatedMacAddresses(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory, const char **macAddresses, uint32_t count)](#oh_audioaccessorymanager_setassociatedmacaddresses) | - | Sets the list of associated MAC addresses for the audio accessory.This interface replaces the existing list of associated MAC addresseslinked to the accessory instance. It is designed for multi-transmitterscenarios (e.g., 1-to-2, 1-to-4 systems) where the group of connectedtransmitters may change dynamically.Call this after the accessory is createdto report all currently active transmitters associated with the primary MAC.If a transmitter is replaced or disconnected, call this again with theupdated list to overwrite the previous state. Safe to call during an activerecording session. |
| [OH_AudioCommon_Result OH_AudioAccessoryManager_RegisterNoiseReductionCapability(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory, const OH_AudioAccessoryNoiseReductionCapability *capability, OH_AudioAccessory_SetNoiseReductionCallback onNoiseReduction)](#oh_audioaccessorymanager_registernoisereductioncapability) | - | Registers the noise reduction capability of an audio accessory.The framework performs a deep copy of the supportedModes array and otherfields in the capability structure. The caller may free the capabilitystructure and the supportedModes array after this function returns. |
| [OH_AudioCommon_Result OH_AudioAccessoryManager_SetNoiseReductionMode(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory, OH_AudioNoiseReductionMode mode)](#oh_audioaccessorymanager_setnoisereductionmode) | - | Sets the noise reduction mode of an audio accessory.This function allows the accessory service to actively synchronize thecurrent noise reduction mode to the framework. It is typically used whenthe mode is changed through other means (e.g., hardware buttons or acompanion app), ensuring the framework stays updated with the accessory'sactual state. |
| [OH_AudioCommon_Result OH_AudioAccessoryManager_Connected(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory)](#oh_audioaccessorymanager_connected) | - | Connects the audio accessory to the audio framework.All required capabilities must be registered before calling this function.<b>Recommendation:</b> It is recommended that third-party audio accessoriesprioritize integration with the Smart Life app. This ensures a consistentuser experience for device discovery and connection, allowing the accessoryservice to avoid direct permission management. |
| [OH_AudioCommon_Result OH_AudioAccessoryManager_Disconnected(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory)](#oh_audioaccessorymanager_disconnected) | - | Disconnects the audio accessory from the audio framework. |
| [OH_AudioCommon_Result OH_AudioAccessoryManager_Destroy(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory)](#oh_audioaccessorymanager_destroy) | - | Destroys the audio accessory instance.The accessory must be disconnected before destroying. |

## Function description

### OH_AudioAccessory_SetNoiseReductionCallback()

```c
typedef bool (*OH_AudioAccessory_SetNoiseReductionCallback)(OH_AudioAccessory *accessory, OH_AudioNoiseReductionMode mode)
```

**Description**

Callback for noise reduction mode change on an accessory.<b>When Called:</b> When the system requests a change to the noisereduction mode on the accessory. This callback may be called at any timeafter the accessory is connected.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| (OH_AudioAccessory \*accessory | [in] The audio accessory. |
| OH_AudioNoiseReductionMode mode | [in] The noise reduction mode to set on the accessory. |

**Returns**:

| Type | Description |
| -- | -- |
| bool | <ul><br>         <li>`true` if the requested mode is handled successfully.</li><br>         <li>`false` otherwise.</li><br>         </ul> |

### OH_AudioManager_GetAccessoryManager()

```c
OH_AudioCommon_Result OH_AudioManager_GetAccessoryManager(OH_AudioAccessoryManager **outManager)
```

**Description**

Obtains the audio accessory manager instance.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) **outManager | [out] Returns a pointer to the manager handle.Note that the handle is managed by the system and must not be releasedby the caller, otherwise an exception may occur. |

**Returns**:

| Type | Description |
| -- | -- |
| OH_AudioCommon_Result | <ul><br>         <li>{@link AUDIOCOMMON_RESULT_SUCCESS} if execution succeeds.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM} if manager is null.</li><br>         </ul> |

### OH_AudioAccessoryManager_CreateInput()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_CreateInput(OH_AudioAccessoryManager *manager, const OH_AudioAccessoryInfo *info, const OH_AudioAccessoryCapabilities *capabilities, OH_AudioAccessory_OpenInputStreamCallback openInputStream, OH_AudioAccessory **outOwnedAccessory)
```

**Description**

Creates an input audio accessory instance and registers its capabilities.This function creates only the audio accessory instance. It does not createany input stream immediately.The framework performs a deep copy of the accessoryName, manufacturer,modelNumber, and macAddress fields. The caller may free these buffersafter this function returns.The framework also performs a deep copy of the streamProperties arrayin capabilities. The caller may free this array after this function returns.On success, the framework allocates an [OH_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) handle andreturns it through accessory pointer.Input streams are created lazily by the framework when an applicationactually starts recording from this accessory. At that time, the frameworkcreates a new [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) handle and invokesopen stream. The callback receives the newly created stream handleand the requested stream information, and is where the caller must registerthe required stream callbacks.The stream handle is managed by the framework and must not be released bythe caller. A stream remains valid until the framework invokes[OH_AudioAccessoryInputStream_ReleaseCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstream_releasecallback) for that stream. Afterthe release callback returns, the stream handle becomes invalid and must notbe used again. During the lifetime of one accessory handle, input streamsmay be created and released multiple times.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) *manager | [in] Pointer to the audio accessory manager. |
| [const OH_AudioAccessoryInfo](capi-ohaudio-oh-audioaccessoryinfo.md) *info | [in] Pointer to the accessory basic information. Must not be null. |
| [const OH_AudioAccessoryCapabilities](capi-ohaudio-oh-audioaccessorycapabilities.md) *capabilities | [in] Pointer to the accessory capabilities. Must not be null. |
| [OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback) openInputStream | [in] Callback invoked when the framework opens an input stream.Must not be null. The callback is invoked only when the framework createsa stream for this accessory, not when this function is called. |
| [OH_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) **outOwnedAccessory | [out] Returns the created accessory handle. |

**Returns**:

| Type | Description |
| -- | -- |
| OH_AudioCommon_Result | <ul><br>         <li>{@link AUDIOCOMMON_RESULT_SUCCESS} if execution succeeds.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM} if any parameter is null.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE} if the manager is not initialized.</li><br>         </ul> |

### OH_AudioAccessoryManager_SetAssociatedMacAddresses()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_SetAssociatedMacAddresses(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory, const char **macAddresses, uint32_t count)
```

**Description**

Sets the list of associated MAC addresses for the audio accessory.This interface replaces the existing list of associated MAC addresseslinked to the accessory instance. It is designed for multi-transmitterscenarios (e.g., 1-to-2, 1-to-4 systems) where the group of connectedtransmitters may change dynamically.Call this after the accessory is createdto report all currently active transmitters associated with the primary MAC.If a transmitter is replaced or disconnected, call this again with theupdated list to overwrite the previous state. Safe to call during an activerecording session.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) *manager | [in] Pointer to the audio accessory manager. |
| [OH_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) *accessory | [in] Pointer to the accessory handle. |
| const char **macAddresses | [in] Array of MAC addresses to associate.<b>Can be null if count is 0</b>, indicating that all associated MAC addressesshould be cleared (e.g., when all secondary transmitters disconnect).If not null, the framework performs a deep copy of these strings.Each element must conform to the following rules:- Must be a NUL-terminated ASCII string in colon-separated hexadecimalnotation, e.g. "00:11:22:33:44:55". Both upper-case and lower-casehex digits (A-F / a-f) are accepted.- Must be a non-null, non-empty string.- Duplicate addresses within the same array are ignored; only the firstoccurrence of each unique address takes effect. |
| uint32_t count | [in] Number of MAC addresses in the array. |

**Returns**:

| Type | Description |
| -- | -- |
| OH_AudioCommon_Result | <ul><br>         <li>{@link AUDIOCOMMON_RESULT_SUCCESS} if execution succeeds.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM} if parameters are invalid.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE} if the accessory is not created.</li><br>         </ul> |

### OH_AudioAccessoryManager_RegisterNoiseReductionCapability()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_RegisterNoiseReductionCapability(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory, const OH_AudioAccessoryNoiseReductionCapability *capability, OH_AudioAccessory_SetNoiseReductionCallback onNoiseReduction)
```

**Description**

Registers the noise reduction capability of an audio accessory.The framework performs a deep copy of the supportedModes array and otherfields in the capability structure. The caller may free the capabilitystructure and the supportedModes array after this function returns.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) *manager | [in] Pointer to the audio accessory manager. |
| [OH_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) *accessory | [in] Pointer to the accessory handle created by CreateInput. |
| [const OH_AudioAccessoryNoiseReductionCapability](capi-ohaudio-oh-audioaccessorynoisereductioncapability.md) *capability | [in] Pointer to the noise reduction capability. Must not be null. |
| [OH_AudioAccessory_SetNoiseReductionCallback](capi-native-audio-accessory-manager-h.md#oh_audioaccessory_setnoisereductioncallback) onNoiseReduction | [in] Callback invoked when the frameworkrequests a noise reduction mode change. May be null if the accessorydoes not support dynamic mode switching. If provided, the callback mustreturn `true` on success and `false` on failure. |

**Returns**:

| Type | Description |
| -- | -- |
| OH_AudioCommon_Result | <ul><br>         <li>{@link AUDIOCOMMON_RESULT_SUCCESS} if execution succeeds.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM} if parameters are invalid.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE} if the accessory is not created.</li><br>         </ul> |

### OH_AudioAccessoryManager_SetNoiseReductionMode()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_SetNoiseReductionMode(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory, OH_AudioNoiseReductionMode mode)
```

**Description**

Sets the noise reduction mode of an audio accessory.This function allows the accessory service to actively synchronize thecurrent noise reduction mode to the framework. It is typically used whenthe mode is changed through other means (e.g., hardware buttons or acompanion app), ensuring the framework stays updated with the accessory'sactual state.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) *manager | [in] Pointer to the audio accessory manager. |
| [OH_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) *accessory | [in] Pointer to the accessory handle. |
| OH_AudioNoiseReductionMode mode | [in] The noise reduction mode to set. Must be one of the modesregistered via RegisterNoiseReductionCapability. |

**Returns**:

| Type | Description |
| -- | -- |
| OH_AudioCommon_Result | <ul><br>         <li>{@link AUDIOCOMMON_RESULT_SUCCESS} if execution succeeds.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM} if parameters are invalid.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE} if the accessory is not connected.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_UNSUPPORTED} if the mode is not supported.</li><br>         </ul> |

### OH_AudioAccessoryManager_Connected()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_Connected(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory)
```

**Description**

Connects the audio accessory to the audio framework.All required capabilities must be registered before calling this function.<b>Recommendation:</b> It is recommended that third-party audio accessoriesprioritize integration with the Smart Life app. This ensures a consistentuser experience for device discovery and connection, allowing the accessoryservice to avoid direct permission management.

**Required permission**: ohos.permission.MANAGE_AUDIO_ACCESSORY

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) *manager | [in] Pointer to the audio accessory manager. |
| [OH_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) *accessory | [in] Pointer to the accessory handle to connect. |

**Returns**:

| Type | Description |
| -- | -- |
| OH_AudioCommon_Result | <ul><br>         <li>{@link AUDIOCOMMON_RESULT_SUCCESS} if execution succeeds.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_PERMISSION_DENIED} if the caller does not have the<br>                  required permission.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM} if accessory is null.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE} if capabilities are not registered or<br>                  the accessory is already connected.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_SYSTEM} if audio server process die.</li><br>         </ul> |

### OH_AudioAccessoryManager_Disconnected()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_Disconnected(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory)
```

**Description**

Disconnects the audio accessory from the audio framework.

**Required permission**: ohos.permission.MANAGE_AUDIO_ACCESSORY

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) *manager | [in] Pointer to the audio accessory manager. |
| [OH_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) *accessory | [in] Pointer to the accessory handle to disconnect. |

**Returns**:

| Type | Description |
| -- | -- |
| OH_AudioCommon_Result | <ul><br>         <li>{@link AUDIOCOMMON_RESULT_SUCCESS} if execution succeeds.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_PERMISSION_DENIED} if the caller does not have the<br>                  required permission.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM} if accessory is null.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE} if the accessory is not connected.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_SYSTEM} if audio server process die.</li><br>         </ul> |

### OH_AudioAccessoryManager_Destroy()

```c
OH_AudioCommon_Result OH_AudioAccessoryManager_Destroy(OH_AudioAccessoryManager *manager, OH_AudioAccessory *accessory)
```

**Description**

Destroys the audio accessory instance.The accessory must be disconnected before destroying.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryManager](capi-ohaudio-oh-audioaccessorymanager.md) *manager | [in] Pointer to the audio accessory manager. |
| [OH_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) *accessory | [in] Pointer to the accessory handle to destroy. |

**Returns**:

| Type | Description |
| -- | -- |
| OH_AudioCommon_Result | <ul><br>         <li>{@link AUDIOCOMMON_RESULT_SUCCESS} if execution succeeds.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM} if accessory is null.</li><br>         <li>{@link AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE} if the accessory is still connected.</li><br>         </ul> |


