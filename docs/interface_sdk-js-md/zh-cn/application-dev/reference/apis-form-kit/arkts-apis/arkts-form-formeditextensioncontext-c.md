# FormEditExtensionContext

FormEditExtensionContext是 [FormEditExtensionAbility](arkts-form-app-form-formeditextensionability-formeditextensionability-c.md)的上下文，继承自 [UIExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiextensioncontext-c.md)。用于管理卡片编辑场景的上下文环境，支持拉起卡片提供方页面和所属应用UIAbility，适用于卡片编 辑流程中需要与卡片提供方交互的场景。

**继承/实现关系：** FormEditExtensionContext extends UIExtensionContext

**起始版本：** 18

**系统能力：** SystemCapability.Ability.Form

## startSecondPage

```TypeScript
startSecondPage(want: Want): Promise<AbilityResult>
```

拉起需要被编辑的卡片提供方页面。使用Promise异步回调。  
- 用户在卡片编辑界面点击编辑按钮，需要打开卡片提供方的编辑页面。  
- 用户需要修改卡片配置或内容时，拉起卡片提供方应用进行编辑。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AbilityResult](../../apis-ability-kit/arkts-apis/arkts-ability-abilityresult-abilityresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |

## startUIAbility

```TypeScript
startUIAbility(want: Want): Promise<void>
```

拉起卡片所属应用的UIAbility。使用Promise异步回调。说明：需在卡片编辑页面处于前台时调用，页面不在前台时调用将返回错误码16501014。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16000130](../../apis-ability-kit/errorcode-ability.md#16000130-uiability不属于调用方) |
| [16501014](../errorcode-form.md#16501014-半模态卡片编辑页不在前台) |
| [16000121](../../apis-ability-kit/errorcode-ability.md#16000121-待启动的目标组件类型不是uiability) |
