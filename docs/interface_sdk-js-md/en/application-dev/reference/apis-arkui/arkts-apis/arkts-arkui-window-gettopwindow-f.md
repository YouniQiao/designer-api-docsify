# getTopWindow

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## getTopWindow

```TypeScript
function getTopWindow(callback: AsyncCallback<Window>): void
```

Obtains the top window of the current application. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getLastWindow](arkts-arkui-window-getlastwindow-f.md)(ctx: BaseContext, callback: AsyncCallback&lt;Window&gt;)

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | Yes |


## getTopWindow

```TypeScript
function getTopWindow(): Promise<Window>
```

Obtains the top window of the current application. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getLastWindow](arkts-arkui-window-getlastwindow-f.md)(ctx: BaseContext)

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |


## getTopWindow

```TypeScript
function getTopWindow(ctx: BaseContext): Promise<Window>
```

Obtains the top window of the current application. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getLastWindow](arkts-arkui-window-getlastwindow-f.md)(ctx: BaseContext)

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ctx](arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |


## getTopWindow

```TypeScript
function getTopWindow(ctx: BaseContext, callback: AsyncCallback<Window>): void
```

Obtains the top window of the current application. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getLastWindow](arkts-arkui-window-getlastwindow-f.md)(ctx: BaseContext, callback: AsyncCallback&lt;Window&gt;)

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ctx](arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | Yes |
