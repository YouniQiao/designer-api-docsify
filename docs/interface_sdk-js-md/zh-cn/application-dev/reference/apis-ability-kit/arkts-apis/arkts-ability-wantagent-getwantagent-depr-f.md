# getWantAgent

## 导入模块

```TypeScript
```

## getWantAgent

```TypeScript
function getWantAgent(info: WantAgentInfo, callback: AsyncCallback<WantAgent>): void
```

创建WantAgent。创建失败返回的WantAgent为空值。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getWantAgent](arkts-ability-wantagent-getwantagent-f.md)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [WantAgentInfo](arkts-ability-wantagentinfo-wantagentinfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[WantAgent](arkts-ability-wantagent-depr-t.md)&gt; | 是 |


## getWantAgent

```TypeScript
function getWantAgent(info: WantAgentInfo): Promise<WantAgent>
```

创建WantAgent。创建失败返回的WantAgent为空值。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getWantAgent](arkts-ability-wantagent-getwantagent-f.md)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [WantAgentInfo](arkts-ability-wantagentinfo-wantagentinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[WantAgent](arkts-ability-wantagent-depr-t.md)&gt; |
