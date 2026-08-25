# compare

## 导入模块

```TypeScript
import { fastbuffer } from '@kit.ArkTS';
```

## compare

```TypeScript
function compare(buf1: FastBuffer | Uint8Array, buf2: FastBuffer | Uint8Array): -1 | 0 | 1
```

返回两个FastBuffer对象的比较结果，通常用于对FastBuffer对象数组进行排序。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf1 | [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| Uint8Array | 是 |
| buf2 | [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| -1 \| 0 \| 1 |

**错误码：**

| 错误码ID |
| --- |
| [10200068](../errorcode-utils.md#10200068-引用已释放或分离的arraybuffer) |

**示例**

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from('1234');
let buf2 = fastbuffer.from('0123');
let compareResult = fastbuffer.compare(buf1, buf2);

console.info(Number(compareResult).toString());
// 输出结果：1
```

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from([1, 2, 3, 4, 5, 6, 7, 8, 9]);
let buf2 = fastbuffer.from([5, 6, 7, 8, 9, 1, 2, 3, 4]);

// 比较buf1[0,4)与buf2[5,9)，结果为0表示相同
console.info(buf1.compare(buf2, 5, 9, 0, 4).toString());
// 输出结果：0
// 比较buf1[4,end)与buf2[0,6)，结果为-1表示buf1排在前面
console.info(buf1.compare(buf2, 0, 6, 4).toString());
// 输出结果：-1
// 比较buf1[5,end)与buf2[5,6)，结果为1表示buf1排在后面
console.info(buf1.compare(buf2, 5, 6, 5).toString());
// 输出结果：1
```
