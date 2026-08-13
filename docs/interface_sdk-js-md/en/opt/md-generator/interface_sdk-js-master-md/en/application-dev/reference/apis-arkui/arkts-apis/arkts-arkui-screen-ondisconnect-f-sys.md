# onDisconnect (System API)

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
```

## onDisconnect

```TypeScript
function onDisconnect(callback: Callback<number>): void
```

Register the callback for screen disconnection events.

**Since:** 23

**Deprecated since:** -1

<!--Device-screen-function onDisconnect(callback: Callback<long>): void--><!--Device-screen-function onDisconnect(callback: Callback<long>): void-End-->

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
