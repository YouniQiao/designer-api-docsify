# onBrightnessInfoChange

## onBrightnessInfoChange

```TypeScript
function onBrightnessInfoChange(callback: BrightnessCallback<long, BrightnessInfo>): void
```

Register the callback for brightness info changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-display-function onBrightnessInfoChange(callback: BrightnessCallback<long, BrightnessInfo>): void--><!--Device-display-function onBrightnessInfoChange(callback: BrightnessCallback<long, BrightnessInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;long, BrightnessInfo&gt; | Yes | Callback used to return the display if and corresponding brightness info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |
| [1400004](../errorcode-display.md#1400004-parameter-error) | Parameter error. Possible cause: 1. Invalid parameter range. |

