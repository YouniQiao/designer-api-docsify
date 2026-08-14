# on_cooperateMouse (System API)

## Modules to Import

```TypeScript
import { cooperate } from 'cooperate';
```

## on_cooperateMouse

```TypeScript
function on(type: 'cooperateMouse', networkId: string, callback: Callback<MouseLocation>): void
```

Registers a listener for the mouse cursor position of a device.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function on(type: 'cooperateMouse', networkId: string, callback: Callback<MouseLocation>): void--><!--Device-cooperate-function on(type: 'cooperateMouse', networkId: string, callback: Callback<MouseLocation>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cooperateMouse' | Yes | Event type, which is **'cooperateMouse'**. |
| networkId | string | Yes | Descriptor of the target device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MouseLocation](arkts-distributedservice-cooperate-mouselocation-i-sys.md)&gt; | Yes | Callback used to return the mouse cursor position of the device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified. <br>2.Incorrect parameter types. <br>3.Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

