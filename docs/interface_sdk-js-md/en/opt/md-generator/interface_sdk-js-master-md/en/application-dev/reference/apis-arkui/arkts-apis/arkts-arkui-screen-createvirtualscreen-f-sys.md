# createVirtualScreen (System API)

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
```

## createVirtualScreen

```TypeScript
function createVirtualScreen(options:VirtualScreenOption, callback: AsyncCallback<Screen>): void
```

Creates a virtual screen. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CAPTURE_SCREEN

<!--Device-screen-function createVirtualScreen(options:VirtualScreenOption, callback: AsyncCallback<Screen>): void--><!--Device-screen-function createVirtualScreen(options:VirtualScreenOption, callback: AsyncCallback<Screen>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [VirtualScreenOption](arkts-arkui-screen-virtualscreenoption-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Screen&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let screenClass: screen.Screen | null = null;
class VirtualScreenOption {
  name : string = '';
  width : number =  0;
  height : number = 0;
  density : number = 0;
  surfaceId : string = '';
  supportsFocus ?: boolean = true;
}

let option: VirtualScreenOption = { 
  name: 'screen01',
  width: 1080,
  height: 2340,
  density: 2,
  surfaceId: '',
  supportsFocus: false
}; // Create virtual screen parameters.
// Create a virtual screen.
screen.createVirtualScreen(option, (err: BusinessError, data: screen.Screen) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to create the virtual screen. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  screenClass = data;
  console.info(`Succeeded in creating the virtual screen. Data: ${JSON.stringify(data)}`);
});
```


## createVirtualScreen

```TypeScript
function createVirtualScreen(options:VirtualScreenOption): Promise<Screen>
```

Creates a virtual screen. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CAPTURE_SCREEN

<!--Device-screen-function createVirtualScreen(options:VirtualScreenOption): Promise<Screen>--><!--Device-screen-function createVirtualScreen(options:VirtualScreenOption): Promise<Screen>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [VirtualScreenOption](arkts-arkui-screen-virtualscreenoption-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Screen & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let screenClass: screen.Screen | null = null;
class VirtualScreenOption {
  name : string = '';
  width : number =  0;
  height : number = 0;
  density : number = 0;
  surfaceId : string = '';
  supportsFocus ?: boolean = true;
}

let option: VirtualScreenOption = { 
  name: 'screen01',
  width: 1080,
  height: 2340,
  density: 2,
  surfaceId: '',
  supportsFocus: false
}; // Create virtual screen parameters.

// Create a virtual screen.
screen.createVirtualScreen(option).then((data: screen.Screen) => {
  screenClass = data;
  console.info(`Succeeded in creating the virtual screen. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create the virtual screen. Code: ${err.code}, message: ${err.message}`);
});
```
