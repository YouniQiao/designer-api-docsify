# create

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## create

```TypeScript
function create(id: string, type: WindowType, callback: AsyncCallback<Window>): void
```

Creates a child window. This API uses an asynchronous callback to return the result.The child window created uses an [immersive layout](../../../windowmanager/window-terminology.md#immersive-layout) by default.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [createWindow](arkts-arkui-window-createwindow-f.md)(config: Configuration, callback: AsyncCallback&lt;Window&gt;)

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| type | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | Yes |


## create

```TypeScript
function create(id: string, type: WindowType): Promise<Window>
```

Creates a child window. This API uses a promise to return the result.The child window created uses an [immersive layout](../../../windowmanager/window-terminology.md#immersive-layout) by default.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [createWindow](arkts-arkui-window-createwindow-f.md)(config: Configuration)

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| type | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |


## create

```TypeScript
function create(ctx: BaseContext, id: string, type: WindowType): Promise<Window>
```

Creates a system window. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [createWindow](arkts-arkui-window-createwindow-f.md)(config: Configuration)

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ctx](arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| id | string | Yes |
| type | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |


## create

```TypeScript
function create(ctx: BaseContext, id: string, type: WindowType, callback: AsyncCallback<Window>): void
```

Creates a system window. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [createWindow](arkts-arkui-window-createwindow-f.md)(config: Configuration, callback: AsyncCallback&lt;Window&gt;)

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ctx](arkts-arkui-window-configuration-i.md) | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| id | string | Yes |
| type | [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | Yes |
