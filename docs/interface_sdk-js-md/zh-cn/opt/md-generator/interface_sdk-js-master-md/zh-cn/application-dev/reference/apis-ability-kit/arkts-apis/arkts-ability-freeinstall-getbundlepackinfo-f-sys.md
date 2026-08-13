# getBundlePackInfo（系统接口）

## getBundlePackInfo

```TypeScript
function getBundlePackInfo(bundleName: string, 
    bundlePackFlag : BundlePackFlag, callback: AsyncCallback<BundlePackInfo>): void
```

基于bundleName和bundlePackFlag来获取bundlePackInfo。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function getBundlePackInfo(bundleName: string,     bundlePackFlag : BundlePackFlag, callback: AsyncCallback<BundlePackInfo>): void--><!--Device-freeInstall-function getBundlePackInfo(bundleName: string,     bundlePackFlag : BundlePackFlag, callback: AsyncCallback<BundlePackInfo>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.FreeInstall

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| bundlePackFlag | [BundlePackFlag](arkts-ability-freeinstall-bundlepackflag-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;BundlePackInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |


## getBundlePackInfo

```TypeScript
function getBundlePackInfo(bundleName: string, bundlePackFlag : BundlePackFlag): Promise<BundlePackInfo>
```

基于bundleName和BundlePackFlag来获取bundlePackInfo。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function getBundlePackInfo(bundleName: string, bundlePackFlag : BundlePackFlag): Promise<BundlePackInfo>--><!--Device-freeInstall-function getBundlePackInfo(bundleName: string, bundlePackFlag : BundlePackFlag): Promise<BundlePackInfo>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.FreeInstall

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| bundlePackFlag | [BundlePackFlag](arkts-ability-freeinstall-bundlepackflag-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;BundlePackInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
