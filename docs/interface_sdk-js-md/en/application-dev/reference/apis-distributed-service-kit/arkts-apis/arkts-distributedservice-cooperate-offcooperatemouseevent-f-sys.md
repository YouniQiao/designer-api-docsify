# offCooperateMouseEvent (System API)

## Modules to Import

```TypeScript
import { cooperate } from '@kit.DistributedServiceKit';
```

## offCooperateMouseEvent

```TypeScript
function offCooperateMouseEvent(networkId: string, callback?: Callback<MouseLocation>): void
```

Disables listening for mouse pointer position information on the specified device for cooperation.

**Since:** 23

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function offCooperateMouseEvent(networkId: string, callback?: Callback<MouseLocation>): void--><!--Device-cooperate-function offCooperateMouseEvent(networkId: string, callback?: Callback<MouseLocation>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | string | Yes | Specified device. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MouseLocation](arkts-distributedservice-cooperate-mouselocation-i-sys.md)&gt; | No | Callback for receiving reported events. <br> If no callback is specified, listening will be disabled for all **cooperateMouse**. <br> events of the device specified by **networkId**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. <br>3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

