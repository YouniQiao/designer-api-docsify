# PiPController

Implements a PiP controller that starts, stops, or updates a PiP window and registers callbacks. Before calling any of the following APIs, you must use [PiPWindow.create()](arkts-arkui-pipwindow-create-f.md#create) to create a PiPController instance.

**Since:** 26.0.0

<!--Device-PiPWindow-interface PiPController--><!--Device-PiPWindow-interface PiPController-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
```

## isPiPSupported

```TypeScript
isPiPSupported(): boolean
```

Returns a Boolean value that indicates whether picture-in-picture is supported

**Since:** 26.0.0

<!--Device-PiPController-isPiPSupported(): boolean--><!--Device-PiPController-isPiPSupported(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1300014](../errorcode-window.md#1300014-pip-internal-error) |
