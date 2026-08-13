# getWant（系统接口）

## getWant

```TypeScript
function getWant(agent: WantAgent, callback: AsyncCallback<Want>): void
```

获取WantAgent对象的want。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-wantAgent-function getWant(agent: WantAgent, callback: AsyncCallback<Want>): void--><!--Device-wantAgent-function getWant(agent: WantAgent, callback: AsyncCallback<Want>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [agent](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000007](../errorcode-ability.md#16000007-服务未响应) |
| [16000151](../errorcode-ability.md#16000151-无效wantagent对象) |
| [16000015](../errorcode-ability.md#16000015-服务超时) |


## getWant

```TypeScript
function getWant(agent: WantAgent): Promise<Want>
```

获取WantAgent对象的want。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-wantAgent-function getWant(agent: WantAgent): Promise<Want>--><!--Device-wantAgent-function getWant(agent: WantAgent): Promise<Want>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [agent](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000007](../errorcode-ability.md#16000007-服务未响应) |
| [16000151](../errorcode-ability.md#16000151-无效wantagent对象) |
| [16000015](../errorcode-ability.md#16000015-服务超时) |
