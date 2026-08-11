# native_audio_accessory_input_stream_manager.h

## Overview

Declare audio accessory input stream manager related interfaces.

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 26.0.0

**Related module**: [OHAudio](capi-ohaudio.md)

## Summary

### Function

| Name | typedef keyword | Description |
| -- | -- | -- |
| [typedef bool (\*OH_AudioAccessory_OpenInputStreamCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream, OH_AudioStreamInfo *streamInfo)](#oh_audioaccessory_openinputstreamcallback) | OH_AudioAccessory_OpenInputStreamCallback | Callback for opening an input stream on an audio accessory.<b>When Called:</b> The audio framework calls this callback when anapplication requests audio capture from this audio accessory.The framework passes the audio stream information of the stream beingopened, so the accessory can prepare the corresponding data path.<b>Usage Requirements:</b> In this callback, you MUST call[OH_AudioAccessoryInputStreamManager_RegisterStartCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerstartcallback),[OH_AudioAccessoryInputStreamManager_RegisterStopCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerstopcallback),[OH_AudioAccessoryInputStreamManager_RegisterReleaseCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerreleasecallback),[OH_AudioAccessoryInputStreamManager_RegisterLatencyCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerlatencycallback), and[OH_AudioAccessoryInputStreamManager_RegisterFramePositionCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerframepositioncallback) toregister required stream callbacks. This is the ONLY time when callbackregistration is allowed. |
| [typedef bool (\*OH_AudioAccessoryInputStream_StartCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream)](#oh_audioaccessoryinputstream_startcallback) | OH_AudioAccessoryInputStream_StartCallback | Callback for stream started event.<b>When Called:</b> After the stream is successfully started and readyto receive audio data. After this callback returns, you may call Write()to send audio data. |
| [typedef bool (\*OH_AudioAccessoryInputStream_StopCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream)](#oh_audioaccessoryinputstream_stopcallback) | OH_AudioAccessoryInputStream_StopCallback | Callback for stream stopped event.<b>When Called:</b> After the stream is stopped. After this callbackreturns, you must stop calling Write(). The stream handle remainsvalid and may be started again. |
| [typedef bool (\*OH_AudioAccessoryInputStream_ReleaseCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream)](#oh_audioaccessoryinputstream_releasecallback) | OH_AudioAccessoryInputStream_ReleaseCallback | Callback for stream released event.<b>When Called:</b> When the stream is being released. This is alwaysthe last callback for a stream. After this callback returns, the streamhandle is no longer valid and must not be used. |
| [typedef bool (\*OH_AudioAccessoryInputStream_GetLatencyCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream, int32_t *latency)](#oh_audioaccessoryinputstream_getlatencycallback) | OH_AudioAccessoryInputStream_GetLatencyCallback | Callback for querying the current latency of the stream.<b>When Called:</b> When the framework needs the current latency valuereported by the accessory stream. |
| [typedef bool (\*OH_AudioAccessoryInputStream_GetFramePositionCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream, int64_t *framePosition, int64_t *timestamp)](#oh_audioaccessoryinputstream_getframepositioncallback) | OH_AudioAccessoryInputStream_GetFramePositionCallback | Callback for querying the current frame position of the stream.<b>When Called:</b> When the framework needs the current capture positionreported by the accessory stream. |
| [OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterStartCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_StartCallback callback)](#oh_audioaccessoryinputstreammanager_registerstartcallback) | - | Registers the callback for stream started event.<b>CRITICAL: Registration Timing Constraint</b>This function MUST be called ONLY during the execution of[OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback). Calling thisfunction at any other time will result in [AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result).<b>Requirement:</b> This callback is MANDATORY. If not registered,the framework will reject the stream creation and trigger cleanup. |
| [OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterStopCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_StopCallback callback)](#oh_audioaccessoryinputstreammanager_registerstopcallback) | - | Registers the callback for stream stopped event.<b>CRITICAL: Registration Timing Constraint</b>This function MUST be called ONLY during the execution of[OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback). Calling thisfunction at any other time will result in [AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result).<b>Requirement:</b> This callback is MANDATORY. If not registered,the framework will reject the stream creation and trigger cleanup. |
| [OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterReleaseCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_ReleaseCallback callback)](#oh_audioaccessoryinputstreammanager_registerreleasecallback) | - | Registers the callback for stream released event.<b>CRITICAL: Registration Timing Constraint</b>This function MUST be called ONLY during the execution of[OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback). Calling thisfunction at any other time will result in [AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result).<b>Requirement:</b> This callback is MANDATORY. If not registered,the framework will reject the stream creation and trigger cleanup. |
| [OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterLatencyCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_GetLatencyCallback callback)](#oh_audioaccessoryinputstreammanager_registerlatencycallback) | - | Registers the callback for stream latency query.<b>CRITICAL: Registration Timing Constraint</b>This function MUST be called ONLY during the execution of[OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback). Calling thisfunction at any other time will result in [AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result).<b>Requirement:</b> This callback is MANDATORY. If not registered,the framework will reject the stream creation and trigger cleanup. |
| [OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterFramePositionCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_GetFramePositionCallback callback)](#oh_audioaccessoryinputstreammanager_registerframepositioncallback) | - | Registers the callback for stream frame position query.<b>CRITICAL: Registration Timing Constraint</b>This function MUST be called ONLY during the execution of[OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback). Calling thisfunction at any other time will result in [AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result).<b>Requirement:</b> This callback is MANDATORY. If not registered,the framework will reject the stream creation and trigger cleanup. |
| [OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_Write(OH_AudioAccessoryInputStream *stream, const uint8_t *data, uint32_t dataSize)](#oh_audioaccessoryinputstreammanager_write) | - | Writes audio data to the audio accessory input stream.This is a blocking interface. After being called, the function blocks untilthe whole frame is written successfully or an error occurs. Each call mustwrite exactly 20 ms of audio data. The caller must ensure that dataSizematches the byte count corresponding to 20 ms under the current streamconfiguration. If dataSize does not match 20 ms of audio data, thisfunction returns [AUDIOCOMMON_RESULT_ERROR_FRAME_LENGTH_MISMATCH](capi-native-audio-common-h.md#oh_audiocommon_result).The caller must invoke this function at a 20 ms cadence. That is, each callmust submit 20 ms of audio data, and the interval between two consecutivecalls must also be 20 ms.If the stream buffer does not currently have enough writable space for thewhole frame, this function blocks until enough space becomes available or anerror occurs. Partial-frame writes are not supported by this interface. Ifthe last frame has less than 20 ms of audio data, the caller may discardthis frame or pad it with zeros to 20 ms before calling this function.<b>Calling Context and Concurrency:</b>This function is not reentrant for the same stream. The caller is advisedto use only one thread to write audio data serially to the same stream.If this function is called concurrently with the stop or release callbackfor the same stream, it returns[AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result) if the stop or releaseoperation completes before this function acquires the lock. |
| [OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_GetWritableSize(OH_AudioAccessoryInputStream *stream, uint32_t *writableSize)](#oh_audioaccessoryinputstreammanager_getwritablesize) | - | Obtains the writable size of the audio accessory input stream buffer.This function can be used by the caller to probe current buffer availabilitybefore calling [OH_AudioAccessoryInputStreamManager_Write](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_write). The returnedwritable size reflects the current state only, and may change immediatelyafter the function returns. |

## Function description

### OH_AudioAccessory_OpenInputStreamCallback()

```c
typedef bool (*OH_AudioAccessory_OpenInputStreamCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream, OH_AudioStreamInfo *streamInfo)
```

**Description**

Callback for opening an input stream on an audio accessory.<b>When Called:</b> The audio framework calls this callback when anapplication requests audio capture from this audio accessory.The framework passes the audio stream information of the stream beingopened, so the accessory can prepare the corresponding data path.<b>Usage Requirements:</b> In this callback, you MUST call[OH_AudioAccessoryInputStreamManager_RegisterStartCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerstartcallback),[OH_AudioAccessoryInputStreamManager_RegisterStopCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerstopcallback),[OH_AudioAccessoryInputStreamManager_RegisterReleaseCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerreleasecallback),[OH_AudioAccessoryInputStreamManager_RegisterLatencyCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerlatencycallback), and[OH_AudioAccessoryInputStreamManager_RegisterFramePositionCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerframepositioncallback) toregister required stream callbacks. This is the ONLY time when callbackregistration is allowed.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| (OH_AudioAccessory \*accessory | [in] The audio accessory on which the stream is opened. |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | [in] Reference to the newly created input stream.Use this handle to register callbacks via Register...Callback. |
| [OH_AudioStreamInfo](capi-ohaudio-oh-audiostreaminfo.md) \*streamInfo | [in] Pointer to the audio stream information of the streambeing opened. This parameter describes the requested stream format andcan be used by the accessory to configure its data path. |

**Returns**:

| Type | Description |
| -- | -- |
| bool | <ul><br>         <li>`true` if the stream is accepted.</li><br>         <li>`false` otherwise.</li><br>         </ul> |

**Reference**:

[OH_AudioAccessoryInputStreamManager_RegisterStartCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerstartcallback)


### OH_AudioAccessoryInputStream_StartCallback()

```c
typedef bool (*OH_AudioAccessoryInputStream_StartCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream)
```

**Description**

Callback for stream started event.<b>When Called:</b> After the stream is successfully started and readyto receive audio data. After this callback returns, you may call Write()to send audio data.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| (OH_AudioAccessory \*accessory | [in] The audio accessory that owns this stream. |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | [in] Reference to the input stream that is started. |

**Returns**:

| Type | Description |
| -- | -- |
| bool | <ul><br>         <li>`true` if the start event is handled successfully.</li><br>         <li>`false` otherwise.</li><br>         </ul> |

### OH_AudioAccessoryInputStream_StopCallback()

```c
typedef bool (*OH_AudioAccessoryInputStream_StopCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream)
```

**Description**

Callback for stream stopped event.<b>When Called:</b> After the stream is stopped. After this callbackreturns, you must stop calling Write(). The stream handle remainsvalid and may be started again.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| (OH_AudioAccessory \*accessory | [in] The audio accessory that owns this stream. |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | [in] Reference to the input stream that is stopped. |

**Returns**:

| Type | Description |
| -- | -- |
| bool | <ul><br>         <li>`true` if the stop event is handled successfully.</li><br>         <li>`false` otherwise.</li><br>         </ul> |

### OH_AudioAccessoryInputStream_ReleaseCallback()

```c
typedef bool (*OH_AudioAccessoryInputStream_ReleaseCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream)
```

**Description**

Callback for stream released event.<b>When Called:</b> When the stream is being released. This is alwaysthe last callback for a stream. After this callback returns, the streamhandle is no longer valid and must not be used.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| (OH_AudioAccessory \*accessory | [in] The audio accessory that owns this stream. |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | [in] Reference to the input stream that is released. |

**Returns**:

| Type | Description |
| -- | -- |
| bool | <ul><br>         <li>`true` if the release event is handled successfully.</li><br>         <li>`false` otherwise.</li><br>         </ul> |

### OH_AudioAccessoryInputStream_GetLatencyCallback()

```c
typedef bool (*OH_AudioAccessoryInputStream_GetLatencyCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream, int32_t *latency)
```

**Description**

Callback for querying the current latency of the stream.<b>When Called:</b> When the framework needs the current latency valuereported by the accessory stream.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| (OH_AudioAccessory \*accessory | [in] The audio accessory that owns this stream. |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | [in] Reference to the input stream. |
| int32_t \*latency | [out] Output parameter. Returns the latency, in milliseconds. |

**Returns**:

| Type | Description |
| -- | -- |
| bool | <ul><br>         <li>`true` if the latency is obtained successfully.</li><br>         <li>`false` otherwise.</li><br>         </ul> |

### OH_AudioAccessoryInputStream_GetFramePositionCallback()

```c
typedef bool (*OH_AudioAccessoryInputStream_GetFramePositionCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream, int64_t *framePosition, int64_t *timestamp)
```

**Description**

Callback for querying the current frame position of the stream.<b>When Called:</b> When the framework needs the current capture positionreported by the accessory stream.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| (OH_AudioAccessory \*accessory | [in] The audio accessory that owns this stream. |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | [in] Reference to the input stream. |
| int64_t \*framePosition | [out] Output parameter. Returns the cumulative number of audioframes captured since the most recent successful start of this inputstream. |
| int64_t \*timestamp | [out] Returns the capture timestamp corresponding to the frameposition reported through {@p framePosition}. The timestamp must use the{@link CLOCK_MONOTONIC} time base and is expressed in nanoseconds. It representsthe monotonic clock time at which the frame identified by {@p framePosition} was captured. |

**Returns**:

| Type | Description |
| -- | -- |
| bool | <ul><br>         <li>`true` if the frame position is obtained successfully.</li><br>         <li>`false` otherwise.</li><br>         </ul> |

### OH_AudioAccessoryInputStreamManager_RegisterStartCallback()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterStartCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_StartCallback callback)
```

**Description**

Registers the callback for stream started event.<b>CRITICAL: Registration Timing Constraint</b>This function MUST be called ONLY during the execution of[OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback). Calling thisfunction at any other time will result in [AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result).<b>Requirement:</b> This callback is MANDATORY. If not registered,the framework will reject the stream creation and trigger cleanup.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) *stream | [in] Pointer to the input stream handle. |
| [OH_AudioAccessoryInputStream_StartCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstream_startcallback) callback | [in] Pointer to the callback function. Must not be null. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_AudioCommon_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | <ul><br>         <li>[AUDIOCOMMON_RESULT_SUCCESS](capi-native-audio-common-h.md#oh_audiocommon_result) if execution succeeds.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM](capi-native-audio-common-h.md#oh_audiocommon_result) if parameters are null.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result) if called outside<br>                  [OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback) or stream is released.</li><br>         </ul> |

### OH_AudioAccessoryInputStreamManager_RegisterStopCallback()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterStopCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_StopCallback callback)
```

**Description**

Registers the callback for stream stopped event.<b>CRITICAL: Registration Timing Constraint</b>This function MUST be called ONLY during the execution of[OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback). Calling thisfunction at any other time will result in [AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result).<b>Requirement:</b> This callback is MANDATORY. If not registered,the framework will reject the stream creation and trigger cleanup.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) *stream | [in] Pointer to the input stream handle. |
| [OH_AudioAccessoryInputStream_StopCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstream_stopcallback) callback | [in] Pointer to the callback function. Must not be null. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_AudioCommon_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | <ul><br>         <li>[AUDIOCOMMON_RESULT_SUCCESS](capi-native-audio-common-h.md#oh_audiocommon_result) if execution succeeds.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM](capi-native-audio-common-h.md#oh_audiocommon_result) if parameters are null.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result) if called outside<br>                  [OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback) or stream is released.</li><br>         </ul> |

### OH_AudioAccessoryInputStreamManager_RegisterReleaseCallback()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterReleaseCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_ReleaseCallback callback)
```

**Description**

Registers the callback for stream released event.<b>CRITICAL: Registration Timing Constraint</b>This function MUST be called ONLY during the execution of[OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback). Calling thisfunction at any other time will result in [AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result).<b>Requirement:</b> This callback is MANDATORY. If not registered,the framework will reject the stream creation and trigger cleanup.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) *stream | [in] Pointer to the input stream handle. |
| [OH_AudioAccessoryInputStream_ReleaseCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstream_releasecallback) callback | [in] Pointer to the callback function. Must not be null. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_AudioCommon_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | <ul><br>         <li>[AUDIOCOMMON_RESULT_SUCCESS](capi-native-audio-common-h.md#oh_audiocommon_result) if execution succeeds.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM](capi-native-audio-common-h.md#oh_audiocommon_result) if parameters are null.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result) if called outside<br>                  [OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback) or stream is released.</li><br>         </ul> |

### OH_AudioAccessoryInputStreamManager_RegisterLatencyCallback()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterLatencyCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_GetLatencyCallback callback)
```

**Description**

Registers the callback for stream latency query.<b>CRITICAL: Registration Timing Constraint</b>This function MUST be called ONLY during the execution of[OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback). Calling thisfunction at any other time will result in [AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result).<b>Requirement:</b> This callback is MANDATORY. If not registered,the framework will reject the stream creation and trigger cleanup.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) *stream | [in] Pointer to the input stream handle. |
| [OH_AudioAccessoryInputStream_GetLatencyCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstream_getlatencycallback) callback | [in] Pointer to the callback function. Must not be null. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_AudioCommon_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | <ul><br>         <li>[AUDIOCOMMON_RESULT_SUCCESS](capi-native-audio-common-h.md#oh_audiocommon_result) if execution succeeds.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM](capi-native-audio-common-h.md#oh_audiocommon_result) if parameters are null.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result) if called outside<br>                  [OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback) or stream is released.</li><br>         </ul> |

### OH_AudioAccessoryInputStreamManager_RegisterFramePositionCallback()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterFramePositionCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_GetFramePositionCallback callback)
```

**Description**

Registers the callback for stream frame position query.<b>CRITICAL: Registration Timing Constraint</b>This function MUST be called ONLY during the execution of[OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback). Calling thisfunction at any other time will result in [AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result).<b>Requirement:</b> This callback is MANDATORY. If not registered,the framework will reject the stream creation and trigger cleanup.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) *stream | [in] Pointer to the input stream handle. |
| [OH_AudioAccessoryInputStream_GetFramePositionCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstream_getframepositioncallback) callback | [in] Pointer to the callback function. Must not be null. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_AudioCommon_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | <ul><br>         <li>[AUDIOCOMMON_RESULT_SUCCESS](capi-native-audio-common-h.md#oh_audiocommon_result) if execution succeeds.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM](capi-native-audio-common-h.md#oh_audiocommon_result) if parameters are null.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result) if called outside<br>                  [OH_AudioAccessory_OpenInputStreamCallback](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback) or stream is released.</li><br>         </ul> |

### OH_AudioAccessoryInputStreamManager_Write()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_Write(OH_AudioAccessoryInputStream *stream, const uint8_t *data, uint32_t dataSize)
```

**Description**

Writes audio data to the audio accessory input stream.This is a blocking interface. After being called, the function blocks untilthe whole frame is written successfully or an error occurs. Each call mustwrite exactly 20 ms of audio data. The caller must ensure that dataSizematches the byte count corresponding to 20 ms under the current streamconfiguration. If dataSize does not match 20 ms of audio data, thisfunction returns [AUDIOCOMMON_RESULT_ERROR_FRAME_LENGTH_MISMATCH](capi-native-audio-common-h.md#oh_audiocommon_result).The caller must invoke this function at a 20 ms cadence. That is, each callmust submit 20 ms of audio data, and the interval between two consecutivecalls must also be 20 ms.If the stream buffer does not currently have enough writable space for thewhole frame, this function blocks until enough space becomes available or anerror occurs. Partial-frame writes are not supported by this interface. Ifthe last frame has less than 20 ms of audio data, the caller may discardthis frame or pad it with zeros to 20 ms before calling this function.<b>Calling Context and Concurrency:</b>This function is not reentrant for the same stream. The caller is advisedto use only one thread to write audio data serially to the same stream.If this function is called concurrently with the stop or release callbackfor the same stream, it returns[AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result) if the stop or releaseoperation completes before this function acquires the lock.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) *stream | [in] Pointer to the input stream handle. |
| const uint8_t *data | [in] Pointer to the audio data buffer. Must not be null. |
| uint32_t dataSize | [in] Size of the audio data in bytes. Must be > 0. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_AudioCommon_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | <ul><br>         <li>[AUDIOCOMMON_RESULT_SUCCESS](capi-native-audio-common-h.md#oh_audiocommon_result) if execution succeeds.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM](capi-native-audio-common-h.md#oh_audiocommon_result) if parameters are null.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_FRAME_LENGTH_MISMATCH](capi-native-audio-common-h.md#oh_audiocommon_result) if dataSize does not correspond<br>                  to 20 ms of audio data under the current stream configuration.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result) if stream is not started or the required<br>                  stream callbacks are not fully registered.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_SYSTEM](capi-native-audio-common-h.md#oh_audiocommon_result) if audio server process die.</li><br>         </ul> |

### OH_AudioAccessoryInputStreamManager_GetWritableSize()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_GetWritableSize(OH_AudioAccessoryInputStream *stream, uint32_t *writableSize)
```

**Description**

Obtains the writable size of the audio accessory input stream buffer.This function can be used by the caller to probe current buffer availabilitybefore calling [OH_AudioAccessoryInputStreamManager_Write](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_write). The returnedwritable size reflects the current state only, and may change immediatelyafter the function returns.

**Since**: 26.0.0

**Parameters**:

| Parameter | Description |
| -- | -- |
| [OH_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) *stream | [in] Pointer to the input stream handle. |
| uint32_t *writableSize | [out] Output parameter. Returns the number of bytes that can be written. |

**Returns**:

| Type | Description |
| -- | -- |
| [OH_AudioCommon_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | <ul><br>         <li>[AUDIOCOMMON_RESULT_SUCCESS](capi-native-audio-common-h.md#oh_audiocommon_result) if execution succeeds.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM](capi-native-audio-common-h.md#oh_audiocommon_result) if parameters are null.</li><br>         <li>[AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE](capi-native-audio-common-h.md#oh_audiocommon_result) if the stream is released.</li><br>         </ul> |


