# Context

Context模块提供了Ability或Application的上下文的基础能力，包括允许访问特定于应用程序的资源、请求和验证权限等。

**继承/实现关系：** Context extends BaseContext

**起始版本：** 6

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## getAbilityInfo

```TypeScript
getAbilityInfo(callback: AsyncCallback<AbilityInfo>): void
```

检查此能力的配置是否正在更改。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)&gt; | 是 |

## getAbilityInfo

```TypeScript
getAbilityInfo(): Promise<AbilityInfo>
```

查询当前归属Ability详细信息。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)&gt; |

## getApplicationContext

```TypeScript
getApplicationContext(): Context
```

获取应用上下文信息。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| [Context](arkts-ability-context-context-depr-i.md) |

## getApplicationInfo

```TypeScript
getApplicationInfo(callback: AsyncCallback<ApplicationInfo>): void
```

获取有关当前应用程序的信息。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt; | 是 |

## getApplicationInfo

```TypeScript
getApplicationInfo(): Promise<ApplicationInfo>
```

获取有关当前应用程序的信息。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt; |

## getAppType

```TypeScript
getAppType(callback: AsyncCallback<string>): void
```

获取此应用的类型。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getAppType

```TypeScript
getAppType(): Promise<string>
```

获取此应用的类型。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getAppVersionInfo

```TypeScript
getAppVersionInfo(callback: AsyncCallback<AppVersionInfo>): void
```

获取应用的版本信息。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AppVersionInfo](arkts-ability-appversioninfo-appversioninfo-depr-i.md)&gt; | 是 |

## getAppVersionInfo

```TypeScript
getAppVersionInfo(): Promise<AppVersionInfo>
```

获取应用的版本信息。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AppVersionInfo](arkts-ability-appversioninfo-appversioninfo-depr-i.md)&gt; |

## getBundleName

```TypeScript
getBundleName(callback: AsyncCallback<string>): void
```

获取当前ability的Bundle名称。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getBundleName

```TypeScript
getBundleName(): Promise<string>
```

获取当前ability的Bundle名称。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getCacheDir

```TypeScript
getCacheDir(callback: AsyncCallback<string>): void
```

获取该应用程序的内部存储目录。使用callback异步回调。

**起始版本：** 6

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getCacheDir

```TypeScript
getCacheDir(): Promise<string>
```

获取该应用程序的内部存储目录。使用Promise异步回调。

**起始版本：** 6

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getCallingBundle

```TypeScript
getCallingBundle(callback: AsyncCallback<string>): void
```

获取ability调用方的Bundle名称。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getCallingBundle

```TypeScript
getCallingBundle(): Promise<string>
```

获取ability调用方的Bundle名称。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getDisplayOrientation

```TypeScript
getDisplayOrientation(callback: AsyncCallback<bundle.DisplayOrientation>): void
```

获取当前ability的显示方向。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;bundle.DisplayOrientation&gt; | 是 |

## getDisplayOrientation

```TypeScript
getDisplayOrientation(): Promise<bundle.DisplayOrientation>
```

获取此能力的当前显示方向。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;bundle.DisplayOrientation & gt; |

## getElementName

```TypeScript
getElementName(callback: AsyncCallback<ElementName>): void
```

获取当前ability的ohos.bundleManager.ElementName对象。使用callback异步回调。 此方法仅适用于页面功能。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ElementName](arkts-ability-elementname-elementname-depr-i.md)&gt; | 是 |

## getElementName

```TypeScript
getElementName(): Promise<ElementName>
```

获取当前能力的ohos.bundleManager.ElementName对象。使用Promise异步回调。 此方法仅适用于页面功能。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ElementName](arkts-ability-elementname-elementname-depr-i.md)&gt; |

## getExternalCacheDir

```TypeScript
getExternalCacheDir(callback: AsyncCallback<string>): void
```

获取应用程序的外部缓存目录。使用callback异步回调。

**起始版本：** 6

**废弃版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getExternalCacheDir

```TypeScript
getExternalCacheDir(): Promise<string>
```

获取应用程序的外部缓存目录。使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getFilesDir

```TypeScript
getFilesDir(callback: AsyncCallback<string>): void
```

获取内部存储器上此应用程序的文件目录。使用callback异步回调。

**起始版本：** 6

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getFilesDir

```TypeScript
getFilesDir(): Promise<string>
```

获取内部存储器上此应用程序的文件目录。使用Promise异步回调。

**起始版本：** 6

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getHapModuleInfo

```TypeScript
getHapModuleInfo(callback: AsyncCallback<HapModuleInfo>): void
```

获取应用的ModuleInfo对象。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[HapModuleInfo](arkts-ability-hapmoduleinfo-hapmoduleinfo-depr-i.md)&gt; | 是 |

## getHapModuleInfo

```TypeScript
getHapModuleInfo(): Promise<HapModuleInfo>
```

获取应用的ModuleInfo对象。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HapModuleInfo](arkts-ability-hapmoduleinfo-hapmoduleinfo-depr-i.md)&gt; |

## getOrCreateDistributedDir

```TypeScript
getOrCreateDistributedDir(): Promise<string>
```

