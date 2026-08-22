# onConnect (System API)

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
import { screenshot } from '@kit.ArkUI';
```

## onConnect

```TypeScript
function onConnect(callback: Callback<long>): void
```

Register the callback for screen connection events.

**Since:** 23

<!--Device-screen-function onConnect(callback: Callback<long>): void--><!--Device-screen-function onConnect(callback: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | Callback used to return the screen ID. This parameter is callable. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

