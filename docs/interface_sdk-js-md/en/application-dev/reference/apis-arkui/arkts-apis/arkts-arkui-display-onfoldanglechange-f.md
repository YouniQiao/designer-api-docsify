# onFoldAngleChange

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## onFoldAngleChange

```TypeScript
function onFoldAngleChange(callback: Callback<Array<double>>): void
```

Register the callback for fold angle changes.

**Since:** 23

<!--Device-display-function onFoldAngleChange(callback: Callback<Array<double>>): void--><!--Device-display-function onFoldAngleChange(callback: Callback<Array<double>>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;double&gt;&gt; | Yes | Callback used to return the current fold angle of device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

