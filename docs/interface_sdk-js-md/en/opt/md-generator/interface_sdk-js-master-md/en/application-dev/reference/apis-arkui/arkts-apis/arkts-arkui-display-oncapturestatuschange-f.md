# onCaptureStatusChange

## Modules to Import

```TypeScript
```

## onCaptureStatusChange

```TypeScript
function onCaptureStatusChange(callback: Callback<boolean>): void
```

Register the callback for the status of the device's screen content is being captured.

**Since:** 23

<!--Device-display-function onCaptureStatusChange(callback: Callback<boolean>): void--><!--Device-display-function onCaptureStatusChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
