# getTopAbility（系统接口）

## getTopAbility

```TypeScript
function getTopAbility(): Promise<ElementName>
```

获取窗口焦点所在的Ability。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-abilityManager-function getTopAbility(): Promise<ElementName>--><!--Device-abilityManager-function getTopAbility(): Promise<ElementName>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ElementName](arkts-ability-elementname-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## getTopAbility

```TypeScript
function getTopAbility(callback: AsyncCallback<ElementName>): void
```

获取窗口焦点所在的Ability。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-abilityManager-function getTopAbility(callback: AsyncCallback<ElementName>): void--><!--Device-abilityManager-function getTopAbility(callback: AsyncCallback<ElementName>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ElementName](arkts-ability-elementname-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
