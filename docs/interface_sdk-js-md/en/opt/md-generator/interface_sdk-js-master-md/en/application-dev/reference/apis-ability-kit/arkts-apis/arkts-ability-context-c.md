# Context

Context is the context base class of the stage model. It is used to access application-specific resources and perform callbacks for application-level operations.../../../

**Inheritance/Implementation:** Context extends [BaseContext](arkts-ability-basecontext-c.md)

**Since:** 9

<!--Device-unnamed-declare class Context extends BaseContext--><!--Device-unnamed-declare class Context extends BaseContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## createAreaModeContext

```TypeScript
createAreaModeContext(areaMode: contextConstant.AreaMode): Context
```

Creates an application context with a specific data encryption level. You can call this API to create contexts with different encryption levels, thereby obtaining the corresponding sandbox paths.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Context-createAreaModeContext(areaMode: contextConstant.AreaMode): Context--><!--Device-Context-createAreaModeContext(areaMode: contextConstant.AreaMode): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| areaMode | contextConstant.AreaMode | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) |

## createDisplayContext

```TypeScript
createDisplayContext(displayId: number): Context
```

Creates an application context based on the specified display ID with screen information (including  
[ScreenDensity](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-screendensity-e.md/arkts-localization-resourcemanager-screendensity-e.md) and  
[Direction](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-direction-e.md/arkts-localization-resourcemanager-direction-e.md)).

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-Context-createDisplayContext(displayId: long): Context--><!--Device-Context-createDisplayContext(displayId: long): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## createModuleContext

```TypeScript
createModuleContext(moduleName: string): Context
```

Creates the context based on the module name.

> **NOTE：**
> 
> - Only the context of other modules in the current application and the context of the intra-application HSP can
> be obtained. The context of other applications cannot be obtained.
> 
> - This API has been supported since API version 9 and deprecated since API version 12. You are advised to use
> [application.createModuleContext](arkts-ability-application-createmodulecontext-f.md#createmodulecontext)
> instead. Otherwise, resource acquisition may fail.
> 
> - Creating a module context involves resource querying and initialization, which can be time-consuming. In
> scenarios where application fluidity is critical, avoid frequently or repeatedly calling the
> **createModuleContext** API to create multiple context instances, as this may negatively impact user experience.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [@ohos.app.ability.application:application.createModuleContext](arkts-ability-application-createmodulecontext-f.md#createmodulecontext)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-createModuleContext(moduleName: string): Context--><!--Device-Context-createModuleContext(moduleName: string): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getApplicationContext

```TypeScript
getApplicationContext(): ApplicationContext
```

Obtains the application context.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-getApplicationContext(): ApplicationContext--><!--Device-Context-getApplicationContext(): ApplicationContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ApplicationContext](arkts-ability-applicationcontext-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getGroupDir

```TypeScript
getGroupDir(dataGroupID: string, callback: AsyncCallback<string>): void
```

Obtains the shared directory based on a group ID. This API uses an asynchronous callback to return the result.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-getGroupDir(dataGroupID: string, callback: AsyncCallback<string>): void--><!--Device-Context-getGroupDir(dataGroupID: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataGroupID | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## getGroupDir

```TypeScript
getGroupDir(dataGroupID: string): Promise<string>
```

Obtains the shared directory based on a group ID. This API uses a promise to return the result.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-getGroupDir(dataGroupID: string): Promise<string>--><!--Device-Context-getGroupDir(dataGroupID: string): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataGroupID | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## isContextOf

```TypeScript
isContextOf(contextType: contextConstant.ContextType): boolean
```

Checks if the current instance is associated with the specified context type.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Context-isContextOf(contextType: contextConstant.ContextType): boolean--><!--Device-Context-isContextOf(contextType: contextConstant.ContextType): boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| contextType | contextConstant.ContextType | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## applicationInfo

```TypeScript
applicationInfo: ApplicationInfo
```

Application information.

**Type:** [ApplicationInfo](arkts-ability-applicationinfo-i.md)

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-applicationInfo: ApplicationInfo--><!--Device-Context-applicationInfo: ApplicationInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## area

```TypeScript
area: contextConstant.AreaMode
```

Information about file partitions, which are divided according to the encryption level specified by  
[AreaMode](arkts-ability-contextconstant-areamode-e.md).

**Type:** contextConstant.AreaMode

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-area: contextConstant.AreaMode--><!--Device-Context-area: contextConstant.AreaMode-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## bundleCodeDir

```TypeScript
bundleCodeDir: string
```

Bundle code directory. Do not access resource files using concatenated paths.Use [resource manager APIs](arkts-ability-context-c.md#resourcemanager) instead.For details, see [Application Sandbox](../../../file-management/app-sandbox-directory.md).

**Type:** string

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-bundleCodeDir: string--><!--Device-Context-bundleCodeDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## cacheDir

```TypeScript
cacheDir: string
```

Cache directory.For details, see [Application Sandbox](../../../file-management/app-sandbox-directory.md).

**Type:** string

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-cacheDir: string--><!--Device-Context-cacheDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## cloudFileDir

```TypeScript
cloudFileDir: string
```

Cloud file directory.

**Type:** string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Context-cloudFileDir: string--><!--Device-Context-cloudFileDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## databaseDir

```TypeScript
databaseDir: string
```

Database directory.For details, see [Application Sandbox](../../../file-management/app-sandbox-directory.md).

**Type:** string

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-databaseDir: string--><!--Device-Context-databaseDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## distributedFilesDir

```TypeScript
distributedFilesDir: string
```

Distributed file directory.For details, see [Application Sandbox](../../../file-management/app-sandbox-directory.md).

**Type:** string

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-distributedFilesDir: string--><!--Device-Context-distributedFilesDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## eventHub

```TypeScript
eventHub: EventHub
```

Event hub that implements event subscription, unsubscription, and triggering.

**Type:** [EventHub](arkts-ability-eventhub-c.md)

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-eventHub: EventHub--><!--Device-Context-eventHub: EventHub-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## filesDir

```TypeScript
filesDir: string
```

File directory.For details, see [Application Sandbox](../../../file-management/app-sandbox-directory.md).

**Type:** string

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-filesDir: string--><!--Device-Context-filesDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## logFileDir

```TypeScript
get logFileDir(): string
```

Directory for storing log files.

**Type:** string

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Context-get logFileDir(): string--><!--Device-Context-get logFileDir(): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## preferencesDir

```TypeScript
preferencesDir: string
```

Preferences directory.For details, see [Application Sandbox](../../../file-management/app-sandbox-directory.md).

**Type:** string

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-preferencesDir: string--><!--Device-Context-preferencesDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## processName

```TypeScript
processName: string
```

Process name of the current application.

**Type:** string

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Context-processName: string--><!--Device-Context-processName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## resourceDir

```TypeScript
resourceDir: string
```

Resource directory.

> **NOTE: **
> 
> You are required to manually create the resfile directory in **&lt;module-name&gt;\resource**.
> The **resfile** directory can be accessed only in read-only mode.

**Type:** string

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-resourceDir: string--><!--Device-Context-resourceDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## resourceManager

```TypeScript
resourceManager: resmgr.ResourceManager
```

Object for resource management.

**Type:** resmgr.ResourceManager

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-resourceManager: resmgr.ResourceManager--><!--Device-Context-resourceManager: resmgr.ResourceManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## tempDir

```TypeScript
tempDir: string
```

Temporary directory.For details, see [Application Sandbox](../../../file-management/app-sandbox-directory.md).

**Type:** string

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Context-tempDir: string--><!--Device-Context-tempDir: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
