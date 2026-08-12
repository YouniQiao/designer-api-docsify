# AppStorageV2

AppStorageV2提供应用级全局共享状态变量的能力，开发者可以通过connect绑定同一个key，进行跨Ability的数据共享。具体UI使用说明，详见  
[AppStorageV2(应用全局的UI状态存储)](../../../ui/state-management/arkts-new-appstoragev2.md)。

**起始版本：** 12

<!--Device-unnamed-export declare class AppStorageV2--><!--Device-unnamed-export declare class AppStorageV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

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

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AppStorageV2-static connect<T extends object>(    type: TypeConstructorWithArgs<T>,    keyOrDefaultCreator?: string | StorageDefaultCreator<T>,    defaultCreator?: StorageDefaultCreator<T>  ): T | undefined--><!--Device-AppStorageV2-static connect<T extends object>(    type: TypeConstructorWithArgs<T>,    keyOrDefaultCreator?: string | StorageDefaultCreator<T>,    defaultCreator?: StorageDefaultCreator<T>  ): T | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [TypeConstructorWithArgs](arkts-arkui-arkui-statemanagement-typeconstructorwithargs-i.md)&lt;T&gt; | 是 |
| keyOrDefaultCreator | string \| [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;T&gt; | 否 |
| defaultCreator | [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;T&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## keys

```TypeScript
static keys(): Array<string>
```

获取[AppStorageV2](../../../ui/state-management/arkts-new-appstoragev2.md)中的所有key。

> **说明：**
> 
> key在Array中的顺序是无序的，与key插入到AppStorageV2中的顺序无关。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AppStorageV2-static keys(): Array<string>--><!--Device-AppStorageV2-static keys(): Array<string>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

## remove

```TypeScript
static remove<T>(keyOrType: string | TypeConstructorWithArgs<T>): void
```

将指定的键值对数据从[AppStorageV2](../../../ui/state-management/arkts-new-appstoragev2.md)里面删除。如果指定的键值不存在于AppStorageV2中，将删除失败。

> **说明：**
> 
> 删除AppStorageV2中不存在的key会报警告。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-AppStorageV2-static remove<T>(keyOrType: string | TypeConstructorWithArgs<T>): void--><!--Device-AppStorageV2-static remove<T>(keyOrType: string | TypeConstructorWithArgs<T>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyOrType | string \| [TypeConstructorWithArgs](arkts-arkui-arkui-statemanagement-typeconstructorwithargs-i.md)&lt;T&gt; | 是 |
