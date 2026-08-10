# Context

Context模块提供了Ability或Application的上下文的基础能力，包括允许访问特定于应用程序的资源、请求和验证权限等。

**Inheritance/Implementation:** Context extends [BaseContext](arkts-ability-basecontext-c.md)

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

<!--Device-unnamed-export interface Context extends BaseContext--><!--Device-unnamed-export interface Context extends BaseContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## getAbilityInfo

```TypeScript
getAbilityInfo(callback: AsyncCallback<AbilityInfo>): void
```

检查此能力的配置是否正在更改。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getAbilityInfo(callback: AsyncCallback<AbilityInfo>): void--><!--Device-Context-getAbilityInfo(callback: AsyncCallback<AbilityInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)&gt; | Yes | 回调函数，返回true表示该Ability的配置正在更改，否则返回false。 |

## getAbilityInfo

```TypeScript
getAbilityInfo(): Promise<AbilityInfo>
```

查询当前归属Ability详细信息。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getAbilityInfo(): Promise<AbilityInfo>--><!--Device-Context-getAbilityInfo(): Promise<AbilityInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)&gt; | Promise对象，返回当前归属Ability详细信息。 |

## getAppType

```TypeScript
getAppType(callback: AsyncCallback<string>): void
```

获取此应用的类型。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getAppType(callback: AsyncCallback<string>): void--><!--Device-Context-getAppType(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，返回此应用程序的类型。 |

## getAppType

```TypeScript
getAppType(): Promise<string>
```

获取此应用的类型。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getAppType(): Promise<string>--><!--Device-Context-getAppType(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回此应用的类型。 |

## getAppVersionInfo

```TypeScript
getAppVersionInfo(callback: AsyncCallback<AppVersionInfo>): void
```

获取应用的版本信息。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getAppVersionInfo(callback: AsyncCallback<AppVersionInfo>): void--><!--Device-Context-getAppVersionInfo(callback: AsyncCallback<AppVersionInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AppVersionInfo](arkts-ability-appversioninfo-appversioninfo-depr-i.md)&gt; | Yes | 回调函数，返回应用版本信息。 |

## getAppVersionInfo

```TypeScript
getAppVersionInfo(): Promise<AppVersionInfo>
```

获取应用的版本信息。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getAppVersionInfo(): Promise<AppVersionInfo>--><!--Device-Context-getAppVersionInfo(): Promise<AppVersionInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AppVersionInfo](arkts-ability-appversioninfo-appversioninfo-depr-i.md)&gt; | Promise对象，返回应用版本信息。 |

## getApplicationContext

```TypeScript
getApplicationContext(): Context
```

获取应用上下文信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getApplicationContext(): Context--><!--Device-Context-getApplicationContext(): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | 返回应用上下文信息。 |

## getApplicationInfo

```TypeScript
getApplicationInfo(callback: AsyncCallback<ApplicationInfo>): void
```

获取有关当前应用程序的信息。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getApplicationInfo(callback: AsyncCallback<ApplicationInfo>): void--><!--Device-Context-getApplicationInfo(callback: AsyncCallback<ApplicationInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt; | Yes | 回调函数，返回当前应用程序的信息。 |

## getApplicationInfo

```TypeScript
getApplicationInfo(): Promise<ApplicationInfo>
```

获取有关当前应用程序的信息。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getApplicationInfo(): Promise<ApplicationInfo>--><!--Device-Context-getApplicationInfo(): Promise<ApplicationInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt; | Promise对象，返回当前应用程序的信息。 |

## getBundleName

```TypeScript
getBundleName(callback: AsyncCallback<string>): void
```

获取当前ability的Bundle名称。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getBundleName(callback: AsyncCallback<string>): void--><!--Device-Context-getBundleName(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，返回当前ability的Bundle名称。 |

## getBundleName

```TypeScript
getBundleName(): Promise<string>
```

获取当前ability的Bundle名称。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getBundleName(): Promise<string>--><!--Device-Context-getBundleName(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回当前ability的Bundle名称。 |

## getCacheDir

```TypeScript
getCacheDir(callback: AsyncCallback<string>): void
```

获取该应用程序的内部存储目录。使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getCacheDir(callback: AsyncCallback<string>): void--><!--Device-Context-getCacheDir(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，返回该应用程序的内部存储目录。 |

## getCacheDir

```TypeScript
getCacheDir(): Promise<string>
```

获取该应用程序的内部存储目录。使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getCacheDir(): Promise<string>--><!--Device-Context-getCacheDir(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回该应用程序的内部存储目录。 |

## getCallingBundle

```TypeScript
getCallingBundle(callback: AsyncCallback<string>): void
```

获取ability调用方的Bundle名称。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getCallingBundle(callback: AsyncCallback<string>): void--><!--Device-Context-getCallingBundle(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，返回ability调用方的Bundle名称。 |

## getCallingBundle

```TypeScript
getCallingBundle(): Promise<string>
```

获取ability调用方的Bundle名称。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getCallingBundle(): Promise<string>--><!--Device-Context-getCallingBundle(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回ability调用方的Bundle名称。 |

## getDisplayOrientation

```TypeScript
getDisplayOrientation(callback: AsyncCallback<bundle.DisplayOrientation>): void
```

获取当前ability的显示方向。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getDisplayOrientation(callback: AsyncCallback<bundle.DisplayOrientation>): void--><!--Device-Context-getDisplayOrientation(callback: AsyncCallback<bundle.DisplayOrientation>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;bundle.DisplayOrientation&gt; | Yes | 回调函数，返回屏幕显示方向。 |

## getDisplayOrientation

```TypeScript
getDisplayOrientation(): Promise<bundle.DisplayOrientation>
```

获取此能力的当前显示方向。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getDisplayOrientation(): Promise<bundle.DisplayOrientation>--><!--Device-Context-getDisplayOrientation(): Promise<bundle.DisplayOrientation>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;bundle.DisplayOrientation&gt; | Indicates the screen display direction. |

## getElementName

```TypeScript
getElementName(callback: AsyncCallback<ElementName>): void
```

获取当前ability的ohos.bundleManager.ElementName对象。使用callback异步回调。此方法仅适用于页面功能。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getElementName(callback: AsyncCallback<ElementName>): void--><!--Device-Context-getElementName(callback: AsyncCallback<ElementName>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ElementName](arkts-ability-elementname-elementname-depr-i.md)&gt; | Yes | 回调函数，返回当前ability的ohos.bundleManager.ElementName对象。 |

## getElementName

```TypeScript
getElementName(): Promise<ElementName>
```

获取当前能力的ohos.bundleManager.ElementName对象。使用Promise异步回调。此方法仅适用于页面功能。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getElementName(): Promise<ElementName>--><!--Device-Context-getElementName(): Promise<ElementName>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ElementName](arkts-ability-elementname-elementname-depr-i.md)&gt; | Promise对象，返回当前ability的ohos.bundleManager.ElementName对象。 |

## getExternalCacheDir

```TypeScript
getExternalCacheDir(callback: AsyncCallback<string>): void
```

获取应用程序的外部缓存目录。使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getExternalCacheDir(callback: AsyncCallback<string>): void--><!--Device-Context-getExternalCacheDir(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，返回应用程序的缓存目录的绝对路径。 |

## getExternalCacheDir

```TypeScript
getExternalCacheDir(): Promise<string>
```

获取应用程序的外部缓存目录。使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getExternalCacheDir(): Promise<string>--><!--Device-Context-getExternalCacheDir(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回应用程序的缓存目录的绝对路径。 |

## getFilesDir

```TypeScript
getFilesDir(callback: AsyncCallback<string>): void
```

获取内部存储器上此应用程序的文件目录。使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getFilesDir(callback: AsyncCallback<string>): void--><!--Device-Context-getFilesDir(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，返回内部存储器上此应用程序的文件目录。 |

## getFilesDir

```TypeScript
getFilesDir(): Promise<string>
```

获取内部存储器上此应用程序的文件目录。使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getFilesDir(): Promise<string>--><!--Device-Context-getFilesDir(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回内部存储器上此应用程序的文件目录。 |

## getHapModuleInfo

```TypeScript
getHapModuleInfo(callback: AsyncCallback<HapModuleInfo>): void
```

获取应用的ModuleInfo对象。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getHapModuleInfo(callback: AsyncCallback<HapModuleInfo>): void--><!--Device-Context-getHapModuleInfo(callback: AsyncCallback<HapModuleInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HapModuleInfo](arkts-ability-hapmoduleinfo-hapmoduleinfo-depr-i.md)&gt; | Yes | 回调函数，返回应用的ModuleInfo对象。 |

## getHapModuleInfo

```TypeScript
getHapModuleInfo(): Promise<HapModuleInfo>
```

获取应用的ModuleInfo对象。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getHapModuleInfo(): Promise<HapModuleInfo>--><!--Device-Context-getHapModuleInfo(): Promise<HapModuleInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[HapModuleInfo](arkts-ability-hapmoduleinfo-hapmoduleinfo-depr-i.md)&gt; | Promise对象，返回应用的ModuleInfo对象。 |

## getOrCreateDistributedDir

```TypeScript
getOrCreateDistributedDir(): Promise<string>
```

获取Ability或应用的分布式文件路径。使用callback异步回调。如果分布式文件路径不存在，系统将创建一个路径并返回创建的路径。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getOrCreateDistributedDir(): Promise<string>--><!--Device-Context-getOrCreateDistributedDir(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | 回调函数，返回Ability或应用的分布式文件路径。若路径不存在，系统将创建一个路径并返回创建的路径。 |

## getOrCreateDistributedDir

```TypeScript
getOrCreateDistributedDir(callback: AsyncCallback<string>): void
```

获取Ability或应用的分布式文件路径。使用Promise异步回调。如果分布式文件路径不存在，系统将创建一个路径并返回创建的路径。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getOrCreateDistributedDir(callback: AsyncCallback<string>): void--><!--Device-Context-getOrCreateDistributedDir(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Promise对象，返回Ability或应用的分布式文件路径。若为首次调用，则将创建建目录。 |

## getOrCreateLocalDir

```TypeScript
getOrCreateLocalDir(): Promise<string>
```

获取应用程序的本地根目录。使用Promise异步回调。如果是第一次调用，将创建目录。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getOrCreateLocalDir(): Promise<string>--><!--Device-Context-getOrCreateLocalDir(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回应用程序的本地根目录。 |

## getOrCreateLocalDir

```TypeScript
getOrCreateLocalDir(callback: AsyncCallback<string>): void
```

获取应用程序的本地根目录。使用callback异步回调。如果是第一次调用，将创建目录。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getOrCreateLocalDir(callback: AsyncCallback<string>): void--><!--Device-Context-getOrCreateLocalDir(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，返回应用程序的本地根目录。 |

## getProcessInfo

```TypeScript
getProcessInfo(callback: AsyncCallback<ProcessInfo>): void
```

获取有关当前进程的信息，包括进程ID和名称。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getProcessInfo(callback: AsyncCallback<ProcessInfo>): void--><!--Device-Context-getProcessInfo(callback: AsyncCallback<ProcessInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ProcessInfo](arkts-ability-processinfo-processinfo-depr-i.md)&gt; | Yes | 回调函数，返回当前进程的信息。 |

## getProcessInfo

```TypeScript
getProcessInfo(): Promise<ProcessInfo>
```

获取有关当前进程的信息，包括进程id和名称。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getProcessInfo(): Promise<ProcessInfo>--><!--Device-Context-getProcessInfo(): Promise<ProcessInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ProcessInfo](arkts-ability-processinfo-processinfo-depr-i.md)&gt; | Promise对象，返回当前进程的信息。 |

## getProcessName

```TypeScript
getProcessName(callback: AsyncCallback<string>): void
```

获取当前进程的名称。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getProcessName(callback: AsyncCallback<string>): void--><!--Device-Context-getProcessName(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | 回调函数，返回当前进程的名称。 |

## getProcessName

```TypeScript
getProcessName(): Promise<string>
```

获取当前进程的名称。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getProcessName(): Promise<string>--><!--Device-Context-getProcessName(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回当前进程的名称。 |

## isUpdatingConfigurations

```TypeScript
isUpdatingConfigurations(callback: AsyncCallback<boolean>): void
```

检查此能力的配置是否正在更改。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-isUpdatingConfigurations(callback: AsyncCallback<boolean>): void--><!--Device-Context-isUpdatingConfigurations(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数，返回true表示该Ability的配置正在更改，否则返回false。 |

## isUpdatingConfigurations

```TypeScript
isUpdatingConfigurations(): Promise<boolean>
```

检查此能力的配置是否正在更改。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-isUpdatingConfigurations(): Promise<boolean>--><!--Device-Context-isUpdatingConfigurations(): Promise<boolean>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回true表示该Ability的配置正在更改，否则返回false。 |

## printDrawnCompleted

```TypeScript
printDrawnCompleted(callback: AsyncCallback<void>): void
```

通知系统绘制此页面功能所需的时间。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-printDrawnCompleted(callback: AsyncCallback<void>): void--><!--Device-Context-printDrawnCompleted(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当通知系统绘制此页面功能所需的时间成功，err为undefined，否则为错误对象。 |

## printDrawnCompleted

```TypeScript
printDrawnCompleted(): Promise<void>
```

通知系统绘制此页面功能所需的时间。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-printDrawnCompleted(): Promise<void>--><!--Device-Context-printDrawnCompleted(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象 |

## requestPermissionsFromUser

```TypeScript
requestPermissionsFromUser(
    permissions: Array<string>,
    requestCode: number,
    resultCallback: AsyncCallback<PermissionRequestResult>
  ): void
```

从系统请求某些权限。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-requestPermissionsFromUser(    permissions: Array<string>,    requestCode: number,    resultCallback: AsyncCallback<PermissionRequestResult>  ): void--><!--Device-Context-requestPermissionsFromUser(    permissions: Array<string>,    requestCode: number,    resultCallback: AsyncCallback<PermissionRequestResult>  ): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissions | Array&lt;string&gt; | Yes | 指示要请求的权限列表。此参数不能为null。 |
| requestCode | number | Yes | 指示要传递给[PermissionRequestResult](arkts-ability-context-permissionrequestresult-depr-i.md)的请求代码。 |
| resultCallback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PermissionRequestResult&gt; | Yes | 回调函数，返回授权结果信息。 |

## requestPermissionsFromUser

```TypeScript
requestPermissionsFromUser(permissions: Array<string>, requestCode: number): Promise<PermissionRequestResult>
```

从系统请求某些权限。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-requestPermissionsFromUser(permissions: Array<string>, requestCode: number): Promise<PermissionRequestResult>--><!--Device-Context-requestPermissionsFromUser(permissions: Array<string>, requestCode: number): Promise<PermissionRequestResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissions | Array&lt;string&gt; | Yes | 指示要请求的权限列表。此参数不能为null。 |
| requestCode | number | Yes | 指示要传递给[PermissionRequestResult](arkts-ability-context-permissionrequestresult-depr-i.md)的请求代码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PermissionRequestResult&gt; | Promise对象，返回授权结果信息。 |

## setDisplayOrientation

```TypeScript
setDisplayOrientation(orientation: bundle.DisplayOrientation, callback: AsyncCallback<void>): void
```

设置当前Ability的显示方向。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-setDisplayOrientation(orientation: bundle.DisplayOrientation, callback: AsyncCallback<void>): void--><!--Device-Context-setDisplayOrientation(orientation: bundle.DisplayOrientation, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| orientation | bundle.DisplayOrientation | Yes | 指示当前能力的新方向。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当设置当前Ability的显示方向成功，err为undefined，否则为错误对象。 |

## setDisplayOrientation

```TypeScript
setDisplayOrientation(orientation: bundle.DisplayOrientation): Promise<void>
```

设置当前Ability的显示方向。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-setDisplayOrientation(orientation: bundle.DisplayOrientation): Promise<void>--><!--Device-Context-setDisplayOrientation(orientation: bundle.DisplayOrientation): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| orientation | bundle.DisplayOrientation | Yes | 表示屏幕显示方向。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

## setShowOnLockScreen

```TypeScript
setShowOnLockScreen(show: boolean, callback: AsyncCallback<void>): void
```

设置每当显示锁屏时是否在锁屏顶部显示此功能，使该功能保持激活状态。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.window:window.WindowStage.setShowOnLockScreen](../../apis-arkui/arkts-apis/arkts-arkui-window-windowstage-i-sys.md/arkts-arkui-window-windowstage-i-sys.md#setshowonlockscreen)

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-setShowOnLockScreen(show: boolean, callback: AsyncCallback<void>): void--><!--Device-Context-setShowOnLockScreen(show: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| show | boolean | Yes | 指定是否在锁屏顶部显示此功能。值true表示在锁屏上显示，值false表示不显示。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当设置每当显示锁屏时是否在锁屏顶部显示此功能并使该功能保持激活状态的操作成功，err为undefined，否则为错误对象。 |

## setShowOnLockScreen

```TypeScript
setShowOnLockScreen(show: boolean): Promise<void>
```

设置每当显示锁屏时是否在锁屏顶部显示此功能，使该功能保持激活状态。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.window:window.WindowStage.setShowOnLockScreen](../../apis-arkui/arkts-apis/arkts-arkui-window-windowstage-i-sys.md/arkts-arkui-window-windowstage-i-sys.md#setshowonlockscreen)

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-setShowOnLockScreen(show: boolean): Promise<void>--><!--Device-Context-setShowOnLockScreen(show: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| show | boolean | Yes | 指定是否在锁屏顶部显示此功能。值true表示在锁屏上显示，值false表示不显示。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

## setWakeUpScreen

```TypeScript
setWakeUpScreen(wakeUp: boolean, callback: AsyncCallback<void>): void
```

设置恢复此功能时是否唤醒屏幕。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 12

**Substitutes:** @ohos.window:window.setWakeUpScreen

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-setWakeUpScreen(wakeUp: boolean, callback: AsyncCallback<void>): void--><!--Device-Context-setWakeUpScreen(wakeUp: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wakeUp | boolean | Yes | 指定是否唤醒屏幕。值true表示唤醒它，值false表示不唤醒它。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当设置恢复此功能时是否唤醒屏幕成功，err为undefined，否则为错误对象。 |

## setWakeUpScreen

```TypeScript
setWakeUpScreen(wakeUp: boolean): Promise<void>
```

设置恢复此功能时是否唤醒屏幕。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 12

**Substitutes:** @ohos.window:window.setWakeUpScreen

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-setWakeUpScreen(wakeUp: boolean): Promise<void>--><!--Device-Context-setWakeUpScreen(wakeUp: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wakeUp | boolean | Yes | 指定是否唤醒屏幕。值true表示唤醒它，值false表示不唤醒它。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

## verifyPermission

```TypeScript
verifyPermission(permission: string, options?: PermissionOptions): Promise<number>
```

验证系统中运行的特定pid和uid是否具有指定的权限。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-verifyPermission(permission: string, options?: PermissionOptions): Promise<number>--><!--Device-Context-verifyPermission(permission: string, options?: PermissionOptions): Promise<number>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permission | string | Yes | 指定权限的名称。 |
| options | [PermissionOptions](arkts-ability-context-permissionoptions-depr-i.md) | No | 权限选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise对象，如果pid和uid具有权限，则使用0进行异步回调；否则使用-1回调。 |

## verifyPermission

```TypeScript
verifyPermission(permission: string, options: PermissionOptions, callback: AsyncCallback<number>): void
```

验证系统中运行的特定pid和uid是否允许指定的权限。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-verifyPermission(permission: string, options: PermissionOptions, callback: AsyncCallback<number>): void--><!--Device-Context-verifyPermission(permission: string, options: PermissionOptions, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permission | string | Yes | 指定权限的名称。 |
| options | [PermissionOptions](arkts-ability-context-permissionoptions-depr-i.md) | Yes | 权限选项。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 回调函数，返回权限验证结果，0有权限，-1无权限。 |

## verifyPermission

```TypeScript
verifyPermission(permission: string, callback: AsyncCallback<number>): void
```

验证系统中运行的当前pid和uid是否具有指定的权限。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-verifyPermission(permission: string, callback: AsyncCallback<number>): void--><!--Device-Context-verifyPermission(permission: string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permission | string | Yes | 指定权限的名称。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 回调函数，返回权限验证结果，0有权限，-1无权限。 |

