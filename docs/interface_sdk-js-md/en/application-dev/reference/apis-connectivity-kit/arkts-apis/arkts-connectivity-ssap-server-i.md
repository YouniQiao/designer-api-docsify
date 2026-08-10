# Server

管理SSAP服务端。在调用SSAP服务端方法之前，必须使用{@link createServer}创建SSAP服务端实例。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-ssap-interface Server--><!--Device-ssap-interface Server-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from 'kits/@kit.ConnectivityKit';
```

## addService

```TypeScript
addService(service: Service): void
```

添加SSAP服务。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-addService(service: Service): void--><!--Device-Server-addService(service: Service): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| service | [Service](arkts-connectivity-ssap-service-i.md) | Yes | 需要添加并注册ssap服务 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 36100044 | NearLink standard UUID not allowed. |
| 36100043 | Invalid UUID. |

## close

```TypeScript
close(): void
```

关闭此{@code Server}对象并注销其回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-close(): void--><!--Device-Server-close(): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |

## notifyPropertyChanged

```TypeScript
notifyPropertyChanged(address: string, property: Property): Promise<void>
```

通知客户端此服务端的属性值发生了变化。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-notifyPropertyChanged(address: string, property: Property): Promise<void>--><!--Device-Server-notifyPropertyChanged(address: string, property: Property): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| address | string | Yes | 设备地址。 &lt;br&gt;长度必须为17，由16进制数字和冒号组成，形如 "11:22:33:AA:BB:FF"。 |
| property | [Property](arkts-connectivity-ssap-property-i.md) | Yes | 指示要通知的属性 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 返回promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 36100044 | NearLink standard UUID not allowed. |
| 36100043 | Invalid UUID in property. |
| 36100041 | Invalid address. |

## offConnectionStateChange

```TypeScript
offConnectionStateChange(callback?: Callback<ConnectionChangeState>): void
```

取消订阅服务器连接状态更改事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-offConnectionStateChange(callback?: Callback<ConnectionChangeState>): void--><!--Device-Server-offConnectionStateChange(callback?: Callback<ConnectionChangeState>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ConnectionChangeState&gt; | No | 用于监听连接状态改变事件的回调。 |

## offMtuChange

ArkTS-Dyn:
```TypeScript
offMtuChange(callback?: Callback<number>): void
```

ArkTS-Sta:
```TypeScript
offMtuChange(callback?: Callback<int>): void
```

取消订阅MTU更改事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-offMtuChange(callback?: Callback<int>): void--><!--Device-Server-offMtuChange(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ArkTS-Dyn: [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | No | 用于监听mtu变化事件的回调。 |

## offPropertyRead

```TypeScript
offPropertyRead(callback?: Callback<PropertyReadRequest>): void
```

取消订阅来自客户端的属性读取事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-offPropertyRead(callback?: Callback<PropertyReadRequest>): void--><!--Device-Server-offPropertyRead(callback?: Callback<PropertyReadRequest>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PropertyReadRequest&gt; | No | 用于监听属性操作事件的回调。 |

## offPropertyWrite

```TypeScript
offPropertyWrite(callback?: Callback<PropertyWriteRequest>): void
```

取消订阅来自客户端的属性写入事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-offPropertyWrite(callback?: Callback<PropertyWriteRequest>): void--><!--Device-Server-offPropertyWrite(callback?: Callback<PropertyWriteRequest>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PropertyWriteRequest&gt; | No | 用于监听属性操作事件的回调。 |

## onConnectionStateChange

```TypeScript
onConnectionStateChange(callback: Callback<ConnectionChangeState>): void
```

订阅服务器连接状态更改事件。

只有授予了ohos.permission.NEARLINK_ACCESS权限的应用程序才能访问此事件。如果应用被赋予了ohos.permission.GET_NEARLINK_PEER_MAC权限。回调返回真实设备地址，否则返回随机设备地址。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-onConnectionStateChange(callback: Callback<ConnectionChangeState>): void--><!--Device-Server-onConnectionStateChange(callback: Callback<ConnectionChangeState>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ConnectionChangeState&gt; | Yes | 用于监听连接状态改变事件的回调。 |

## onMtuChange

ArkTS-Dyn:
```TypeScript
onMtuChange(callback: Callback<number>): void
```

ArkTS-Sta:
```TypeScript
onMtuChange(callback: Callback<int>): void
```

订阅MTU变化事件。

只有授予了ohos.permission.NEARLINK_ACCESS权限的应用程序才能访问此事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-onMtuChange(callback: Callback<int>): void--><!--Device-Server-onMtuChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ArkTS-Dyn: [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | 用于监听mtu变化事件的回调。 |

## onPropertyRead

```TypeScript
onPropertyRead(callback: Callback<PropertyReadRequest>): void
```

从客户端订阅属性读取事件。

只有授予了ohos.permission.NEARLINK_ACCESS权限的应用程序才能访问此事件。如果应用被赋予了ohos.permission.GET_NEARLINK_PEER_MAC权限。回调返回真实设备地址，否则返回随机设备地址。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-onPropertyRead(callback: Callback<PropertyReadRequest>): void--><!--Device-Server-onPropertyRead(callback: Callback<PropertyReadRequest>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PropertyReadRequest&gt; | Yes | 用于监听属性操作事件的回调。 |

## onPropertyWrite

```TypeScript
onPropertyWrite(callback: Callback<PropertyWriteRequest>): void
```

从客户端订阅属性写入事件。

只有授予了ohos.permission.NEARLINK_ACCESS权限的应用程序才能访问此事件。如果应用被赋予了ohos.permission.GET_NEARLINK_PEER_MAC权限。回调返回真实设备地址，否则返回随机设备地址。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-onPropertyWrite(callback: Callback<PropertyWriteRequest>): void--><!--Device-Server-onPropertyWrite(callback: Callback<PropertyWriteRequest>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PropertyWriteRequest&gt; | Yes | 用于监听属性操作事件的回调。 |

## removeService

```TypeScript
removeService(serviceUuid: string): void
```

删除指定的SSAP服务。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-removeService(serviceUuid: string): void--><!--Device-Server-removeService(serviceUuid: string): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| serviceUuid | string | Yes | 要删除的特定SSAP服务 &lt;br&gt;长度必须为36，由16进制数字字符和连字符共36个字符组成，形如“FFFFFFFF-1234-5678-ABCD-000000001234”，代表128比特标识。 &lt;br&gt;禁止使用星闪标准服务UUID。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 36100044 | NearLink standard UUID not allowed. |
| 36100043 | Invalid UUID. |

## sendResponse

```TypeScript
sendResponse(response: ServerResponse): void
```

响应客户端的读或写请求。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-Server-sendResponse(response: ServerResponse): void--><!--Device-Server-sendResponse(response: ServerResponse): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| response | [ServerResponse](arkts-connectivity-bluetoothmanager-serverresponse-i.md) | Yes | 表示响应。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| 201 | Permission denied. |
| 36100041 | Invalid address. |

