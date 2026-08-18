# onPrivateModeChange (System API)

## Modules to Import

```TypeScript
```

## onPrivateModeChange

```TypeScript
function onPrivateModeChange(callback: Callback<boolean>): void
```

Register the callback for private mode changes.

**Since:** 23

<!--Device-display-function onPrivateModeChange(callback: Callback<boolean>): void--><!--Device-display-function onPrivateModeChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
