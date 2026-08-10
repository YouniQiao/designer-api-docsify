# SecurityUIExtensionProxy (System API)

用于在双方建立连接成功后，向被拉起的Ability发送数据，以及订阅和取消订阅事件回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface SecurityUIExtensionProxy--><!--Device-unnamed-export declare interface SecurityUIExtensionProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## offAsyncReceiverRegister

```TypeScript
offAsyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void
```

取消订阅被拉起的Ability发生异步注册的回调。使用callback异步回调。AnonyMous Object Rectification

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionProxy-offAsyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void--><!--Device-SecurityUIExtensionProxy-offAsyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-arkui-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; | No | 回调函数。为空代表取消订阅所有扩展Ability异步注册后触发回调。非空代表取消订阅异步对应回调。 ArkTS-Sta模式下，可传入undefined，表示取消所有回调。 |

## offSyncReceiverRegister

```TypeScript
offSyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void
```

取消订阅被拉起的Ability发生同步注册的回调。使用callback异步回调。AnonyMous Object Rectification

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionProxy-offSyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void--><!--Device-SecurityUIExtensionProxy-offSyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-arkui-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; | No | 回调函数。为空代表取消订阅所有扩展Ability同步注册后触发回调。非空代表取消订阅同步对应回调。 ArkTS-Sta模式下，可传入undefined，表示取消所有回调。 |

## onAsyncReceiverRegister

```TypeScript
onAsyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void
```

订阅被拉起的Ability发生异步注册的回调。使用callback异步回调。AnonyMous Object Rectification

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionProxy-onAsyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void--><!--Device-SecurityUIExtensionProxy-onAsyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-arkui-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; | Yes | 回调函数。订阅扩展Ability注册setReceiveDataCallback后触发的回调。 |

## onSyncReceiverRegister

```TypeScript
onSyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void
```

订阅被拉起的Ability发生同步注册的回调。使用callback异步回调。AnonyMous Object Rectification

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionProxy-onSyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void--><!--Device-SecurityUIExtensionProxy-onSyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-arkui-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; | Yes | 回调函数。扩展Ability注册setReceiveDataForResultCallback后触发的回调。 |

## send

```TypeScript
send(data: Record<string, RecordData>): void
```

用于在双方建立连接成功后，向被拉起的Ability发送数据，提供异步发送能力。数据将被扩展Ability通过setReceiveDataCallback接收处理。AnonyMous Object Rectification

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionProxy-send(data: Record<string, RecordData>): void--><!--Device-SecurityUIExtensionProxy-send(data: Record<string, RecordData>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, RecordData&gt; | Yes | 异步发送给被拉起的Ability的数据。 |

## sendSync

```TypeScript
sendSync(data: Record<string, RecordData>): Record<string, RecordData>
```

用于在双方建立连接成功后，向被拉起的Ability同步发送数据，数据将被拉起的Ability通过setReceiveDataForResultCallback处理并返回结果。AnonyMous Object Rectification

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionProxy-sendSync(data: Record<string, RecordData>): Record<string, RecordData>--><!--Device-SecurityUIExtensionProxy-sendSync(data: Record<string, RecordData>): Record<string, RecordData>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, RecordData&gt; | Yes | 同步发送给被拉起的Ability的数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, RecordData&gt; | data - 被拉起的Ability对同步发送请求处理后返回的响应数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100011 | 没有注册响应该请求的回调。 |
| 100012 | 传输数据失败。 |

