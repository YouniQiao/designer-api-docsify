# getAllDisplay

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getAllDisplay

```TypeScript
function getAllDisplay(callback: AsyncCallback<Array<Display>>): void
```

获取当前所有的Display对象，使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [display.getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getalldisplays)(callback:

<!--Device-display-function getAllDisplay(callback: AsyncCallback<Array<Display>>): void--><!--Device-display-function getAllDisplay(callback: AsyncCallback<Array<Display>>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Display&gt;&gt; | Yes | 回调函数。返回当前所有的Display对象。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

display.getAllDisplay((err: BusinessError, data: Array<display.Display>) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in obtaining the default display objects. Data: ${JSON.stringify(data)}`);
});
```


## getAllDisplay

```TypeScript
function getAllDisplay(): Promise<Array<Display>>
```

获取当前所有的Display对象，使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [display.getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getalldisplays)()

<!--Device-display-function getAllDisplay(): Promise<Array<Display>>--><!--Device-display-function getAllDisplay(): Promise<Array<Display>>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Display&gt;&gt; | Promise对象。返回当前所有的Display对象。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise: Promise<Array<display.Display>> = display.getAllDisplay();
promise.then((data: Array<display.Display>) => {
  console.info(`Succeeded in obtaining the default display objects. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}`);
});
```

