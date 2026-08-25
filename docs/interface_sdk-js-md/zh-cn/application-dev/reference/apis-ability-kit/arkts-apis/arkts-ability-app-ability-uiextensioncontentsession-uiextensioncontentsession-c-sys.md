# UIExtensionContentSession

UIExtensionAbility组件的界面操作类，提供页面加载、设置宿主应用窗口隐私模式等功能。

**起始版本：** 10

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { UIExtensionContentSession } from 'kits/@kit.AbilityKit';
```

## getUIExtensionHostWindowProxy

```TypeScript
getUIExtensionHostWindowProxy(): uiExtensionHost.UIExtensionHostWindowProxy
```

获取当前UIExtension对应的窗口对象，用于通知宽高、位置、避让信息等。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| uiExtensionHost.UIExtensionHostWindowProxy |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## sendData

```TypeScript
sendData(data: Record<string, Object>): void
```

发送数据给UIExtensionComponent控件。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Record & lt;string, Object & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## setReceiveDataCallback

```TypeScript
setReceiveDataCallback(callback: (data: Record<string, Object>) => void): void
```

设置从UIExtensionComponent控件接收数据的回调方法。使用callback异步回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (data: Record & lt;string, Object & gt;) = & gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## setReceiveDataForResultCallback

```TypeScript
setReceiveDataForResultCallback(callback: (data: Record<string, Object>) => Record<string, Object>): void
```

设置从UIExtensionComponent控件接收数据带返回值的回调方法。使用callback异步回调。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (data: Record & lt;string, Object & gt;) = & gt; Record & lt;string, Object & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## setWindowBackgroundColor

```TypeScript
setWindowBackgroundColor(color: string): void
```

设置UIExtensionAbility加载界面的背景色。该接口需要在 [loadContent()](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md#loadcontent)调用生效后使用。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## startAbility

```TypeScript
startAbility(want: Want, callback: AsyncCallback<void>): void
```

启动Ability。使用callback异步回调。

> **说明：**&gt;
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> 
> 对应UIExtensionComponent控件所在的应用需要处于前台获焦状态。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## startAbility

```TypeScript
startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
```

启动Ability。使用callback异步回调。

> **说明：**&gt;
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> 
> 对应UIExtensionComponent控件所在的应用需要处于前台获焦状态。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## startAbility

```TypeScript
startAbility(want: Want, options?: StartOptions): Promise<void>
```

启动Ability。使用Promise异步回调。

> **说明：**&gt;
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> 
> 对应UIExtensionComponent控件所在的应用需要处于前台获焦状态。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## startAbilityAsCaller

```TypeScript
startAbilityAsCaller(want: Want, callback: AsyncCallback<void>): void
```

初始Ability将自己的caller信息（如BundleName、AbilityName等）置于want参数中，传递给中间层的ExtensionAbility。当ExtensionAbility通过该接口拉起另外一个 Ability，被拉起的Ability可以从onCreate生命周期获取到初始Ability的caller信息。使用callback异步回调。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## startAbilityAsCaller

```TypeScript
startAbilityAsCaller(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
```

初始Ability将自己的caller信息（如BundleName、AbilityName等）置于want参数中，传递给中间层的ExtensionAbility。当ExtensionAbility通过该接口拉起另外一个 Ability，被拉起的Ability可以从onCreate生命周期获取到初始Ability的caller信息。使用callback异步回调。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## startAbilityAsCaller

```TypeScript
startAbilityAsCaller(want: Want, options?: StartOptions): Promise<void>
```

初始Ability将自己的caller信息（如BundleName、AbilityName等）置于want参数中，传递给中间层的ExtensionAbility。当ExtensionAbility通过该接口拉起另外一个 Ability，被拉起的Ability可以从onCreate生命周期获取到初始Ability的caller信息。使用Promise异步回调。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void
```

启动一个Ability，在Ability终止后返回结果给调用方。使用callback异步回调。 Ability的终止方式包括以下几种情况：  
- 正常情况下可通过调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) 接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死Ability会返回异常信息给调用方，异常信息中resultCode为-1。  
- 如果被启动的Ability模式是单实例模式，不同应用多次调用该接口启动这个Ability，当这个Ability调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) 接口使之终止时，只将正常结果返回给最后一个调用方，其他调用方返回异常信息，异常信息中resultCode为-1。

> **说明：**&gt;
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> 
> 对应UIExtensionComponent控件所在的应用需要处于前台获焦状态。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void
```

启动一个Ability，在Ability终止后返回结果给调用方。使用callback异步回调。 Ability的终止方式包括以下几种情况：  
- 正常情况下可通过调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) 接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死Ability会返回异常信息给调用方，异常信息中resultCode为-1。  
- 如果被启动的Ability模式是单实例模式，不同应用多次调用该接口启动这个Ability，当这个Ability调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) 接口使之终止时，只将正常结果返回给最后一个调用方，其他调用方返回异常信息，异常信息中resultCode为-1。

> **说明：**&gt;
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> 
> 对应UIExtensionComponent控件所在的应用需要处于前台获焦状态。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>
```

启动一个Ability，在Ability终止后返回结果给调用方。使用Promise异步回调。 Ability的终止方式包括以下几种情况：  
- 正常情况下可通过调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) 接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死Ability会返回异常信息给调用方，异常信息中resultCode为-1。  
- 如果被启动的Ability模式是单实例模式，不同应用多次调用该接口启动这个Ability，当这个Ability调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) 接口使之终止时，只将正常结果返回给最后一个调用方，其他调用方返回异常信息，异常信息中resultCode为-1。

> **说明：**&gt;
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> 
> 对应UIExtensionComponent控件所在的应用需要处于前台获焦状态。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
