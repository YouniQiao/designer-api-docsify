# clearPreloadedUIExtensionAbility（系统接口）

## 导入模块

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## clearPreloadedUIExtensionAbility

```TypeScript
function clearPreloadedUIExtensionAbility(preloadId: number): Promise<void>
```

清除指定的[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)实例。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| preloadId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000003](../errorcode-ability.md#16000003-指定的id不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
