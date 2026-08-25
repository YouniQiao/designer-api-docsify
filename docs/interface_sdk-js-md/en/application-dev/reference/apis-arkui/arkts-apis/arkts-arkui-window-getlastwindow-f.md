# getLastWindow

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getLastWindow

```TypeScript
function getLastWindow(ctx: BaseContext, callback: AsyncCallback<Window>): void
```

Obtains the topmost layer child window of the current application. This API uses an asynchronous callback to return the result.If no child window exists or the child window is not displayed by calling [showWindow()](arkts-arkui-window-window-i.md#showwindow), the main window of the application is returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ctx](arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300006](../errorcode-window.md#1300006-abnormal-window-context) |


## getLastWindow

```TypeScript
function getLastWindow(ctx: BaseContext): Promise<Window>
```

Obtains the topmost layer child window of the current application. This API uses a promise to return the result.If no child window exists or the child window is not displayed by calling [showWindow()](arkts-arkui-window-window-i.md#showwindow), the main window of the application is returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ctx](arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300006](../errorcode-window.md#1300006-abnormal-window-context) |
