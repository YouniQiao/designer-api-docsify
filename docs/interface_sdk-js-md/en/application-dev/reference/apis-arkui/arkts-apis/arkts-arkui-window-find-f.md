# find

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## find

```TypeScript
function find(id: string, callback: AsyncCallback<Window>): void
```

Finds a window based on the ID. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [findWindow](arkts-arkui-window-findwindow-f.md)

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Window](arkts-arkui-window-window-i.md)&gt; | Yes |


## find

```TypeScript
function find(id: string): Promise<Window>
```

Finds a window based on the ID. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [findWindow](arkts-arkui-window-findwindow-f.md)

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Window](arkts-arkui-window-window-i.md)&gt; |
