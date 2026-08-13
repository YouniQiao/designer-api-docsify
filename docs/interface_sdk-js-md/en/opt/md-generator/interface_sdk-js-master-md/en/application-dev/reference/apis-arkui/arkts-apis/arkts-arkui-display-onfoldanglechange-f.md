# onFoldAngleChange

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## onFoldAngleChange

```TypeScript
function onFoldAngleChange(callback: Callback<Array<number>>): void
```

Register the callback for fold angle changes.

**Since:** 23

**Deprecated since:** -1

<!--Device-display-function onFoldAngleChange(callback: Callback<Array<double>>): void--><!--Device-display-function onFoldAngleChange(callback: Callback<Array<double>>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;number&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
