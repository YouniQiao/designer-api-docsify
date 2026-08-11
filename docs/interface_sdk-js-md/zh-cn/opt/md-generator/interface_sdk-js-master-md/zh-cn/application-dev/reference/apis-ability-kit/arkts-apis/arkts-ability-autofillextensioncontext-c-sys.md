# AutoFillExtensionContext（系统接口）

AutoFillExtensionContext模块是AutoFillExtensionAbility的上下文环境，继承自  
[ExtensionContext](arkts-ability-extensioncontext-c.md)。

**继承/实现关系：** AutoFillExtensionContext extends [ExtensionContext](arkts-ability-extensioncontext-c.md)

**起始版本：** 11

<!--Device-unnamed-declare class AutoFillExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class AutoFillExtensionContext extends ExtensionContext-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

## reloadInModal

```TypeScript
reloadInModal(customData: CustomData): Promise<void>
```

拉起模态页面。使用Promise异步回调。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AutoFillExtensionContext-reloadInModal(customData: CustomData): Promise<void>--><!--Device-AutoFillExtensionContext-reloadInModal(customData: CustomData): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| customData | [CustomData](arkts-ability-customdata-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
