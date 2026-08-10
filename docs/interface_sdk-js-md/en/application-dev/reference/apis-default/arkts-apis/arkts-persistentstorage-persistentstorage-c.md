# PersistentStorage

Defines the PersistentStorage interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class PersistentStorage--><!--Device-unnamed-export declare class PersistentStorage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deleteProp

```TypeScript
static deleteProp(key: string): void
```

[persistProp](../../apis-arkui/arkts-apis/arkts-arkui-persistpropsoptions-i.md/arkts-arkui-persistpropsoptions-i.md)的逆向操作。将key对应的属性从PersistentStorage中删除，后续  
[AppStorage](../../../ui/state-management-static/arkts-static-appstorage.md)的操作，对  
[PersistentStorage](../../../ui/state-management-static/arkts-static-persiststorage.md)不会再有影响。该操作会将对应的key从持久化文件中删除，如果希望再次持久化，可以再次调用[persistProp](../../apis-arkui/arkts-apis/arkts-arkui-persistpropsoptions-i.md/arkts-arkui-persistpropsoptions-i.md)接口。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

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

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistentStorage-static keys(): Array<string>--><!--Device-PersistentStorage-static keys(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 返回所有持久化属性的属性名的数组。 |

## persistProp

```TypeScript
static persistProp<T>(key: string, defaultValue: T, toJson?: ToJSONType<T>, fromJson?: FromJSONType<T>): boolean
```

将[AppStorage](../../../ui/state-management-static/arkts-static-appstorage.md)中key对应的属性持久化到文件中。该接口的调用通常在访问AppStorage之前。

确定属性的类型和值的顺序如下：

1. 如果[PersistentStorage](../../../ui/state-management-static/arkts-static-persiststorage.md)文件中存在key对应的属性，则返回false。

2. 如果PersistentStorage文件中没有查询到key对应的属性，则在AppStorage中查找key对应的属性。如果找到key对应的属性，则将该属性持久化，并返回true。

3. 如果AppStorage中也没查找到key对应的属性，则在磁盘中查找key对应的属性。如果找到key对应的属性，则在AppStorage中创建和初始化key对应的属性，并将该属性持久化，最终返回true。

4. 如果磁盘中不存在对应属性，则在AppStorage中创建和初始化key对应的属性，并将该属性持久化，最终返回true。

 根据上述的初始化流程，如果AppStorage中有该属性，则会使用其值，覆盖掉PersistentStorage文件中的值。由于AppStorage是内存内数据，该行为会导致数据丧失持久化能力。

5. 对于复杂类型(联合类型都是复杂类型)，开发者必须实现toJson和fromJson才能实现持久化，只有boolean、int、double、long、string，开发者可以不传入toJson和fromJson。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistentStorage-static persistProp<T>(key: string, defaultValue: T, toJson?: ToJSONType<T>, fromJson?: FromJSONType<T>): boolean--><!--Device-PersistentStorage-static persistProp<T>(key: string, defaultValue: T, toJson?: ToJSONType<T>, fromJson?: FromJSONType<T>): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 属性名。 |
| defaultValue | T | Yes | 当在[PersistentStorage](../../apis-arkui/arkts-apis/arkts-arkui-persistentstorage-c.md/arkts-arkui-persistentstorage-c.md)和 [AppStorage](../../../reference/apis-arkui/arkui-ts/ts-state-management-Static-copy.md#appstorage)中未查询到key时，使用 defaultValue中。 |
| toJson | [ToJSONType](arkts-tojsontype-t.md)&lt;T&gt; | No | 见[ToJSONType](arkts-tojsontype-t.md)，用于序列化。对于复杂类型（除boolean、int、double、long、string外）， 开发者必须实现该方法才能成功序列化。 |
| fromJson | [FromJSONType](arkts-fromjsontype-t.md)&lt;T&gt; | No | 见[FromJSONType](arkts-fromjsontype-t.md)，用于反序列化。对于复杂类型（除boolean、int、double、long、 string外），开发者必须实现该方法才能成功反序列化。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果PersistentStorage文件中存在key对应的属性，则返回false。否则将依次从AppStorage、磁盘中查找对应属性，若存在，则返回true，若不存在，则创建并持久化 key对应的属性，并返回true。 |

## persistProps

```TypeScript
static persistProps(props: PersistPropsOptions<Any>[]): void
```

将[AppStorage](../../../ui/state-management-static/arkts-static-appstorage.md)中key对应的属性持久化到文件中。与  
[persistProp](../../apis-arkui/arkts-apis/arkts-arkui-persistpropsoptions-i.md/arkts-arkui-persistpropsoptions-i.md)的区别在于可以一次性持久化多个数据，适用场景是：应用启动时调用持久化接口。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PersistentStorage-static persistProps(props: PersistPropsOptions<Any>[]): void--><!--Device-PersistentStorage-static persistProps(props: PersistPropsOptions<Any>[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| props | [PersistPropsOptions](../../apis-arkui/arkts-apis/arkts-arkui-persistpropsoptions-i.md)&lt;Any&gt;[] | Yes | 持久化数组。 |

