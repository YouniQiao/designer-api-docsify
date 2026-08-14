# onFoldDisplayModeChange

## Modules to Import

```TypeScript
import { display } from 'display';
```

## onFoldDisplayModeChange

```TypeScript
function onFoldDisplayModeChange(callback: Callback<FoldDisplayMode>): void
```

Register the callback for fold display mode changes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-display-function onFoldDisplayModeChange(callback: Callback<FoldDisplayMode>): void--><!--Device-display-function onFoldDisplayModeChange(callback: Callback<FoldDisplayMode>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md)&gt; | Yes | Callback used to return the current fold display mode |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

