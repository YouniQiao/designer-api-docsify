# UIExtensionProxy (System API)

This interface is used for send data to the UIExtensionAbility.&lt;br/&gt;It is returned from onRemoteReady callback of UIExtensionComponent&lt;br/&gt;when UIExtensionAbility connects successfully

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface UIExtensionProxy--><!--Device-unnamed-export declare interface UIExtensionProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## offAsyncReceiverRegister

```TypeScript
offAsyncReceiverRegister(callback?: Callback<UIExtensionProxy>): void
```

Deregisters the listener that watches for async data receiver callback being registered by UIExtensionAbility.AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-offAsyncReceiverRegister(callback?: Callback<UIExtensionProxy>): void--><!--Device-UIExtensionProxy-offAsyncReceiverRegister(callback?: Callback<UIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[UIExtensionProxy](arkts-arkui-uiextensioncomponent-uiextensionproxy-i-sys.md)&gt; | No | Callback of the listened event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |

## offSyncReceiverRegister

```TypeScript
offSyncReceiverRegister(callback?: Callback<UIExtensionProxy>): void
```

Deregisters the listener that watches for sync data receiver callback being registered by UIExtensionAbility.AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-offSyncReceiverRegister(callback?: Callback<UIExtensionProxy>): void--><!--Device-UIExtensionProxy-offSyncReceiverRegister(callback?: Callback<UIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[UIExtensionProxy](arkts-arkui-uiextensioncomponent-uiextensionproxy-i-sys.md)&gt; | No | Callback of the listened event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |

## onAsyncReceiverRegister

```TypeScript
onAsyncReceiverRegister(callback: Callback<UIExtensionProxy>): void
```

Register the listener that watches for async data receiver callback being registered by UIExtensionAbility.AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-onAsyncReceiverRegister(callback: Callback<UIExtensionProxy>): void--><!--Device-UIExtensionProxy-onAsyncReceiverRegister(callback: Callback<UIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[UIExtensionProxy](arkts-arkui-uiextensioncomponent-uiextensionproxy-i-sys.md)&gt; | Yes | Callback of the listened event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |

## onSyncReceiverRegister

```TypeScript
onSyncReceiverRegister(callback: Callback<UIExtensionProxy>): void
```

Register the listener that watches for sync data receiver callback being registered by UIExtensionAbility.AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-onSyncReceiverRegister(callback: Callback<UIExtensionProxy>): void--><!--Device-UIExtensionProxy-onSyncReceiverRegister(callback: Callback<UIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[UIExtensionProxy](arkts-arkui-uiextensioncomponent-uiextensionproxy-i-sys.md)&gt; | Yes | Callback of the listened event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |

## send

```TypeScript
send(data: Record<string, RecordData>): void
```

This function is for sending data to the UIExtensionAbility.AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-send(data: Record<string, RecordData>): void--><!--Device-UIExtensionProxy-send(data: Record<string, RecordData>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |

## sendSync

```TypeScript
sendSync(data: Record<string, RecordData>): Record<string, RecordData>
```

This function is for sending data to the UIExtensionAbility and waiting for the result in blocking mode.AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionProxy-sendSync(data: Record<string, RecordData>): Record<string, RecordData>--><!--Device-UIExtensionProxy-sendSync(data: Record<string, RecordData>): Record<string, RecordData>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes | Data send to the UIExtensionAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | data - Data transferred from the UIExtensionAbility. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100011](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-uiextension.md#100011-no-synchronous-callback-registered) | No callback has been registered to respond to this request. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |
| [100012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-uiextension.md#100012-data-transfer-failure) | Transferring data failed. |

