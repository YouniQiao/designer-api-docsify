# postCardAction

## postCardAction

```TypeScript
declare function postCardAction(component: Object, action: Object): void
```

执行函数内部的交互，处理component和action对象的相关操作。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-unnamed-declare function postCardAction(component: Object, action: Object): void--><!--Device-unnamed-declare function postCardAction(component: Object, action: Object): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### action参数说明

| **参数名** | **类型** | **必填** | **说明：** |
| -------- | -------- | -------- | -------- |  
| action | string | 是 |action的类型，支持以下预定义的类型：<br>-&nbsp;router：跳转到提供方应用的指定UIAbility，只允许在点击事件中触发。<br>-&nbsp;message：自定义消息，触发后会调用提供方FormExtensionAbility的[onFormEvent()](../../apis-form-kit/arkts-apis/arkts-form-app-form-formextensionability-formextensionability-c.md#onformevent)生命周期回调。<br>-&nbsp;call：后台启动提供方应用。触发后会拉起提供方应用的指定UIAbility（仅支持launchType为singleton的[UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md)，即启动模式为单实例的UIAbility），但不会调度到前台。提供方应用需要具备后台运行权限ohos.permission.KEEP_BACKGROUND_RUNNING。<!--Del--><br>-&nbsp;insightIntent：通过[意图框架](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-insightintent.md)执行意图跳转到提供方应用，只允许在点击事件中触发，仅拥有意图执行权限ohos.permission.EXECUTE_INSIGHT_INTENT 的系统应用支持。<br>**起始版本：** 26.0.1<!--DelEnd--> |  
| bundleName | string | 否 | action为router&nbsp;/&nbsp;call&nbsp;类型时跳转的包名。<!--Del-->action为insightIntent&nbsp;类型时可指定意图跳转目标的包名，缺省时使用卡片提供方应用的包名。<!--DelEnd--> |  
| moduleName | string | 否 | action为router&nbsp;/&nbsp;call&nbsp;类型时跳转的模块名。<!--Del-->action为insightIntent&nbsp;类型时可指定意图跳转目标的模块名，缺省时使用卡片提供方应用的模块名。<!--DelEnd--> |  
| abilityName | string | 否 | action为router&nbsp;/&nbsp;call&nbsp;类型时跳转的UIAbility名。<!--Del-->action为insightIntent&nbsp;类型时可指定意图跳转目标的UIAbility名，缺省时使用提供方应用[module.json5配置文件](../../quick-start/module-configuration-file.md)中入口UIAbility对应的名称。<!--DelEnd--> |  
| uri<sup>11+</sup> | string | 否 | action为router&nbsp;类型时跳转的UIAbility的统一资源标识符。uri和abilityName同时存在时，abilityName优先。<!--Del-->enableRouteSecondPage为true时，uri可与abilityName同时生效，用于跳转到提供方应用的二级页面，仅系统应用支持。<!--DelEnd--> |<!--Del-->  
| enableRouteSecondPage | boolean | 否 | action为router&nbsp;类型时是否允许uri与abilityName同时生效，以跳转到提供方应用的二级页面，默认为false，仅系统应用支持。<br>**起始版本：** 26.0.1 |  
| intentName | string | 否 | action为insightIntent&nbsp;类型时指定要执行的意图名称，缺省时会导致无法找到对应意图名称，仅拥有意图执行权限ohos.permission.EXECUTE_INSIGHT_INTENT 的系统应用支持。<br>**起始版本：** 26.0.1 |<!--DelEnd-->  
| params | Object | 否 | 当前action携带的额外参数，内容使用JSON格式的键值对形式。<!--Del-->action为insightIntent&nbsp;类型时，"params"中可填入参数'intentParams'和'executeMode'，详见下方说明。<!--DelEnd--> |

### 说明

"action"为"call" 类型时，"params"需填入参数'method'，且类型需为string类型，用于触发UIAbility中对应的方法。<!--Del-->"action"为"insightIntent" 类型时，"intentName"类型需为string类型，用于指定要执行的意图名称；"params"中可填入参数'intentParams'和'executeMode'：'intentParams'类型为object，用于承载意图执行所需的业务参数，参数值仅支持string、number和boolean类型；'executeMode'类型为number，用于指定意图的执行模式，取值参考ExecuteMode，缺省为0，当前仅支持取值为0（UI_ABILITY_FOREGROUND），即前台拉起；意图执行场景不支持隐式uri类型，跳转目标仅支持通过bundleName、moduleName、abilityName显式指定。使用insightIntent类型时，提供方应用需申请ohos.permission.EXECUTE_INSIGHT_INTENT权限。<!--DelEnd-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| component | Object | 是 | 自定义组件的实例，通常传入this。 |
| action | Object | 是 | action的具体描述，参考action参数说明。 |
