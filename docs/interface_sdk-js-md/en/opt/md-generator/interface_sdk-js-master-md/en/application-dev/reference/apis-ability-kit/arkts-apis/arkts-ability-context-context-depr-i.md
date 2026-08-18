# Context

The context of an ability or an application. It allows access to application-specific resources, request and verification permissions. Can only be obtained through the ability.

**Inheritance/Implementation:** Context extends BaseContext

**Since:** 6

<!--Device-unnamed-export interface Context--><!--Device-unnamed-export interface Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## getAbilityInfo

```TypeScript
getAbilityInfo(callback: AsyncCallback<AbilityInfo>): void
```

Checks the detailed information of this ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getAbilityInfo(callback: AsyncCallback<AbilityInfo>): void--><!--Device-Context-getAbilityInfo(callback: AsyncCallback<AbilityInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)&gt; | Yes |

## getAbilityInfo

```TypeScript
getAbilityInfo(): Promise<AbilityInfo>
```

Checks the detailed information of this ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getAbilityInfo(): Promise<AbilityInfo>--><!--Device-Context-getAbilityInfo(): Promise<AbilityInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)&gt; |

## getAppType

```TypeScript
getAppType(callback: AsyncCallback<string>): void
```

Obtains the application type.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getAppType(callback: AsyncCallback<string>): void--><!--Device-Context-getAppType(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getAppType

```TypeScript
getAppType(): Promise<string>
```

Obtains the application type.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getAppType(): Promise<string>--><!--Device-Context-getAppType(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getAppVersionInfo

```TypeScript
getAppVersionInfo(callback: AsyncCallback<AppVersionInfo>): void
```

Obtains the application version information.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getAppVersionInfo(callback: AsyncCallback<AppVersionInfo>): void--><!--Device-Context-getAppVersionInfo(callback: AsyncCallback<AppVersionInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AppVersionInfo](arkts-ability-appversioninfo-appversioninfo-depr-i.md)&gt; | Yes |

## getAppVersionInfo

```TypeScript
getAppVersionInfo(): Promise<AppVersionInfo>
```

Obtains the application version information.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getAppVersionInfo(): Promise<AppVersionInfo>--><!--Device-Context-getAppVersionInfo(): Promise<AppVersionInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AppVersionInfo](arkts-ability-appversioninfo-appversioninfo-depr-i.md)&gt; |

## getApplicationContext

```TypeScript
getApplicationContext(): Context
```

Obtains the context of this application.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getApplicationContext(): Context--><!--Device-Context-getApplicationContext(): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Context](arkts-ability-context-context-depr-i.md) |

## getApplicationInfo

```TypeScript
getApplicationInfo(callback: AsyncCallback<ApplicationInfo>): void
```

