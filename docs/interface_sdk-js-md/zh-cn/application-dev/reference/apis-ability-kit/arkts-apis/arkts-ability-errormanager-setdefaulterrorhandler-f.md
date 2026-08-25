# setDefaultErrorHandler

## 导入模块

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## setDefaultErrorHandler

```TypeScript
function setDefaultErrorHandler(defaultHandler?: ErrorHandler) : ErrorHandler
```

发生JS_CRASH异常时，支持链式回调，返回上一次注册的处理器，仅限主线程调用。如果传入非法参数或在子线程调用，将抛出错误码并返回undefined，因此建议使用try-catch逻辑进行处理。若接口参数为空，后续注册的处理器将无法与前序已注册的处理器建立关联，从而中断链式调用。

**起始版本：** 21

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| defaultHandler | [ErrorHandler](arkts-ability-errormanager-errorhandler-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ErrorHandler](arkts-ability-errormanager-errorhandler-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [16000205](../errorcode-ability.md#16000205-当前接口未在主线程中调用) |
