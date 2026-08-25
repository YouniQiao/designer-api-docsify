# queryBusinessAbilityInfo（系统接口）

## 导入模块

```TypeScript
import { businessAbilityRouter } from 'kits/@kit.AbilityKit';
```

## queryBusinessAbilityInfo

```TypeScript
function queryBusinessAbilityInfo(
    filter: BusinessAbilityFilter,
    callback: AsyncCallback<Array<BusinessAbilityInfo>>
  ): void
```

通过给定的过滤条件查询Ability信息。使用callback异步回调，成功时返回查询到的路由Ability信息，失败时返回错误信息。

**起始版本：** 10

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [BusinessAbilityFilter](arkts-ability-businessabilityrouter-businessabilityfilter-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;BusinessAbilityInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## queryBusinessAbilityInfo

```TypeScript
function queryBusinessAbilityInfo(filter: BusinessAbilityFilter): Promise<Array<BusinessAbilityInfo>>
```

通过给定的过滤条件查询Ability信息。使用Promise异步回调，成功时返回查询到的路由Ability信息，失败时返回错误信息。

**起始版本：** 10

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [BusinessAbilityFilter](arkts-ability-businessabilityrouter-businessabilityfilter-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;BusinessAbilityInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
