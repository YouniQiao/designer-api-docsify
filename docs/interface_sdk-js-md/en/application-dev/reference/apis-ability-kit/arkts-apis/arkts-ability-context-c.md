# Context

Context是Stage模型的上下文基类，主要用于访问特定应用程序的资源，以及执行应用级操作的回调。

**Inheritance/Implementation:** Context extends [BaseContext](arkts-ability-basecontext-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class Context extends BaseContext--><!--Device-unnamed-declare class Context extends BaseContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## createAreaModeContext

```TypeScript
createAreaModeContext(areaMode: contextConstant.AreaMode): Context
```

创建特定数据加密级别的应用上下文。开发者可以调用该接口创建不同加密级别的上下文，从而获取对应的沙箱路径。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Context-createAreaModeContext(areaMode: contextConstant.AreaMode): Context--><!--Device-Context-createAreaModeContext(areaMode: contextConstant.AreaMode): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| areaMode | contextConstant.AreaMode | Yes | 指定的数据加密等级。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | 指定数据加密等级的上下文。 |

## createDisplayContext

ArkTS-Dyn:
```TypeScript
createDisplayContext(displayId: number): Context
```

ArkTS-Sta:
```TypeScript
createDisplayContext(displayId: long): Context
```

根据指定的物理屏幕ID创建带有屏幕信息（包括屏幕密度[ScreenDensity](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-screendensity-e.md/arkts-localization-resourcemanager-screendensity-e.md)和屏幕方向  
[Direction](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-direction-e.md/arkts-localization-resourcemanager-direction-e.md)）的应用上下文。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-Context-createDisplayContext(displayId: long): Context--><!--Device-Context-createDisplayContext(displayId: long): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 物理屏幕ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | 带有指定物理屏幕信息的上下文。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

## createModuleContext

```TypeScript
createModuleContext(moduleName: string): Context
```

根据模块名创建上下文。

> **说明：**
> 
> - 仅支持获取本应用中其他Module的Context和应用内HSP的Context，不支持获取其他应用的Context。
> - 由于创建模块上下文的过程涉及资源查询与初始化，耗时相对较长，在对应用流畅性要求较高的场景下，不建议频繁或多次调用createModuleContext接口创建多个Context实例，以免影响用户体验。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

**Substitutes:** [@ohos.app.ability.application:application.createModuleContext](arkts-ability-application-createmodulecontext-f.md#createmodulecontext)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-createModuleContext(moduleName: string): Context--><!--Device-Context-createModuleContext(moduleName: string): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 模块名。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | 模块的上下文。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

## getApplicationContext

```TypeScript
getApplicationContext(): ApplicationContext
```

获取当前应用上下文。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-getApplicationContext(): ApplicationContext--><!--Device-Context-getApplicationContext(): ApplicationContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ApplicationContext](arkts-ability-applicationcontext-c.md) | 应用上下文。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2 .Incorrect parameter types. |

## getGroupDir

```TypeScript
getGroupDir(dataGroupID: string, callback: AsyncCallback<string>): void
```

通过应用中的Group ID获取对应的共享目录，使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-getGroupDir(dataGroupID: string, callback: AsyncCallback<string>): void--><!--Device-Context-getGroupDir(dataGroupID: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataGroupID | string | Yes | 原子化服务类型的应用创建时，系统会指定分配唯一Group ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数。当获取共享目录成功，err为undefined，data为对应的共享目录，如果不存在则返回为空；否则为错误对象。&lt;br&gt;**说明：**仅支持应用el2加密级别。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |

## getGroupDir

```TypeScript
getGroupDir(dataGroupID: string): Promise<string>
```

通过应用中的Group ID获取对应的共享目录，使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-getGroupDir(dataGroupID: string): Promise<string>--><!--Device-Context-getGroupDir(dataGroupID: string): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dataGroupID | string | Yes | 原子化服务类型的应用创建时，系统会指定分配唯一Group ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回对应的共享目录。如果不存在则返回为空，仅支持应用el2加密级别。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2 .Incorrect parameter types. |
| 16000011 | The context does not exist. |

## isContextOf

```TypeScript
isContextOf(contextType: contextConstant.ContextType): boolean
```

判断当前Context是否为指定的ContextType类型。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Context-isContextOf(contextType: contextConstant.ContextType): boolean--><!--Device-Context-isContextOf(contextType: contextConstant.ContextType): boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| contextType | contextConstant.ContextType | Yes | 上下文类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否为指定类型的上下文。返回true表示Context类型为指定类型，返回false表示Context类型匹配失败。 |

## applicationInfo

```TypeScript
applicationInfo: ApplicationInfo
```

当前应用程序的信息。

**Type:** [ApplicationInfo](arkts-ability-applicationinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-applicationInfo: ApplicationInfo--><!--Device-Context-applicationInfo: ApplicationInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## area

```TypeScript
area: contextConstant.AreaMode
```

文件分区信息，按加密等级[AreaMode](arkts-ability-contextconstant-areamode-e.md)进行分区。

**Type:** contextConstant.AreaMode

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-area: contextConstant.AreaMode--><!--Device-Context-area: contextConstant.AreaMode-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## bundleCodeDir

```TypeScript
bundleCodeDir: string
```

安装包目录。不能拼接路径访问资源文件，请使用[资源管理接口](arkts-ability-context-c.md#resourcemanager)访问资源，详情参考  
[应用沙箱目录](../../../file-management/app-sandbox-directory.md)。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-bundleCodeDir: string--><!--Device-Context-bundleCodeDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## cacheDir

```TypeScript
cacheDir: string
```

缓存目录，详情参考[应用沙箱目录](../../../file-management/app-sandbox-directory.md)。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-cacheDir: string--><!--Device-Context-cacheDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## cloudFileDir

```TypeScript
cloudFileDir: string
```

云文件目录。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Context-cloudFileDir: string--><!--Device-Context-cloudFileDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## databaseDir

```TypeScript
databaseDir: string
```

数据库目录，详情参考[应用沙箱目录](../../../file-management/app-sandbox-directory.md)。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-databaseDir: string--><!--Device-Context-databaseDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## distributedFilesDir

```TypeScript
distributedFilesDir: string
```

分布式文件目录，详情参考[应用沙箱目录](../../../file-management/app-sandbox-directory.md)。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-distributedFilesDir: string--><!--Device-Context-distributedFilesDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## eventHub

```TypeScript
eventHub: EventHub
```

事件中心，提供订阅、取消订阅、触发事件对象。

**Type:** [EventHub](arkts-ability-eventhub-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-eventHub: EventHub--><!--Device-Context-eventHub: EventHub-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## filesDir

```TypeScript
filesDir: string
```

文件目录，详情参考[应用沙箱目录](../../../file-management/app-sandbox-directory.md)。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-filesDir: string--><!--Device-Context-filesDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## logFileDir

```TypeScript
get logFileDir(): string
```

日志文件目录。

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Context-get logFileDir(): string--><!--Device-Context-get logFileDir(): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## preferencesDir

```TypeScript
preferencesDir: string
```

preferences目录，详情参考[应用沙箱目录](../../../file-management/app-sandbox-directory.md)。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-preferencesDir: string--><!--Device-Context-preferencesDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## processName

```TypeScript
processName: string
```

当前应用的进程名。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Context-processName: string--><!--Device-Context-processName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## resourceDir

```TypeScript
resourceDir: string
```

资源目录。

> **说明：**
> 
> 需要开发者手动在`\&lt;module-name&gt;\resource`路径下创建`resfile`目录。创建的`resfile`目录仅支持以只读方式访问。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-resourceDir: string--><!--Device-Context-resourceDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## resourceManager

```TypeScript
resourceManager: resmgr.ResourceManager
```

资源管理对象。

**Type:** resmgr.ResourceManager

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-resourceManager: resmgr.ResourceManager--><!--Device-Context-resourceManager: resmgr.ResourceManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## tempDir

```TypeScript
tempDir: string
```

临时目录，详情参考[应用沙箱目录](../../../file-management/app-sandbox-directory.md)。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-tempDir: string--><!--Device-Context-tempDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

