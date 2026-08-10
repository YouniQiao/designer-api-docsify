# isHapModuleRemovable (System API)

## Modules to Import

```TypeScript
import { freeInstall } from 'kits/@kit.AbilityKit';
```

## isHapModuleRemovable

```TypeScript
function isHapModuleRemovable(bundleName: string, moduleName: string, callback: AsyncCallback<boolean>): void
```

查询指定模块是否可以被移除。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function isHapModuleRemovable(bundleName: string, moduleName: string, callback: AsyncCallback<boolean>): void--><!--Device-freeInstall-function isHapModuleRemovable(bundleName: string, moduleName: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 应用Bundle名称。 |
| moduleName | string | Yes | 应用程序模块名称。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)。当获取成功时，err为undefined，data为bool值 ，true表示可以移除；false表示不可移除；否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700002 | The specified module name is not found. |
| 17700001 | The specified bundle name is not found. |


## isHapModuleRemovable

```TypeScript
function isHapModuleRemovable(bundleName: string, moduleName: string): Promise<boolean>
```

查询指定模块是否可以被移除。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function isHapModuleRemovable(bundleName: string, moduleName: string): Promise<boolean>--><!--Device-freeInstall-function isHapModuleRemovable(bundleName: string, moduleName: string): Promise<boolean>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 应用Bundle名称。 |
| moduleName | string | Yes | 应用程序模块名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示可以移除；返回false表示不可移除。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700002 | The specified module name is not found. |
| 17700001 | The specified bundle name is not found. |

