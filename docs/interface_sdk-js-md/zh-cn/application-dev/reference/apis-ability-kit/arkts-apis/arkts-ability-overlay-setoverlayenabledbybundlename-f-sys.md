# setOverlayEnabledByBundleName（系统接口）

## 导入模块

```TypeScript
import { overlay } from 'kits/@kit.AbilityKit';
```

## setOverlayEnabledByBundleName

```TypeScript
function setOverlayEnabledByBundleName(bundleName:string, moduleName:string, isEnabled: boolean, callback: AsyncCallback<void>): void
```

设置指定应用的overlay module的禁用使能状态。使用callback异步回调。指定应用是调用方自身时不需要权限。

**起始版本：** 10

**需要权限：** ohos.permission.CHANGE_OVERLAY_ENABLED_STATE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |
| isEnabled | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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


## setOverlayEnabledByBundleName

```TypeScript
function setOverlayEnabledByBundleName(bundleName:string, moduleName:string, isEnabled: boolean): Promise<void>
```

设置指定应用的overlay module的禁用使能状态。使用Promise异步回调。指定应用是调用方自身时不需要权限。

**起始版本：** 10

**需要权限：** ohos.permission.CHANGE_OVERLAY_ENABLED_STATE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |
| isEnabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

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
