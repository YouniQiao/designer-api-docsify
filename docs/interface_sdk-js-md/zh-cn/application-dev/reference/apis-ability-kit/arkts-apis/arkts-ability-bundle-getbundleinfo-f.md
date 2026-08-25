# getBundleInfo

## 导入模块

```TypeScript
import { bundle } from 'kits/@kit.AbilityKit';
```

## getBundleInfo

```TypeScript
function getBundleInfo(bundleName: string,
    bundleFlags: number, options: BundleOptions, callback: AsyncCallback<BundleInfo>): void
```

根据给定的Bundle名称获取BundleInfo，使用callback异步回调。获取调用方自己的信息时不需要权限。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** null

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| bundleFlags | number | 是 |
| options | [BundleOptions](arkts-ability-bundle-bundleoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt; | 是 |


## getBundleInfo

```TypeScript
function getBundleInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void
```

根据给定的Bundle名称获取BundleInfo，使用callback异步回调。获取调用方自己的信息时不需要权限。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** null

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| bundleFlags | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt; | 是 |


## getBundleInfo

```TypeScript
function getBundleInfo(bundleName: string, bundleFlags: number, options?: BundleOptions): Promise<BundleInfo>
```

根据给定的Bundle名称获取BundleInfo，使用Promise异步回调。获取调用方自己的信息时不需要权限。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** null

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| bundleFlags | number | 是 |
| options | [BundleOptions](arkts-ability-bundle-bundleoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt; |
