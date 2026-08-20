# Record

Map的子类，其键只能为数字、字符串或枚举。

**继承/实现关系：** Record extends Map<K, V>

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Record--><!--Device-unnamed-export class Record-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { HashMap } from '@kit.ArkTS';
import { HashMapCbFn } from '@kit.ArkTS';
import { LightWeightMap } from '@kit.ArkTS';
import { LightWeightMapCbFn } from '@kit.ArkTS';
import { TreeMap } from '@kit.ArkTS';
import { TreeMapForEachCb } from '@kit.ArkTS';
import { TreeMapComparator } from '@kit.ArkTS';
```

## $_get

```TypeScript
$_get(k : K) : V | undefined
```

根据键从Record中获取值。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Record-$_get(k : K) : V | undefined--><!--Device-Record-$_get(k : K) : V | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| k | K | 是 | 待获取的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V \| undefined | 该键关联的值，未找到时返回undefined。 |

## $_set

```TypeScript
$_set(k: K, v: V) : void
```

根据键在Record中设置值。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Record-$_set(k: K, v: V) : void--><!--Device-Record-$_set(k: K, v: V) : void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| k | K | 是 | 待设置的键。 |
| v | V | 是 | 待设置的值。 |

