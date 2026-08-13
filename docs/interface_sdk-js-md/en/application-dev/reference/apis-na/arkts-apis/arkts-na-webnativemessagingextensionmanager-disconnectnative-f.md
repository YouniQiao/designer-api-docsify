# disconnectNative

## disconnectNative

```TypeScript
function disconnectNative(connectionId: int): Promise<void>
```

Disconnects the connection of a specified web native message extension.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.WEB_NATIVE_MESSAGING

**Model restriction:** This API can be used only in the stage model.

<!--Device-webNativeMessagingExtensionManager-function disconnectNative(connectionId: int): Promise<void>--><!--Device-webNativeMessagingExtensionManager-function disconnectNative(connectionId: int): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connectionId | int | Yes | Connection ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

