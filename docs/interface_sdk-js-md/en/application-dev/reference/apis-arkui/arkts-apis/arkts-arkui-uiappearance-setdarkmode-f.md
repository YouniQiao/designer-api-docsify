# setDarkMode

## Modules to Import

```TypeScript
import { uiAppearance } from 'kits/@kit.ArkUI';
```

## setDarkMode

```TypeScript
function setDarkMode(mode: DarkMode, callback: AsyncCallback<void>): void
```

Sets the system color mode. This API uses an asynchronous callback to return the result.

**Permission required**: ohos.permission.UPDATE_CONFIGURATION

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function setDarkMode(mode: DarkMode, callback: AsyncCallback<void>): void--><!--Device-uiAppearance-function setDarkMode(mode: DarkMode, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [DarkMode](arkts-arkui-uiappearance-darkmode-e.md) | Yes | indicates the dark-mode to set |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of setDarkMode |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [500001](../errorcode-uiappearance.md#500001-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  uiAppearance.setDarkMode(uiAppearance.DarkMode.ALWAYS_DARK, (error) => {
    if (error) {
      console.error('Set dark-mode failed, ' + error.message);
    } else {
      console.info('Set dark-mode successfully.');
    }
  })
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Set dark-mode failed, ' + message);
}
```


## setDarkMode

```TypeScript
function setDarkMode(mode: DarkMode): Promise<void>
```

Sets the system color mode. This API uses a promise to return the result.

**Permission required**: ohos.permission.UPDATE_CONFIGURATION

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function setDarkMode(mode: DarkMode): Promise<void>--><!--Device-uiAppearance-function setDarkMode(mode: DarkMode): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [DarkMode](arkts-arkui-uiappearance-darkmode-e.md) | Yes | indicates the dark-mode to set |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [500001](../errorcode-uiappearance.md#500001-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  uiAppearance.setDarkMode(uiAppearance.DarkMode.ALWAYS_DARK).then(() => {
    console.info('Set dark-mode successfully.');
  }).catch((error: Error) => {
    console.error('Set dark-mode failed, ' + error.message);
  });
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Set dark-mode failed, ' + message);
}
```

