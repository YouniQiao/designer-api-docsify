# AppStorageV2

AppStorageV2提供应用级全局共享状态变量的能力，开发者可以通过connect绑定同一个key，进行跨Ability的数据共享。具体UI使用说明，详见  
[AppStorageV2(应用全局的UI状态存储)](../../../ui/state-management/arkts-new-appstoragev2.md)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export declare class AppStorageV2--><!--Device-unnamed-export declare class AppStorageV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Binding, ComponentReuse, CustomComponentLifecycleState, ComponentInactive, PersistenceV2, ComponentDisappear, MutableBinding, CustomComponentLifecycleObserver, AppStorageV2, Type, ConnectOptionsCollections, CollectionType, CustomComponentContext, IReusePool, ConnectOptions, UIUtils, ComponentActive, CustomComponentLifecycle, ComponentInit, ComponentAppear, ComponentBuilt, ComponentRecycle, IReusableInfo } from 'kits/@kit.ArkUI';
```

## connect

```TypeScript
static connect<T extends object>(
    type: TypeConstructorWithArgs<T>,
    keyOrDefaultCreator?: string | StorageDefaultCreator<T>,
    defaultCreator?: StorageDefaultCreator<T>
  ): T | undefined
```

将键值对数据存储在应用内存中。如果给定的key已经存在于[AppStorageV2](../../../ui/state-management/arkts-new-appstoragev2.md)中，返回对应的值；否则，通过获取默认值的构造器构造默认值，并返回。

> **说明：**
> 
> 1、若未指定key，使用第二个参数作为默认构造器；否则使用第三个参数（第二个参数非法也使用第三个参数作为默认构造器）。
> 
> 2、确保数据已经存储在AppStorageV2中，可省略默认构造器，获取存储的数据；否则必须指定默认构造器，不指定将导致应用异常。
> 
> 3、同一个key，connect不同类型的数据会导致应用异常，应用需要确保类型匹配。
> 
> 4、key建议使用有意义的值，可由字母、数字、下划线组成，长度不超过255个字符，使用非法字符或空字符的行为是未定义的。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AppStorageV2-static connect<T extends object>(    type: TypeConstructorWithArgs<T>,    keyOrDefaultCreator?: string | StorageDefaultCreator<T>,    defaultCreator?: StorageDefaultCreator<T>  ): T | undefined--><!--Device-AppStorageV2-static connect<T extends object>(    type: TypeConstructorWithArgs<T>,    keyOrDefaultCreator?: string | StorageDefaultCreator<T>,    defaultCreator?: StorageDefaultCreator<T>  ): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [TypeConstructorWithArgs](arkts-arkui-arkui-statemanagement-typeconstructorwithargs-i.md)&lt;T&gt; | Yes | 指定的类型，若未指定key，则使用type的name作为key。 |
| keyOrDefaultCreator | string \| StorageDefaultCreator&lt;T&gt; | No | 指定的key，或者是获取默认值的构造器。默认值为undefined。 |
| defaultCreator | [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;T&gt; | No | 获取默认值的构造器。默认值为undefined。如果数据未存储在AppStorageV2中，且没有传递默认构造器，则返回 undefined。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 创建或获取AppStorageV2数据成功时，返回数据；否则返回undefined。 |

## keys

```TypeScript
static keys(): Array<string>
```

获取[AppStorageV2](../../../ui/state-management/arkts-new-appstoragev2.md)中的所有key。

> **说明：**
> 
> key在Array中的顺序是无序的，与key插入到AppStorageV2中的顺序无关。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AppStorageV2-static keys(): Array<string>--><!--Device-AppStorageV2-static keys(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 所有AppStorageV2中的key。 |

## remove

```TypeScript
static remove<T>(keyOrType: string | TypeConstructorWithArgs<T>): void
```

将指定的键值对数据从[AppStorageV2](../../../ui/state-management/arkts-new-appstoragev2.md)里面删除。如果指定的键值不存在于AppStorageV2中，将删除失败。

> **说明：**
> 
> 删除AppStorageV2中不存在的key会报警告。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AppStorageV2-static remove<T>(keyOrType: string | TypeConstructorWithArgs<T>): void--><!--Device-AppStorageV2-static remove<T>(keyOrType: string | TypeConstructorWithArgs<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyOrType | string \| TypeConstructorWithArgs&lt;T&gt; | Yes | 需要删除的key；如果指定的是type类型，删除的key为type的name。 |

