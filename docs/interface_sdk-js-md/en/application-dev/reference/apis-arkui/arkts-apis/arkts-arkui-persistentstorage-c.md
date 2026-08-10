# PersistentStorage

PersistentStorage提供了UI状态的持久化存储能力，将选定的AppStorage属性持久化到文件中，在应用重启时从文件中恢复这些属性值并写入到AppStorage。具体UI使用说明，详见  
[PersistentStorage：持久化存储UI状态](../../../ui/state-management/arkts-persiststorage.md)。

> **说明：**
> 
> 从API version 12开始，PersistentStorage支持null、undefined。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare class PersistentStorage--><!--Device-unnamed-declare class PersistentStorage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DeleteProp

```TypeScript
static DeleteProp(key: string): void
```

是[PersistProp](arkts-arkui-persistentstorage-c.md#persistprop)的逆向操作。将key对应的属性从  
[PersistentStorage](../../../ui/state-management/arkts-persiststorage.md)中删除，后续  
[AppStorage](../../../ui/state-management/arkts-appstorage.md)的操作对PersistentStorage不会再有影响。如需再次持久化，可再次调用  
[PersistProp](arkts-arkui-persistentstorage-c.md#persistprop)接口。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [PersistentStorage#deleteProp](arkts-arkui-persistentstorage-c.md#deleteprop)

<!--Device-PersistentStorage-static DeleteProp(key: string): void--><!--Device-PersistentStorage-static DeleteProp(key: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | PersistentStorage中的属性名。 |

## Keys

```TypeScript
static Keys(): Array<string>
```

返回所有持久化属性的属性名的数组。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [PersistentStorage#keys](arkts-arkui-persistentstorage-c.md#keys)

<!--Device-PersistentStorage-static Keys(): Array<string>--><!--Device-PersistentStorage-static Keys(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 返回所有持久化属性的属性名的数组。 |

## PersistProp

```TypeScript
static PersistProp<T>(key: string, defaultValue: T): void
```

将[AppStorage](../../../ui/state-management/arkts-appstorage.md)中key对应的属性持久化到文件中。该接口应在访问AppStorage之前调用。

确定属性的类型和值的顺序如下：

1. 如果[PersistentStorage](../../../ui/state-management/arkts-persiststorage.md)文件中存在key对应的属性，在AppStorage中创建对应的key，并用在PersistentStorage中找到的key的属性初始化。

2. 如果PersistentStorage文件中没有查询到key对应的属性，则在AppStorage中查找key对应的属性。如果找到key对应的属性，则将该属性持久化。

3. 如果AppStorage也没查找到key对应的属性，则在AppStorage中创建key对应的属性。用defaultValue初始化其值，并将该属性持久化。

根据上述的初始化流程，如果AppStorage中有该属性，则会使用其值覆盖PersistentStorage文件中的值。由于AppStorage是内存中的数据，这种操作会使持久化文件中的数据被内存数据覆盖，导致持久化数据失去意义。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [PersistentStorage#persistProp](arkts-arkui-persistentstorage-c.md#persistprop)

<!--Device-PersistentStorage-static PersistProp<T>(key: string, defaultValue: T): void--><!--Device-PersistentStorage-static PersistProp<T>(key: string, defaultValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要持久化的属性名。 |
| defaultValue | T | Yes | 在PersistentStorage和AppStorage中未查询到时，则使用默认值进行初始化。默认值不允许为null或undefined。 |

## PersistProps

```TypeScript
static PersistProps(
    properties: {
      key: string;
      defaultValue: any;
    }[],
  ): void
```

行为与[PersistProp](arkts-arkui-persistentstorage-c.md#persistprop)类似，不同在于可以一次性持久化多个数据。该接口应在访问AppStorage之前调用，适合在应用启动时初始化。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [PersistentStorage#PersistProps](arkts-arkui-persistentstorage-c.md#persistprops)

<!--Device-PersistentStorage-static PersistProps(    properties: {      key: string;      defaultValue: any;    }[],  ): void--><!--Device-PersistentStorage-static PersistProps(    properties: {      key: string;      defaultValue: any;    }[],  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| properties | {       key: string;       defaultValue: any;     }[] | Yes |  |

## deleteProp

```TypeScript
static deleteProp(key: string): void
```

是[persistProp](arkts-arkui-persistentstorage-c.md#persistprop)的逆向操作。将key对应的属性从  
[PersistentStorage](../../../ui/state-management/arkts-persiststorage.md)中删除，后续  
[AppStorage](../../../ui/state-management/arkts-appstorage.md)的操作对PersistentStorage不会再有影响。如需再次持久化，可再次调用  
[persistProp](arkts-arkui-persistentstorage-c.md#persistprop)接口。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PersistentStorage-static deleteProp(key: string): void--><!--Device-PersistentStorage-static deleteProp(key: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | PersistentStorage中的属性名。 |

## keys

```TypeScript
static keys(): Array<string>
```

返回所有持久化属性的属性名的数组。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PersistentStorage-static keys(): Array<string>--><!--Device-PersistentStorage-static keys(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 返回所有持久化属性的属性名的数组。 |

## persistProp

```TypeScript
static persistProp<T>(key: string, defaultValue: T): void
```

将[AppStorage](../../../ui/state-management/arkts-appstorage.md)中key对应的属性持久化到文件中。该接口通常在访问AppStorage之前调用。

确定属性的类型和值的顺序如下：

1. 如果[PersistentStorage](../../../ui/state-management/arkts-persiststorage.md)文件中存在key对应的属性，在AppStorage中创建对应的key，并用在PersistentStorage中找到的key的属性初始化。

2. 如果PersistentStorage文件中没有查询到key对应的属性，则在AppStorage中查找key对应的属性。如果找到key对应的属性，则将该属性持久化。

3. 如果AppStorage中也没查找到key对应的属性，则在AppStorage中创建key对应的属性。用defaultValue初始化其值，并将该属性持久化。

根据上述的初始化流程，如果AppStorage中有该属性，则会使用其值覆盖PersistentStorage文件中的值。由于AppStorage是内存中的数据，这种操作会使持久化文件中的数据被内存数据覆盖，导致持久化数据失去意义。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PersistentStorage-static persistProp<T>(key: string, defaultValue: T): void--><!--Device-PersistentStorage-static persistProp<T>(key: string, defaultValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 要持久化的属性名。 |
| defaultValue | T | Yes | 在PersistentStorage和AppStorage中未查询到时，则使用默认值进行初始化。从API version 12开始可以为null或undefined。 |

## persistProps

```TypeScript
static persistProps(props: PersistPropsOptions[]): void
```

行为与[persistProp](arkts-arkui-persistentstorage-c.md#persistprop)类似，不同在于可以一次性持久化多个数据。该接口通常在访问AppStorage之前调用，适合在应用启动时初始化。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PersistentStorage-static persistProps(props: PersistPropsOptions[]): void--><!--Device-PersistentStorage-static persistProps(props: PersistPropsOptions[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| props | [PersistPropsOptions](arkts-arkui-persistpropsoptions-i.md)[] | Yes | 持久化数组，每项包含属性名和默认值。 |

