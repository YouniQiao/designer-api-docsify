# getAllScreens (System API)

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
```

## getAllScreens

```TypeScript
function getAllScreens(callback: AsyncCallback<Array<Screen>>): void
```

Obtains all screens. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-screen-function getAllScreens(callback: AsyncCallback<Array<Screen>>): void--><!--Device-screen-function getAllScreens(callback: AsyncCallback<Array<Screen>>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;Screen&gt;&gt; | Yes | Callback used to return all the Screen objects obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let screenClass: screen.Screen | null = null;
screen.getAllScreens((err: BusinessError, data: Array<screen.Screen>) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to get all screens. Code:${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting all screens. Data: ${JSON.stringify(data)}`);
  if (data.length > 0) {
    screenClass = data[0];
  }
});
```


## getAllScreens

```TypeScript
function getAllScreens(callback: AsyncCallback<Array<Screen>>, isNeedUnused?: boolean): void
```

Obtains all screens. This API uses an asynchronous callback to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-screen-function getAllScreens(callback: AsyncCallback<Array<Screen>>, isNeedUnused?: boolean): void--><!--Device-screen-function getAllScreens(callback: AsyncCallback<Array<Screen>>, isNeedUnused?: boolean): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;Screen&gt;&gt; | Yes | Callback used to return the result. If obtaining all screens is successful is successful, **err** is **undefined**, and the returned object is screen object set obtained. Otherwise, **err** is an error object. |
| isNeedUnused | boolean | No | Indicates whether unused screen information is required. **true** means they should be provided, **false** means they should not. &lt;br&gt;Default value: false. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |


## getAllScreens

```TypeScript
function getAllScreens(): Promise<Array<Screen>>
```

Obtains all screens. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-screen-function getAllScreens(): Promise<Array<Screen>>--><!--Device-screen-function getAllScreens(): Promise<Array<Screen>>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Screen&gt;&gt; | Promise used to return all the Screen objects obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let screenClass: screen.Screen | null = null;
let promise: Promise<Array<screen.Screen>> = screen.getAllScreens();
promise.then((data: Array<screen.Screen>) => {
  if(data.length > 0){
    screenClass = data[0];
  }
  console.info(`Succeeded in getting all screens. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get all screens. Code: ${err.code}, message : ${err.message}`);
});
```


## getAllScreens

```TypeScript
function getAllScreens(isNeedUnused?: boolean): Promise<Array<Screen>>
```

Obtains all screens. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-screen-function getAllScreens(isNeedUnused?: boolean): Promise<Array<Screen>>--><!--Device-screen-function getAllScreens(isNeedUnused?: boolean): Promise<Array<Screen>>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isNeedUnused | boolean | No | Indicates whether unused screen information is required. This parameter is optional. If not provided, the unused screen information will not be returned &lt;br&gt;Default value: false. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Screen&gt;&gt; | Promise used to return all the Screen objects obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

