# makeExpand (System API)

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
```

## makeExpand

```TypeScript
function makeExpand(options:Array<ExpandOption>, callback: AsyncCallback<number>): void
```

Sets the screen to extended mode. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 20

<!--Device-screen-function makeExpand(options:Array<ExpandOption>, callback: AsyncCallback<long>): void--><!--Device-screen-function makeExpand(options:Array<ExpandOption>, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | Array&lt;[ExpandOption](arkts-arkui-screen-expandoption-i-sys.md)&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let groupId: number | null = null;
class ExpandOption {
  screenId: number = 0;
  startX: number = 0;
  startY: number = 0;
}
let mainScreenOption: ExpandOption = { screenId: 0, startX: 0, startY: 0 };
let otherScreenOption: ExpandOption = { screenId: 1, startX: 1080, startY: 0 };
let expandOptionArray : ExpandOption[] = [ mainScreenOption, otherScreenOption ];
// Set the screen to extend mode.
screen.makeExpand(expandOptionArray, (err: BusinessError, data: number) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to expand the screen. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  groupId = data;
  console.info(`Succeeded in expanding the screen. Data: ${data}`);
});
```


## makeExpand

```TypeScript
function makeExpand(options:Array<ExpandOption>): Promise<number>
```

Sets the screen to extended mode. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 20

<!--Device-screen-function makeExpand(options:Array<ExpandOption>): Promise<long>--><!--Device-screen-function makeExpand(options:Array<ExpandOption>): Promise<long>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | Array&lt;[ExpandOption](arkts-arkui-screen-expandoption-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

class ExpandOption {
  screenId: number = 0;
  startX: number = 0;
  startY: number = 0;
}
let mainScreenOption: ExpandOption = { screenId: 0, startX: 0, startY: 0 };
let otherScreenOption: ExpandOption = { screenId: 1, startX: 1080, startY: 0 };
let expandOptionArray : ExpandOption[] = [ mainScreenOption, otherScreenOption ];
// Set the screen to extend mode.
screen.makeExpand(expandOptionArray).then((data: number) => {
  console.info(`Succeeded in expanding the screen. Data: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to expand the screen. Code: ${err.code}, message: ${err.message}`);
});
```
