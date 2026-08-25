# isAbilityEnabled

## 导入模块

```TypeScript
import { bundle } from 'kits/@kit.AbilityKit';
```

## isAbilityEnabled

```TypeScript
function isAbilityEnabled(info: AbilityInfo, callback: AsyncCallback<boolean>): void
```

根据给定的AbilityInfo查询ability是否已经启用，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isAbilityEnabled

```TypeScript
function isAbilityEnabled(info: AbilityInfo): Promise<boolean>
```

根据给定的AbilityInfo查询ability是否已经启用，使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
