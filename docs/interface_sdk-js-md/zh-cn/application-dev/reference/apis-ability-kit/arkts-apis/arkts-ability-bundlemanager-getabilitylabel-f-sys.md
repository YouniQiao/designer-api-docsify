# getAbilityLabel（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAbilityLabel

```TypeScript
function getAbilityLabel(bundleName: string, moduleName: string, abilityName: string, callback: AsyncCallback<string>): void
```

获取指定bundleName、moduleName和abilityName的label。使用callback异步回调。获取调用方自身的信息时不需要权限。

**起始版本：** 9

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

**系统能力：** SystemCapability.BundleManager.BundleFramework.Resource

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |
| abilityName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700026](../errorcode-bundle.md#17700026-指定应用被禁用) |
| [17700029](../errorcode-bundle.md#17700029-指定的ability被禁用) |


## getAbilityLabel

```TypeScript
function getAbilityLabel(bundleName: string, moduleName: string, abilityName: string): Promise<string>
```

获取指定bundleName、moduleName和abilityName的label。使用Promise异步回调。获取调用方自身的信息时不需要权限。

**起始版本：** 9

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

**系统能力：** SystemCapability.BundleManager.BundleFramework.Resource

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |
| abilityName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700026](../errorcode-bundle.md#17700026-指定应用被禁用) |
| [17700029](../errorcode-bundle.md#17700029-指定的ability被禁用) |
