# addVirtualScreenSurface (System API)

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## addVirtualScreenSurface

```TypeScript
function addVirtualScreenSurface(screenId: long, surfaceId: string, surfaceRegion?: Rect): Promise<void>
```

Add surface for the virtual screen.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-display-function addVirtualScreenSurface(screenId: long, surfaceId: string, surfaceRegion?: Rect): Promise<void>--><!--Device-display-function addVirtualScreenSurface(screenId: long, surfaceId: string, surfaceRegion?: Rect): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| screenId | long | Yes | Indicates the screen id of the virtual screen. |
| surfaceId | string | Yes | ID of the surface bound to the virtual screen. You can use the getXComponentSurfaceId method to obtain the ID of the surface corresponding to an existing surface. The maximum length for this parameter is 4096 bytes. If it goes beyond that, only the first 4096 bytes are used. |
| surfaceRegion | Rect | No | Rectangular area of the virtual screen displayed by the surface. If the virtual screen has not bound any surface via [setVirtualScreenSurface()](arkts-arkui-display-setvirtualscreensurface-f.md) or [addVirtualScreenSurface()](#addvirtualscreensurface-system-api), the surfaceRegion is invalid and defaults to full screen. In mirror mode, the surfaceRegion is invalid and defaults to full screen. In independent display mode, the surfaceRegion is valid. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |
| [1400004](../errorcode-display.md#1400004-parameter-error) | Parameter error. Possible cause: 1. Invalid parameter range. |

