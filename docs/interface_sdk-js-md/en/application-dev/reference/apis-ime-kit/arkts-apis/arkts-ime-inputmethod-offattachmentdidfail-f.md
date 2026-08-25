# offAttachmentDidFail

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## offAttachmentDidFail

```TypeScript
function offAttachmentDidFail(callback?: Callback<AttachFailureReason>): void
```

Unsubscribes from attachment failure events. This API uses an asynchronous callback to return the result.

**Since:** 22

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AttachFailureReason](arkts-ime-inputmethod-attachfailurereason-e.md)&gt; | No |
