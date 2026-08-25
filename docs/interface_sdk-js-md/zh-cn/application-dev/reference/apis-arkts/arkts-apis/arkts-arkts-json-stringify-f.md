# stringify

## 导入模块

```TypeScript
import { JSON } from '@kit.ArkTS';
```

## stringify

```TypeScript
function stringify(value: Object, replacer?: (number | string)[] | null, space?: string | number): string
```

该方法将一个ArkTS对象或数组转换为JSON字符串，支持线性容器的转换，不支持非线性容器（传入非线性容器时无法正确序列化）。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |
| replacer | (number \| string)[] \| null | 否 |
| space | string \| number | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import { JSON } from '@kit.ArkTS';

interface Person {
  name: string;
  age: number;
  city: string;
}

let person: Person = { name: "John", age: 30, city: "New York" };

let rstArrStr = JSON.stringify(person, ["name", "age"]);
console.info(rstArrStr);
// 打印结果：{"name":"John","age":30}

let rstStrSpace = JSON.stringify(person, ["name", "age"], '  ');
console.info(rstStrSpace);
/*
打印结果：
{
  "name": "John",
  "age": 30
}
 */

let rstStrStar = JSON.stringify(person, ["name", "age"], '  &&');
console.info(rstStrStar);
/*
打印结果：
{
  &&"name": "John",
  &&"age": 30
}
 */

let bigIntObj = BigInt(112233445566778899n);
console.info(JSON.stringify(bigIntObj));
// 打印结果：112233445566778899
```

```TypeScript
import { JSON } from '@kit.ArkTS';

function replacer(key: string, value: Object): Object {
  if (typeof value === 'string') {
    return value.toUpperCase();
  }
  return value;
}

interface Person {
  name: string;
  age: number;
  city: string;
}
let inputObj = {"name": "John", "age": 30, "city": "ChongQing"} as Person;

console.info(JSON.stringify(inputObj, replacer));
// 打印结果：{"name":"JOHN","age":30,"city":"CHONGQING"}

console.info(JSON.stringify(inputObj, replacer, '  '));
/*
打印结果：
{
  "name": "JOHN",
  "age": 30,
  "city": "CHONGQING"
}
 */
```


## stringify

```TypeScript
function stringify(value: Object, replacer?: Transformer, space?: string | number): string
```

该方法将一个ArkTS对象或数组转换为JSON字符串，支持线性容器的转换，不支持非线性容器。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |
| replacer | [Transformer](arkts-arkts-ason-transformer-t.md) | 否 |
| space | string \| number | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**示例**

参见 [stringify](#stringify)
