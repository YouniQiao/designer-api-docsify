# MediaKeySystem

Manages and record MediaKeySessions. Before calling an MediaKeySystem method, we must use getMediaKeySystem to get a MediaKeySystem instance, then we can call functions.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

<!--Device-drm-interface MediaKeySystem--><!--Device-drm-interface MediaKeySystem-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

## 导入模块

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## clearOfflineMediaKeys

```TypeScript
clearOfflineMediaKeys(mediaKeyId: Uint8Array): void
```

Remove media keys corresponding to the mediaKeyId.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-clearOfflineMediaKeys(mediaKeyId: Uint8Array): void--><!--Device-MediaKeySystem-clearOfflineMediaKeys(mediaKeyId: Uint8Array): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaKeyId | Uint8Array | 是 | The mediaKeyId specifies which media key should be cleared. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed.Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## createMediaKeySession

```TypeScript
createMediaKeySession(level: ContentProtectionLevel): MediaKeySession
```

Create a MediaKeySession instance with level.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-createMediaKeySession(level: ContentProtectionLevel): MediaKeySession--><!--Device-MediaKeySystem-createMediaKeySession(level: ContentProtectionLevel): MediaKeySession-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) | 是 | Used to specify the content protection level. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) | A MediaKeySession instance. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24700104 | Meet max MediaKeySession num limit. |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.The param level exceeds reasonable range, please use value in ContentProtectionLevel. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## createMediaKeySession

```TypeScript
createMediaKeySession(level: ContentProtectionLevel): MediaKeySession | undefined
```

Create a MediaKeySession instance with level.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-MediaKeySystem-createMediaKeySession(level: ContentProtectionLevel): MediaKeySession | undefined--><!--Device-MediaKeySystem-createMediaKeySession(level: ContentProtectionLevel): MediaKeySession | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) | 是 | Used to specify the content protection level. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) | A MediaKeySession instance or undefined. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24700104 | Meet max MediaKeySession num limit. |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.The param level exceeds reasonable range, please use value in ContentProtectionLevel. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## createMediaKeySession

```TypeScript
createMediaKeySession(): MediaKeySession
```

Create a MediaKeySession instance.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-createMediaKeySession(): MediaKeySession--><!--Device-MediaKeySystem-createMediaKeySession(): MediaKeySession-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) | A MediaKeySession instance. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24700104 | Meet max MediaKeySession num limit. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## createMediaKeySession

```TypeScript
createMediaKeySession(): MediaKeySession | undefined
```

Create a MediaKeySession instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-MediaKeySystem-createMediaKeySession(): MediaKeySession | undefined--><!--Device-MediaKeySystem-createMediaKeySession(): MediaKeySession | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) | A MediaKeySession instance or undefined |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24700104 | Meet max MediaKeySession num limit. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## destroy

```TypeScript
destroy(): void
```

Release the resource before the MediaKeySystem gonna be unused.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-destroy(): void--><!--Device-MediaKeySystem-destroy(): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## generateKeySystemRequest

```TypeScript
generateKeySystemRequest(): Promise<ProvisionRequest>
```

Generate a media key system provision request.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-generateKeySystemRequest(): Promise<ProvisionRequest>--><!--Device-MediaKeySystem-generateKeySystemRequest(): Promise<ProvisionRequest>-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ProvisionRequest&gt; | Promise with ProvisionRequest used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## getCertificateStatus

```TypeScript
getCertificateStatus(): CertificateStatus
```

Get certificate status of the MediaKeySystem.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-getCertificateStatus(): CertificateStatus--><!--Device-MediaKeySystem-getCertificateStatus(): CertificateStatus-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CertificateStatus](arkts-drm-drm-certificatestatus-e.md) | Certificate Status of the MediaKeySystem instance. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## getConfigurationByteArray

```TypeScript
getConfigurationByteArray(configName: string): Uint8Array
```

Get the specified configuration.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-getConfigurationByteArray(configName: string): Uint8Array--><!--Device-MediaKeySystem-getConfigurationByteArray(configName: string): Uint8Array-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configName | string | 是 | Used to specify the config name. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | The config value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## getConfigurationString

```TypeScript
getConfigurationString(configName: string): string
```

Get the specified configuration.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-getConfigurationString(configName: string): string--><!--Device-MediaKeySystem-getConfigurationString(configName: string): string-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configName | string | 是 | Used to specify the config name. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The config value string. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed, the param's length is zero or too big(exceeds 4096 Bytes). |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## getMaxContentProtectionLevel

