# getOverlayModuleInfo

## Modules to Import

```TypeScript
```

## getOverlayModuleInfo

```TypeScript
function getOverlayModuleInfo(moduleName: string, callback: AsyncCallback<OverlayModuleInfo>): void
```

Obtains the OverlayModuleInfo about a module with the overlay feature in the current application. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-overlay-function getOverlayModuleInfo(moduleName: string, callback: AsyncCallback<OverlayModuleInfo>): void--><!--Device-overlay-function getOverlayModuleInfo(moduleName: string, callback: AsyncCallback<OverlayModuleInfo>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Overlay

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;OverlayModuleInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700032](../errorcode-bundle.md#17700032-application-does-not-contain-a-module-with-the-overlay-feature) |
| [17700033](../errorcode-bundle.md#17700033-module-is-not-configured-with-the-overlay-feature) |

**Examples**

```TypeScript
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let moduleName = "feature";

try {
  overlay.getOverlayModuleInfo(moduleName, (err, data) => {
    if (err) {
      console.error('getOverlayModuleInfo failed due to err code : ' + err.code + ' ' + 'message :' + err.message);
      return;
    }
    console.info('overlayModuleInfo is ' + JSON.stringify(data));
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('getOverlayModuleInfo failed due to err code : ' + code + ' ' + 'message :' + message);
}
```


## getOverlayModuleInfo

```TypeScript
function getOverlayModuleInfo(moduleName: string): Promise<OverlayModuleInfo>
```

Obtains the OverlayModuleInfo about a module with the overlay feature in the current application. This API uses a promise to return the result.

**Since:** 23

<!--Device-overlay-function getOverlayModuleInfo(moduleName: string): Promise<OverlayModuleInfo>--><!--Device-overlay-function getOverlayModuleInfo(moduleName: string): Promise<OverlayModuleInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Overlay

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;OverlayModuleInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700032](../errorcode-bundle.md#17700032-application-does-not-contain-a-module-with-the-overlay-feature) |
| [17700033](../errorcode-bundle.md#17700033-module-is-not-configured-with-the-overlay-feature) |

**Examples**

```TypeScript
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let moduleName = "feature";

(async () => {
  try {
    let overlayModuleInfo = await overlay.getOverlayModuleInfo(moduleName);
    console.info('overlayModuleInfo is ' + JSON.stringify(overlayModuleInfo));
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error('getOverlayModuleInfo failed due to err code : ' + code + ' ' + 'message :' + message);
  }
})();
```
