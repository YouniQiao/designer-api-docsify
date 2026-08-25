# getProfileByAbility

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getProfileByAbility

```TypeScript
function getProfileByAbility(moduleName: string, abilityName: string, metadataName: string, callback: AsyncCallback<Array<string>>): void
```

根据给定的moduleName、abilityName和metadataName（module.json5中 [abilities标签](../../../quick-start/module-configuration-file.md#abilities标签)下的metadata标签的name）获取自身相应配置文件的json格式字符串 。使用callback异步回调。

> 说明：
> 
> 如果配置文件信息采用了资源引用格式，则返回值将保持资源引用格式（例如 \$string:res_id），开发者可以通过[资源管理](../../apis-localization-kit/arkts-apis/arkts-resourcemanager.md)的相
> 关接口，来获取引用的资源。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| abilityName | string | 是 |
| metadataName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700024](../errorcode-bundle.md#17700024-没有相应的配置文件) |
| [17700029](../errorcode-bundle.md#17700029-指定的ability被禁用) |


## getProfileByAbility

```TypeScript
function getProfileByAbility(moduleName: string, abilityName: string, metadataName?: string): Promise<Array<string>>
```

根据给定的moduleName、abilityName和metadataName（module.json5中 [abilities标签](../../../quick-start/module-configuration-file.md#abilities标签)下的metadata标签的name）获取自身相应配置文件的json格式字符串 。使用Promise异步回调。

> 说明：
> 
> 如果配置文件信息采用了资源引用格式，则返回值将保持资源引用格式（例如 \$string:res_id），开发者可以通过[资源管理](../../apis-localization-kit/arkts-apis/arkts-resourcemanager.md)的相
> 关接口，来获取引用的资源。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| abilityName | string | 是 |
| metadataName | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
| [17700024](../errorcode-bundle.md#17700024-没有相应的配置文件) |
| [17700029](../errorcode-bundle.md#17700029-指定的ability被禁用) |
