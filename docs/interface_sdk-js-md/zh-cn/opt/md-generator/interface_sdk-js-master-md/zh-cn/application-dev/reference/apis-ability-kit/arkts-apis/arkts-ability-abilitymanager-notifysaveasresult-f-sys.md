# notifySaveAsResult（系统接口）

## notifySaveAsResult

```TypeScript
function notifySaveAsResult(parameter: AbilityResult, requestCode: number, callback: AsyncCallback<void>): void
```

该接口仅供[DLP](../../apis-data-protection-kit/arkts-apis/arkts-dlppermission.md/arkts-dlppermission.md)（Data Loss Prevention, 数据丢失防护）管理应用使用，其他应用禁止使用，DLP管理应用通过该接口通知沙箱应用另存为结果。使用callback异步回调。

> **说明：**
> 
> 从API version 10开始支持，从API version 24开始废弃。

**起始版本：** 10

**废弃版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-abilityManager-function notifySaveAsResult(parameter: AbilityResult, requestCode: int, callback: AsyncCallback<void>): void--><!--Device-abilityManager-function notifySaveAsResult(parameter: AbilityResult, requestCode: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | 是 |
| requestCode | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## notifySaveAsResult

```TypeScript
function notifySaveAsResult(parameter: AbilityResult, requestCode: number): Promise<void>
```

该接口仅供[DLP](../../apis-data-protection-kit/arkts-apis/arkts-dlppermission.md/arkts-dlppermission.md)（Data Loss Prevention, 数据丢失防护）管理应用使用，其他应用禁止使用，DLP管理应用通过该接口通知沙箱应用另存为结果。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-abilityManager-function notifySaveAsResult(parameter: AbilityResult, requestCode: int): Promise<void>--><!--Device-abilityManager-function notifySaveAsResult(parameter: AbilityResult, requestCode: int): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | 是 |
| requestCode | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
