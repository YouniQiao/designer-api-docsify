# getBundlePackInfo（系统接口）

## 导入模块

```TypeScript
import { freeInstall } from 'kits/@kit.AbilityKit';
```

## getBundlePackInfo

```TypeScript
function getBundlePackInfo(bundleName: string, 
    bundlePackFlag : BundlePackFlag, callback: AsyncCallback<BundlePackInfo>): void
```

基于bundleName和bundlePackFlag来获取bundlePackInfo。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function getBundlePackInfo(bundleName: string,     bundlePackFlag : BundlePackFlag, callback: AsyncCallback<BundlePackInfo>): void--><!--Device-freeInstall-function getBundlePackInfo(bundleName: string,     bundlePackFlag : BundlePackFlag, callback: AsyncCallback<BundlePackInfo>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.FreeInstall

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用Bundle名称。 |
| bundlePackFlag | [BundlePackFlag](arkts-ability-freeinstall-bundlepackflag-e-sys.md) | 是 | 指示要查询的应用包标志。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;BundlePackInfo&gt; | 是 | [回调函数](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md/arkts-basicservices-base-asynccallback-i.md)。当函数调用成功，err为undefined， data为获取到的BundlePackInfo信息。否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700001 | The specified bundle name is not found. |


## getBundlePackInfo

```TypeScript
function getBundlePackInfo(bundleName: string, bundlePackFlag : BundlePackFlag): Promise<BundlePackInfo>
```

基于bundleName和BundlePackFlag来获取bundlePackInfo。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function getBundlePackInfo(bundleName: string, bundlePackFlag : BundlePackFlag): Promise<BundlePackInfo>--><!--Device-freeInstall-function getBundlePackInfo(bundleName: string, bundlePackFlag : BundlePackFlag): Promise<BundlePackInfo>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.FreeInstall

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用程序Bundle名称。 |
| bundlePackFlag | [BundlePackFlag](arkts-ability-freeinstall-bundlepackflag-e-sys.md) | 是 | 指示要查询的应用包标志。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;BundlePackInfo&gt; | Promise对象，返回BundlePackInfo信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700001 | The specified bundle name is not found. |

