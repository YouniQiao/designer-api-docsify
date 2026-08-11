# isHapModuleRemovable（系统接口）

## isHapModuleRemovable

```TypeScript
function isHapModuleRemovable(bundleName: string, moduleName: string, callback: AsyncCallback<boolean>): void
```

查询指定模块是否可以被移除。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function isHapModuleRemovable(bundleName: string, moduleName: string, callback: AsyncCallback<boolean>): void--><!--Device-freeInstall-function isHapModuleRemovable(bundleName: string, moduleName: string, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.FreeInstall

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |


## isHapModuleRemovable

```TypeScript
function isHapModuleRemovable(bundleName: string, moduleName: string): Promise<boolean>
```

查询指定模块是否可以被移除。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function isHapModuleRemovable(bundleName: string, moduleName: string): Promise<boolean>--><!--Device-freeInstall-function isHapModuleRemovable(bundleName: string, moduleName: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.FreeInstall

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
