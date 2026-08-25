# LiveFormExtensionContext

LiveFormExtensionContext是[LiveFormExtensionAbility](arkts-form-app-form-liveformextensionability-liveformextensionability-c.md)的上下文，继承自 [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md)。它提供访问特定于LiveFormExtensionAbility资源的能力，支持在互动卡片中拉起应用页面，适用 于需要在互动卡片中响应用户点击并跳转到应用页面的场景，解决了互动卡片无法主动拉起应用页面的限制问题。

**继承/实现关系：** LiveFormExtensionContext extends ExtensionContext

**起始版本：** 20

**系统能力：** SystemCapability.Ability.Form

## startAbilityByLiveForm

```TypeScript
startAbilityByLiveForm(want: Want): Promise<void>
```

拉起互动卡片提供方（应用）的页面，使用Promise异步回调。该接口仅支持拉起互动卡片提供方（应用）的页面，不支持拉起其他应用的页面，否则会抛出错误码16501011。该接口仅限在点击事件回调中调用，且需要直接调用，不支持延时后调用，否则会抛出错误码16501011。  
- 互动卡片激活态中点击跳转到应用主页或详情页。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16501011](../errorcode-form.md#16501011-卡片不支持调用当前接口) |
