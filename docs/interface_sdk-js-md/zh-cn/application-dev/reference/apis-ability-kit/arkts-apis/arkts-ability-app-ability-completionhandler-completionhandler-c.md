# CompletionHandler

CompletionHandler提供了 [onRequestSuccess](#onrequestsuccess)和 [onRequestFailure](#onrequestfailure)两个回调函数，分别用来处理拉 起应用成功和失败时的结果。

**起始版本：** 20

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { CompletionHandler } from 'kits/@kit.AbilityKit';
```

## onRequestFailure

```TypeScript
onRequestFailure(elementName: ElementName, message: string): void
```

拉起应用失败时的回调函数。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| message | string | 是 |

## onRequestSuccess

```TypeScript
onRequestSuccess(elementName: ElementName, message: string): void
```

拉起应用成功时的回调函数。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| message | string | 是 |