```TypeScript
getMaxContentProtectionLevel(): ContentProtectionLevel
```

Get max content protection level the device supports.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-getMaxContentProtectionLevel(): ContentProtectionLevel--><!--Device-MediaKeySystem-getMaxContentProtectionLevel(): ContentProtectionLevel-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) | The max content protection level of the MediaKeySystem instance. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## getOfflineMediaKeyIds

```TypeScript
getOfflineMediaKeyIds(): Uint8Array[]
```

Get the list of offline MediaKeyIds.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-getOfflineMediaKeyIds(): Uint8Array[]--><!--Device-MediaKeySystem-getOfflineMediaKeyIds(): Uint8Array[]-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array[] | The list of offline MediaKeyIds. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## getOfflineMediaKeyStatus

```TypeScript
getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus
```

Get offline media key status corresponding to the mediaKeyId.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus--><!--Device-MediaKeySystem-getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaKeyId | Uint8Array | 是 | The media key identifier. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OfflineMediaKeyStatus](arkts-drm-drm-offlinemediakeystatus-e.md) | Offline media key Status. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## getStatistics

```TypeScript
getStatistics(): StatisticKeyValue[]
```

Get performance statistics information.That includes currentSessionNum, version, decryptNumber,and errorDecryptNumber.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-getStatistics(): StatisticKeyValue[]--><!--Device-MediaKeySystem-getStatistics(): StatisticKeyValue[]-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StatisticKeyValue](arkts-drm-drm-statistickeyvalue-i.md)[] | A list that includes performance index and corresponding statistics. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## off('keySystemRequired')

```TypeScript
off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void
```

Unregister keySystemRequired events.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySystem-off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'keySystemRequired' | 是 | Type of the drm event to listen for. |
| callback | (eventInfo: EventInfo) =&gt; void | 否 | Used to listen for the key system required event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 24700101 | All unknown errors. |

## offKeySystemRequired

```TypeScript
offKeySystemRequired(callback?: (eventInfo: EventInfo) => void): void
```

Unregister keySystemRequired events.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-MediaKeySystem-offKeySystemRequired(callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySystem-offKeySystemRequired(callback?: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (eventInfo: EventInfo) =&gt; void | 否 | Used to listen for the key system required event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors. |

## on('keySystemRequired')

```TypeScript
on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void
```

Register keySystemRequired events.

**起始版本：** 14

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为14。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySystem-on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'keySystemRequired' | 是 | Type of the drm event to listen for. |
| callback | (eventInfo: EventInfo) =&gt; void | 是 | Used to listen for the key system required event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 24700101 | All unknown errors. |

## onKeySystemRequired

```TypeScript
onKeySystemRequired(callback: (eventInfo: EventInfo) => void): void
```

Register keySystemRequired events.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-MediaKeySystem-onKeySystemRequired(callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySystem-onKeySystemRequired(callback: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (eventInfo: EventInfo) =&gt; void | 是 | Used to listen for the key system required event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24700101 | All unknown errors. |

## processKeySystemResponse

```TypeScript
processKeySystemResponse(response: Uint8Array): Promise<void>
```

Process the response corresponding the key system request obtained by the application.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-processKeySystemResponse(response: Uint8Array): Promise<void>--><!--Device-MediaKeySystem-processKeySystemResponse(response: Uint8Array): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | Uint8Array | 是 | Response corresponding to the request. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## setConfigurationByteArray

```TypeScript
setConfigurationByteArray(configName: string, value: Uint8Array): void
```

Set the specified configuration.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-setConfigurationByteArray(configName: string, value: Uint8Array): void--><!--Device-MediaKeySystem-setConfigurationByteArray(configName: string, value: Uint8Array): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configName | string | 是 | Used to specify the config name. |
| value | Uint8Array | 是 | The value to be set. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

## setConfigurationString

```TypeScript
setConfigurationString(configName: string, value: string): void
```

Set the specified configuration.

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystem-setConfigurationString(configName: string, value: string): void--><!--Device-MediaKeySystem-setConfigurationString(configName: string, value: string): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| configName | string | 是 | Used to specify the config name. |
| value | string | 是 | The value to be set. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700201 | Fatal service error, for example, service died. |
| 24700101 | All unknown errors. |

