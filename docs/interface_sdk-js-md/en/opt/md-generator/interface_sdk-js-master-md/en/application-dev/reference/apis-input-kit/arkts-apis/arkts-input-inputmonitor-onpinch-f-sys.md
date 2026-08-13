# onPinch (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from '@kit.InputKit';
```

## onPinch

```TypeScript
function onPinch(receiver: Callback<Pinch>): void
```

Listens for touchPad pinch events.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onPinch(receiver: Callback<Pinch>): void--><!--Device-inputMonitor-function onPinch(receiver: Callback<Pinch>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Pinch](arkts-input-multimodalinput-gestureevent-pinch-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## onPinch

```TypeScript
function onPinch(fingers: number, receiver: Callback<Pinch>): void
```

Listens for touchPad fingers pinch events.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onPinch(fingers: int, receiver: Callback<Pinch>): void--><!--Device-inputMonitor-function onPinch(fingers: int, receiver: Callback<Pinch>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fingers | number | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Pinch](arkts-input-multimodalinput-gestureevent-pinch-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
