# onAttachmentDidFail

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## onAttachmentDidFail

```TypeScript
function onAttachmentDidFail(callback: Callback<AttachFailureReason>): void
```

Subscribes to attachment failure events. This API uses an asynchronous callback to return the result.

**Since:** 22

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AttachFailureReason](arkts-ime-inputmethod-attachfailurereason-e.md)&gt; | Yes |
