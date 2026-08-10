# getNameForUid

## Modules to Import

```TypeScript
import { bundle } from 'kits/@kit.AbilityKit';
```

## getNameForUid

```TypeScript
function getNameForUid(uid: number, callback: AsyncCallback<string>): void
```

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager#getBundleNameByUid

<!--Device-bundle-function getNameForUid(uid: number, callback: AsyncCallback<string>): void--><!--Device-bundle-function getNameForUid(uid: number, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | number | Yes | @param { AsyncCallback&lt;string&gt; } callback |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |  |


## getNameForUid

```TypeScript
function getNameForUid(uid: number): Promise<string>
```

通过uid获取对应的Bundle名称，使用Promise异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [null]

<!--Device-bundle-function getNameForUid(uid: number): Promise<string>--><!--Device-bundle-function getNameForUid(uid: number): Promise<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | number | Yes | 要查询的uid。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Returns the bundle name. |

