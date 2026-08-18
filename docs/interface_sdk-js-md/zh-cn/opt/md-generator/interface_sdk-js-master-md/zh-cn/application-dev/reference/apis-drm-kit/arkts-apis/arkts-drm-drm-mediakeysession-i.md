# MediaKeySession(Defines the DRM capability.)

支持媒体密钥管理。在调用MediaKeySession方法之前，必须使用 [createMediaKeySession](arkts-drm-drm-mediakeysystem-i.md#createmediakeysession) 获取一个MediaKeySession实例。

**起始版本：** 23

<!--Device-drm-interface MediaKeySession--><!--Device-drm-interface MediaKeySession-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

## 导入模块

```TypeScript
```

## checkMediaKeyStatus

```TypeScript
checkMediaKeyStatus(): MediaKeyStatus[]
```

检查当前媒体密钥状态。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-checkMediaKeyStatus(): MediaKeyStatus[]--><!--Device-MediaKeySession-checkMediaKeyStatus(): MediaKeyStatus[]-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 |
| --- |
| [MediaKeyStatus](arkts-drm-drm-mediakeystatus-i.md)[] |

**错误码：**

| 错误码ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## clearMediaKeys

```TypeScript
clearMediaKeys(): void
```

清除当前媒体密钥。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-clearMediaKeys(): void--><!--Device-MediaKeySession-clearMediaKeys(): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**错误码：**

| 错误码ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## destroy

```TypeScript
destroy(): void
```

销毁MediaKeySession实例。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-destroy(): void--><!--Device-MediaKeySession-destroy(): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**错误码：**

| 错误码ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## generateMediaKeyRequest

```TypeScript
generateMediaKeyRequest(mimeType: string, initData: Uint8Array, mediaKeyType: number, options?: OptionsData[]): Promise<MediaKeyRequest>
```

生成媒体密钥请求。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-generateMediaKeyRequest(mimeType: string, initData: Uint8Array, mediaKeyType: int, options?: OptionsData[]): Promise<MediaKeyRequest>--><!--Device-MediaKeySession-generateMediaKeyRequest(mimeType: string, initData: Uint8Array, mediaKeyType: int, options?: OptionsData[]): Promise<MediaKeyRequest>-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mimeType | string | 是 |
| initData | Uint8Array | 是 |
| mediaKeyType | number | 是 |
| options | [OptionsData](arkts-drm-drm-optionsdata-i.md)[] | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[MediaKeyRequest](arkts-drm-drm-mediakeyrequest-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## generateOfflineReleaseRequest

```TypeScript
generateOfflineReleaseRequest(mediaKeyId: Uint8Array): Promise<Uint8Array>
```

生成离线媒体密钥释放请求。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-generateOfflineReleaseRequest(mediaKeyId: Uint8Array): Promise<Uint8Array>--><!--Device-MediaKeySession-generateOfflineReleaseRequest(mediaKeyId: Uint8Array): Promise<Uint8Array>-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mediaKeyId | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## getContentProtectionLevel

```TypeScript
getContentProtectionLevel(): ContentProtectionLevel
```

获取当前会话的内容保护级别。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-getContentProtectionLevel(): ContentProtectionLevel--><!--Device-MediaKeySession-getContentProtectionLevel(): ContentProtectionLevel-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**返回值：**

| 类型 |
| --- |
| [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## offExpirationUpdate

```TypeScript
offExpirationUpdate(callback?: (eventInfo: EventInfo) => void): void
```

Unregister expirationUpdate event.

**起始版本：** 23

<!--Device-MediaKeySession-offExpirationUpdate(callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-offExpirationUpdate(callback?: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## offKeyExpired

```TypeScript
offKeyExpired(callback?: (eventInfo: EventInfo) => void): void
```

Unregister keyExpired event.

**起始版本：** 23

<!--Device-MediaKeySession-offKeyExpired(callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-offKeyExpired(callback?: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## offKeyRequired

```TypeScript
offKeyRequired(callback?: (eventInfo: EventInfo) => void): void
```

Unregister keyRequired event.

**起始版本：** 23

<!--Device-MediaKeySession-offKeyRequired(callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-offKeyRequired(callback?: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## offKeysChange

```TypeScript
offKeysChange(callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void
```

Unregister keysChange event.

**起始版本：** 23

<!--Device-MediaKeySession-offKeysChange(callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void--><!--Device-MediaKeySession-offKeysChange(callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (keyInfo: KeysInfo[], newKeyAvailable: boolean) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## offVendorDefined

```TypeScript
offVendorDefined(callback?: (eventInfo: EventInfo) => void): void
```

Unregister vendorDefined event.

**起始版本：** 23

<!--Device-MediaKeySession-offVendorDefined(callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-offVendorDefined(callback?: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## off_expirationUpdate

```TypeScript
off(type: 'expirationUpdate', callback?: (eventInfo: EventInfo) => void): void
```

注销过期更新事件监听。使用callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-off(type: 'expirationUpdate', callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-off(type: 'expirationUpdate', callback?: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'expirationUpdate' | 是 |
| callback | (eventInfo: EventInfo) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## off_keyExpired

```TypeScript
off(type: 'keyExpired', callback?: (eventInfo: EventInfo) => void): void
```

注销密钥过期事件监听。使用callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-off(type: 'keyExpired', callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-off(type: 'keyExpired', callback?: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyExpired' | 是 |
| callback | (eventInfo: EventInfo) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## off_keyRequired

```TypeScript
off(type: 'keyRequired', callback?: (eventInfo: EventInfo) => void): void
```

注销密钥请求事件监听。使用callback异步回调。 该接口用于注销已在on('keyRequired')中注册的监听，当播放DRM节目需要获取媒体密钥时触发的事件。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-off(type: 'keyRequired', callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-off(type: 'keyRequired', callback?: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyRequired' | 是 |
| callback | (eventInfo: EventInfo) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## off_keysChange

```TypeScript
off(type: 'keysChange', callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void
```

注销密钥变化事件监听。使用callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-off(type: 'keysChange', callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void--><!--Device-MediaKeySession-off(type: 'keysChange', callback?: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keysChange' | 是 |
| callback | (keyInfo: KeysInfo[], newKeyAvailable: boolean) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## off_vendorDefined

```TypeScript
off(type: 'vendorDefined', callback?: (eventInfo: EventInfo) => void): void
```

注销DRM解决方案自定义事件监听。使用callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-off(type: 'vendorDefined', callback?: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-off(type: 'vendorDefined', callback?: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'vendorDefined' | 是 |
| callback | (eventInfo: EventInfo) = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## onExpirationUpdate

```TypeScript
onExpirationUpdate(callback: (eventInfo: EventInfo) => void): void
```

Register expirationUpdate event.

**起始版本：** 23

<!--Device-MediaKeySession-onExpirationUpdate(callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-onExpirationUpdate(callback: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## onKeyExpired

```TypeScript
onKeyExpired(callback: (eventInfo: EventInfo) => void): void
```

Register keyExpired event.

**起始版本：** 23

<!--Device-MediaKeySession-onKeyExpired(callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-onKeyExpired(callback: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## onKeyRequired

```TypeScript
onKeyRequired(callback: (eventInfo: EventInfo) => void): void
```

Register keyRequired event.

**起始版本：** 23

<!--Device-MediaKeySession-onKeyRequired(callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-onKeyRequired(callback: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## onKeysChange

```TypeScript
onKeysChange(callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void
```

Register keysChange event.

**起始版本：** 23

<!--Device-MediaKeySession-onKeysChange(callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void--><!--Device-MediaKeySession-onKeysChange(callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (keyInfo: KeysInfo[], newKeyAvailable: boolean) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## onVendorDefined

```TypeScript
onVendorDefined(callback: (eventInfo: EventInfo) => void): void
```

Register vendorDefined event.

**起始版本：** 23

<!--Device-MediaKeySession-onVendorDefined(callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-onVendorDefined(callback: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (eventInfo: EventInfo) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## on_expirationUpdate

```TypeScript
on(type: 'expirationUpdate', callback: (eventInfo: EventInfo) => void): void
```

监听密钥过期更新事件。使用callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-on(type: 'expirationUpdate', callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-on(type: 'expirationUpdate', callback: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'expirationUpdate' | 是 |
| callback | (eventInfo: EventInfo) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## on_keyExpired

```TypeScript
on(type: 'keyExpired', callback: (eventInfo: EventInfo) => void): void
```

监听密钥过期事件。使用callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-on(type: 'keyExpired', callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-on(type: 'keyExpired', callback: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyExpired' | 是 |
| callback | (eventInfo: EventInfo) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## on_keyRequired

```TypeScript
on(type: 'keyRequired', callback: (eventInfo: EventInfo) => void): void
```

监听密钥请求事件。使用callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-on(type: 'keyRequired', callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-on(type: 'keyRequired', callback: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyRequired' | 是 |
| callback | (eventInfo: EventInfo) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## on_keysChange

```TypeScript
on(type: 'keysChange', callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void
```

监听密钥变化事件。使用callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-on(type: 'keysChange', callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void--><!--Device-MediaKeySession-on(type: 'keysChange', callback: (keyInfo: KeysInfo[], newKeyAvailable: boolean) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keysChange' | 是 |
| callback | (keyInfo: KeysInfo[], newKeyAvailable: boolean) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## on_vendorDefined

```TypeScript
on(type: 'vendorDefined', callback: (eventInfo: EventInfo) => void): void
```

监听DRM解决方案自定义事件。使用callback异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-on(type: 'vendorDefined', callback: (eventInfo: EventInfo) => void): void--><!--Device-MediaKeySession-on(type: 'vendorDefined', callback: (eventInfo: EventInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'vendorDefined' | 是 |
| callback | (eventInfo: EventInfo) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## processMediaKeyResponse

```TypeScript
processMediaKeyResponse(response: Uint8Array): Promise<Uint8Array>
```

处理媒体密钥响应。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-processMediaKeyResponse(response: Uint8Array): Promise<Uint8Array>--><!--Device-MediaKeySession-processMediaKeyResponse(response: Uint8Array): Promise<Uint8Array>-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| response | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Uint8Array & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## processOfflineReleaseResponse

```TypeScript
processOfflineReleaseResponse(mediaKeyId: Uint8Array, response: Uint8Array): Promise<void>
```

处理离线媒体密钥释放响应。使用Promise异步回调。 如果设备上的DRM解决方案不支持离线媒体密钥释放，将抛出错误码24700101。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-processOfflineReleaseResponse(mediaKeyId: Uint8Array, response: Uint8Array): Promise<void>--><!--Device-MediaKeySession-processOfflineReleaseResponse(mediaKeyId: Uint8Array, response: Uint8Array): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mediaKeyId | Uint8Array | 是 |
| response | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## requireSecureDecoderModule

```TypeScript
requireSecureDecoderModule(mimeType: string): boolean
```

是否需要安全解码。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-requireSecureDecoderModule(mimeType: string): boolean--><!--Device-MediaKeySession-requireSecureDecoderModule(mimeType: string): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mimeType | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |

## restoreOfflineMediaKeys

```TypeScript
restoreOfflineMediaKeys(mediaKeyId: Uint8Array): Promise<void>
```

恢复离线媒体密钥。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySession-restoreOfflineMediaKeys(mediaKeyId: Uint8Array): Promise<void>--><!--Device-MediaKeySession-restoreOfflineMediaKeys(mediaKeyId: Uint8Array): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mediaKeyId | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24700201](../errorcode-drm.md#24700201-服务异常) |
| [24700101](../errorcode-drm.md#24700101-未知错误) |
