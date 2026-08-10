# Collator

提供字符串排序的能力。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-intl-export class Collator--><!--Device-intl-export class Collator-End-->

**System capability:** SystemCapability.Global.I18n

## compare

```TypeScript
compare(first: string, second: string): int
```

根据配置项的排序规则，比较两个字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Collator-compare(first: string, second: string): int--><!--Device-Collator-compare(first: string, second: string): int-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| first | string | Yes | 进行比较的第一个字符串。 |
| second | string | Yes | 进行比较的第二个字符串。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 比较结果。 &lt;br&gt;- number为负数时，表示first排序在second之前。 &lt;br&gt;- number为0时，表示first与second排序相同。 &lt;br&gt;- number为正数，表示first排序在second之后。 |

## constructor

```TypeScript
constructor()
```

使用当前系统区域创建排序对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Collator-constructor()--><!--Device-Collator-constructor()-End-->

**System capability:** SystemCapability.Global.I18n

## constructor

```TypeScript
constructor(locale: string | Array<string>, options?: CollatorOptions)
```

根据指定的区域和配置项创建排序对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Collator-constructor(locale: string | Array<string>, options?: CollatorOptions)--><!--Device-Collator-constructor(locale: string | Array<string>, options?: CollatorOptions)-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locale | string \| Array&lt;string&gt; | Yes | 区域ID或区域ID数组。输入是区域ID数组时，使用第一个有效的区域ID。 |
| options | [CollatorOptions](../../apis-arkts/arkts-apis/arkts-arkts-intl-collatoroptions-i.md) | No | 创建排序对象时可设置的配置项。 &lt;br&gt;默认值：所有属性都取默认值时的配置项。 |

## resolvedOptions

```TypeScript
resolvedOptions(): CollatorOptions
```

获取创建排序对象时设置的配置项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Collator-resolvedOptions(): CollatorOptions--><!--Device-Collator-resolvedOptions(): CollatorOptions-End-->

**System capability:** SystemCapability.Global.I18n

**Return value:**

| Type | Description |
| --- | --- |
| [CollatorOptions](../../apis-arkts/arkts-apis/arkts-arkts-intl-collatoroptions-i.md) | 返回排序对象的属性。 |

