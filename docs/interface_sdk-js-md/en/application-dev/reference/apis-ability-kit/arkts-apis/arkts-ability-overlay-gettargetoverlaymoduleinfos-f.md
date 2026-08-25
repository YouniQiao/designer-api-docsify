# getTargetOverlayModuleInfos

## Modules to Import

```TypeScript
import { overlay } from 'kits/@kit.AbilityKit';
```

## getTargetOverlayModuleInfos

```TypeScript
function getTargetOverlayModuleInfos(targetModuleName: string, callback: AsyncCallback<Array<OverlayModuleInfo>>): void
```

Obtains the OverlayModuleInfo associated with the specified target module. Modules with the overlay feature generally provide an overlay resource file for other modules (target module) on the device. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.BundleManager.BundleFramework.Overlay

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [targetModuleName](arkts-ability-overlaymoduleinfo-i.md) | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;OverlayModuleInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700034](../errorcode-bundle.md#17700034-module-is-configured-with-the-overlay-feature) |


## getTargetOverlayModuleInfos

```TypeScript
function getTargetOverlayModuleInfos(targetModuleName: string): Promise<Array<OverlayModuleInfo>>
```

Obtains the OverlayModuleInfo associated with the specified target module. Modules with the overlay feature generally provide an overlay resource file for other modules (target module) on the device. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.BundleManager.BundleFramework.Overlay

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [targetModuleName](arkts-ability-overlaymoduleinfo-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;OverlayModuleInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700034](../errorcode-bundle.md#17700034-module-is-configured-with-the-overlay-feature) |
