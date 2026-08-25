# MediaKeySystem

支持MediaKeySystem实例管理、设备证书申请与处理、会话创建、离线媒体密钥管理、获取DRM度量记录、设备属性等。在调用MediaKeySystem方法之前，必须使用 [createMediaKeySystem](arkts-drm-drm-createmediakeysystem-f.md)创建一个MediaKeySystem实例。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Drm.Core

## 导入模块

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## clearOfflineMediaKeys

```TypeScript
clearOfflineMediaKeys(mediaKeyId: Uint8Array): void
```

删除指定媒体密钥标识的离线媒体密钥。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mediaKeyId | Uint8Array | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## createMediaKeySession

```TypeScript
createMediaKeySession(level: ContentProtectionLevel): MediaKeySession
```

创建指定内容保护级别的MediaKeySession实例。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| level | [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700104](../errorcode-drm.md#24700104-mediakeysession数量达到极限) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## createMediaKeySession

```TypeScript
createMediaKeySession(): MediaKeySession
```

创建DRM解决方案默认内容保护级别的MediaKeySession实例。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 |
| --- |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700104](../errorcode-drm.md#24700104-mediakeysession数量达到极限) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## destroy

```TypeScript
destroy(): void
```

销毁MediaKeySystem实例。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## generateKeySystemRequest

```TypeScript
generateKeySystemRequest(): Promise<ProvisionRequest>
```

生成获取mediaKeySystem设备证书的请求。使用Promise异步回调。如果设备上已存在设备证书，调用此接口会返回失败。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ProvisionRequest](arkts-drm-drm-provisionrequest-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## getCertificateStatus

```TypeScript
getCertificateStatus(): CertificateStatus
```

获取设备证书状态值。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 |
| --- |
| [CertificateStatus](arkts-drm-drm-certificatestatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## getConfigurationByteArray

```TypeScript
getConfigurationByteArray(configName: string): Uint8Array
```

获取数组类型的配置信息。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [configName](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## getConfigurationString

```TypeScript
getConfigurationString(configName: string): string
```

获取字符串类型的配置属性值。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [configName](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## getMaxContentProtectionLevel

```TypeScript
getMaxContentProtectionLevel(): ContentProtectionLevel
```

获取当前DRM解决方案支持的最大内容保护级别。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 |
| --- |
| [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## getOfflineMediaKeyIds

```TypeScript
getOfflineMediaKeyIds(): Uint8Array[]
```

获取离线媒体密钥标识列表。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 |
| --- |
| Uint8Array[] |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## getOfflineMediaKeyStatus

```TypeScript
getOfflineMediaKeyStatus(mediaKeyId: Uint8Array): OfflineMediaKeyStatus
```

获取指定离线媒体密钥标识的媒体密钥的状态值。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mediaKeyId | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| [OfflineMediaKeyStatus](arkts-drm-drm-offlinemediakeystatus-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## getStatistics

```TypeScript
getStatistics(): StatisticKeyValue[]
```

获取性能度量记录。其中包括当前会话数、插件版本信息、每个会话最大三次解密耗时、解密次数和解密失败次数。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 |
| --- |
| [StatisticKeyValue](arkts-drm-drm-statistickeyvalue-i.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## off('keySystemRequired')

```TypeScript
off(type: 'keySystemRequired', callback?: (eventInfo: EventInfo) => void): void
```

注销设备证书请求事件的监听。使用callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keySystemRequired' | 是 |
| callback | (eventInfo: EventInfo) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## on('keySystemRequired')

```TypeScript
on(type: 'keySystemRequired', callback: (eventInfo: EventInfo) => void): void
```

监听设备证书请求事件，获取事件信息。使用callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keySystemRequired' | 是 |
| callback | (eventInfo: EventInfo) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## processKeySystemResponse

```TypeScript
processKeySystemResponse(response: Uint8Array): Promise<void>
```

处理获得的设备证书请求的响应。使用Promise异步回调。如果设备上已存在设备证书，调用此接口会返回失败。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| response | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## setConfigurationByteArray

```TypeScript
setConfigurationByteArray(configName: string, value: Uint8Array): void
```

设置数组类型的配置信息。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [configName](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | 是 |
| value | Uint8Array | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |

## setConfigurationString

```TypeScript
setConfigurationString(configName: string, value: string): void
```

设置字符串类型的配置信息。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [configName](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | 是 |
| value | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
