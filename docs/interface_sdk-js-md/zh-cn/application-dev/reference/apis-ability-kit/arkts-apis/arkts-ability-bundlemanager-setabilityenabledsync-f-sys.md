# setAbilityEnabledSync（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## setAbilityEnabledSync

```TypeScript
function setAbilityEnabledSync(info: AbilityInfo, isEnabled: boolean): void
```

以同步方法设置指定组件的禁用或使能状态。

**起始版本：** 10

**需要权限：** ohos.permission.CHANGE_ABILITY_ENABLED_STATE

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [AbilityInfo](arkts-ability-abilityinfo-i.md) | 是 |
| isEnabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700003](../errorcode-bundle.md#17700003-指定的abilityname不存在) |
