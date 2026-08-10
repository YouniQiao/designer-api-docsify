# onCooperateMouseEvent (System API)

## Modules to Import

```TypeScript
import { cooperate } from 'kits/@kit.DistributedServiceKit';
```

## onCooperateMouseEvent

```TypeScript
function onCooperateMouseEvent(networkId: string, callback: Callback<MouseLocation>): void
```

Enables listening for mouse pointer position information on the specified device for cooperation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function onCooperateMouseEvent(networkId: string, callback: Callback<MouseLocation>): void--><!--Device-cooperate-function onCooperateMouseEvent(networkId: string, callback: Callback<MouseLocation>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | string | Yes | Specified device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MouseLocation&gt; | Yes | Callback for receiving reported events. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| 201 | Permission denied. |
| 202 | Permission verification failed. A non-system application calls a system API. |

