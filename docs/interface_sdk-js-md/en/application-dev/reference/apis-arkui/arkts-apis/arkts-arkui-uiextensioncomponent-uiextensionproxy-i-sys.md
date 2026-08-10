# UIExtensionProxy (System API)

用于在双方建立连接成功后，组件使用方将数据发送给被拉起的Ability，并订阅和取消订阅扩展Ability的注册事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface UIExtensionProxy--><!--Device-unnamed-export declare interface UIExtensionProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## offAsyncReceiverRegister

```TypeScript
offAsyncReceiverRegister(callback?: Callback<UIExtensionProxy>): void
```

注销监听UIExtensionAbility注册异步数据接收回调的监听器。AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-offAsyncReceiverRegister(callback?: Callback<UIExtensionProxy>): void--><!--Device-UIExtensionProxy-offAsyncReceiverRegister(callback?: Callback<UIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIExtensionProxy&gt; | No | 监听事件的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | 非系统应用不允许使用系统API。 |

## offSyncReceiverRegister

```TypeScript
offSyncReceiverRegister(callback?: Callback<UIExtensionProxy>): void
```

注销监听UIExtensionAbility注册同步数据接收回调的监听器。AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-offSyncReceiverRegister(callback?: Callback<UIExtensionProxy>): void--><!--Device-UIExtensionProxy-offSyncReceiverRegister(callback?: Callback<UIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIExtensionProxy&gt; | No | 监听事件的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | 非系统应用不允许使用系统API。 |

## onAsyncReceiverRegister

```TypeScript
onAsyncReceiverRegister(callback: Callback<UIExtensionProxy>): void
```

注册监听器，用于监听UIExtensionAbility注册异步数据接收回调。AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-onAsyncReceiverRegister(callback: Callback<UIExtensionProxy>): void--><!--Device-UIExtensionProxy-onAsyncReceiverRegister(callback: Callback<UIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIExtensionProxy&gt; | Yes | 监听事件的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | 非系统应用不允许使用系统API。 |

## onSyncReceiverRegister

```TypeScript
onSyncReceiverRegister(callback: Callback<UIExtensionProxy>): void
```

注册监听器，用于监听UIExtensionAbility注册同步数据接收回调。AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-onSyncReceiverRegister(callback: Callback<UIExtensionProxy>): void--><!--Device-UIExtensionProxy-onSyncReceiverRegister(callback: Callback<UIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;UIExtensionProxy&gt; | Yes | 监听事件的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | 非系统应用不允许使用系统API。 |

## send

```TypeScript
send(data: Record<string, RecordData>): void
```

用于在双方建立连接成功后，组件使用方将数据发送给被拉起的Ability的场景，提供异步发送数据。AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-send(data: Record<string, RecordData>): void--><!--Device-UIExtensionProxy-send(data: Record<string, RecordData>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, RecordData&gt; | Yes | 异步发送给被拉起的UIExtensionAbility的数据。API version 18之前的版本，data的类型为Object。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | 非系统应用不允许使用系统API。 |

## sendSync

```TypeScript
sendSync(data: Record<string, RecordData>): Record<string, RecordData>
```

用于在双方建立连接成功后，组件使用方将数据发送给被拉起的Ability的场景，提供同步发送数据。AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-sendSync(data: Record<string, RecordData>): Record<string, RecordData>--><!--Device-UIExtensionProxy-sendSync(data: Record<string, RecordData>): Record<string, RecordData>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, RecordData&gt; | Yes | 同步发送给被拉起的UIExtensionAbility的数据。API version 18之前的版本，data的类型为Object。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, RecordData&gt; | data - 扩展Ability回复的数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100011 | 没有注册响应该请求的回调。 |
| 202 | 非系统应用不允许使用系统API。 |
| 100012 | 传输数据失败。 |