Obtains information about the current application.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getApplicationInfo(callback: AsyncCallback<ApplicationInfo>): void--><!--Device-Context-getApplicationInfo(callback: AsyncCallback<ApplicationInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt; | Yes |

## getApplicationInfo

```TypeScript
getApplicationInfo(): Promise<ApplicationInfo>
```

Obtains information about the current application.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getApplicationInfo(): Promise<ApplicationInfo>--><!--Device-Context-getApplicationInfo(): Promise<ApplicationInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt; |

## getBundleName

```TypeScript
getBundleName(callback: AsyncCallback<string>): void
```

Obtains the bundle name of the current ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getBundleName(callback: AsyncCallback<string>): void--><!--Device-Context-getBundleName(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getBundleName

```TypeScript
getBundleName(): Promise<string>
```

Obtains the bundle name of the current ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getBundleName(): Promise<string>--><!--Device-Context-getBundleName(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getCacheDir

```TypeScript
getCacheDir(callback: AsyncCallback<string>): void
```

Obtains the cache directory of this application on the internal storage.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getCacheDir(callback: AsyncCallback<string>): void--><!--Device-Context-getCacheDir(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getCacheDir

```TypeScript
getCacheDir(): Promise<string>
```

Obtains the cache directory of this application on the internal storage.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getCacheDir(): Promise<string>--><!--Device-Context-getCacheDir(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getCallingBundle

```TypeScript
getCallingBundle(callback: AsyncCallback<string>): void
```

Obtains the bundle name of the ability that called the current ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getCallingBundle(callback: AsyncCallback<string>): void--><!--Device-Context-getCallingBundle(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getCallingBundle

```TypeScript
getCallingBundle(): Promise<string>
```

Obtains the bundle name of the ability that called the current ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getCallingBundle(): Promise<string>--><!--Device-Context-getCallingBundle(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getDisplayOrientation

```TypeScript
getDisplayOrientation(callback: AsyncCallback<bundle.DisplayOrientation>): void
```

Obtains the current display orientation of this ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getDisplayOrientation(callback: AsyncCallback<bundle.DisplayOrientation>): void--><!--Device-Context-getDisplayOrientation(callback: AsyncCallback<bundle.DisplayOrientation>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;bundle.DisplayOrientation&gt; | Yes |

## getDisplayOrientation

```TypeScript
getDisplayOrientation(): Promise<bundle.DisplayOrientation>
```

Obtains the current display orientation of this ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getDisplayOrientation(): Promise<bundle.DisplayOrientation>--><!--Device-Context-getDisplayOrientation(): Promise<bundle.DisplayOrientation>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;bundle.DisplayOrientation & gt; |

## getElementName

```TypeScript
getElementName(callback: AsyncCallback<ElementName>): void
```

Obtains the ohos.bundle.ElementName object of the current ability.This method is available only to Page abilities.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getElementName(callback: AsyncCallback<ElementName>): void--><!--Device-Context-getElementName(callback: AsyncCallback<ElementName>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ElementName](arkts-ability-elementname-elementname-depr-i.md)&gt; | Yes |

## getElementName

```TypeScript
getElementName(): Promise<ElementName>
```

Obtains the ohos.bundle.ElementName object of the current ability.This method is available only to Page abilities.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getElementName(): Promise<ElementName>--><!--Device-Context-getElementName(): Promise<ElementName>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ElementName](arkts-ability-elementname-elementname-depr-i.md)&gt; |

## getExternalCacheDir

```TypeScript
getExternalCacheDir(callback: AsyncCallback<string>): void
```

Obtains the absolute path to the application-specific cache directory

**Since:** 6

**Deprecated since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getExternalCacheDir(callback: AsyncCallback<string>): void--><!--Device-Context-getExternalCacheDir(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getExternalCacheDir

```TypeScript
getExternalCacheDir(): Promise<string>
```

Obtains the absolute path to the application-specific cache directory

**Since:** 6

**Deprecated since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getExternalCacheDir(): Promise<string>--><!--Device-Context-getExternalCacheDir(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getFilesDir

```TypeScript
getFilesDir(callback: AsyncCallback<string>): void
```

Obtains the file directory of this application on the internal storage.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getFilesDir(callback: AsyncCallback<string>): void--><!--Device-Context-getFilesDir(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getFilesDir

```TypeScript
getFilesDir(): Promise<string>
```

Obtains the file directory of this application on the internal storage.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getFilesDir(): Promise<string>--><!--Device-Context-getFilesDir(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getHapModuleInfo

```TypeScript
getHapModuleInfo(callback: AsyncCallback<HapModuleInfo>): void
```

Obtains the ModuleInfo object for this application.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getHapModuleInfo(callback: AsyncCallback<HapModuleInfo>): void--><!--Device-Context-getHapModuleInfo(callback: AsyncCallback<HapModuleInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HapModuleInfo](arkts-ability-hapmoduleinfo-hapmoduleinfo-depr-i.md)&gt; | Yes |

## getHapModuleInfo

```TypeScript
getHapModuleInfo(): Promise<HapModuleInfo>
```

Obtains the ModuleInfo object for this application.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getHapModuleInfo(): Promise<HapModuleInfo>--><!--Device-Context-getHapModuleInfo(): Promise<HapModuleInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[HapModuleInfo](arkts-ability-hapmoduleinfo-hapmoduleinfo-depr-i.md)&gt; |

## getOrCreateDistributedDir

```TypeScript
getOrCreateDistributedDir(): Promise<string>
```

Obtains the distributed file path for storing ability or application data files. If the distributed file path does not exist, the system will create a path and return the created path.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getOrCreateDistributedDir(): Promise<string>--><!--Device-Context-getOrCreateDistributedDir(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getOrCreateDistributedDir

```TypeScript
getOrCreateDistributedDir(callback: AsyncCallback<string>): void
```

Obtains the distributed file path for storing ability or application data files. If the distributed file path does not exist, the system will create a path and return the created path.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getOrCreateDistributedDir(callback: AsyncCallback<string>): void--><!--Device-Context-getOrCreateDistributedDir(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getOrCreateLocalDir

```TypeScript
getOrCreateLocalDir(): Promise<string>
```

Get the local root dir of an app. If it is the first call, the dir will be created. If in the context of the ability, return the root dir of the ability; if in the context of the application, return the root dir of the application.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getOrCreateLocalDir(): Promise<string>--><!--Device-Context-getOrCreateLocalDir(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getOrCreateLocalDir

```TypeScript
getOrCreateLocalDir(callback: AsyncCallback<string>): void
```

Get the local root dir of an app. If it is the first call, the dir will be created. If in the context of the ability, return the root dir of the ability; if in the context of the application, return the root dir of the application.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getOrCreateLocalDir(callback: AsyncCallback<string>): void--><!--Device-Context-getOrCreateLocalDir(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getProcessInfo

```TypeScript
getProcessInfo(callback: AsyncCallback<ProcessInfo>): void
```

Obtains information about the current process, including the process ID and name.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getProcessInfo(callback: AsyncCallback<ProcessInfo>): void--><!--Device-Context-getProcessInfo(callback: AsyncCallback<ProcessInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ProcessInfo](arkts-ability-processinfo-processinfo-depr-i.md)&gt; | Yes |

## getProcessInfo

```TypeScript
getProcessInfo(): Promise<ProcessInfo>
```

Obtains information about the current process, including the process ID and name.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getProcessInfo(): Promise<ProcessInfo>--><!--Device-Context-getProcessInfo(): Promise<ProcessInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ProcessInfo](arkts-ability-processinfo-processinfo-depr-i.md)&gt; |

## getProcessName

```TypeScript
getProcessName(callback: AsyncCallback<string>): void
```

Obtains the name of the current process.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getProcessName(callback: AsyncCallback<string>): void--><!--Device-Context-getProcessName(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getProcessName

```TypeScript
getProcessName(): Promise<string>
```

Obtains the name of the current process.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-getProcessName(): Promise<string>--><!--Device-Context-getProcessName(): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## isUpdatingConfigurations

```TypeScript
isUpdatingConfigurations(callback: AsyncCallback<boolean>): void
```

Checks whether the configuration of this ability is changing.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-isUpdatingConfigurations(callback: AsyncCallback<boolean>): void--><!--Device-Context-isUpdatingConfigurations(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isUpdatingConfigurations

```TypeScript
isUpdatingConfigurations(): Promise<boolean>
```

Checks whether the configuration of this ability is changing.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-isUpdatingConfigurations(): Promise<boolean>--><!--Device-Context-isUpdatingConfigurations(): Promise<boolean>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## printDrawnCompleted

```TypeScript
printDrawnCompleted(callback: AsyncCallback<void>): void
```

Inform the system of the time required for drawing this Page ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-printDrawnCompleted(callback: AsyncCallback<void>): void--><!--Device-Context-printDrawnCompleted(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## printDrawnCompleted

```TypeScript
printDrawnCompleted(): Promise<void>
```

Inform the system of the time required for drawing this Page ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-printDrawnCompleted(): Promise<void>--><!--Device-Context-printDrawnCompleted(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## requestPermissionsFromUser

```TypeScript
requestPermissionsFromUser(
    permissions: Array<string>,
    requestCode: number,
    resultCallback: AsyncCallback<PermissionRequestResult>
  ): void
```

Requests certain permissions from the system.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-requestPermissionsFromUser(    permissions: Array<string>,    requestCode: number,    resultCallback: AsyncCallback<PermissionRequestResult>  ): void--><!--Device-Context-requestPermissionsFromUser(    permissions: Array<string>,    requestCode: number,    resultCallback: AsyncCallback<PermissionRequestResult>  ): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissions | Array & lt;string & gt; | Yes |
| requestCode | number | Yes |
| resultCallback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PermissionRequestResult](arkts-ability-context-permissionrequestresult-depr-i.md)&gt; | Yes |

## requestPermissionsFromUser

```TypeScript
requestPermissionsFromUser(permissions: Array<string>, requestCode: number): Promise<PermissionRequestResult>
```

Requests certain permissions from the system.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-requestPermissionsFromUser(permissions: Array<string>, requestCode: number): Promise<PermissionRequestResult>--><!--Device-Context-requestPermissionsFromUser(permissions: Array<string>, requestCode: number): Promise<PermissionRequestResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permissions | Array & lt;string & gt; | Yes |
| requestCode | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PermissionRequestResult](arkts-ability-context-permissionrequestresult-depr-i.md)&gt; |

## setDisplayOrientation

```TypeScript
setDisplayOrientation(orientation: bundle.DisplayOrientation, callback: AsyncCallback<void>): void
```

Sets the display orientation of the current ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-setDisplayOrientation(orientation: bundle.DisplayOrientation, callback: AsyncCallback<void>): void--><!--Device-Context-setDisplayOrientation(orientation: bundle.DisplayOrientation, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| orientation | bundle.DisplayOrientation | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setDisplayOrientation

```TypeScript
setDisplayOrientation(orientation: bundle.DisplayOrientation): Promise<void>
```

Sets the display orientation of the current ability.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-setDisplayOrientation(orientation: bundle.DisplayOrientation): Promise<void>--><!--Device-Context-setDisplayOrientation(orientation: bundle.DisplayOrientation): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| orientation | bundle.DisplayOrientation | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setShowOnLockScreen

```TypeScript
setShowOnLockScreen(show: boolean, callback: AsyncCallback<void>): void
```

Sets whether to show this ability on top of the lock screen whenever the lock screen is displayed, keeping the ability in the ACTIVE state. The interface can only take effect in API8 and below versions.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setShowOnLockScreen](../../apis-arkui/arkts-apis/arkts-arkui-window-windowstage-i-sys.md#setshowonlockscreen)

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-setShowOnLockScreen(show: boolean, callback: AsyncCallback<void>): void--><!--Device-Context-setShowOnLockScreen(show: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| show | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setShowOnLockScreen

```TypeScript
setShowOnLockScreen(show: boolean): Promise<void>
```

Sets whether to show this ability on top of the lock screen whenever the lock screen is displayed, keeping the ability in the ACTIVE state. The interface can only take effect in API8 and below versions.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setShowOnLockScreen](../../apis-arkui/arkts-apis/arkts-arkui-window-windowstage-i-sys.md#setshowonlockscreen)

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-setShowOnLockScreen(show: boolean): Promise<void>--><!--Device-Context-setShowOnLockScreen(show: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| show | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## setWakeUpScreen

```TypeScript
setWakeUpScreen(wakeUp: boolean, callback: AsyncCallback<void>): void
```

Sets whether to wake up the screen when this ability is restored.

**Since:** 7

**Deprecated since:** 12

**Substitutes:** setWakeUpScreen

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-setWakeUpScreen(wakeUp: boolean, callback: AsyncCallback<void>): void--><!--Device-Context-setWakeUpScreen(wakeUp: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wakeUp | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## setWakeUpScreen

```TypeScript
setWakeUpScreen(wakeUp: boolean): Promise<void>
```

Sets whether to wake up the screen when this ability is restored.

**Since:** 7

**Deprecated since:** 12

**Substitutes:** setWakeUpScreen

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-setWakeUpScreen(wakeUp: boolean): Promise<void>--><!--Device-Context-setWakeUpScreen(wakeUp: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wakeUp | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## verifyPermission

```TypeScript
verifyPermission(permission: string, options?: PermissionOptions): Promise<number>
```

Verify whether the specified permission is allowed for a particular pid and uid running in the system. Pid and uid are optional. If you do not pass in pid and uid, it will check your own permission.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-verifyPermission(permission: string, options?: PermissionOptions): Promise<number>--><!--Device-Context-verifyPermission(permission: string, options?: PermissionOptions): Promise<number>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permission | string | Yes |
| options | [PermissionOptions](arkts-ability-context-permissionoptions-depr-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## verifyPermission

```TypeScript
verifyPermission(permission: string, options: PermissionOptions, callback: AsyncCallback<number>): void
```

Verify whether the specified permission is allowed for a particular pid and uid running in the system. Pid and uid are optional. If you do not pass in pid and uid, it will check your own permission.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-verifyPermission(permission: string, options: PermissionOptions, callback: AsyncCallback<number>): void--><!--Device-Context-verifyPermission(permission: string, options: PermissionOptions, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permission | string | Yes |
| options | [PermissionOptions](arkts-ability-context-permissionoptions-depr-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## verifyPermission

```TypeScript
verifyPermission(permission: string, callback: AsyncCallback<number>): void
```

Verify whether the specified permission is allowed for a particular pid and uid running in the system. Pid and uid are optional. If you do not pass in pid and uid, it will check your own permission.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

<!--Device-Context-verifyPermission(permission: string, callback: AsyncCallback<number>): void--><!--Device-Context-verifyPermission(permission: string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| permission | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |
