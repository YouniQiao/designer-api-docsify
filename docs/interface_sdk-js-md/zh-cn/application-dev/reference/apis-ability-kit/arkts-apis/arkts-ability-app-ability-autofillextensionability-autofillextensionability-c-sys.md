# AutoFillExtensionAbility（系统接口）

AutoFillExtensionAbility模块支持账号、密码、地址等多种数据类型的自动填充与保存，继承自 [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md)。

**继承/实现关系：** AutoFillExtensionAbility extends ExtensionAbility

**起始版本：** 11

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { AutoFillExtensionAbility } from 'kits/@kit.AbilityKit';
```

## onBackground

```TypeScript
onBackground(): void
```

当AutoFillExtensionAbility从前台转到后台时触发。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

## onCreate

```TypeScript
onCreate(): void
```

AutoFillExtensionAbility创建时触发回调函数。在此方法中可进行初始化操作，如注册监听器、加载必要资源等。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

## onDestroy

```TypeScript
onDestroy(): void | Promise<void>
```

在AutoFillExtensionAbility销毁时回调，执行资源清理等操作。回调结束直接返回，或者使用Promise异步回调。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

## onFillRequest

```TypeScript
onFillRequest(session: UIExtensionContentSession, request: FillRequest, callback: FillRequestCallback): void
```

当发起自动填充请求或者生成密码时触发此回调函数。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| session | [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | 是 |
| request | [FillRequest](arkts-ability-autofillrequest-fillrequest-i.md) | 是 |
| callback | [FillRequestCallback](arkts-ability-autofillrequest-fillrequestcallback-i-sys.md) | 是 |

## onForeground

```TypeScript
onForeground(): void
```

当AutoFillExtensionAbility从后台转到前台时触发。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

## onSaveRequest

```TypeScript
onSaveRequest(session: UIExtensionContentSession, request: SaveRequest, callback: SaveRequestCallback): void
```

当发起自动保存或者手动保存时触发此回调函数。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| session | [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | 是 |
| request | [SaveRequest](arkts-ability-autofillrequest-saverequest-i-sys.md) | 是 |
| callback | [SaveRequestCallback](arkts-ability-autofillrequest-saverequestcallback-i-sys.md) | 是 |

## onSessionDestroy

```TypeScript
onSessionDestroy(session: UIExtensionContentSession): void
```

当AutoFillExtensionAbility的session销毁时触发此回调。session通常在用户取消填充操作或填充任务完成后销毁。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| session | [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | 是 |

## onUpdateRequest

```TypeScript
onUpdateRequest(request: UpdateRequest): void
```

当应用界面数据发生变化、需要更新已填充的内容时，系统触发此回调函数。request参数包含更新后的viewData等信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [UpdateRequest](arkts-ability-autofillrequest-updaterequest-i-sys.md) | 是 |

## context

```TypeScript
context: AutoFillExtensionContext
```

AutoFillExtension的上下文环境，继承自ExtensionContext。

**类型：** [AutoFillExtensionContext](arkts-ability-autofillextensioncontext-c-sys.md)

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**系统接口：** 此接口为系统接口。
