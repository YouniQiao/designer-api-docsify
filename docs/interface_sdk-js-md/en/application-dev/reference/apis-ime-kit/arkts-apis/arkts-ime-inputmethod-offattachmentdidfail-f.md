# offAttachmentDidFail

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## offAttachmentDidFail

```TypeScript
function offAttachmentDidFail(callback?: Callback<AttachFailureReason>): void
```

Unsubscribe the attachment failure event.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-inputMethod-function offAttachmentDidFail(callback?: Callback<AttachFailureReason>): void--><!--Device-inputMethod-function offAttachmentDidFail(callback?: Callback<AttachFailureReason>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachFailureReason&gt; | No | the callback is invoked only when the attachment triggered by the registrant's process fails. When subscriber unsubscribes all callback, this parameter can be left blank. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let attachmentDidFailCallback: Callback<inputMethod.AttachFailureReason> = 
  (reason: inputMethod.AttachFailureReason): void => {
    console.info(`Attachment failed with reason: ${reason}.`);
  if (reason === inputMethod.AttachFailureReason.CALLER_NOT_FOCUSED) {
    console.info(`Failure reason is CALLER_NOT_FOCUSED.`);
  }
  };
inputMethod.onAttachmentDidFail(attachmentDidFailCallback);
inputMethod.offAttachmentDidFail(attachmentDidFailCallback);
```

