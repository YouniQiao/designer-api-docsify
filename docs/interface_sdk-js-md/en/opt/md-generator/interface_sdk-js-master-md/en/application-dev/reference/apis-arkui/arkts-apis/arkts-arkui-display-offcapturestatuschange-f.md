# offCaptureStatusChange

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## offCaptureStatusChange

```TypeScript
function offCaptureStatusChange(callback?: Callback<boolean>): void
```

Unregister the callback for the status of the device's screen content is being captured.

**Since:** 23

**Deprecated since:** -1

<!--Device-display-function offCaptureStatusChange(callback?: Callback<boolean>): void--><!--Device-display-function offCaptureStatusChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
