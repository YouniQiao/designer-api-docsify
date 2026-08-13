# onBrightnessInfoChange

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## onBrightnessInfoChange

```TypeScript
function onBrightnessInfoChange(callback: BrightnessCallback<number, BrightnessInfo>): void
```

Register the callback for brightness info changes.

**Since:** 23

**Deprecated since:** -1

<!--Device-display-function onBrightnessInfoChange(callback: BrightnessCallback<long, BrightnessInfo>): void--><!--Device-display-function onBrightnessInfoChange(callback: BrightnessCallback<long, BrightnessInfo>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [BrightnessCallback](arkts-arkui-display-brightnesscallback-t.md)&lt;number, [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1400004](../errorcode-display.md#1400004-parameter-error) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
