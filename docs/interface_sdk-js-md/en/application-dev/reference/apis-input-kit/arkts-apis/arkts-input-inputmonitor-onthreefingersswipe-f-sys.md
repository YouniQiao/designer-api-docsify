# onThreeFingersSwipe (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from 'inputMonitor';
```

## onThreeFingersSwipe

```TypeScript
function onThreeFingersSwipe(receiver: Callback<ThreeFingersSwipe>): void
```

Listens for touchPad three fingers swipe events.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onThreeFingersSwipe(receiver: Callback<ThreeFingersSwipe>): void--><!--Device-inputMonitor-function onThreeFingersSwipe(receiver: Callback<ThreeFingersSwipe>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ThreeFingersSwipe](arkts-input-multimodalinput-gestureevent-threefingersswipe-i.md)&gt; | Yes | Callback used to receive the reported data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | SystemAPI permit error. |

