# AppStorageV2

状态管理模块提供了应用程序动态刷新、UI数据存储、使能数据观察等能力。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class AppStorageV2--><!--Device-unnamed-export declare class AppStorageV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## connect

```TypeScript
public static connect<T extends object>(ttype: Class, key: string,
    defaultCreator?: StorageDefaultCreator<T>): T | undefined
```

将键值对数据存储在应用内存中。如果给定的key已经存在于[AppStorageV2](../../../ui/state-management-static/arkts-static-appstoragev2.md)中，返回对应的值；否则，通过获取默认值的构造器构造默认值，存储后返回。

> **说明：**

> - 如果数据已存储在AppStorageV2中，可省略默认构造器，获取存储的数据；否则必须指定默认构造器，不指定将导致应用异常。
> 
> - key相同，connect类型不同的数据会导致应用异常，开发者需要确保类型匹配。
> 
> - 建议key使用有意义的值，可由字母、数字和下划线组成，长度不超过255字符，避免使用非法字符或空字符。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppStorageV2-public static connect<T extends object>(ttype: Class, key: string,    defaultCreator?: StorageDefaultCreator<T>): T | undefined--><!--Device-AppStorageV2-public static connect<T extends object>(ttype: Class, key: string,    defaultCreator?: StorageDefaultCreator<T>): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ttype | [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md) | Yes | 指定的类型。 |
| key | string | Yes | 指定的key。 |
| defaultCreator | [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;T&gt; | No | 获取默认值的构造器，默认值为undefined。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 创建或获取AppStorageV2数据成功时，返回数据；否则返回undefined。 |

## connect

```TypeScript
public static connect<T extends object>(ttype: Class, defaultCreator?: StorageDefaultCreator<T>): T | undefined
```

将键值对数据存储在应用内存中。如果给定的ttype已经存在于[AppStorageV2](../../../ui/state-management-static/arkts-static-appstoragev2.md)中，返回对应的值；否则，通过获取默认值的构造器构造默认值，存储后返回。

> **说明：**

> - ttype使用Class.from\&lt;classname\&gt;()方法获得。
> 
> - 未传入key时，默认使用ttype的name作为key。
> 
> - 如果数据已存储在AppStorageV2中，可省略默认构造器，获取存储的数据；否则必须指定默认构造器，不指定将导致应用异常。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppStorageV2-public static connect<T extends object>(ttype: Class, defaultCreator?: StorageDefaultCreator<T>): T | undefined--><!--Device-AppStorageV2-public static connect<T extends object>(ttype: Class, defaultCreator?: StorageDefaultCreator<T>): T | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ttype | [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md) | Yes | 指定的类型。 |
| defaultCreator | [StorageDefaultCreator](arkts-arkui-storagedefaultcreator-t.md)&lt;T&gt; | No | 获取默认值的构造器，默认值为undefined。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 创建或获取AppStorageV2数据成功时，返回数据；否则返回undefined。 |

## keys

```TypeScript
public static keys(): string[]
```

获取[AppStorageV2](../../../ui/state-management-static/arkts-static-appstoragev2.md)中的所有key。

> **说明：**

> key在Array中的顺序是无序的，与key插入到AppStorageV2中的顺序无关。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppStorageV2-public static keys(): string[]--><!--Device-AppStorageV2-public static keys(): string[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string[] | 所有AppStorageV2中的key。 |

## remove

```TypeScript
public static remove(keyOrType: string | Class): void
```

将指定的键值对数据从[AppStorageV2](../../../ui/state-management-static/arkts-static-appstoragev2.md)里面删除。如果指定的键值不存在于AppStorageV2中，将删除失败。

> **说明：**

> 删除AppStorageV2中不存在的key会报警告。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppStorageV2-public static remove(keyOrType: string | Class): void--><!--Device-AppStorageV2-public static remove(keyOrType: string | Class): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyOrType | string \| Class | Yes | 需要删除的key。如果传入的是Class类型，则删除的key为Class类型入参的name。 |

