# getAllDisplay

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getAllDisplay

```TypeScript
function getAllDisplay(callback: AsyncCallback<Array<Display>>): void
```

Obtains all Display objects. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [display.getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getalldisplays)(callback:

<!--Device-display-function getAllDisplay(callback: AsyncCallback<Array<Display>>): void--><!--Device-display-function getAllDisplay(callback: AsyncCallback<Array<Display>>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Display&gt;&gt; | Yes |

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

Obtains all Display objects. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [display.getAllDisplays](arkts-arkui-display-getalldisplays-f.md#getalldisplays)()

<!--Device-display-function getAllDisplay(): Promise<Array<Display>>--><!--Device-display-function getAllDisplay(): Promise<Array<Display>>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;Display&gt;&gt; |

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
