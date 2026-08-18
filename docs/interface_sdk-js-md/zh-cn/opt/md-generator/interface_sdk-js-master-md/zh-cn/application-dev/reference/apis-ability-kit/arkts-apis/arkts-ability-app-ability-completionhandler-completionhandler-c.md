# CompletionHandler

CompletionHandler提供了 [onRequestSuccess](#onrequestsuccess)和 [onRequestFailure](#onrequestfailure)两个回调函数，分别用来处理拉 起应用成功和失败时的结果。

**起始版本：** 23

<!--Device-unnamed-declare class CompletionHandler--><!--Device-unnamed-declare class CompletionHandler-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
```

## onRequestFailure

```TypeScript
onRequestFailure(elementName: ElementName, message: string): void
```

拉起应用失败时的回调函数。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-CompletionHandler-onRequestFailure(elementName: ElementName, message: string): void--><!--Device-CompletionHandler-onRequestFailure(elementName: ElementName, message: string): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| message | string | 是 |

**示例**

参见CompletionHandler使用。

## onRequestSuccess

```TypeScript
onRequestSuccess(elementName: ElementName, message: string): void
```

拉起应用成功时的回调函数。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-CompletionHandler-onRequestSuccess(elementName: ElementName, message: string): void--><!--Device-CompletionHandler-onRequestSuccess(elementName: ElementName, message: string): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| message | string | 是 |

**示例**

参见CompletionHandler使用。

## onRequestFailure

```TypeScript
onRequestFailure: OnRequestFailureFn
```

拉端失败时的回调函数。

**类型：** [OnRequestFailureFn](arkts-ability-onrequestfailurefn-t.md)

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CompletionHandler-onRequestFailure: OnRequestFailureFn--><!--Device-CompletionHandler-onRequestFailure: OnRequestFailureFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onRequestSuccess

```TypeScript
onRequestSuccess: OnRequestSuccessFn
```

拉端成功时的回调函数。

**类型：** [OnRequestSuccessFn](arkts-ability-onrequestsuccessfn-t.md)

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CompletionHandler-onRequestSuccess: OnRequestSuccessFn--><!--Device-CompletionHandler-onRequestSuccess: OnRequestSuccessFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
