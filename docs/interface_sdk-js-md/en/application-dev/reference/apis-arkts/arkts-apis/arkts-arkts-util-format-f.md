# format

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## format

```TypeScript
function format(format: string, ...args: Object[]): string
```

%s: 用于转换除BigInt、Object和-0之外的所有值。BigInt值将以n表示，没有用户定义toString函数的对象使用util.inspect()检查，选项为{ depth: 0, colors: false, compact: 3 }。%d: 用于转换除BigInt和Symbol之外的所有值。%i: 对除BigInt和Symbol之外的所有值使用parseInt(value, 10)。%f: 对除BigInt和Symbol之外的所有值使用parseFloat(value)。%j: JSON。如果参数包含循环引用，则替换为字符串'[Circular]'。%o: Object。对象的通用JavaScript对象格式字符串表示。类似于util.inspect()，选项为{ showHidden: true, showProxy: true}。这将显示完整对象，包括不可枚举属性和代理。%O: Object。对象的通用JavaScript对象格式字符串表示。%O: Object。对象的通用JavaScript对象格式字符串表示。类似于util.inspect()，没有选项。这将显示完整对象，不包括不可枚举属性和代理。%c: CSS。此说明符被忽略，将跳过传入的任何CSS。%%: 单个百分号('%')。这不会消耗参数。返回：&lt;string&gt; 格式化的字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-util-function format(format: string, ...args: Object[]): string--><!--Device-util-function format(format: string, ...args: Object[]): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| format | string | Yes | 格式字符串 |
| args | Object[] | Yes | 要格式化的数据 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 按特定格式格式化的字符串。 |

