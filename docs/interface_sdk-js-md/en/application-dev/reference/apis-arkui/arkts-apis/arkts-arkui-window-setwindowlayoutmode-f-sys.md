# setWindowLayoutMode (System API)

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## setWindowLayoutMode

```TypeScript
function setWindowLayoutMode(mode: WindowLayoutMode, callback: AsyncCallback<void>): void
```

Sets the window layout mode. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WindowLayoutMode](arkts-arkui-window-windowlayoutmode-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |


## setWindowLayoutMode

```TypeScript
function setWindowLayoutMode(mode: WindowLayoutMode): Promise<void>
```

Sets the window layout mode. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 26.0.0

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WindowLayoutMode](arkts-arkui-window-windowlayoutmode-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
