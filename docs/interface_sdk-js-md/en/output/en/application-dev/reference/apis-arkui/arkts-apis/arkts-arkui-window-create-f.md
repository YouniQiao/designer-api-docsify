# create

## create

```TypeScript
function create(id: string, type: WindowType, callback: AsyncCallback<Window>): void
```

Creates a child window. This API uses an asynchronous callback to return the result. The child window created uses an \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ by default.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [window.createWindow](arkts-arkui-window-createwindow-f.md#createwindow)(config:

**Model restriction:** This API can be used only in the FA model.

<!--Device-window-function create(id: string, type: WindowType, callback: AsyncCallback<Window>): void--><!--Device-window-function create(id: string, type: WindowType, callback: AsyncCallback<Window>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | Window name, that is, the value of name in [Configuration]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Window type. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Window&gt; | Yes | Callback used to return the child window created. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
window.create('test', window.WindowType.TYPE_APP, (err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to create the subWindow. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  windowClass = data;
  console.info('Succeeded in creating the subWindow. Data: ' + JSON.stringify(data));
});
```


## create

```TypeScript
function create(id: string, type: WindowType): Promise<Window>
```

Creates a child window. This API uses a promise to return the result. The child window created uses an \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ by default.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [window.createWindow](arkts-arkui-window-createwindow-f.md#createwindow)(config:

**Model restriction:** This API can be used only in the FA model.

<!--Device-window-function create(id: string, type: WindowType): Promise<Window>--><!--Device-window-function create(id: string, type: WindowType): Promise<Window>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | Window name, that is, the value of name in [Configuration]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Window type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Window&gt; | Promise used to return the child window created. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
let promise = window.create('test', window.WindowType.TYPE_APP);
promise.then((data) => {
  windowClass = data;
  console.info('Succeeded in creating the subWindow. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to create the subWindow. Cause code: ${err.code}, message: ${err.message}`);
});
```


## create

```TypeScript
function create(ctx: BaseContext, id: string, type: WindowType): Promise<Window>
```

Creates a system window. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [window.createWindow](arkts-arkui-window-createwindow-f.md#createwindow)(config:

<!--Device-window-function create(ctx: BaseContext, id: string, type: WindowType): Promise<Window>--><!--Device-window-function create(ctx: BaseContext, id: string, type: WindowType): Promise<Window>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctx | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Current application context. |
| id | string | Yes | Window name, that is, the value of name in [Configuration]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Window type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Window&gt; | Promise used to return the child window created. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
let promise = window.create(globalThis.getContext(), 'test', window.WindowType.TYPE_SYSTEM_ALERT);
promise.then((data) => {
  windowClass = data;
  console.info('Succeeded in creating the window. Data:' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to create the Window. Cause code: ${err.code}, message: ${err.message}`);
});
```


## create

```TypeScript
function create(ctx: BaseContext, id: string, type: WindowType, callback: AsyncCallback<Window>): void
```

Creates a system window. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [window.createWindow](arkts-arkui-window-createwindow-f.md#createwindow)(config:

<!--Device-window-function create(ctx: BaseContext, id: string, type: WindowType, callback: AsyncCallback<Window>): void--><!--Device-window-function create(ctx: BaseContext, id: string, type: WindowType, callback: AsyncCallback<Window>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ctx | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Current application context. |
| id | string | Yes | Window name, that is, the value of name in [Configuration]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Window type. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Window&gt; | Yes | Callback used to return the child window created. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
window.create(globalThis.getContext(), 'test', window.WindowType.TYPE_SYSTEM_ALERT, (err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  windowClass = data;
  console.info('Succeeded in creating the window. Data: ' + JSON.stringify(data));
  windowClass.resetSize(500, 1000);
});
```

