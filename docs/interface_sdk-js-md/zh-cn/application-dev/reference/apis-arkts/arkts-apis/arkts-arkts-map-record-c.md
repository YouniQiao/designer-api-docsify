# Record

A Map subclass with keys restricted to numbers, strings, or enums

**继承/实现关系：** Record extends [Map<K, V>](arkts-arkts-collections-map-c.md#set)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Record<K extends Numeric | string | BaseEnum<Int> | BaseEnum<Long> | BaseEnum<string> | BaseEnum<Float> |    BaseEnum<Double> | BaseEnum<Byte> | BaseEnum<Short>, V> extends Map<K, V>--><!--Device-unnamed-export class Record<K extends Numeric | string | BaseEnum<Int> | BaseEnum<Long> | BaseEnum<string> | BaseEnum<Float> |    BaseEnum<Double> | BaseEnum<Byte> | BaseEnum<Short>, V> extends Map<K, V>-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_get

```TypeScript
$_get(k : K) : V | undefined
```

Gets a value from the Record by key

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Record-$_get(k : K) : V | undefined--><!--Device-Record-$_get(k : K) : V | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| k | K | 是 | The key to get |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | The value associated with the key, or undefined if not found |

## $_set

```TypeScript
$_set(k: K, v: V) : void
```

Sets a value in the Record by key

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Record-$_set(k: K, v: V) : void--><!--Device-Record-$_set(k: K, v: V) : void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| k | K | 是 | The key to set |
| v | V | 是 | The value to set |

