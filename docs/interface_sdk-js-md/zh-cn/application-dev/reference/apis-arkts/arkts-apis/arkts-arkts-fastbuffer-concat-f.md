# concat

## 导入模块

```TypeScript
import { fastbuffer } from '@kit.ArkTS';
```

## concat

```TypeScript
function concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer
```

将数组中指定字节长度的内容复制并拼接后，返回新的FastBuffer对象。当数组中所有对象的长度总和大于totalLength时，返回结果的长度将被截断为totalLength。当数组中所有对象的长度总和小于totalLength时，返回结果的多余部分将会被填充为0。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| list | [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md)[] \| Uint8Array[] | 是 |
| totalLength | number | 否 |

**返回值：**

| 类型 |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [10200001](../errorcode-utils.md#10200001-参数范围越界错误) |

**示例**

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf1 = fastbuffer.from('1234');
let buf2 = fastbuffer.from('abcd');
let buf = fastbuffer.concat([buf1, buf2]);
console.info(buf.toString('hex'));
// 输出结果：3132333461626364
```
