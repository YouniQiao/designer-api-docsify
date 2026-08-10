# getResourceManager

## Modules to Import

```TypeScript
import { resourceManager } from 'kits/@kit.LocalizationKit';
```

## getResourceManager

```TypeScript
export function getResourceManager(callback: AsyncCallback<ResourceManager>): void
```

获取当前应用的资源管理对象。使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-resourceManager-export function getResourceManager(callback: AsyncCallback<ResourceManager>): void--><!--Device-resourceManager-export function getResourceManager(callback: AsyncCallback<ResourceManager>): void-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;ResourceManager&gt; | Yes | 回调函数，返回资源管理对象。 |

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

获取指定应用的资源管理对象。使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-resourceManager-export function getResourceManager(bundleName: string, callback: AsyncCallback<ResourceManager>): void--><!--Device-resourceManager-export function getResourceManager(bundleName: string, callback: AsyncCallback<ResourceManager>): void-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 应用包名。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;ResourceManager&gt; | Yes | 回调函数，返回应用包名对应的资源管理对象。 |

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

获取当前应用的资源管理对象。使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-resourceManager-export function getResourceManager(): Promise<ResourceManager>--><!--Device-resourceManager-export function getResourceManager(): Promise<ResourceManager>-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ResourceManager&gt; | Promise对象，返回资源管理对象。 |

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

获取指定应用的资源管理对象。使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-resourceManager-export function getResourceManager(bundleName: string): Promise<ResourceManager>--><!--Device-resourceManager-export function getResourceManager(bundleName: string): Promise<ResourceManager>-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 应用包名。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ResourceManager&gt; | Promise对象，返回应用包名对应的资源管理对象。 |

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

