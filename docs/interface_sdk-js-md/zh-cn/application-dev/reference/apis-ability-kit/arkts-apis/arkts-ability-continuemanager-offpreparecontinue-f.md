# offPrepareContinue

## 导入模块

```TypeScript
import { continueManager } from 'kits/@kit.AbilityKit';
```

## offPrepareContinue

```TypeScript
function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void
```

Unregister prepareContinue event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-continueManager-function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void--><!--Device-continueManager-function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | 是 | the ability context. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ContinueResultInfo&gt; | 否 | Used to handle ('prepareContinue') command. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16300501 | the system ability work abnormally. |

