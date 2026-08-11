# ApplicationContext

ApplicationContext作为应用上下文，继承自[Context](arkts-ability-context-t.md)，提供了应用生命周期监听、进程管理、应用环境设置等应用级别的管控能力。

> **说明：**
> 
> 本模块接口仅可在Stage模型下使用。

**继承/实现关系：** ApplicationContext extends [Context](arkts-ability-context-t.md)

**起始版本：** 9

<!--Device-unnamed-declare class ApplicationContext extends Context--><!--Device-unnamed-declare class ApplicationContext extends Context-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## preloadUIExtensionAbility

```TypeScript
preloadUIExtensionAbility(want: Want): Promise<void>
```

Preload UIExtensionAbility.

**起始版本：** 12

**需要权限：** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ApplicationContext-preloadUIExtensionAbility(want: Want): Promise<void>--><!--Device-ApplicationContext-preloadUIExtensionAbility(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
