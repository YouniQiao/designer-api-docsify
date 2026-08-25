# getAllApplicationInfo（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAllApplicationInfo

```TypeScript
function getAllApplicationInfo(appFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void
```

根据给定的appFlags获取系统中所有的ApplicationInfo。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.GET_INSTALLED_BUNDLE_LIST

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appFlags | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;ApplicationInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getAllApplicationInfo

```TypeScript
function getAllApplicationInfo(appFlags: number,
    userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void
```

根据给定的appFlags和userId获取系统中所有的ApplicationInfo。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.GET_INSTALLED_BUNDLE_LIST

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appFlags | number | 是 |
| userId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;ApplicationInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |


## getAllApplicationInfo

```TypeScript
function getAllApplicationInfo(appFlags: number, userId?: number): Promise<Array<ApplicationInfo>>
```

根据给定的appFlags和userId获取系统中所有的ApplicationInfo。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.GET_INSTALLED_BUNDLE_LIST

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appFlags | number | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;ApplicationInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
