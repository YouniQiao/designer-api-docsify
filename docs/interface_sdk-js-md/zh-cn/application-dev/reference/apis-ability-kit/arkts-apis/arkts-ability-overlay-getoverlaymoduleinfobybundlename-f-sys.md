# getOverlayModuleInfoByBundleName（系统接口）

## 导入模块

```TypeScript
import { overlay } from 'kits/@kit.AbilityKit';
```

## getOverlayModuleInfoByBundleName

```TypeScript
function getOverlayModuleInfoByBundleName(bundleName: string,
      callback: AsyncCallback<Array<OverlayModuleInfo>>): void
```

获取指定应用中所有module的OverlayModuleInfo信息。使用callback异步回调。指定应用是调用方自身时不需要权限。

**起始版本：** 10

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;OverlayModuleInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700032](../errorcode-bundle.md#17700032-指定的应用不包含overlay特征的module) |


## getOverlayModuleInfoByBundleName

```TypeScript
function getOverlayModuleInfoByBundleName(bundleName: string, moduleName: string, callback: AsyncCallback<Array<OverlayModuleInfo>>): void
```

获取指定应用中指定module的OverlayModuleInfo信息。使用callback异步回调。指定应用是调用方自身时不需要权限。

**起始版本：** 10

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;OverlayModuleInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700032](../errorcode-bundle.md#17700032-指定的应用不包含overlay特征的module) |
| [17700033](../errorcode-bundle.md#17700033-指定的module不是overlay特征的module) |


## getOverlayModuleInfoByBundleName

```TypeScript
function getOverlayModuleInfoByBundleName(bundleName: string, moduleName?: string): Promise<Array<OverlayModuleInfo>>
```

获取指定应用中指定module的OverlayModuleInfo信息。使用promise异步回调。指定应用是调用方自身时不需要权限。

**起始版本：** 10

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;OverlayModuleInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700032](../errorcode-bundle.md#17700032-指定的应用不包含overlay特征的module) |
| [17700033](../errorcode-bundle.md#17700033-指定的module不是overlay特征的module) |
