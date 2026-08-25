# setOverlayEnabled

## Modules to Import

```TypeScript
import { overlay } from 'kits/@kit.AbilityKit';
```

## setOverlayEnabled

```TypeScript
function setOverlayEnabled(moduleName:string, isEnabled: boolean, callback: AsyncCallback<void>): void
```

Enables or disables a module with the overlay feature in the current application. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.BundleManager.BundleFramework.Overlay

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| isEnabled | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700033](../errorcode-bundle.md#17700033-module-is-not-configured-with-the-overlay-feature) |


## setOverlayEnabled

```TypeScript
function setOverlayEnabled(moduleName:string, isEnabled: boolean): Promise<void>
```

Enables or disables a module with the overlay feature in the current application. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.BundleManager.BundleFramework.Overlay

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| isEnabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700033](../errorcode-bundle.md#17700033-module-is-not-configured-with-the-overlay-feature) |
