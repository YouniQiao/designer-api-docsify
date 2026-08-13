# getResourceManager

## Modules to Import

```TypeScript
import { resourceManager } from '@kit.LocalizationKit';
```

## getResourceManager

```TypeScript
export function getResourceManager(callback: AsyncCallback<ResourceManager>): void
```

Obtains the **ResourceManager** object of the current application. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-resourceManager-export function getResourceManager(callback: AsyncCallback<ResourceManager>): void--><!--Device-resourceManager-export function getResourceManager(callback: AsyncCallback<ResourceManager>): void-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | AsyncCallback&lt;[ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md)&gt; | Yes |

## Examples

```TypeScript
import resourceManager from '@ohos.resourceManager';
// Use this method to import the module in the FA model.

export default {
    onCreate() {
        resourceManager.getResourceManager((error, mgr) => {
            if (error != null) {
                console.error("error is " + error);
                return;
            }
            // Replace "test" with the actual resource name.
            mgr.getStringByName('test', (error, value) => {
                if (error) {
                    console.error("error is " + JSON.stringify(error));
                } else {
                    console.info("success is " + value);
                }

            });
        });
    }
};
```


## getResourceManager

```TypeScript
export function getResourceManager(bundleName: string, callback: AsyncCallback<ResourceManager>): void
```

Obtains the **ResourceManager** object of the specified application. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-resourceManager-export function getResourceManager(bundleName: string, callback: AsyncCallback<ResourceManager>): void--><!--Device-resourceManager-export function getResourceManager(bundleName: string, callback: AsyncCallback<ResourceManager>): void-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | AsyncCallback&lt;[ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md)&gt; | Yes |

## Examples

```TypeScript
import resourceManager from '@ohos.resourceManager';
// Use this method to import the module in the FA model.

// Replace 'com.example.testapp' with the actual application package name.
const BUNDLE_NAME = 'com.example.testapp';

export default {
    onCreate() {
        resourceManager.getResourceManager(BUNDLE_NAME, (error, mgr) => {
            if (error != null) {
                console.error("getResourceManager error is " + error);
                return;
            }
            // Replace "test" with the actual resource name.
            mgr.getStringByName('test', (error, value) => {
                if (error) {
                    console.error("getResourceManager error is " + JSON.stringify(error));
                } else {
                    console.info("getResourceManager success is " + value);
                }
            });
        });
    }
};
```


## getResourceManager

```TypeScript
export function getResourceManager(): Promise<ResourceManager>
```

Obtains the **ResourceManager** object of the current application. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-resourceManager-export function getResourceManager(): Promise<ResourceManager>--><!--Device-resourceManager-export function getResourceManager(): Promise<ResourceManager>-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md)&gt; |

## Examples

```TypeScript
import resourceManager from '@ohos.resourceManager';
// Use this method to import the module in the FA model.

export default {
    onCreate() {
        resourceManager.getResourceManager().then(resMgr => {
            try {
                // Replace "test" with the actual resource name.
                let testStr = resMgr.getStringByNameSync('test')
                console.info("getResourceManager success is " + testStr);
            } catch (error) {
                console.error("getResourceManager error is " + JSON.stringify(error));
            }
        }).catch(error => {
            console.error("getResourceManager error is " + error);
        });
    }
};
```


## getResourceManager

```TypeScript
export function getResourceManager(bundleName: string): Promise<ResourceManager>
```

Obtains the **ResourceManager** object of the specified application. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-resourceManager-export function getResourceManager(bundleName: string): Promise<ResourceManager>--><!--Device-resourceManager-export function getResourceManager(bundleName: string): Promise<ResourceManager>-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md)&gt; |

## Examples

```TypeScript
import resourceManager from '@ohos.resourceManager';
// Use this method to import the module in the FA model.

// Replace 'com.example.testapp' with the actual application package name.
const BUNDLE_NAME = 'com.example.testapp';

export default {
    onCreate() {
        resourceManager.getResourceManager(BUNDLE_NAME).then(resMgr => {
            try {
                // Replace "test" with the actual resource name.
                let testStr = resMgr.getStringByNameSync('test')
                console.info("getResourceManager success is " + testStr);
            } catch (error) {
                console.error("getResourceManager error is " + JSON.stringify(error));
            }
        }).catch(error => {
            console.error("getResourceManager error is " + error);
        });
    }
};
```
