# createWindow

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## createWindow

```TypeScript
function createWindow(config: Configuration, callback: AsyncCallback<Window>): void
```

Creates a child window or system window. This API uses an asynchronous callback to return the result.In non-[freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, the child window created uses an [immersive layout](../../../windowmanager/window-terminology.md#immersive-layout) by default.In freeform window mode, the child window created uses an immersive layout when [decorEnabled](arkts-arkui-window-configuration-i.md) is set to **false**, and it uses a non-immersive layout when this parameter is set to **true**.

**Since:** 9

**Required permissions:** 
- API version 12+: ohos.permission.SYSTEM_FLOAT_WINDOW

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [Configuration](arkts-arkui-window-configuration-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300001](../errorcode-window.md#1300001-repeated-operation) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300006](../errorcode-window.md#1300006-abnormal-window-context) |
| [1300008](../errorcode-window.md#1300008-display-device-exception) |
| [1300009](../errorcode-window.md#1300009-invalid-parent-window) |


## createWindow

```TypeScript
function createWindow(config: Configuration): Promise<Window>
```

Creates a child window or system window. This API uses a promise to return the result.In non-[freeform window](../../../windowmanager/window-terminology.md#freeform-window) mode, the child window created uses an [immersive layout](../../../windowmanager/window-terminology.md#immersive-layout) by default.In freeform window mode, the child window created uses an immersive layout when [decorEnabled](arkts-arkui-window-configuration-i.md) is set to **false**, and it uses a non-immersive layout when this parameter is set to **true**.

**Since:** 9

**Required permissions:** 
- API version 12+: ohos.permission.SYSTEM_FLOAT_WINDOW

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [Configuration](arkts-arkui-window-configuration-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300001](../errorcode-window.md#1300001-repeated-operation) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300006](../errorcode-window.md#1300006-abnormal-window-context) |
| [1300008](../errorcode-window.md#1300008-display-device-exception) |
| [1300009](../errorcode-window.md#1300009-invalid-parent-window) |
