# OnErrorFn（系统接口）

```TypeScript
type OnErrorFn = (code: number, name: string, message: string) => void
```

Defines a OnError function.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-type OnErrorFn = (code: number, name: string, message: string) => void--><!--Device-unnamed-type OnErrorFn = (code: number, name: string, message: string) => void-End-->

**系统能力：** SystemCapability.Ability.AppExtension.VerticalPanel

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | The code returned if the UIAbility or UIExtensionAbility failed to start. |
| name | string | 是 | The name returned if the UIAbility or UIExtensionAbility failed to start. |
| message | string | 是 | The message returned if the UIAbility or UIExtensionAbility failed to start. |

