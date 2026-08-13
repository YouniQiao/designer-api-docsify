# offRotate (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from '@kit.InputKit';
```

## offRotate

```TypeScript
function offRotate(fingers: number, receiver?: Callback<Rotate>): void
```

Cancel listening for touchPad fingers rotate events.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function offRotate(fingers: int, receiver?: Callback<Rotate>): void--><!--Device-inputMonitor-function offRotate(fingers: int, receiver?: Callback<Rotate>): void-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fingers | number | Yes |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Rotate](arkts-input-multimodalinput-gestureevent-rotate-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
