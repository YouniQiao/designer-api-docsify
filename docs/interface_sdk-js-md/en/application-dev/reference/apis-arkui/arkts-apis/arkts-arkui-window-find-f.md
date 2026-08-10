# find

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## find

```TypeScript
function find(id: string, callback: AsyncCallback<Window>): void
```

查找id所对应的窗口，使用callback异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃，建议使用[findWindow()](arkts-arkui-window-findwindow-f.md#findwindow)替代。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [window.findWindow](arkts-arkui-window-findwindow-f.md#findwindow)

<!--Device-window-function find(id: string, callback: AsyncCallback<Window>): void--><!--Device-window-function find(id: string, callback: AsyncCallback<Window>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | 窗口名字，即[Configuration](arkts-arkui-window-configuration-i.md)中的name。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Window&gt; | Yes | 回调函数。返回当前查找到的窗口对象。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
window.find('test', (err: BusinessError, data) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to find the Window. Cause code: ${err.code}, message: ${err.message}`);
    return;
  }
  windowClass = data;
  console.info('Succeeded in finding the window. Data: ' + JSON.stringify(data));
});
```


## find

```TypeScript
function find(id: string): Promise<Window>
```

查找id所对应的窗口，使用Promise异步回调。

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃，建议使用[findWindow()](arkts-arkui-window-findwindow-f.md#findwindow)替代。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [window.findWindow](arkts-arkui-window-findwindow-f.md#findwindow)

<!--Device-window-function find(id: string): Promise<Window>--><!--Device-window-function find(id: string): Promise<Window>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | 窗口名字，即[Configuration](arkts-arkui-window-configuration-i.md)中的name。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Window&gt; | Promise对象。返回当前查找的窗口对象。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let windowClass: window.Window | undefined = undefined;
let promise = window.find('test');
promise.then((data) => {
  windowClass = data;
  console.info('Succeeded in finding the window. Data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to find the Window. Cause code: ${err.code}, message: ${err.message}`);
});
```

