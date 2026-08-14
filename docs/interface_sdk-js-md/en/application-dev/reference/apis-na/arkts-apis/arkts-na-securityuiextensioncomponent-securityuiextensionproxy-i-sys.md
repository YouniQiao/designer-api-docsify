# SecurityUIExtensionProxy (System API)

This interface is used for send data to the UIExtensionAbility.<br/> It is returned from onRemoteReady callback of SecurityUIExtensionComponent<br/> when UIExtensionAbility connects successfully

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface SecurityUIExtensionProxy--><!--Device-unnamed-export declare interface SecurityUIExtensionProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## offAsyncReceiverRegister

```TypeScript
offAsyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void
```

Deregisters the listener that watches for async data receiver callback being registered by UIExtensionAbility. AnonyMous Object Rectification

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionProxy-offAsyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void--><!--Device-SecurityUIExtensionProxy-offAsyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-na-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; | No | Callback of the listened event. |

## offSyncReceiverRegister

```TypeScript
offSyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void
```

Deregisters the listener that watches for sync data receiver callback being registered by UIExtensionAbility. AnonyMous Object Rectification

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionProxy-offSyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void--><!--Device-SecurityUIExtensionProxy-offSyncReceiverRegister(callback?: Callback<SecurityUIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-na-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; | No | Callback of the listened event. |

## onAsyncReceiverRegister

```TypeScript
onAsyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void
```

Register the listener that watches for async data receiver callback being registered by UIExtensionAbility. AnonyMous Object Rectification

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionProxy-onAsyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void--><!--Device-SecurityUIExtensionProxy-onAsyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-na-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; | Yes | Callback of the listened event. |

## onSyncReceiverRegister

```TypeScript
onSyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void
```

Register the listener that watches for sync data receiver callback being registered by UIExtensionAbility. AnonyMous Object Rectification

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionProxy-onSyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void--><!--Device-SecurityUIExtensionProxy-onSyncReceiverRegister(callback: Callback<SecurityUIExtensionProxy>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SecurityUIExtensionProxy](arkts-na-securityuiextensioncomponent-securityuiextensionproxy-i-sys.md)&gt; | Yes | Callback of the listened event. |

## send

```TypeScript
send(data: Record<string, RecordData>): void
```

This function is for sending data to the UIExtensionAbility. AnonyMous Object Rectification

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionProxy-send(data: Record<string, RecordData>): void--><!--Device-SecurityUIExtensionProxy-send(data: Record<string, RecordData>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes |  |

## sendSync

```TypeScript
sendSync(data: Record<string, RecordData>): Record<string, RecordData>
```

This function is for sending data to the UIExtensionAbility and waiting for the result in blocking mode. AnonyMous Object Rectification

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityUIExtensionProxy-sendSync(data: Record<string, RecordData>): Record<string, RecordData>--><!--Device-SecurityUIExtensionProxy-sendSync(data: Record<string, RecordData>): Record<string, RecordData>-End-->

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
| [100011](../../apis-arkui/errorcode-uiextension.md#100011-no-synchronous-callback-registered) | No callback has been registered to respond to this request. |
| [100012](../../apis-arkui/errorcode-uiextension.md#100012-data-transfer-failure) | Transferring data failed. |

