# getPostProcessingTrack

## getPostProcessingTrack

```TypeScript
function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>
```

Obtain post-processing trajectory information under specific sport mode. Only  
[SKIING]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is supported currently.

Before calling this API, you need to call  
[on('locationChange')]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ and set the input parameter  
[sportsType]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ to the specific sport mode to start tracking.

Returns data within 24 hours since tracking started; Subsequent calls return only new records.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 26.1.0.

**Required permissions:** ohos.permission.LOCATION

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-geoLocationManager-function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>--><!--Device-geoLocationManager-function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sportsType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicate the type of sports. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Location&gt;&gt; | Promise used to return \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call \_\_\_ESCAPED\_DOLLAR\_\_\_{geoLocationManager.getPostProcessingTrack} due to limited device capabilities. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) | The location switch is off. |
| [3301200](../errorcode-geoLocationManager.md#3301200-failed-to-obtain-the-positioning-result) | Failed to obtain the post processing track because sports type is not supported. |

