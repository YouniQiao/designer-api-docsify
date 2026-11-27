# AudioSuiteDownloadManager (System API)

```TypeScript
interface AudioSuiteDownloadManager
```

Provides the capabilities to manage the download of audio suite features, including starting, pausing, and canceling the download, querying the status, and uninstalling the features.

**Since:** 26.0.1

<!--Device-audio-interface AudioSuiteDownloadManager--><!--Device-audio-interface AudioSuiteDownloadManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.SuiteEngine

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## cancelDownload

```TypeScript
cancelDownload(featureTypes: Array<AudioSuiteFeatureType>): Promise<void>
```

Cancels the download of specified features. This API uses a promise to return the result. This API should be called when the feature status is [DOWNLOADING](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#downloading) or [DOWNLOAD_PAUSED](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#download_paused). After this API is called, the status changes to [VERSION_CHECK_SUCCEEDED](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#version_check_succeeded).

If this API is called when the feature status is not [DOWNLOADING](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#downloading) or [DOWNLOAD_PAUSED](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#download_paused), the API returns a successful response and retains the original status.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSuiteDownloadManager-cancelDownload(featureTypes: Array<AudioSuiteFeatureType>): Promise<void>--><!--Device-AudioSuiteDownloadManager-cancelDownload(featureTypes: Array<AudioSuiteFeatureType>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.SuiteEngine

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| featureTypes | Array&lt;[AudioSuiteFeatureType](arkts-audio-audio-audiosuitefeaturetype-e-sys.md)&gt; | Yes | Types of features to cancel downloading. The array can contain at most 5 elements. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. The value of featureTypes is invalid. |
| [6800302](../errorcode-audio.md#6800302-system-service-process-terminated) | System service process terminated. |

## getFeatureStatus

```TypeScript
getFeatureStatus(featureTypes: Array<AudioSuiteFeatureType>): Promise<AudioSuiteFeatureStatusInfoArray>
```

Obtains the status of specified features. This API uses a promise to return the result.

This API queries the local installation status of features and does not depend on the network environment.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSuiteDownloadManager-getFeatureStatus(featureTypes: Array<AudioSuiteFeatureType>): Promise<AudioSuiteFeatureStatusInfoArray>--><!--Device-AudioSuiteDownloadManager-getFeatureStatus(featureTypes: Array<AudioSuiteFeatureType>): Promise<AudioSuiteFeatureStatusInfoArray>-End-->

**System capability:** SystemCapability.Multimedia.Audio.SuiteEngine

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| featureTypes | Array&lt;[AudioSuiteFeatureType](arkts-audio-audio-audiosuitefeaturetype-e-sys.md)&gt; | Yes | Types of features to query. The array can contain at most 5 elements. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioSuiteFeatureStatusInfoArray](arkts-audio-audio-audiosuitefeaturestatusinfoarray-t-sys.md)&gt; | Promise used to return the feature status array. Each element corresponds to the feature at the matching index in **featureTypes**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. The value of featureTypes is invalid. |
| [6800302](../errorcode-audio.md#6800302-system-service-process-terminated) | System service process terminated. |

## getNewVersionInfo

```TypeScript
getNewVersionInfo(featureTypes: Array<AudioSuiteFeatureType>): Promise<Array<AudioSuiteFeatureVersionInfo>>
```

Obtains the latest version information about specified features. This API uses a promise to return the result.

Before calling this API, ensure that the device is connected to an available network.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSuiteDownloadManager-getNewVersionInfo(featureTypes: Array<AudioSuiteFeatureType>): Promise<Array<AudioSuiteFeatureVersionInfo>>--><!--Device-AudioSuiteDownloadManager-getNewVersionInfo(featureTypes: Array<AudioSuiteFeatureType>): Promise<Array<AudioSuiteFeatureVersionInfo>>-End-->

**System capability:** SystemCapability.Multimedia.Audio.SuiteEngine

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| featureTypes | Array&lt;[AudioSuiteFeatureType](arkts-audio-audio-audiosuitefeaturetype-e-sys.md)&gt; | Yes | Types of features to query. The array can contain at most 5 elements. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[AudioSuiteFeatureVersionInfo](arkts-audio-audio-audiosuitefeatureversioninfo-i-sys.md)&gt;&gt; | Promise used to return the version information array. Each element corresponds to the feature at the matching index in **featureTypes**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. The value of featureTypes is invalid. |
| [6800302](../errorcode-audio.md#6800302-system-service-process-terminated) | System service process terminated. |
| [6800501](../errorcode-audio.md#6800501-network-conditions-not-met) | Required network conditions not met. The current network status is unavailable. |

## isFeatureInstalled

```TypeScript
isFeatureInstalled(featureTypes: Array<AudioSuiteFeatureType>): Promise<Array<boolean>>
```

Checks whether specified features have been installed. This API uses a promise to return the result.

This API queries the local installation status of features and does not depend on the network environment.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSuiteDownloadManager-isFeatureInstalled(featureTypes: Array<AudioSuiteFeatureType>): Promise<Array<boolean>>--><!--Device-AudioSuiteDownloadManager-isFeatureInstalled(featureTypes: Array<AudioSuiteFeatureType>): Promise<Array<boolean>>-End-->

**System capability:** SystemCapability.Multimedia.Audio.SuiteEngine

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| featureTypes | Array&lt;[AudioSuiteFeatureType](arkts-audio-audio-audiosuitefeaturetype-e-sys.md)&gt; | Yes | Types of features to query. The array can contain at most 5 elements. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;boolean&gt;&gt; | Promise used to return the installation status array. Each element corresponds to the feature at the matching index in **featureTypes**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. The value of featureTypes is invalid. |
| [6800302](../errorcode-audio.md#6800302-system-service-process-terminated) | System service process terminated. |

## offDownloadStatusChange

```TypeScript
offDownloadStatusChange(callback?: Callback<AudioSuiteFeatureStatusInfoArray>): void
```

Unsubscribes from the download status change event. Upon unsubscription, the system will no longer trigger the callback.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSuiteDownloadManager-offDownloadStatusChange(callback?: Callback<AudioSuiteFeatureStatusInfoArray>): void--><!--Device-AudioSuiteDownloadManager-offDownloadStatusChange(callback?: Callback<AudioSuiteFeatureStatusInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.SuiteEngine

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSuiteFeatureStatusInfoArray](arkts-audio-audio-audiosuitefeaturestatusinfoarray-t-sys.md)&gt; | No | Callback to unsubscribe. By default, this parameter is left empty. If this parameter is not set, all callbacks subscribed to in the current process are unsubscribed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [6800302](../errorcode-audio.md#6800302-system-service-process-terminated) | System service process terminated. |

## onDownloadStatusChange

```TypeScript
onDownloadStatusChange(callback: Callback<AudioSuiteFeatureStatusInfoArray>): void
```

Subscribes to the download status change event. The callback is triggered when the download status or progress of any feature changes.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSuiteDownloadManager-onDownloadStatusChange(callback: Callback<AudioSuiteFeatureStatusInfoArray>): void--><!--Device-AudioSuiteDownloadManager-onDownloadStatusChange(callback: Callback<AudioSuiteFeatureStatusInfoArray>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.SuiteEngine

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioSuiteFeatureStatusInfoArray](arkts-audio-audio-audiosuitefeaturestatusinfoarray-t-sys.md)&gt; | Yes | Callback used to return the updated download status information array. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [6800302](../errorcode-audio.md#6800302-system-service-process-terminated) | System service process terminated. |

## pauseDownload

```TypeScript
pauseDownload(featureTypes: Array<AudioSuiteFeatureType>): Promise<void>
```

Pauses the download of specified features. This API uses a promise to return the result. This API should be called after the feature status changes to [DOWNLOADING](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#downloading). After this API is called, the status changes to [DOWNLOAD_PAUSED](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#download_paused).

If this API is called when the feature is not in the [DOWNLOADING](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#downloading) status, the API returns a successful response and retains the original status.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSuiteDownloadManager-pauseDownload(featureTypes: Array<AudioSuiteFeatureType>): Promise<void>--><!--Device-AudioSuiteDownloadManager-pauseDownload(featureTypes: Array<AudioSuiteFeatureType>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.SuiteEngine

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| featureTypes | Array&lt;[AudioSuiteFeatureType](arkts-audio-audio-audiosuitefeaturetype-e-sys.md)&gt; | Yes | Types of features to pause downloading. The value can contain a maximum of 5 characters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. The value of featureTypes is invalid. |
| [6800302](../errorcode-audio.md#6800302-system-service-process-terminated) | System service process terminated. |

## startBackgroundDownload

```TypeScript
startBackgroundDownload(featureTypes: Array<AudioSuiteFeatureType>): Promise<void>
```

Starts downloading features in the background. This API uses a promise to return the result. If the current network is Wi-Fi, the system audio service directly downloads the features. If the current network is not Wi-Fi, the system audio service automatically downloads the features once the network switches to Wi-Fi. This API can be called in any feature status (specified by [AudioSuiteFeatureStatus](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md)). After the client process exits, the system audio service continuously monitors the network environment until the download task is completed.

The API returns a result immediately after a request is sent. During the download, you can obtain the download progress by subscribing to the download status change event via [onDownloadStatusChange](#ondownloadstatuschange).

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSuiteDownloadManager-startBackgroundDownload(featureTypes: Array<AudioSuiteFeatureType>): Promise<void>--><!--Device-AudioSuiteDownloadManager-startBackgroundDownload(featureTypes: Array<AudioSuiteFeatureType>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.SuiteEngine

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| featureTypes | Array&lt;[AudioSuiteFeatureType](arkts-audio-audio-audiosuitefeaturetype-e-sys.md)&gt; | Yes | Types of features to download. The array can contain at most 5 elements. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. The value of featureTypes is invalid. |
| [6800302](../errorcode-audio.md#6800302-system-service-process-terminated) | System service process terminated. |

## startDownload

```TypeScript
startDownload(featureTypes: Array<AudioSuiteFeatureType>, networkType: NetworkType): Promise<void>
```

Starts downloading features over the specified network. This API uses a promise to return the result. Call [getNewVersionInfo](#getnewversioninfo) to query the new version. If the query is successful and the status changes to [VERSION_CHECK_SUCCEEDED](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#version_check_succeeded), call this API. Alternatively, you can call this API to resume the download when the status is [DOWNLOAD_PAUSED](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#download_paused). After this API is called, the status changes to [DOWNLOADING](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#downloading). After the download is successful, the status automatically changes to [INSTALLING](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#installing).

This API returns a result immediately after the download starts. During the download, you can obtain the download progress through the download status change event subscribed to by [onDownloadStatusChange](#ondownloadstatuschange).

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSuiteDownloadManager-startDownload(featureTypes: Array<AudioSuiteFeatureType>, networkType: NetworkType): Promise<void>--><!--Device-AudioSuiteDownloadManager-startDownload(featureTypes: Array<AudioSuiteFeatureType>, networkType: NetworkType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.SuiteEngine

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| featureTypes | Array&lt;[AudioSuiteFeatureType](arkts-audio-audio-audiosuitefeaturetype-e-sys.md)&gt; | Yes | Types of features to download. The value can contain a maximum of 5 characters. |
| networkType | [NetworkType](arkts-audio-audio-networktype-e-sys.md) | Yes | Network type for the download. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. The value of featureTypes is invalid. |
| [6800302](../errorcode-audio.md#6800302-system-service-process-terminated) | System service process terminated. |
| [6800501](../errorcode-audio.md#6800501-network-conditions-not-met) | Required network conditions not met. The current network conditions do not match the type specified by networkType. |
| [6800502](../errorcode-audio.md#6800502-insufficient-storage-space) | Insufficient storage space. |

## uninstallFeature

```TypeScript
uninstallFeature(featureTypes: Array<AudioSuiteFeatureType>): Promise<void>
```

Uninstalls downloaded features. This API uses a promise to return the result. This API should be called after the feature status changes to [INSTALLATION_SUCCEEDED](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#installation_succeeded). After this API is called, the status changes to [UNINSTALLING](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#uninstalling) and the uninstallation starts.

If this API is called when the feature status is not [INSTALLATION_SUCCEEDED](arkts-audio-audio-audiosuitefeaturestatus-e-sys.md#installation_succeeded), the API returns a successful response and retains the original status.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSuiteDownloadManager-uninstallFeature(featureTypes: Array<AudioSuiteFeatureType>): Promise<void>--><!--Device-AudioSuiteDownloadManager-uninstallFeature(featureTypes: Array<AudioSuiteFeatureType>): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.SuiteEngine

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| featureTypes | Array&lt;[AudioSuiteFeatureType](arkts-audio-audio-audiosuitefeaturetype-e-sys.md)&gt; | Yes | Types of features to uninstall. The array can contain at most 5 elements. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. The value of featureTypes is invalid. |
| [6800302](../errorcode-audio.md#6800302-system-service-process-terminated) | System service process terminated. |
