# getAbilityInfo

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAbilityInfo

```TypeScript
function getAbilityInfo(uri: string, abilityFlags: number): Promise<Array<AbilityInfo>>
```

获取指定资源标识符和组件信息标志对应的Ability信息。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.GET_ABILITY_INFO

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| abilityFlags | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;AbilityInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
