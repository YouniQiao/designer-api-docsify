# onConnect (System API)

## Modules to Import

```TypeScript
```

## onConnect

```TypeScript
function onConnect(callback: Callback<number>): void
```

Register the callback for screen connection events.

**Since:** 23

<!--Device-screen-function onConnect(callback: Callback<long>): void--><!--Device-screen-function onConnect(callback: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
