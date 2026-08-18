# attachId

## 导入模块

```TypeScript
```

## attachId

```TypeScript
function attachId(uri: string, id: number): string
```

将ID附加到uri的路径末尾。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [attachId](arkts-ability-datauriutils-attachid-f.md#attachid)

<!--Device-dataUriUtils-function attachId(uri: string, id: number): string--><!--Device-dataUriUtils-function attachId(uri: string, id: number): string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import dataUriUtils from '@ohos.ability.dataUriUtils';

let id = 1122;
let uri = dataUriUtils.attachId(
    'com.example.dataUriUtils',
	id,
);
```