获取Ability或应用的分布式文件路径。使用callback异步回调。 如果分布式文件路径不存在，系统将创建一个路径并返回创建的路径。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getOrCreateDistributedDir

```TypeScript
getOrCreateDistributedDir(callback: AsyncCallback<string>): void
```

获取Ability或应用的分布式文件路径。使用Promise异步回调。 如果分布式文件路径不存在，系统将创建一个路径并返回创建的路径。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getOrCreateLocalDir

```TypeScript
getOrCreateLocalDir(): Promise<string>
```

获取应用程序的本地根目录。使用Promise异步回调。 如果是第一次调用，将创建目录。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## getOrCreateLocalDir

```TypeScript
getOrCreateLocalDir(callback: AsyncCallback<string>): void
```

获取应用程序的本地根目录。使用callback异步回调。 如果是第一次调用，将创建目录。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getProcessInfo

```TypeScript
getProcessInfo(callback: AsyncCallback<ProcessInfo>): void
```

获取有关当前进程的信息，包括进程ID和名称。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ProcessInfo](arkts-ability-processinfo-processinfo-depr-i.md)&gt; | 是 |

## getProcessInfo

```TypeScript
getProcessInfo(): Promise<ProcessInfo>
```

获取有关当前进程的信息，包括进程id和名称。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ProcessInfo](arkts-ability-processinfo-processinfo-depr-i.md)&gt; |

## getProcessName

```TypeScript
getProcessName(callback: AsyncCallback<string>): void
```

获取当前进程的名称。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## getProcessName

```TypeScript
getProcessName(): Promise<string>
```

获取当前进程的名称。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## isUpdatingConfigurations

```TypeScript
isUpdatingConfigurations(callback: AsyncCallback<boolean>): void
```

检查此能力的配置是否正在更改。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

## isUpdatingConfigurations

```TypeScript
isUpdatingConfigurations(): Promise<boolean>
```

检查此能力的配置是否正在更改。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

## printDrawnCompleted

```TypeScript
printDrawnCompleted(callback: AsyncCallback<void>): void
```

通知系统绘制此页面功能所需的时间。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## printDrawnCompleted

```TypeScript
printDrawnCompleted(): Promise<void>
```

通知系统绘制此页面功能所需的时间。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
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

从系统请求某些权限。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| permissions | Array & lt;string & gt; | 是 |
| requestCode | number | 是 |
| resultCallback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PermissionRequestResult](arkts-ability-context-permissionrequestresult-depr-i.md)&gt; | 是 |

## requestPermissionsFromUser

```TypeScript
requestPermissionsFromUser(permissions: Array<string>, requestCode: number): Promise<PermissionRequestResult>
```

从系统请求某些权限。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| permissions | Array & lt;string & gt; | 是 |
| requestCode | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PermissionRequestResult](arkts-ability-context-permissionrequestresult-depr-i.md)&gt; |

## setDisplayOrientation

```TypeScript
setDisplayOrientation(orientation: bundle.DisplayOrientation, callback: AsyncCallback<void>): void
```

设置当前Ability的显示方向。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| orientation | bundle.DisplayOrientation | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setDisplayOrientation

```TypeScript
setDisplayOrientation(orientation: bundle.DisplayOrientation): Promise<void>
```

设置当前Ability的显示方向。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| orientation | bundle.DisplayOrientation | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setShowOnLockScreen

```TypeScript
setShowOnLockScreen(show: boolean, callback: AsyncCallback<void>): void
```

设置每当显示锁屏时是否在锁屏顶部显示此功能，使该功能保持激活状态。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| show | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setShowOnLockScreen

```TypeScript
setShowOnLockScreen(show: boolean): Promise<void>
```

设置每当显示锁屏时是否在锁屏顶部显示此功能，使该功能保持激活状态。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| show | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setWakeUpScreen

```TypeScript
setWakeUpScreen(wakeUp: boolean, callback: AsyncCallback<void>): void
```

设置恢复此功能时是否唤醒屏幕。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 12

**替代接口：** setWakeUpScreen

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wakeUp | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## setWakeUpScreen

```TypeScript
setWakeUpScreen(wakeUp: boolean): Promise<void>
```

设置恢复此功能时是否唤醒屏幕。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 12

**替代接口：** setWakeUpScreen

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wakeUp | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## verifyPermission

```TypeScript
verifyPermission(permission: string, options?: PermissionOptions): Promise<number>
```

验证系统中运行的特定pid和uid是否具有指定的权限。使用Promise异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| permission | string | 是 |
| options | [PermissionOptions](arkts-ability-context-permissionoptions-depr-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## verifyPermission

```TypeScript
verifyPermission(permission: string, options: PermissionOptions, callback: AsyncCallback<number>): void
```

验证系统中运行的特定pid和uid是否允许指定的权限。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| permission | string | 是 |
| options | [PermissionOptions](arkts-ability-context-permissionoptions-depr-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## verifyPermission

```TypeScript
verifyPermission(permission: string, callback: AsyncCallback<number>): void
```

验证系统中运行的当前pid和uid是否具有指定的权限。使用callback异步回调。

**起始版本：** 7

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| permission | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |
